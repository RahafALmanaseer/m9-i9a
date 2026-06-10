# Integration 9A — Query Suite Notes

## Q1 — Authors at NeurIPS

**Intent:** This query retrieves a distinct list of all authors who have published at least one research paper at the NeurIPS venue.

**Result:** - :author000
- :author001
- :author100
- :author004
- :author111

## Q2 — Papers per topic

**Intent:** This query counts the total number of papers associated with each specific research topic categorized in the dataset.

**Result:** - :topic_question-answering (3)
- :topic_language-models (6)
- :topic_vision-transformers (8)
- :topic_summarization (3)
- :topic_reinforcement-learning (4)

## Q3 — Canonical coauthor pairs

**Intent:** This query identifies unique pairs of coauthors to document collaborations, ensuring each pair is listed only once in a canonical form.

**Result:** - (:author000, :author001)
- (:author000, :author100)
- (:author000, :author004)
- (:author000, :author111)
- (:author000, :author039)

## Q4 — Papers and DOIs

**Intent:** This query lists all papers and their respective DOIs, using an optional pattern to include papers that do not have a DOI assigned.

**Result:** - (:paper000, "10.1000/p000")
- (:paper001, None)
- (:paper002, None)
- (:paper003, "10.1000/p003")
- (:paper004, None)

## Q5 — Prolific authors (ASK)

**Intent:** This query verifies if there is at least one author in the database who has published more than 10 papers.

**Result:** True

## Q6 — 2023 papers with authors (CONSTRUCT)

**Intent:** This query constructs a subgraph containing all author-paper relationships specifically for works published in the year 2023.

**Result:** 31 triples emitted.

## Q7 — Top 5 most-cited

**Intent:** This query identifies the top 5 most-cited papers by ordering them based on their citation count in descending order.

**Result:** - (:paper063, 485)
- (:paper043, 475)
- (:paper004, 473)
- (:paper007, 470)
- (:paper048, 470)

## Q8 — "Hinton" via SKOS

**Intent:** This query retrieves author URIs that match the name "Hinton" by searching across both preferred labels (skos:prefLabel) and alternative labels (skos:altLabel).

**Result:** - :author000 (matched)
- :author007 (matched)