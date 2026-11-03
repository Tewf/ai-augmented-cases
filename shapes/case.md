# Shape: case

A **case** is a report on one real project run with the method: what was asked, what was run, what it cost and produced, measured where a program can measure it. It is written for a reader who was absent.

Each part answers an item of the reader's checklist of Runeson 2009, the repository's baseline. Its grade is convention. The choice and the sources are in the [baseline](../evidence/case-reports/baseline.md).

Its filled examples are the [first case](../cases/2026-10-29-family-night/README.md) and the [second case](../cases/2026-11-02-eight-first-jobs/README.md); each carries a `**Shape:**` line back to this page.

## When to use it

- A project is finished or has a closed period, such as a day, and the writers took part in it.
- Part of what is said can be counted by a program from a repository's history.
- It is not for a study by an outside observer; that is a case study, with its own standard.

## Parts, in order

| Part | It holds | Item | Evidence |
|---|---|---|---|
| Summary | the asked, the produced, the counts and their cautions, in a few lines | 39 | overview first: measured |
| Genre and baseline | which genre this is, and the checklist it meets | 42 | convention |
| The case | site, actors, unit of analysis, context, what lies outside | 40 | convention |
| Why this case | why it suits the questions, and if it is a convenience case, that | 41 | convention |
| Data and procedure | each source, how it was taken, what it cannot see | 43 | convention |
| Analysis | how the data were read, and that no model analysed them | 45 | convention |
| Results | every count as taken, with the caution beside it | 44 | convention |
| Chain of evidence | each finding, its measure, its source | 46 | convention |
| Threats to validity | construct, internal, external, reliability, and selection | 47 | convention |
| Triangulation | the sources, and which were not independent | 48 | convention |
| Roles and ethics | who wrote, who took part, what is confidential | 49 | convention |
| Lessons | what carries over, under what conditions, good and bad | 50 | convention |
| Method version | the commit of each member the case ran with, and whether the reasoning went through the blueprint | none | repository rule |
| Rerun | the command that retakes the numbers | 45 | measured, for programs |

## The measures table

The Results part prints what the program took as a table of one form, so that every case reads alike and the check finds it.

| Repository | Commits | Files | Tags | Records | First | Last | Carried | Minutes |
|---|---|---|---|---|---|---|---|---|
| one row per repository | committer time on the day | distinct paths those commits touch | tags created on the day | decision records first added | first commit | last commit | commits that recur under another hash | the person's minutes, only in the last row |

- A last row **all** sums the columns that add. Under the table, one line states the commits summed, the distinct pairs of author time and subject, and the pin or move records where the case has them.
- The Carried column is required: it is the caution that turns a commit total into distinct work. Shared may stand beside it, as in the second case; shared and skew are in the results file and named in the prose when they are not zero.
- Minutes is the person's minutes, summed by the program from the Cost blocks that close the job briefs (`measures.py --jobs`). It stays out of the table when the case has no such blocks. A job whose Cost is pending or not measured adds nothing, and the line under the table says how many jobs the sum covers, so a total is never read as complete.
- A number taken by hand never enters this table; it follows it in a list, each item marked (by hand, n).
- A day that crosses midnight gets a second table for the second day, with the columns it has.

## Rules

1. The page opens with the answer, then the figure or table, then the prose.
2. A count taken by a program is printed as taken, with its caution in a column beside it.
3. A count taken by hand is marked as such, with its reader and the file that lists it.
4. A language model analyses no data of a case. It may draft prose, which a person reads before it counts.
5. Positive and negative observations both appear. A case with nothing against it is not finished.
6. A case names no tool, no private path and no private repository; its sources are described.
7. Its measures come with a program and a test, and the numbers of the run are kept beside it.
8. The Analysis says that no model analysed the data; the Genre says experience report.

## Skeleton

Copy the headings below into `cases/<date>-<name>/README.md`, and add `measures.py`, its test and `results.json` beside it.

```markdown
# Case: <what, when>

**Shape:** [case](../../shapes/case.md). **Baseline:** the reader's checklist of Runeson 2009.

## Summary
## Genre and baseline
## The case
## Why this case
## Data and procedure
## Analysis
## Results
## Chain of evidence
## Threats to validity
## Triangulation
## Roles and ethics
## Lessons
## Method version
## Rerun
## Worked example

The [first case](../cases/2026-10-29-family-night/README.md) is the full example: each part is filled, the measures table has the form above, and the hand counts follow it in a list. The [second case](../cases/2026-11-02-eight-first-jobs/README.md) shows a case that reuses an earlier case's program and genre by a link, and a night that crosses midnight.

## The principles it applies

| Part | Principle | Check |
|---|---|---|
| Results | [Print the caution beside the count](../principles/counting/caution-beside-the-count.md) | `case-counts` |
| Results | [Distinct work over raw commits](../principles/counting/distinct-work-over-commits.md) | `case-distinct` |
| Results, Data and procedure | [A hand count is marked](../principles/counting/hand-counts-are-marked.md) | `case-hand-counts` |
| Genre and baseline | [A participant's report is an experience report](../principles/reporting/participants-write-experience-reports.md) | `case-genre` |
| All parts | [Answer the reader's checklist](../principles/reporting/answer-the-readers-checklist.md) | `shape-conformance` |
| Analysis | [No model analyses the data](../principles/reporting/no-model-analyses-the-data.md) | `case-analysis` |

## See also
```

## See also

[The standard card](../standard.md); [the decisions](../decisions/README.md); [the review](../evidence/case-reports/README.md).
