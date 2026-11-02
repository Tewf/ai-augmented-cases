# State of the art: the record on each question

Step 3 of the review. For each question: the best evidence, kept apart from the practice most adopted, and the limits.
Terms are in [frame](frame.md); the findings behind each line are in [review](review.md).

## Q1: measures from a history alone

| Record | Holder | Basis | Grade |
|---|---|---|---|
| Best evidence | Kalliamvakou 2014: nine perils, with counts, on a large public dataset and a manual sample | measured, descriptive | measured, descriptive |
| Best evidence on bias of labelled data | Bird 2009b | measured | measured |
| Most adopted | counts of commits, files and releases per period, in dashboards and write-ups | no study of their meaning for work | convention, untested |

- Upper bound, what has been shown: a history can be rewritten, partial, or hosted in several places; a repository is not a project.
- Lower bound, what is impossible: no program can tell from a count whether a commit was one unit of work.
- Not found: a validated measure of work from commits alone.

## Q2: trust in a report by a participant

| Record | Holder | Basis | Grade |
|---|---|---|---|
| Best evidence | none: the guidelines are conventions built from other guidelines and experience | no study tests whether a checklist makes a report more trusted | convention |
| Most adopted | the reader's checklist of Runeson 2009; the Empirical Standards of Ralph 2020 | cited and used by reviewers | convention |
| Nearest practice | the experience-report call of ICSE 2003 | a conference's criteria | convention |

- Upper bound: the standards say what to report and what counts as an antipattern.
- Lower bound: a participant cannot be a neutral observer; the field answers with disclosure of roles and with triangulation.
- Medicine reports one case by a consensus checklist (Gagnier 2013), after finding case reports without guidance too loose. By analogy only.

## Q3: measures of work with coding agents

| Record | Holder | Basis | Grade |
|---|---|---|---|
| Best evidence | Becker 2025: a randomised trial of 16 developers | self-reported time, checked by recordings | measured |
| Largest | Li 2025b: 456,535 pull requests | a dataset of public pull requests | measured, descriptive |
| Most adopted | company write-ups of sessions, tokens and cost (Carlini 2026; Lin 2026) | owner's claim | practice |

- Upper bound: a trial can say whether tasks took longer; a dataset can say whether pull requests were merged.
- Not found in this pool: a measure of a day of several sessions, or of the questions that reached the person.

## Q4: comparison

- A single case does not compare with a control; the standard calls a sample of one an invalid criticism (Ralph 2020).
- Generalization is by concept: what the case teaches carries over if its context is described (Flyvbjerg 2006b, Ralph 2020).
- The family's comparison is therefore the method's own earlier cases, and a contrast inside one case. Convention.
