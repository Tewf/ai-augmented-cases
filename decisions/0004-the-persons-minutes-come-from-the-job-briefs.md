# 0004: The person's minutes come from the job briefs

**Decision:** The measures program reads the Cost blocks that close the briefs of a case's jobs, and the case's table gains a Minutes column when it does.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- Both cases say what they did not measure: the person's time, money and tokens. Git history cannot hold them.
- The brief shape of the project repository now closes with a Cost block (record 0012 there), written by the owner when a task ends.
- A second record of the same numbers, kept for the case, would give a fact two places.

## Decision

- `measures.py --jobs FOLDER ...` reads `brief.md` in each folder and sums Tokens, Dollars and Minutes over the jobs that recorded a number.
- A value that is pending, not measured or absent adds nothing, and the output says over how many jobs each sum was taken.
- The case table gains a Minutes column in its last row only. `case-counts` asks for it when the results hold costs.
- Rejected: counting a missing value as zero, which would make a total look complete; a cost file of the case's own.

## Consequences

- **Good:** the person's minutes enter a case from the file that already holds the task, read by a program.
- **Bad:** the numbers are the owners' own meter readings; the program checks the form, not the truth.
- The two earlier cases keep their tables: they have no Cost blocks to read.

## See also

[Decisions](README.md); [the case shape](../shapes/case.md); [record 0002](0002-a-case-meets-the-readers-checklist.md).
