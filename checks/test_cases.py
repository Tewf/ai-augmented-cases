"""Tests of the local checks in checks/local/: each fails where a case lacks what its principle asks, and stays silent
where it has it.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPOSITORY / "checks" / "local" / f"{name}.py")
    sys.path.insert(0, str(REPOSITORY / "checks" / "local"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


counts, distinct, hands, analysis, genre = (load(n) for n in ("case_counts", "case_distinct", "case_hand_counts", "case_analysis", "case_genre"))

PAGE = """# Case: a day

**Shape:** [case](../../shapes/case.md). **Baseline:** Runeson 2009.

## Genre and baseline

An experience report with repository measures, met against Runeson 2009.

## Data and procedure

The hand counts are in [hand-counts.csv](hand-counts.csv).

## Analysis

No model analysed any data.

## Results

| Repository | Commits | Shared | Carried |
|---|---|---|---|
| r | 12 | 0 | 2 |

12 commits summed; 10 distinct pairs of author time and subject. Reached the person (by hand, 2): two orders.
"""
RESULTS = {"day": "2026-01-02", "summed": 12, "distinct_work": 10, "hand": {"reached": 2},
           "repositories": {"r": {"commits": 12, "shared": 0, "carried": 2, "skew": 0}}}


class Case(unittest.TestCase):
    """A temporary repository holding one case that meets every principle; tests break one part each."""

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.dir)
        self.folder = self.dir / "cases" / "2026-01-02-day"
        self.folder.mkdir(parents=True)
        self.write("README.md", PAGE)
        self.write("measures.py", "")
        self.write("test_measures.py", "")
        self.write("hand-counts.csv", "n,kind\n1,reached\n2,reached\n")
        self.write("results.json", json.dumps(RESULTS))

    def write(self, name, text):
        (self.folder / name).write_text(text, encoding="utf-8")

    def page(self, old, new):
        self.write("README.md", PAGE.replace(old, new))

    def messages(self, module):
        return [finding.message for finding in module.check(self.dir, {})]

    def test_a_complete_case_passes_every_check(self):
        for module in (counts, distinct, hands, analysis, genre):
            self.assertEqual(self.messages(module), [], module.NAME)

    def test_a_page_that_does_not_declare_the_shape_is_not_a_case(self):
        self.page("**Shape:** [case](../../shapes/case.md).", "")
        (self.folder / "measures.py").unlink()
        self.assertEqual(self.messages(counts), [])


class Counts(Case):
    def test_no_program_fails(self):
        (self.folder / "measures.py").unlink()
        self.assertTrue(any("measures.py" in m for m in self.messages(counts)))

    def test_a_linked_program_of_an_earlier_case_counts(self):
        other = self.dir / "cases" / "2025-12-31-earlier"
        other.mkdir()
        (other / "measures.py").write_text("")
        (other / "test_measures.py").write_text("")
        (self.folder / "measures.py").unlink()
        (self.folder / "test_measures.py").unlink()
        self.page("## Analysis", "[program](../2025-12-31-earlier/measures.py)\n\n## Analysis")
        self.assertEqual(self.messages(counts), [])

    def test_a_program_without_a_test_fails(self):
        (self.folder / "test_measures.py").unlink()
        self.assertTrue(any("no test" in m for m in self.messages(counts)))

    def test_results_of_another_day_fail(self):
        self.write("results.json", json.dumps({**RESULTS, "day": "2026-01-03"}))
        self.assertTrue(any("results*.json" in m for m in self.messages(counts)))

    def test_a_row_without_cautions_fails(self):
        self.write("results.json", json.dumps({**RESULTS, "repositories": {"r": {"commits": 12}}}))
        self.assertTrue(any("shared, carried, skew" in m for m in self.messages(counts)))

    def test_no_carried_column_fails(self):
        self.page("| Carried |", "| Other |")
        self.assertTrue(any("Carried column" in m for m in self.messages(counts)))

    def test_a_total_inside_a_longer_number_does_not_count(self):
        self.write("README.md", PAGE.replace("| r | 12 |", "| r | 99 |").replace("12 commits summed", "412 commits summed"))
        self.assertTrue(any("summed" in m for m in self.messages(counts)))


class Minutes(Case):
    def test_costs_in_the_results_need_a_minutes_column(self):
        self.write("results.json", json.dumps({**RESULTS, "costs": {"a": None}}))
        self.assertTrue(any("Minutes column" in m for m in self.messages(counts)))

    def test_a_minutes_column_passes(self):
        self.write("results.json", json.dumps({**RESULTS, "costs": {"a": None}}))
        self.page("| Carried |\n|---|---|---|---|\n| r | 12 | 0 | 2 |", "| Carried | Minutes |\n|---|---|---|---|---|\n| r | 12 | 0 | 2 | 25 |")
        self.assertEqual(self.messages(counts), [])

    def test_a_case_without_costs_is_not_asked_for_minutes(self):
        self.assertEqual(self.messages(counts), [])


class Distinct(Case):
    def test_missing_distinct_count_fails(self):
        self.page("10 distinct pairs", "ten pairs")
        self.assertEqual(len(self.messages(distinct)), 1)

    def test_the_number_without_the_word_fails(self):
        self.page("10 distinct pairs", "10 pairs")
        self.assertEqual(len(self.messages(distinct)), 1)


class HandCounts(Case):
    def test_unmarked_hand_count_fails(self):
        self.page("(by hand, 2)", "(2)")
        self.assertTrue(any("never mark" in m for m in self.messages(hands)))

    def test_marked_count_without_a_file_fails(self):
        (self.folder / "hand-counts.csv").unlink()
        self.assertTrue(any("no hand-counts.csv" in m for m in self.messages(hands)))

    def test_file_not_linked_fails(self):
        self.page("[hand-counts.csv](hand-counts.csv)", "a file")
        self.assertTrue(any("link hand-counts.csv" in m for m in self.messages(hands)))

    def test_tally_that_differs_from_the_results_fails(self):
        self.write("results.json", json.dumps({**RESULTS, "hand": {"reached": 3}}))
        self.assertTrue(any("tallies" in m for m in self.messages(hands)))


class Analysis(Case):
    def test_a_silent_analysis_fails(self):
        self.page("No model analysed any data.", "The data were read.")
        self.assertEqual(len(self.messages(analysis)), 1)

    def test_the_statement_elsewhere_does_not_count(self):
        self.write("README.md", PAGE.replace("No model analysed any data.", "The data were read.")
                   .replace("12 commits summed", "No model analysed. 12 commits summed"))
        self.assertEqual(len(self.messages(analysis)), 1)


class Genre(Case):
    def test_a_case_that_names_no_genre_fails(self):
        self.page("An experience report", "A case study")
        self.assertEqual(len(self.messages(genre)), 1)

    def test_the_genre_may_be_taken_from_an_earlier_case_by_a_link(self):
        other = self.dir / "cases" / "2025-12-31-earlier"
        other.mkdir()
        (other / "README.md").write_text(PAGE)
        self.page("An experience report with repository measures, met against Runeson 2009.",
                  "As in the [earlier case](../2025-12-31-earlier/README.md).")
        self.assertEqual(self.messages(genre), [])


if __name__ == "__main__":
    unittest.main()
