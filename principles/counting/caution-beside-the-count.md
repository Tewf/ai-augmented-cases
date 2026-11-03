# Print the caution beside the count

**Claim:** a count taken from a repository's history is printed by a program, with the program's cautions in columns beside it.

- **Grade:** measured, descriptive, for the ways a history misleads (nine perils; commits edited and moved); convention for printing the caution beside the count.
- **Evidence:** Kalliamvakou 2014, Table 1 and Peril IX; Bird 2009 (secondary, abstract); Git 2026; Ralph 2020, Repository Mining standard. Where: [review, strand B](../../evidence/case-reports/review.md).
- **Check:** `case-counts` (exact): the case has a measures program and its test, the results of its day, the three cautions per repository, a Carried column and the program's total.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- A program takes every count it can: commits, files, tags and records for a day. It only reads the history.
- It prints three cautions per repository: commits **shared** by hash with another repository, commits **carried** under another hash, and commits whose author day differs from the committer day (**skew**).
- The case prints the Results as a table with the Carried column, and states the total the program summed.
- The numbers of the run are kept in a results file beside the case, named for its day.

## Why

- A repository is not a project, commits are reordered and rewritten as they move, and a tag is not a release on the host.
- The measures program is the form of the maintainer's rule that what a program can check is checked by a program.
- The cautions turn a bare number into one a reader can weigh: in the first case, 434 commits and 50 tags.

## Limits

- The check sees the shape of the table and the total, not whether the program counts rightly; its unit test does.
- No program can tell whether a commit was one unit of work (the review's lower bound).
- The grade for the perils is descriptive, from other datasets. Nobody has tested that printing cautions changes what a reader believes.
