"""Shared by the local checks: which documents are cases, where a case's parts are, and which results file is its own.

A document is a case when its `**Shape:**` line links shapes/case.md, as the cases do. A Shape line inside fenced
code, as in the shape's skeleton, declares nothing. A case lives in a folder `cases/<date>-<name>/` beside its
measures program, its hand counts and the results files of its runs; the results file for the case is the one whose
`day` equals the date that opens the folder name.
This module has no NAME, so the runner loads it and skips it; each check puts its folder on sys.path to import it.
"""
from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

from framework.check_api import files_in_scope, prose_only

SHAPE_LINE = re.compile(r"\*\*Shape:\*\*\s*\[[^\]]*\]\(([^)\s]+)\)")


def case_readmes(root: Path, config: dict) -> list[str]:
    """The markdown paths whose Shape line links shapes/case.md."""
    found = []
    for path in files_in_scope(root, config, {".md", ".qmd"}):
        text = prose_only((root / path).read_text(encoding="utf-8", errors="replace"))
        if any(link.split("#")[0].endswith("shapes/case.md") for link in SHAPE_LINE.findall(text)):
            found.append(path)
    return found


def section(text: str, heading: str) -> tuple[int, str]:
    """The line number and body of the level-2 section whose heading holds `heading`; (0, "") when absent."""
    lines = text.splitlines()
    for number, line in enumerate(lines):
        if re.match(r"##\s", line) and heading.lower() in line.lower():
            end = next((k for k in range(number + 1, len(lines)) if re.match(r"##\s", lines[k])), len(lines))
            return number + 1, "\n".join(lines[number + 1:end])
    return 0, ""


def results_of(root: Path, readme: str) -> dict | None:
    """The results of the run for the case's day, or None when the folder holds none."""
    folder = (root / readme).parent
    day = folder.name[:10]
    for path in sorted(folder.glob("results*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if data.get("day") == day:
            return data
    return None


def jobs_of(root: Path, readme: str) -> list[dict] | None:
    """The `[[job]]` tables of the job record `jobs.toml` in the case's folder (ai-augmented-project, shapes/job-record.md).

    None when the folder holds no such file; raises ValueError when the file is not valid TOML.
    """
    path = (root / readme).parent / "jobs.toml"
    if not path.is_file():
        return None
    try:
        return tomllib.loads(path.read_text(encoding="utf-8")).get("job", [])
    except tomllib.TOMLDecodeError as error:
        raise ValueError(str(error)) from error


def minutes_total(jobs: list[dict]) -> tuple[float, int]:
    """The sum of the minutes the jobs recorded, and how many jobs recorded them. A job without minutes adds nothing."""
    values = [job["minutes"] for job in jobs if isinstance(job.get("minutes"), (int, float))]
    return float(sum(values)), len(values)


def has_figure(text: str, figure: float) -> bool:
    """True when the figure stands in the text as a word of its own, written without a trailing zero (17, 17.5)."""
    return re.search(rf"(?<![\d.,]){re.escape(f'{figure:g}')}(?![\d]|[.,]\d)", text) is not None


def has_number(text: str, number: int) -> bool:
    """True when the number stands in the text as a word of its own, not inside a longer number."""
    return re.search(rf"(?<![\d.,]){number}(?![\d]|[.,]\d)", text) is not None


LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)(?:#[^)\s]*)?\)")


def linked_file(root: Path, readme: str, suffix: str) -> Path | None:
    """The first file the page links, by relative path, whose name ends with `suffix` and which exists."""
    text = prose_only((root / readme).read_text(encoding="utf-8", errors="replace"))
    for target in LINK.findall(text):
        if target.endswith(suffix) and not re.match(r"^[a-z]+:", target):
            candidate = ((root / readme).parent / target).resolve()
            if candidate.is_file():
                return candidate
    return None
