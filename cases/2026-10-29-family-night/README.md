# Case: the day six repositories were built at once, 2026-10-29

An experience report with repository measures. Six repositories of the reader-ergonomics family were built by six working sessions of a language-model assistant and one coordinating session, for one maintainer, in one day.

**Shape:** [case](../../shapes/case.md). **Baseline:** the reader's checklist of [Runeson 2009](../../evidence/bibliography.md), met item by item below.

## Summary

- **Asked:** the maintainer asked one session to answer in his place, report at the end, and bring only what he alone decides. Later he asked that all the repositories be finished and a seventh be published.
- **Produced:** 434 commits over seven repositories, 50 tags, 47 decision records and 6 releases on the host, between 00:04 and 23:27 by the commit clock.
- **Reached the person:** 16 decisions or orders, counted by hand; the notes list 4 more that the coordinating session took.
- **Errors named:** 7, of which 1 was caught by a hook, 3 by working sessions, 1 by reviewers and 2 by the coordinating session.
- **Not measured:** the maintainer's time, money, tokens, and any control.
- **Caution:** the 434 commits are 415 distinct by author time and subject, and 50 tags are not 50 releases.

## Genre and baseline

- This is an **experience report** in the sense of ICSE 2003, with a **historical** part drawn from repositories (Ralph 2020). It is not a case study by observation.
- The report is written afterwards by a session that was none of the seven, from the maintainer's notes of the day and the seven git histories.
- The checklist of Runeson 2009 is answered in the sections below; [baseline](../../evidence/case-reports/baseline.md) maps each of its 12 items to a part.

## The case

- **Site:** seven public repositories: the standard, its five extensions (academic, presentations, software-design, learning, topic) and a seventh, blueprint, split off the topic that evening.
- **Actors:** one maintainer, one coordinating session, and one working session for the standard, one for academic and presentations together, and one each for software-design, learning, topic and the citation keys. The session count is from the notes, not from history.
- **Unit of analysis:** the repository-day, with the whole day as the frame.
- **Context:** the repositories were two days old or less. Reviews by independent reader sessions ran the same evening.
- **Outside the case:** a repository the maintainer told the coordinating session not to touch.

## Why this case

- It is the first real day of the method with several sessions at once, and the claim to test is that a coordinator absorbs most questions.
- It is a convenience case: the first one available and the one the writers know. It is chosen for what it can teach, not as typical (Baltes 2022).

## Data and procedure

| Source | Taken how | What it cannot see |
|---|---|---|
| Seven git histories | `measures.py`, a program that only reads | work not committed, history rewritten before the day, the host |
| The maintainer's notes of the day | read, then counted by hand | what the notes left out; they were kept by the coordinating session |
| A review of the family that evening | read | the same limit |

- The day is 2026-10-29 at UTC+01:00, by committer time. Author time agrees on every commit that day (skew 0).
- Tags stand for releases because git holds nothing else. The six releases on the host come from the notes.
- A decision record counts on the day its file was first added.
- The hand counts are in [hand-counts.csv](hand-counts.csv): one reader, no second check.

## Analysis

- Counts are printed as taken. Nothing is smoothed.
- Each caution is a column beside the count: commits shared by hash, commits that recur under another hash, commits whose author day differs.
- No model analysed any data. The prose was drafted by a model and is to be read by the maintainer before it counts.

## Results

Taken by [measures.py](measures.py) on the seven checkouts.

| Repository | Commits | Files | Tags | Records | Pin records | First | Last | Carried |
|---|---|---|---|---|---|---|---|---|
| reader-ergonomics | 104 | 127 | 39 | 6 | 0 | 00:29 | 23:27 | 0 |
| reader-ergonomics-academic | 56 | 72 | 1 | 0 | 0 | 00:04 | 22:36 | 6 |
| reader-ergonomics-presentations | 64 | 120 | 1 | 7 | 0 | 00:04 | 22:36 | 6 |
| reader-ergonomics-software-design | 66 | 142 | 1 | 12 | 11 | 00:04 | 22:36 | 1 |
| reader-ergonomics-learning | 42 | 112 | 1 | 4 | 0 | 13:56 | 22:36 | 0 |
| reader-ergonomics-topic | 87 | 162 | 7 | 16 | 7 | 00:21 | 22:17 | 12 |
| reader-ergonomics-blueprint | 15 | 55 | 0 | 2 | 0 | 13:39 | 21:59 | 12 |
| all | 434 | - | 50 | 47 | 18 | - | - | 37 |

- **Distinct work:** 415 pairs of author time and subject; the 37 carried commits form 19 repeats.
- **Pin records:** 18 of 47 records are titled as a move to a release. The same evening the maintainer chose that a pin raise be one line in a changelog instead.
- **Standard:** 39 tags from v1.0.0 to v1.19.2; v1.19.2 at 23:28.
- **Reached the person (by hand, 16):** 5 orders in the brief and 11 decisions from the notes.
- The 11 decisions:
  - leave one repository alone; delete the old archives; one click to amend a commit;
  - readers are outside; the night's bar; the name in public text; the pin form;
  - publish the seventh repository; the descriptions of seven repositories; one question about a release; standing push orders.
- **Absorbed (by hand, 4):** the figure rule, the citation-key rule, the academic layout, the order of two commits. The notes list these four; they do not count the questions that never reached the coordinator.
- **Errors named (by hand, 7):** by a hook 1, by working sessions 3, by reviewers 1, by the coordinating session 2, by the person 0.

## Chain of evidence

| Finding | Measure | Source |
|---|---|---|
| The day was heavy | 434 commits, 50 tags, 47 records | measures.py |
| The count overstates work | 415 distinct of 434 | measures.py, carried column |
| Tags overstate releases | 50 tags, 6 releases on the host | measures.py; notes |
| Pin raises were kept as decisions | 18 of 47 records | measures.py, pin column |
| Few questions reached the person | 16 reached, 4 absorbed and listed | notes, by hand |
| Errors were caught inside the system | none of 7 by the person | notes, by hand |

## Threats to validity

- **Construct:** a commit is not a unit of work; a tag is not a release; a record titled "move-to" is a pin raise by its slug only.
- **Internal:** no cause is claimed. The coordinator may have cut questions, or the sessions may have had few.
- **External:** one day, small text repositories with checks in CI, one maintainer. It may not carry to code.
- **Reliability:** the program can be rerun. The hand counts cannot be rerun by a program.
- **Selection of errors:** the notes record what the coordinating session thought worth noting, including its own catches.

## Triangulation

- Two sources, git and the notes, agree on heads and tags at close.
- They are not independent: the notes were kept by the session that coordinated the day.
- No interviews, no second reader of the hand counts, no timing of the maintainer.

## Roles and ethics

- The writer took no part in the day. The maintainer did, and decides publication.
- Commit authors are not shown; the program prints no names or addresses.
- Nothing confidential is cited. The notes are described, not linked, and name no private repository.

## Lessons

- Count the caution beside the count: here it cut 434 to 415 and 50 to 6.
- A coordinator can be judged by the questions that reached the person, but only if the absorbed ones are logged. Here they were not.
- A pin raise is a changelog line; 18 records of that kind show the cost of keeping it as a decision.
- Conditions: a day of one person with several sessions on text repositories. A project with code and a build may differ.
- Comparison: none yet. Later cases compare with this one, and the next might log absorbed questions as they happen.

## Method version

| Repository | Head at close | Tag |
|---|---|---|
| reader-ergonomics | b9732b9 | v1.19.2 |
| reader-ergonomics-academic | afa2f2b | v1.0.0 |
| reader-ergonomics-presentations | e79bf86 | v1.0.0 |
| reader-ergonomics-software-design | 48b497b | v1.0.0 |
| reader-ergonomics-learning | 342bfad | v1.0.0 |
| reader-ergonomics-topic | 86e14fe | v0.6.1 |
| reader-ergonomics-blueprint | f9b2408 | none |

- The reasoning did not go through the blueprint: it was built that evening and its loop is not built.

## Rerun

```sh
python3 measures.py --root path/to/checkouts --json results.json
python3 -m unittest test_measures
```

`results.json` holds the numbers of the run behind this page.

## See also

[The shape](../../shapes/case.md); [the review](../../evidence/case-reports/README.md).
