# Shape: case

A **case** is a report on one real project run with the method: what was asked, what was run, what it cost and produced, measured where a program can measure it. It is written for a reader who was absent.

Each part answers an item of the reader's checklist of Runeson 2009, the repository's baseline. Its grade is convention. The choice and the sources are in the [baseline](../evidence/case-reports/baseline.md).

Its filled example is the [first case](../cases/2026-10-29-family-night/README.md).

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

## Rules

1. The page opens with the answer, then the figure or table, then the prose.
2. A count taken by a program is printed as taken, with its caution in a column beside it.
3. A count taken by hand is marked as such, with its reader and the file that lists it.
4. A language model analyses no data of a case. It may draft prose, which a person reads before it counts.
5. Positive and negative observations both appear. A case with nothing against it is not finished.
6. A case names no tool, no private path and no private repository; its sources are described.
7. Its measures come with a program and a test, and the numbers of the run are kept beside it.

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
## See also
```

## See also

[The decisions](../decisions/README.md); [the review](../evidence/case-reports/README.md).
