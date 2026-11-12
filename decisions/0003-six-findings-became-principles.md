# 0003: Six findings became principles, the rest stayed findings

**Decision:** the card holds six principles: three about counting, whose grades are measured or convention, and three about reporting, all convention, each enforced by a program or by the standard's shape check. Findings the review graded without a rule a program can check stay in the review.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/shapes/decision-record.md).

## Context

- The review has seven claims, each graded ([review front page](../evidence/case-reports/README.md)). The standard asks a principle to carry a grade and a check.
- The measures program of the first case already checks a count by running; the repository's rule is that what a program can check is checked by a program.
- The family's cards list principles with a Check line; a principle with no registered check fails `principle-coverage`.

## Decision

- **Became principles, counting:**
  - print the caution beside the count (measured, descriptive, for the perils; `case-counts`);
  - distinct work over raw commits (measured, descriptive, and measured in one case; `case-distinct`);
  - a hand count is marked (convention; `case-hand-counts`).
- **Became principles, reporting:** a participant's report is an experience report (`case-genre`), the reader's checklist is answered part by part (`shape-conformance`) and no model analyses the data (`case-analysis`); all three are convention.
- `measures.py` is the program behind the counting principles; the new checks read what it prints, and its unit test stays beside it.
- **Stayed findings:**
  - studies of coding agents measure a task, not a day (measured per study; the gap is of this search);
  - company write-ups report sessions and cost (owner's claim);
  - medicine's case checklists (by analogy) and postmortem practice (convention);
  - no test shows that a checklist makes a case more trusted (untested).

## Options that lost

| Option | Why it lost |
|---|---|
| One principle per claim of the review | the claims about agent studies and company posts have no check a program can run, so they would name none |
| Only the two measured findings | the other four rules are already enforced by a program or by the shape check; leaving them out leaves them without a grade or a reason |
| Copying the shape into `shapes/examples/` | the two cases are the examples and carry the Shape line; a copy would give a fact two places |

## Consequences

- **Good:** every principle names a registered check, and CI runs the tests of the new ones.
- **Bad:** four of six grades are convention, which is what the review found; the card does not claim more.
- **Bad:** `case-analysis` and `case-genre` see a statement, not the practice. The maintainer confirms the statement.
- **To keep true:** a new case follows the shape and carries the program, test, results and hand counts the checks look for; a later case may link an earlier case's program and genre.

## See also

[Decisions](README.md); [the card](../standard.md); [the review](../evidence/case-reports/README.md).
