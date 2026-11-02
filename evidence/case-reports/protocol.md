# Protocol: how the pool was built

A first pass, run on 2026-11-02 by one reviewer. It covers the strings run, the stopping rule and what was not searched.
Terms are in [frame](frame.md); the pool is in [sources](sources.md).

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
- Forward snowballing from Runeson 2009 was not run.

## 5. Grey search

| Id | String or site | Result |
|---|---|---|
| G1 | web: Runeson Höst guidelines checklist | the open copy of Runeson 2009 |
| G2 | web: experience report parallel AI coding agents lessons learned 2026 | Carlini 2026, Lin 2026 |
| G3 | web: guidelines for software experience report submission criteria | ICSE 2003, USENIX 2010 |
| G4 | web: Kalliamvakou perils mining GitHub | an open copy of Kalliamvakou 2014 |
| G5 | site reads: Beyer 2016, Luu 2026, Hashimoto 2026, Git 2026 | read in part |

- Grey types: conference calls, a company book, company engineering posts, a personal blog, a community list, tool documentation.
- An Etsy blog post of 2012 on blameless postmortems returned HTTP 403 and was dropped; it is a lead.

## 6. Stopping rule

- Effort bounded: a first pass capped at 40 sources, 37 reached.
- Saturation, stated before searching: stop a string after 5 consecutive results that add no concept. It was applied by eye; the screened lists were not logged.

## 7. Selection

- Include: a guideline or a measure for reporting on one project; a study of repository bias; a post-mortem method; a measurement of work with coding agents.
- Exclude: tool papers, student-course reports, work on predicting defects from history.

## 8. Quality of grey sources

Garousi Table 7, 20 criteria, threshold 10. Scores are in [sources](sources.md); none fell below the threshold, one sits at 10.5.

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
- Searches ran on 2026-11-02; counts will differ on a rerun.
- Web pages (G2 to G5) were read through a page summary, not as raw text. Every number taken from them is marked "(secondary)".
