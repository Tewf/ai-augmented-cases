# Distinct work over raw commits

**Claim:** a case states the distinct work behind its commit total, counted as distinct pairs of author time and subject, because a commit may recur under another hash.

- **Grade:** measured, descriptive, on other datasets; measured in one case, where 434 commits summed over seven repositories are 415 distinct.
- **Evidence:** Bird 2009 (secondary, abstract); Hindle 2008 (secondary, abstract); Ralph 2020, Repository Mining standard. Where: [review, strand B](../../evidence/case-reports/review.md); [against](../../evidence/case-reports/against.md).
- **Check:** `case-distinct` (exact): the Results state the distinct pairs the program counted, and say distinct.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- Beside the commit total, the case states the number of distinct pairs of author time and subject.
- When the two numbers are equal, it says so: the second case reports 28 commits, all distinct.
- The reader sees the gap, not only the smaller figure.

## Why

- A history moved from one repository to another is rewritten, and the same work then counts twice.
- Large commits differ in intent from small ones, so a sum of commits is not a sum of work.
- A pair of author time and subject is a proxy; it is cheap, and a program can take it.

## Limits

- Two commits of the same subject in the same second would merge into one pair; none was seen in either case.
- A distinct pair is still not a unit of work.
- The evidence for rewritten histories is read from abstracts (secondary); the 415 is read from our own run.
