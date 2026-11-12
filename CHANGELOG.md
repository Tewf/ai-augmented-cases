# Changelog

The releases this repository pins, newest first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
A pin move is recorded here, not in decisions/.

## [Unreleased]

### Changed

- Pinned reader-ergonomics v1.24.2 (`65e4247`), from v1.21.0 (`2e5b6f0`): fixes that remove false findings in the sentence, term and figure checks, and `[defined_terms] cues`.

## [Unreleased]

### Added

- `checks/local/_cases.py` reads a case's job record, `jobs.toml` (ai-augmented-project, shapes/job-record.md); `case-counts` asks the
  Results to state the minutes it sums. 8 tests.

## [0.1.1] - 2026-11-04

### Added

- Pinned reader-ergonomics v1.21.0 (`2e5b6f0`), from v1.20.0 (`4f99372`): duplication skips the lines a declared shape prescribes
- `measures.py --jobs` reads the Cost blocks of job briefs; the case table gains a Minutes column, asked for by
  `case-counts` when the results hold costs; 3 tests of each ([record 0004](decisions/0004-the-persons-minutes-come-from-the-job-briefs.md)).

### Changed

- Pinned reader-ergonomics v1.20.0 (`4f99372`), from v1.19.2 (`b9732b9`): the runner's verdicts file (`--out`), and hand-written llms.txt lines kept through a rebuild
- Tag v0.1.1 and a GitHub release of the same name.

## [0.1.0] - 2026-11-03

First release. What it holds:

### Added

- A first review of 37 sources on reporting a project run with the method, with its frame, protocol, sources, review,
  case against, state of the art, position and baseline, and the shared bibliography.
- A card of six principles in two groups, each with its grade and a check, and the shape of a case.
- Five checks for the documents that link the shape, and 29 unit tests of them.
- Two cases, the day of 2026-10-29 and the night of 2026-11-02, with `measures.py` that takes their counts from git
  history, its 3 unit tests, and the counts it produced.
- Three decision records, the checks workflow (unit tests, then the standard's checks, with a weekly syntax and
  reference job) and the site workflow.
- Pinned reader-ergonomics v1.19.2 (`b9732b9`), the same in both workflows.

## 2026-11-02

### Added

- Pinned reader-ergonomics v1.19.2 (`b9732b9`), at the repository's start: the standard's pin, link, changelog and
  decision-record checks, which this skeleton is written to pass.
