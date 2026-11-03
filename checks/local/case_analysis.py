"""Case analysis: a case says that no language model analysed its data.

A model analysing the data of a case is an antipattern of the community standard (Ralph 2020). For each case, a run
with no error guarantees that the Analysis section states, in so many words, that no model analysed the data. It
does not guarantee that the statement is true: that is the maintainer's to confirm.
Exact. Time O(cases x size).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _cases import case_readmes, section  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "case-analysis"
EXACT = True
STATEMENT = re.compile(r"\bno (language )?model analy[sz]ed\b", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for readme in case_readmes(root, config):
        line, body = section((root / readme).read_text(encoding="utf-8", errors="replace"), "Analysis")
        if not STATEMENT.search(body):
            findings.append(Finding(NAME, readme, line or 1, "the Analysis do not say 'no model analysed' the data"))
    return findings
