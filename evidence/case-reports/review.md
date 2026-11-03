# Review: what the field says, by strand

Step 2 of the review, read on 2026-11-02. Strand 0 holds existing reviews; A to E answer the questions of [frame](frame.md).
Grades follow the repository's four: measured, supported with caveat, convention, not supported. Sources are in [sources](sources.md).

## Strand 0: existing reviews

- Kagdi 2007 surveys mining of repositories along four dimensions: what is mined, why, how and with what evaluation. Supported with caveat.
- Baltes 2022 reviews sampling in software engineering: random sampling is rare, and convenience sampling is popular and controversial. Measured, descriptive.
- Dingsøyr 2005 reviews the purposes and approaches of postmortem reviews. Located only.
- No review of reports written by participants of AI-assisted projects was found.

## Strand A: what makes a case or an experience report trustworthy

| Finding | Source | Grade |
|---|---|---|
| A reader's checklist of 12 items (items 39 to 50) condenses a researcher's checklist of 38 | Runeson 2009, Tables 11 to 13 | convention |
| The checklists were derived from existing checklists and the authors' experience, and fed back by an international network | Runeson 2009, abstract and Acknowledgement | convention |
| Archival data from configuration management is a third degree source, but its documents were not written for research and may miss what the case needs | Runeson 2009, section 4.4 | convention |
| The community standard for case studies has 10 essential attributes, among them the chain of evidence, the units of analysis and the selection of the case | Ralph 2020, Case Study standard | convention |
| The same standard lists the researchers' reflection on their own biases as essential, and using a large language model to analyse the data as an antipattern | Ralph 2020, Case Study standard | convention |
| A sample of one is not a valid criticism of a case study; the point is a concept that transfers | Ralph 2020; Flyvbjerg 2006b | convention; argument |
| The experience-report track asks for a take-home message, positive and negative observations, the authors' roles and limits, and quantitative results where possible | ICSE 2003 | convention, a conference call |
| A failed project can make a good experience report; the project must be completed | USENIX 2010 | convention, a conference call |
| Medicine reports one case by a 13-item checklist agreed by 27 people, with a timeline item | Gagnier 2013 | convention, by analogy |
| Behavioural science reports a single-case design by a 26-item checklist | Tate 2016 | convention, by analogy |

- The checklists of Runeson 2009 and the standard say what to report. None says how an author who took part in the case guards against his own reading; the standard asks only for reflection.
- Kitchenham 1995 and Kitchenham 2002 are the earlier guidelines; both are cited by the later ones. Convention.
- Stol 2018 places the case study among eight research strategies by obtrusiveness and generalizability. Convention.

## Strand B: measures from version control, and their bias

| Finding | Source | Grade |
|---|---|---|
| Nine perils of mining GitHub; for example 71.6% of repositories are personal projects, and many active projects work outside the platform | Kalliamvakou 2014, Table 1 and Peril IX | measured, descriptive |
| About 40% of pull requests appear unmerged though they were merged | Kalliamvakou 2014, abstract | measured, descriptive |
| The survey behind the perils had 240 respondents, a 24% response rate | Kalliamvakou 2014, section 3 | measured, descriptive |
| In git, commits may be reordered, deleted or edited as they move between repositories | Bird 2009 (secondary, abstract) | measured, descriptive |
| Only a fraction of bug fixes are labelled in histories, so datasets drawn from them are biased | Bird 2009b (secondary, abstract) | measured |
| Large commits are often ignored in studies; in nine projects they differ in intent from small ones | Hindle 2008 (secondary, abstract) | measured, descriptive |
| A study that needs all commits of a project must not rely on one hosted copy | Ralph 2020, Repository Mining standard | convention |
| A measure with one dimension standing for a many-sided construct is an antipattern | Ralph 2020, Repository Mining standard | convention |
| A commit has an author time and a committer time; the documentation of the log command does not say which one its date filters use | Git 2026 | convention, tool documentation |

- The Repository Mining standard sends a study of a few context-rich repositories to the Case Study standard. A case here sits on that border.
- Its essential list asks for the units of analysis, the justified data source, the preprocessing steps, the justified measures and the threats to external validity.

## Strand C: post-mortems and retrospectives

- A postmortem review is held after a project to capture experience for the next one (Collier 1996; Birk 2002). Convention.
- A defined process names activities, roles and artefacts, and asks that findings feed the next project's risks (Collier 1996, secondary). Convention.
- A blameless postmortem records the incident, its impact, the actions taken, the root causes and the follow-up actions (Beyer 2016). Convention, a company book.
- It looks for contributing causes in the system, not in a person. Convention.
- 155 public postmortems from game development were analysed for practices and pitfalls (Washburn 2016, secondary). Measured, descriptive.
- A community list of public postmortems states no inclusion criteria and leans toward large cloud companies (Luu 2026). Practice.
- None of these asks for a count of the decisions that reached a person.

## Strand D: measures of work with coding agents

| Finding | Source | Grade |
|---|---|---|
| 16 developers, 246 tasks of 2.0 hours on average: allowing the tools increased completion time by 19%, while developers had forecast a 24% saving | Becker 2025, abstract and section 1 | measured, a randomised trial |
| Time per issue was self-reported; screen recordings checked compliance | Becker 2025, Figure 2 and method | measured |
| One task, an HTTP server, finished 55.8% faster with the assistant | Peng 2023 (secondary, abstract) | measured, a controlled experiment |
| Users' perceptions of productivity were set beside their usage data | Ziegler 2024 (secondary, abstract) | supported with caveat, the owner's study |
| 456,535 pull requests by five agents in 61,453 repositories form a dataset; agent pull requests are accepted less often than human ones | Li 2025b, sections 1 and 3 | measured, descriptive |
| 567 pull requests from one agent in 157 projects: 83.8% merged | Watanabe 2025 (secondary, abstract) | measured, descriptive |
| 16 agents wrote a C compiler over nearly 2,000 sessions and $20,000 in API costs; the post gives two weeks for a later run on another model, and no commit count | Carlini 2026 (secondary) | owner's claim |
| Hundreds of agents on one project; locks and risk aversion cost throughput | Lin 2026 (secondary) | owner's claim |
| A practitioner says he is maybe effective at running a background agent 10 to 20% of a normal working day; all figures self-reported | Hashimoto 2026 (secondary) | practice, an example |

- The two datasets of pull requests disagree on acceptance because they cover different populations.
- Most measures here are per task, per pull request or per project; the survey and the practitioner's estimate are not. None counts the questions that reached a person in a day.

## Strand E: grey sources as evidence

- Grey sources are useful and uneven; a quality checklist of 20 criteria scores them (Garousi 2019, Table 7). Convention.
- Blog-like documents give benefits and carry quality concerns (Rainer 2019). Supported with caveat.
