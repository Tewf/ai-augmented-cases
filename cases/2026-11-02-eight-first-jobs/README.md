# Case: the night eight repositories had their first job, 2026-11-02

An experience report with repository measures. Eight repositories were set up in the afternoon with a scope and nothing else. In the evening, eight owner sessions of a language-model assistant gave each its first job, in two batches of four, under one coordinating session, for one maintainer.

**Shape:** [case](../../shapes/case.md). **Baseline:** the reader's checklist of [Runeson 2009](../../evidence/bibliography.md), met item by item below.

## Summary

- **Asked:** the maintainer asked for the first job of each of eight repositories, under a budget gate, without stopping on anything that was not blocking.
- **Produced:** 33 commits over eight repositories between 15:57 on 2026-11-02 and 00:42 on 2026-11-03. 12 were the afternoon set-up and 21 were the jobs. 16 decision records, 0 tags.
- **Reached the person:** 6 decisions, counted by hand. About 8 messages from the person came during the jobs; they are not itemised.
- **Stalls:** 5 owner runs stopped on a network switch and were resumed. 7 first-pass reviews and 2 programs came back. 8 pushes were made, one held two hours.
- **Errors named:** 3, of which 1 was caught by a hook and 2 by the owner sessions that made them.
- **Not measured:** the maintainer's time, money and tokens, and any control.
- **Caution:** the jobs' commits share timestamps within a repository, so commit time shows when a job was integrated, not when it was worked.

## Genre and baseline

- This is an **experience report** in the sense of ICSE 2003, with a **historical** part drawn from repositories (Ralph 2020). It is not a case study by observation.
- It is written afterwards by a session that was none of the nine, from the maintainer's notes of the night and the eight git histories.
- The checklist of Runeson 2009 is answered in the sections below; the [baseline](../../evidence/case-reports/baseline.md) maps each of its 12 items to a part.
- It follows the [first case](../2026-10-29-family-night/README.md) and runs its program, with one added option, on eight other repositories.

## The case

- **Site:** eight public repositories. Two belong to the reader-ergonomics family (project, family). Six belong to the AI-augmented family: the hub, project, ide, agents, foundations and this one.
- **Actors:** one maintainer, one coordinating session, and eight owner sessions, one per repository. The count of sessions is from the notes, not from history.
- **Unit of analysis:** the repository-night, from the afternoon set-up to the last push of the night.
- **Context:** each repository was a front page and one decision record, hours old. Two batches of four ran in parallel. A budget gate stopped a batch from launching above a share of the weekly limit.
- **Outside the case:** two further jobs of the same night, a logo and a travelling-salesman study, which touched no one of these repositories.

## Why this case

- It is the first night when a coordinator ran owners in two parallel batches, which the first case could only suggest.
- It is a convenience case: the next one available and the one the writers know. It is chosen for what it can teach, not as typical (Baltes 2022).

## Data and procedure

| Source | Taken how | What it cannot see |
|---|---|---|
| Eight git histories | the [measures program](../2026-10-29-family-night/measures.py), which only reads | work not committed, the host, pushes and CI |
| The maintainer's notes of the night | read, then counted by hand | what the notes left out; they were kept by the coordinating session |
| Each job's own notes | read | the same limit, per owner |

- The days are 2026-11-02 and 2026-11-03 at UTC+01:00, by committer time. The night crosses midnight, so the program runs twice. Author time agrees on every commit (skew 0).
- The checkouts are pinned at the heads in the table under Method version, so later commits do not enter.
- A decision record counts on the day its file was first added.
- The set-up and job split is by hand from a git query: a commit before 17:00 on 2026-11-02 is set-up. The program does not print it.
- The hand counts are in [hand-counts.csv](hand-counts.csv): one reader, no second check.

## Analysis

- Counts are printed as taken. Nothing is smoothed.
- Each caution is a column beside the count: commits shared by hash, commits that recur under another hash, commits whose author day differs.
- No model analysed any data. The prose was drafted by a model and is to be read by the maintainer before it counts.

## Results

Taken by the program on the eight pinned checkouts, for 2026-11-02.

| Repository | Commits | Files | Tags | Records | First | Last | Shared | Carried |
|---|---|---|---|---|---|---|---|---|
| ai-augmented | 4 | 21 | 0 | 1 | 15:57 | 23:31 | 0 | 0 |
| ai-augmented-project | 4 | 33 | 0 | 2 | 15:57 | 23:17 | 0 | 0 |
| ai-augmented-ide | 3 | 32 | 0 | 2 | 15:57 | 23:48 | 0 | 0 |
| ai-augmented-agents | 4 | 33 | 0 | 2 | 15:57 | 23:54 | 0 | 0 |
| ai-augmented-foundations | 3 | 43 | 0 | 2 | 15:57 | 23:28 | 0 | 0 |
| ai-augmented-cases | 2 | 19 | 0 | 1 | 15:57 | 16:03 | 0 | 0 |
| reader-ergonomics-project | 4 | 33 | 0 | 2 | 15:57 | 23:22 | 0 | 0 |
| reader-ergonomics-family | 4 | 33 | 0 | 3 | 16:44 | 23:57 | 0 | 0 |
| all | 28 | - | 0 | 15 | - | - | 0 | 0 |

For 2026-11-03, two repositories had commits.

| Repository | Commits | Files | Records | First | Last |
|---|---|---|---|---|---|
| ai-augmented | 2 | 17 | 0 | 00:13 | 00:13 |
| ai-augmented-cases | 3 | 27 | 1 | 00:42 | 00:42 |
| all | 5 | - | 1 | - | - |

- **Together:** 33 commits, all distinct by hash and by author time with subject. 16 records. 0 tags. No history was rewritten, unlike the first case.
- **Set-up and jobs (by hand from a git query):** 12 commits and 8 records before 17:00; 21 commits and 8 records after.
- **Job commits come in bursts:** the final commits of a job share one second, so the 21 are the integration of eight jobs, not 21 working steps.
- **Reached the person (by hand, 6):** four scope questions answered together, one placement question, one hook allowance. About 8 messages came during the jobs; no list of them exists.
- **Stalls (by hand, 5):** the notes name four, jobs C and D, then C and F again. The fifth is from the brief and the notes do not place it. One stall left nothing written.
- **Returns (by hand):** 7 first-pass reviews, 2 programs, one job returning both.
- **Pushes (by hand, 8):** one per repository. One waited two hours on a hook allowance for a cited title; the person gave it. Local git cannot see a push.
- **Errors named (by hand, 3):** by a hook 1, by the owner sessions 2, by the person 0.
- **Found in earlier work, not made that night (by hand, 3):** a repeated record number, a mismatched bibliography row, a name spelled two ways. All three went to the maintainer unfixed.
- **Cost, partly:** the notes give tokens and minutes for two jobs only, about 250 thousand and 35 minutes, and 326 thousand and 83 minutes.

## Chain of evidence

| Finding | Measure | Source |
|---|---|---|
| Little code-history, much text | 33 commits, 0 tags, 16 records | measures program |
| Commit count overstates steps | 21 job commits from 8 jobs, in bursts | measures program; git query by hand |
| Few questions reached the person | 6 decisions | notes, by hand |
| Stalls were common and cheap | 5 resumed, none lost | notes, by hand |
| Errors were caught inside the system | none of 3 by the person | notes, by hand |
| A hook gated the output | 1 push held 2 hours | notes, by hand |

## Threats to validity

- **Construct:** a commit is not a unit of work, and here commits are integration points. A push is not seen by git.
- **Internal:** no cause is claimed. Few questions may come from clear briefs, a good coordinator, or small jobs.
- **External:** one night, small text repositories, one maintainer, and briefs written beforehand. It may not carry to code.
- **Reliability:** the program can be rerun, with the pinned heads. The hand counts cannot be rerun by a program.
- **Selection of errors:** the notes record what the coordinating session and the owners thought worth noting.
- **Selection of the case:** it follows a case by the same writers and shares their reading of the notes.

## Triangulation

- Git and the notes agree on every head at close and on the number of jobs.
- They are not independent: the notes were kept by the session that coordinated the night.
- Each job's own notes add a third reading, written by the owner, and agree with the coordinating notes where they overlap.
- No interviews, no second reader of the hand counts, no timing of the maintainer.

## Roles and ethics

- The writer took no part in the night. The maintainer did, and decides publication.
- Commit authors are not shown; the program prints no names or addresses.
- Nothing confidential is cited. The notes are described, not linked, and name no private repository.

## Lessons

- A history of eight small jobs holds few commits. Count jobs, returns and stalls beside commits.
- Log the absorbed questions as they happen. This night the person's messages were counted as "about 8", which the first case already warned about.
- A stall that writes nothing costs a full resume; asking each step to be written as it exists is the cheap remedy the owners used.
- A hook that refuses a title is a gate worth its two hours when the allowance is a person's call.
- Comparison with the first case: 6 decisions reached the person against 16, over 33 commits against 434. The two days differ in kind, so the ratio proves nothing.
- Conditions: a night of one person with parallel sessions on text repositories and a gate on budget. Code with a build may differ.

## Method version

Heads at close, the commits the checkouts are pinned to for the rerun.

| Repository | Head at close | Tag |
|---|---|---|
| reader-ergonomics-project | e2a1681 | none |
| reader-ergonomics-family | 2319de2 | none |
| ai-augmented | e2e1d28 | none |
| ai-augmented-project | f0ae983 | none |
| ai-augmented-ide | a2be991 | none |
| ai-augmented-agents | 4012e95 | none |
| ai-augmented-foundations | 74aef93 | none |
| ai-augmented-cases | 82fade4 | none |

- The reasoning did not go through the blueprint: its loop is not built.
- The program is the first case's, with the option `--repos` added in this repository.

## Rerun

Clone each repository beside the others and reset it to its head above, then run from this folder:

```sh
python3 ../2026-10-29-family-night/measures.py --root path/to/checkouts --day 2026-11-02 \
  --repos ai-augmented ai-augmented-project ai-augmented-ide ai-augmented-agents ai-augmented-foundations \
          ai-augmented-cases reader-ergonomics-project reader-ergonomics-family \
  --hand hand-counts.csv --json results-2026-11-02.json
python3 ../2026-10-29-family-night/measures.py ... --day 2026-11-03 --json results-2026-11-03.json
python3 -m unittest discover -s ../2026-10-29-family-night
```

The second command takes the same options as the first. The two `results-` files hold the numbers of the run behind this page.

## See also

[The shape](../../shapes/case.md); [the first case](../2026-10-29-family-night/README.md); [the review](../../evidence/case-reports/README.md).
