"""Tests for measures.py: a throwaway repository with fixed dates, so the counts are known."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import measures


def run(repo, *args, when=None):
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid")
    if when:
        env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = when
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "-C", str(repo), *args], check=True, capture_output=True, env=env)


class Measures(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.dir.name) / "r"
        self.repo.mkdir()
        run(self.repo, "init", "-q")
        (self.repo / "decisions").mkdir()

    def tearDown(self):
        self.dir.cleanup()

    def commit(self, path, when, message):
        (self.repo / path).parent.mkdir(exist_ok=True)
        (self.repo / path).write_text(message)
        run(self.repo, "add", "-A")
        run(self.repo, "commit", "-q", "-m", message, when=when)

    def test_day_is_local_and_counts_hold(self):
        tz = measures.parse_offset("+01:00")
        self.commit("a.md", "2026-10-28T23:30:00+00:00", "before")      # 00:30 local on the 29th
        self.commit("decisions/0001-x.md", "2026-10-29T10:00:00+01:00", "record")
        self.commit("b.md", "2026-10-29T12:00:00+01:00", "later")
        self.commit("c.md", "2026-10-29T23:30:00+00:00", "after")       # 00:30 local on the 30th
        run(self.repo, "tag", "v1", "HEAD~1", when="2026-10-29T12:00:00+01:00")
        commits = measures.read_commits(self.repo, tz)
        today = [c for c in commits if c["committer"].date().isoformat() == "2026-10-29"]
        self.assertEqual(len(today), 3)
        self.assertEqual(measures.decisions_added(self.repo, "2026-10-29", tz), ["decisions/0001-x.md"])
        self.assertEqual([t[0] for t in measures.tags_on_day(self.repo, "2026-10-29", tz)], ["v1"])
        self.assertEqual(measures.files_touched(self.repo, [c["hash"] for c in today]),
                         {"a.md", "decisions/0001-x.md", "b.md"})


class Moves(unittest.TestCase):
    def test_slug(self):
        self.assertTrue(measures.is_move("decisions/0006-move-to-reader-ergonomics-v1.1.1.md"))
        self.assertFalse(measures.is_move("decisions/0004-pin-a-release.md"))


if __name__ == "__main__":
    unittest.main()
