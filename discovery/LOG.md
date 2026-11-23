# Vault log

Concise history of changes to the vault, for future maintainers/agents. Session notes are
written by hand; `manage_papers.py` appends one line per `discover` / `add` / `enrich` /
`lint --fix` automatically (newest last).

## 2026-11-23 — session: tooling rewrite + literature update (31 → 113 papers)

- Starting state: 36 ResearchRabbit-exported entries (4 duplicate pairs, no topics), README by year;
  only 2 papers from 2025, i.e. the "investigated up to mid-2025" claim did **not** hold for Jan–May 2025.
- Data fixes: merged 4 duplicates (Wichrowska'17, MAML, Metz'20, Metz'19);
  `learning_ren_2007` had mixed metadata (title/authors from Ören & Zeigler 2007, everything else from
  arXiv 2302.11085) → repaired as `learning_yang_2023`; topic `keywords` assigned to all entries.
- Tooling: rewrote `manage_papers.py` (discover / add / enrich / lint / readme / lo-evidence);
  config in `discovery.toml`; state + seen-candidates in `discovery/state.json`; HTTP cache `.cache/`.
  `update_papers.py` is legacy/superseded (kept, not used).
- API notes: unauthenticated Semantic Scholar returned 429 for the entire session → used arXiv +
  OpenAlex (`add --skip-s2`). Set `S2_API_KEY` / `OPENALEX_API_KEY` for future runs.
  OpenAlex stores year-only dates as YYYY-01-01 → windows are filtered by arXiv month (fixed bug that
  dropped GradMetaNet).
- Discovery windows covered: 2025-06-01 → 2026-11-23 (main) and 2025-01-01 → 2025-06-01 (backfill,
  run after the user noticed arXiv 2504.15399 was missing). Pre-2025 is **not** systematically covered
  (e.g. NFN, DWSNets, UNF absent; used only as citation seeds).
- Added 82 papers total (51 main window, 1 + 25 backfill, 5 weight-generation papers found after scoring
  tweak). Deliberately excluded: "weight-space programming" (LLMs writing weights, ~40 papers Oct–Nov 2026),
  database "learned query optimizers", two Concordia theses (their papers are included).
- LO-link classification: weight-space/metanetwork papers tagged with both `metanetworks` and
  `learned-optimizers` = work on or directly connect to learned optimizers (🔗 in the Markdown views).
  Decided from full-text evidence (`lo-evidence` → `discovery/lo_evidence.json`); strict rule: the paper
  must engage with learned optimization, a future-work or passing mention is not enough (GMN Lim'23 and the
  symmetry survey Zhao'25 are therefore *not* linked). Linked (6): NiNo (Knyazev'24), Neural Graphs
  (Kofinas'24), Zamir'25, GradMetaNet, Geometric Flow Models (Erdogan'25), ScaleGMN amortized opt (Kuipers'25).
- Views: `README.md` (by topic) and `BY_YEAR.md` (by year, by date within year); "Recently added"
  section removed at user request. `enrich --dates` filled first-appearance dates (arXiv v1 / OpenAlex);
  `learned_subramanian_2022` and `tutorial_amos_2022` have no date.

## Automatic entries

