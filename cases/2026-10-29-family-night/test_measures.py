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


class Repos(unittest.TestCase):
    def test_repos_option_names_the_checkouts(self):
        with tempfile.TemporaryDirectory() as root:
            for name in ("one", "two"):
                repo = Path(root) / name
                repo.mkdir()
                run(repo, "init", "-q")
                (repo / "f.md").write_text(name)
                run(repo, "add", "-A")
                run(repo, "commit", "-q", "-m", name, when="2026-11-02T10:00:00+01:00")
            per, distinct, work = measures.measure(root, "2026-11-02", measures.parse_offset("+01:00"), ["one", "two"])
            self.assertEqual(list(per), ["one", "two"])
            self.assertEqual((per["one"]["commits"], distinct, work), (1, 2, 2))


class Moves(unittest.TestCase):
    def test_slug(self):
        self.assertTrue(measures.is_move("decisions/0006-move-to-reader-ergonomics-v1.1.1.md"))
        self.assertFalse(measures.is_move("decisions/0004-pin-a-release.md"))


class Costs(unittest.TestCase):
    BRIEF = "# Brief: x\n\n## Checks\n\n- `true`: passes.\n\n## Cost\n\n- Tokens: 1,200 tokens\n- Dollars: 0.5 dollars\n- Minutes: {m}\n- Produced: a page\n"

    def folder(self, root, name, text):
        d = Path(root) / name
        d.mkdir()
        if text is not None:
            (d / "brief.md").write_text(text)
        return str(d)

    def test_numbers_are_read_and_pending_is_not_zero(self):
        with tempfile.TemporaryDirectory() as root:
            a = self.folder(root, "a", self.BRIEF.format(m="25 minutes"))
            b = self.folder(root, "b", self.BRIEF.format(m="pending"))
            c = self.folder(root, "c", "# Brief: y\n\n## Checks\n\n- `true`: ok.\n")
            d = self.folder(root, "d", None)  # no brief.md: not a job
            costs = measures.read_costs([a, b, c, d])
            self.assertEqual(list(costs), ["a", "b", "c"])
            self.assertEqual(costs["a"], {"Tokens": 1200.0, "Dollars": 0.5, "Minutes": 25.0, "Produced": "a page"})
            self.assertIsNone(costs["b"]["Minutes"])
            self.assertIsNone(costs["c"])
            total = measures.sum_costs(costs)
            self.assertEqual((total["minutes"], total["minutes_jobs"], total["tokens"], total["tokens_jobs"], total["jobs"]),
                             (25.0, 1, 2400.0, 2, 3))

    def test_the_table_gains_minutes_only_when_given(self):
        per = {"r": {"commits": 1, "files": 1, "tags": [], "decisions": [], "moves": 0, "first": "10:00", "last": "10:00",
                     "shared": 0, "carried": 0, "skew": 0}}
        self.assertNotIn("minutes", measures.table(per))
        lines = measures.table(per, 25.0).splitlines()
        self.assertTrue(lines[0].endswith("| minutes |"))
        self.assertTrue(lines[-1].endswith("| 25 |"))
        self.assertEqual(lines[-1].count("|"), lines[0].count("|"))


if __name__ == "__main__":
    unittest.main()
