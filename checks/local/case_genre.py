"""Case genre: a case names its genre, an experience report, and the checklist it meets.

A report written by those who took part is an experience report, not a case study in the sense of the community
standard (Ralph 2020). For each case, a run with no error guarantees that its Genre and baseline section contains the
words experience report and names the baseline, Runeson 2009, in itself or in the earlier case it links. It does not guarantee that the genre fits.
Exact. Time O(cases x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _cases import LINK, case_readmes, section  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "case-genre"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for readme in case_readmes(root, config):
        line, body = section((root / readme).read_text(encoding="utf-8", errors="replace"), "Genre and baseline")
        for target in LINK.findall(body):  # a later case may take the genre of an earlier one, by a link
            earlier = ((root / readme).parent / target).resolve()
            if target.endswith("README.md") and earlier.is_file() and earlier != (root / readme).resolve():
                body += "\n" + section(earlier.read_text(encoding="utf-8", errors="replace"), "Genre and baseline")[1]
        for need in ("experience report", "Runeson 2009"):
            if need.lower() not in body.lower():
                findings.append(Finding(NAME, readme, line or 1, f"the Genre and baseline do not say '{need}'"))
    return findings
