# Protocol: how the pool was built

A first pass, run on 2026-11-02 by one reviewer; extended on 2026-11-03 with forward citations and a second rating (sections 11 and 12). It covers the strings run, the stopping rule and what was not searched.
Terms are in [frame](frame.md); the pool is in [sources](sources.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

## 1. Why grey literature

Garousi 2019, Table 4, answered for this topic: five of seven get a yes.

| # | Question | Answer |
|---|---|---|
| 1 | Complex, not solvable from the formal literature alone? | yes: coding agents changed in 2025 and 2026, and papers lag |
| 2 | Lack of volume or quality of evidence? | yes: no study of a day of several agent sessions was found |
| 3 | Context important? | yes: a research setting differs from a working day |
| 4 | Corroborate research with practice? | yes: company write-ups report what trials do not |
| 5 | Challenge practice with research? | yes: write-ups report no human interventions, trials do |
| 6 | Would a synthesis serve both communities? | no claim made |
| 7 | Large practitioner volume? | not measured |

## 2. Questions

Q1 to Q4 of [frame](frame.md).

## 3. Existing reviews

- Searched first. Found and read: a taxonomy survey of MSR work (Kagdi 2007) and a review of sampling in software engineering (Baltes 2022).
- Found and located only: a review of postmortem approaches (Dingsøyr 2005).
- The guideline paper itself is Runeson 2009.
- Not found: a review of experience reports or case studies written by participants of AI-assisted projects.

## 4. Formal search

Strings run on OpenAlex (title and abstract, no key, no identity), counts of that day:

| Id | String | Count | Result |
|---|---|---|---|
| F1 | "experience report" "software engineering" guidelines | 29 | none new; teaching reports |
| F2 | "post-mortem" software projects | 167 | Collier 1996 confirmed |
| F3 | "mining software repositories" bias perils | 0 | the query was wrong: the field says "promises and perils" |
| F4 | "case study research" "software engineering" guidelines | not returned | the call timed out; not rerun |

- Zero results on F3 was read as a wrong query. The term was replaced by the title words of Bird 2009 and Kalliamvakou 2014.
- Most formal works were recalled by the reviewer and then verified on Crossref or arXiv by DOI or title: about 30 lookups, no key, no identity.
- Backward snowballing: the reading lists of the Case Study and Repository Mining standards (Ralph 2020) gave Lethbridge 2005, Kitchenham 1995, Baltes 2022 and Kalliamvakou 2014.
- Forward snowballing from Runeson 2009 was not run on 2026-11-02; it was run on 2026-11-03 (section 11).

## 5. Grey search

| Id | String or site | Result |
|---|---|---|
| G1 | web: Runeson Höst guidelines checklist | the open copy of Runeson 2009 |
| G2 | web: experience report parallel AI coding agents lessons learned 2026 | Carlini 2026, Lin 2026 |
| G3 | web: guidelines for software experience report submission criteria | ICSE 2003, USENIX 2010 |
| G4 | web: Kalliamvakou perils mining GitHub | an open copy of Kalliamvakou 2014 |
| G5 | site reads: Beyer 2016, Luu 2026, Hashimoto 2026, Git 2026 | 4 pages, each read in part |

- Grey types: conference calls, a company book, company engineering posts, a personal blog, a community list, tool documentation.
- An Etsy blog post of 2012 on blameless postmortems returned HTTP 403 and was dropped; it is a lead.

## 6. Stopping rule

- Effort bounded: a first pass capped at 40 sources, 37 reached.
- Saturation, stated before searching: stop a string after 5 consecutive results that add no concept. It was applied by eye; the screened lists were not logged.

## 7. Selection

- Include: a guideline or a measure for reporting on one project; a study of repository bias; a post-mortem method; a measurement of work with coding agents.
- Exclude: tool papers, student-course reports, work on predicting defects from history.

## 8. Quality of grey sources

Garousi Table 7, 20 criteria, threshold 10. Scores are in [sources](sources.md). Hashimoto 2026 falls below the threshold after the rereading in section 12 (8.5); it is an example of practice only, as it was already used.

## 9. Extraction and synthesis

Narrative by question. Each number below was read in its source, or marked "(secondary)".

## 10. Limits

- One reviewer, no inter-rater check. Search engines personalise and change.
- Not searched: Scopus, Web of Science, Google Scholar, Semantic Scholar, Reddit, Hacker News, video, patents.
- Paywalled works could not be read: Bird 2009, Hindle 2008, Washburn 2016, Collier 1996, Birk 2002 and others are marked abstract read or located only.
- Leads not read, each a work I could name but did not open:
  - a 2017 mapping study of GitHub research, by Cosentino and colleagues;
  - a 2008 paper on the road ahead for MSR, by Hassan;
  - a 2004 tutorial on case studies for software engineers, by Perry and colleagues;
  - a 2001 book on retrospectives, by Kerth, and a 2006 book on agile retrospectives, by Derby and Larsen;
  - a 2010 survey of validity threats, by Feldt and Magazinius;
  - a 1989 paper on building theory from cases, by Eisenhardt;
  - 2009 guidelines for multiple case studies, by Verner and colleagues;
  - a 2025 roadmap for agentic software engineering, by Hassan and colleagues.
- Searches ran on 2026-11-02 and 2026-11-03; counts will differ on a rerun.
- Forward citation used OpenAlex only. Semantic Scholar was not queried.
- The second rating used one model and one text per source. Kappa rests on eight sources and is not evidence of reliability.
- Web pages (G2 to G5) were read through a page summary, not as raw text. Every number taken from them is marked "(secondary)".

## 11. Forward citation (2026-11-03)

Seeds: the three works the review cites most, counted by their exact key in [review](review.md): Ralph 2020 (5 times), Runeson 2009 (4) and Kalliamvakou 2014 (3). Each was found by DOI, then its citing works were listed from OpenAlex, with no email and no account in the request. The key was read from the local secrets file into the request and was not printed.

| Seed | Cited by (OpenAlex) | Listed | Title screen | Read by eye | Abstracts read | Added |
|---|---|---|---|---|---|---|
| Ralph 2020 (W3134402730) | 97 | 97 | 12 matched; 6 from 2023 on | 3 titles | 1 | Korn 2026 |
| Runeson 2009 (W2162739315) | 3,874 | 3,200 | 525 matched; 89 from 2023 on | about 30 titles | 2 | Rainer 2024, Lenberg 2023 |
| Kalliamvakou 2014 (W2140952846) | 806 | 806 | 272 matched; 81 from 2023 on | about 10 titles | 3 | Pinna 2026, Song 2026 |

Strings, each a case-insensitive match on the title:

- Ralph 2020: `empirical standard|case stud|mining|repositor|sampling|reporting`
- Runeson 2009: `case stud|experience report|post-?mortem|retrospective|reporting guideline|checklist|guideline`
- Kalliamvakou 2014: `github|mining|repositor|pull request|bias|perils|commit`
- Agent screen, from 2024 on: `agent|LLM|language model|copilot|\bAI\b|generative|Claude|GPT`

Notes:

- The listing of Runeson 2009 stopped at 3,200 of 3,874, because the script checked its limit after a whole page. The last 674 citing works were not listed.
- The first-pass stopping rule (five results in a row with no new concept) was not used here. The rule suits a search string, not a citation list.
- Not every regex hit was read. About 45 titles were printed and read: the hits from 2023 on, by topic and agent terms.
- Not added, because of the cap of five: Kalliamvakou's citer "Collaborator or Assistant? How AI coding agents partition work across pull request lifecycles" (2026), which bears on who merges agent work. The review does not make that point.
- Requests were spaced by half a second, with up to four tries on an error.

## 12. Second rating of the grey sources (2026-11-03)

**The rater** was `ask-mistral`, one call per source, run through a login shell that loads the Mistral export lines from the shell file. The default model was used. The criteria were Garousi 2019, Table 7, pasted as the sibling repository states them, with the rule that a part not seen scores 0. The answer was the eight subtotals and a total.

**The material** was the page text from a plain fetch on 2026-11-03, the first 12,000 characters. The reviewer read some pages through a summary, so the rater may not have read what the reviewer read.

**Before rereading**, the review's scores against the rater's subtotal sums:

| Source | Review | Rater | Difference | Review yes or no at 10 | Rater yes or no at 10 |
|---|---|---|---|---|---|
| ICSE 2003 | 12.5 | 9 | 3.5 | yes | no |
| USENIX 2010 | 11 | 7 | 4 | yes | no |
| Beyer 2016 | 15 | 18 | 3 | yes | yes |
| Luu 2026 | 12 | 10.5 | 1.5 | yes | yes |
| Carlini 2026 | 15 | 12.5 | 2.5 | yes | yes |
| Lin 2026 | 12.5 | 12 | 0.5 | yes | yes |
| Hashimoto 2026 | 10.5 | 6.5 | 4 | yes | no |
| Git 2026 | 12 | 7 | 5 | yes | no |

- Mean absolute difference: 3.0 points.
- Agreement on the threshold of 10: 4 of 8 (0.50). Kappa: 0. The review said yes for all eight; the rater said yes for four. Chance agreement is 0.50.
- The rater's own totals disagreed with its subtotals for three sources: Beyer 2016 (20 against 18), Lin 2026 (11 against 12) and Git 2026 (8 against 7). The table uses the subtotals.
- The rater put conference calls and tool documentation in tier 1. Garousi's tier 1 is books, standards, government reports and theses. The review's 0.5 stays.

**Disagreements above 3 points** were reread: ICSE 2003, USENIX 2010, Hashimoto 2026 and Git 2026.

- Beyer 2016 differs by exactly 3, so it was not reread.
- The pages were fetched again with the default client identity; the text was the same.
- The changes and their reasons are in [sources](sources.md), section "Changed on rereading". In short:

- ICSE 2003 and USENIX 2010: objectivity lowered, because a call reports no data and its organisers have an interest in submissions.
- Hashimoto 2026: authority lowered, because the page names no organisation; the earlier score used knowledge from outside the page.
- Git 2026: authority and objectivity lowered, date raised, because the page has no named author and no conclusions, and its release history gives dates.

**After rereading**:

| Source | Review | Rater | Difference | Review yes or no at 10 | Rater yes or no at 10 |
|---|---|---|---|---|---|
| ICSE 2003 | 11 | 9 | 2 | yes | no |
| USENIX 2010 | 10 | 7 | 3 | yes | no |
| Beyer 2016 | 15 | 18 | 3 | yes | yes |
| Luu 2026 | 12 | 10.5 | 1.5 | yes | yes |
| Carlini 2026 | 15 | 12.5 | 2.5 | yes | yes |
| Lin 2026 | 12.5 | 12 | 0.5 | yes | yes |
| Hashimoto 2026 | 8.5 | 6.5 | 2 | no | no |
| Git 2026 | 10.5 | 7 | 3.5 | yes | no |

- Mean absolute difference: 2.25 points, down from 3.0.
- Agreement on the threshold: 5 of 8 (0.63). Kappa: 0.25, against a chance agreement of 0.50.
- Three sources still sit on different sides of 10: ICSE 2003, USENIX 2010 and Git 2026. USENIX sits exactly at the threshold.

**What this does not show.** The reread scores are the reviewer's own reading of the page, not a third rater. Kappa on eight sources has a wide interval and is not a measure of reliability. The rater's lower scores came from its reading of tier and objectivity, not from a better reading of the pages.
