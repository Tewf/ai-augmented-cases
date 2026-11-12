# The case-reporting standard

How to report one real project run with the AI-augmented method, as far as the review of case reports goes.
A case is written by the people who took part, with the counts a program can take from the history and the cautions
that go beside them. It extends
[reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/standard.md):
read that one first.

This page adds only what a case changes. Its reader was absent from the project and decides whether the numbers can be trusted.

## How to use it

1. **Copy the shape** [case](shapes/case.md) into `cases/<date>-<name>/README.md`, and keep its `**Shape:**` line:
   the checks find a case by it.
2. **Take the counts with a program.** Add a measures program, its test and the results of the run beside the
   case. A count by hand is marked, listed in `hand-counts.csv` and follows the table.
3. **Write to the principles** below, and to those of reader-ergonomics, which still hold.
4. **Check:** run the standard's checks on the repository. `case-counts`, `case-distinct`, `case-hand-counts`,
   `case-genre` and `case-analysis` read each case; `shape-conformance` finds its headings. The programs and their
   tests are in [checks/local/](checks/local/).

Grades mean what they mean in
[reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/standard.md#grades):
measured, supported with caveat, convention, not supported. Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Counting: what a program takes from a history, and how it is printed

| Principle | Claim | Grade |
|---|---|---|
| [Print the caution beside the count](principles/counting/caution-beside-the-count.md) | a count taken from a repository's history is printed by a program, with the program's cautions in columns beside it. | measured, descriptive, for the ways a history misleads (nine perils; commits edited and moved); convention for printing the caution beside the count |
| [Distinct work over raw commits](principles/counting/distinct-work-over-commits.md) | a case states the distinct work behind its commit total, counted as distinct pairs of author time and subject, because a commit may recur under another hash. | measured, descriptive, on other datasets; measured in one case, where 434 commits summed over seven repositories are 415 distinct |
| [A hand count is marked](principles/counting/hand-counts-are-marked.md) | a count taken by hand is marked as such in the page, listed row by row in a file, and equal to the tally the results record. | convention, the maintainer's practice, written down for the review; no study tests it |

### Reporting: how a report by its participants is made trustworthy

| Principle | Claim | Grade |
|---|---|---|
| [Answer the reader's checklist](principles/reporting/answer-the-readers-checklist.md) | a case holds a part for each of the 12 items of the reader's checklist of Runeson 2009, in a fixed order. | convention; no study shows that meeting the checklist makes a report more trusted |
| [No model analyses the data](principles/reporting/no-model-analyses-the-data.md) | a case states that no language model analysed its data; a model may draft the prose, which a person reads before it counts. | convention |
| [A participant's report is an experience report](principles/reporting/participants-write-experience-reports.md) | a case written by those who took part names its genre, an experience report with repository measures, and the baseline it meets. | convention |

<!-- principles:end -->

## Where the evidence is

Every principle links its review in [evidence/](evidence/README.md), and every work cited is listed once in the
[bibliography](evidence/bibliography.md).
