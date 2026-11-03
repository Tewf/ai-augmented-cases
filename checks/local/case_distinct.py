"""Case distinct work: a case states the distinct work behind its commit total, not the total alone.

A commit may recur under another hash when a history moves between repositories, so a sum of commits overstates the
work. For each case, a run with no error guarantees that its Results section states the number of distinct pairs of
author time and subject that the program counted (`distinct_work` in the results file) and says the word distinct.
It does not guarantee that a pair is a unit of work. Principle: distinct work over raw commits.
Exact. Time O(cases x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _cases import case_readmes, has_number, results_of, section  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "case-distinct"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for readme in case_readmes(root, config):
        results = results_of(root, readme)
        if results is None:
            continue  # case-counts reports the missing results
        line, body = section((root / readme).read_text(encoding="utf-8", errors="replace"), "Results")
        work = int(results.get("distinct_work", -1))
        if "distinct" not in body.lower() or not has_number(body, work):
            findings.append(Finding(NAME, readme, line or 1, f"the Results do not state the {work} distinct pairs of author time and subject beside the commit total"))
    return findings
