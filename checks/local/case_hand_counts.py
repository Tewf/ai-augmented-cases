"""Case hand counts: a count taken by hand is marked, listed in a file, and equal to what the results record.

For each case, a run with no error guarantees that
- when the page says "by hand", the folder holds hand-counts.csv and the Data and procedure section links it;
- when the folder holds hand-counts.csv, the page says "by hand" somewhere in its Results;
- the tally of the file's `kind` column equals the `hand` tally of the case's results file.
It does not guarantee that the hand count is right: a program cannot tell which questions reached a person.
Principle: a hand count is marked as such.
Exact. Time O(cases x rows).
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _cases import case_readmes, results_of, section  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "case-hand-counts"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for readme in case_readmes(root, config):
        folder = (root / readme).parent
        text = (root / readme).read_text(encoding="utf-8", errors="replace")
        csv_path = folder / "hand-counts.csv"
        says = "by hand" in section(text, "Results")[1].lower()
        if says and not csv_path.is_file():
            findings.append(Finding(NAME, readme, 1, "the Results say 'by hand' but the folder has no hand-counts.csv listing them"))
        if csv_path.is_file() and not says:
            findings.append(Finding(NAME, readme, 1, "the folder holds hand-counts.csv but the Results never mark a count 'by hand'"))
        if not csv_path.is_file():
            continue
        if "hand-counts.csv" not in section(text, "Data and procedure")[1]:
            findings.append(Finding(NAME, readme, 1, "the Data and procedure do not link hand-counts.csv"))
        with csv_path.open(newline="", encoding="utf-8") as handle:
            tally = dict(Counter(row["kind"] for row in csv.DictReader(handle)))
        results = results_of(root, readme)
        if results is not None and results.get("hand", {}) != tally:
            findings.append(Finding(NAME, readme, 1, f"hand-counts.csv tallies {tally} but the results record {results.get('hand', {})}"))
    return findings
