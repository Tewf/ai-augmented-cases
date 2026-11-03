"""Case counts: a case prints what a program counted, with the program's cautions beside it.

For each case (a document whose Shape line links shapes/case.md), a run with no error guarantees that
- the case has a measures.py, in its folder or linked from the page, with a test of it (test_*.py) beside it;
- the folder holds the results file of the case's day;
- every repository in that results file carries the three cautions the program takes: shared, carried and skew;
- the Results section holds a table with a Carried column, the caution that turns commits into distinct work;
- when the results hold the Cost blocks of job briefs (a "costs" key), the same table has a Minutes column: the person's minutes;
- the Results section states the total of commits the program summed, as the program printed it.
It does not guarantee that the program is right (its test is), nor that the cautions suffice: a commit is not a unit
of work, and no program can say so. Principle: print the caution beside the count.
Exact. Time O(cases x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _cases import case_readmes, has_number, linked_file, results_of, section  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "case-counts"
EXACT = True
CAUTIONS = ("shared", "carried", "skew")


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for readme in case_readmes(root, config):
        folder = (root / readme).parent
        program = folder / "measures.py"
        if not program.is_file():  # a later case may run the program of an earlier one and link it
            program = linked_file(root, readme, "measures.py") or program
        if not program.is_file():
            findings.append(Finding(NAME, readme, 1, "the case has no measures.py beside it or linked: a program takes its counts"))
        elif not list(program.parent.glob("test_*.py")):
            findings.append(Finding(NAME, readme, 1, "the measures program has no test beside it (test_*.py)"))
        results = results_of(root, readme)
        if results is None:
            findings.append(Finding(NAME, readme, 1, f"no results*.json in the folder has day {folder.name[:10]}: keep the numbers of the run"))
            continue
        for name, row in results.get("repositories", {}).items():
            missing = [key for key in CAUTIONS if key not in row]
            if missing:
                findings.append(Finding(NAME, readme, 1, f"the results of {name} lack the cautions {', '.join(missing)}"))
        text = (root / readme).read_text(encoding="utf-8", errors="replace")
        line, body = section(text, "Results")
        header = next((row for row in body.splitlines() if row.lstrip().startswith("|") and "carried" in row.lower()), "")
        if not header:
            findings.append(Finding(NAME, readme, line or 1, "the Results hold no table with a Carried column: print the caution beside the count"))
        if "costs" in results and header and "minutes" not in header.lower():
            findings.append(Finding(NAME, readme, line or 1, "the results hold Cost blocks: add the person's minutes as a Minutes column"))
        if not has_number(body, int(results.get("summed", -1))):
            findings.append(Finding(NAME, readme, line or 1, f"the Results do not state the {results.get('summed')} commits the program summed"))
    return findings
