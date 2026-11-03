# Frame: a report on one real project, and what the field calls it

Step 1 of the review, read on 2026-11-02. It states the problem, defines each term once, and says whether the field's name matches the repository's.
The pool is in [sources](sources.md); the searches are in [protocol](protocol.md).

**Shape:** [frame](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/frame.md)

## The problem in one sentence

How to write a report on one real project, by people who took part in it and holding counts taken from its repositories, so that a reader who was absent can trust it.

## Names

One row per term; every file of this folder uses these names.

| Term | What the field or practice means by it | Sources |
|---|---|---|
| **case study** | an inquiry into a contemporary phenomenon in its real context, by a researcher who observes it; findings carry by theory, not by sample | Runeson 2009; Yin 2018; Flyvbjerg 2006b |
| **experience report** | an account of a significant project by those who ran it, with a critical review and lessons; a "how we did it" account without lessons is a known mistake | ICSE 2003; USENIX 2010 |
| **post-mortem**, **postmortem review**, **retrospective** | a review held after a project to capture what went right and wrong, for the next one | Collier 1996; Birk 2002; Dingsøyr 2005 |
| **blameless postmortem** | an incident review that looks for contributing causes in the system, not in a person | Beyer 2016 |
| **mining software repositories (MSR)** | taking data from version control, issue trackers and forums, and analysing it | Kagdi 2007; Ralph 2020 |
| **third degree data** | work artefacts that already exist, such as a repository history, collected without contact with the people | Runeson 2009 |
| **historical case study** | a case study that draws on archival data, for instance software repositories | Ralph 2020 |
| **chain of evidence** | the traceable path from an observation to a finding | Runeson 2009 |
| **triangulation** | using several data sources, methods or observers on one finding | Runeson 2009 |
| **construct validity** | whether a measure stands for the thing it is meant to measure; a commit count stands for work only under conditions | Runeson 2009; Ralph 2020 |
| **case report** | the medical genre for one patient, with a 13-item reporting checklist | Gagnier 2013 |
| **single-case design** | a study of one unit with repeated measures, with a 26-item reporting checklist | Tate 2016 |

## Sub-questions

| # | Question | Where answered |
|---|---|---|
| Q1 | Which measures can a program take from a repository's history alone, and with what bias? | [review](review.md) strand B |
| Q2 | How is a report written by a participant made trustworthy to an absent reader? | [review](review.md) strands A, C |
| Q3 | What has been measured about people working with coding agents, and how? | [review](review.md) strand D |
| Q4 | Against what is one case compared? | [position](position.md) |

The front page's third question, what the first day cost and produced, is answered by the case, not by the review.

## The field's name against the repository's

- The repository says **case**. The field says **case study** when a researcher observes, and **experience report** when participants write.
- The community standard for case studies excludes the experience report from its scope: "Is not an experience report" (Ralph 2020, Case Study standard, Application).
- A report here is written by a participant and holds archival counts. It is an experience report with repository measures, or a historical case study written from inside.
- The name stays, as the brief asks: **case** is short, and each page says which genre it is.
- Practice has its own names: lessons learned, post-mortem, incident review, engineering write-up. They share the genre, not the method.
