# User brief and comparison

**User:** Data engineer reconciling exported billing or inventory tables.

**Pain:** Row order and harmless decimal rounding obscure real missing records and cell changes; duplicate keys make joins ambiguous.

**Need:** Inferred workflow need, not verified adoption or a user request.

**Capability:** Deterministic keyed CSV join, exact Decimal tolerances, missing rows, field changes and schema drift with hard duplicate-key failures.

**Acceptance:** Order invariant join, tolerance boundary, duplicate rejection, quoted newline, missing rows and schema drift.

**Discovery:** CSV reconciliation and export validation workflows.

**Portfolio:** csvinfer detects dialect, csv-explorer views files, and json-differ compares JSON. This project performs keyed relational reconciliation rather than renaming those tools.


## Search coverage

GitHub query `csv diff in:description`, sorted by stars descending; observation 2026-10-04T12:43:43.503764+00:00. The top ten search results were screened for relevance. Search is not an exhaustive global ranking. Established comparables outside that query were also inspected; highest-star relevant comparable found among this researched set is identified below. Stars are research context, not technical performance.

Highest-star relevant comparable found: [trailofbits/graphtage](https://github.com/trailofbits/graphtage), 2488 stars; metadata refreshed 2026-10-04T13:03:36.780308+00:00.

| Comparable | Stars | Last push UTC | License | Workflow and tradeoff |
| --- | ---: | --- | --- | --- |
| [trailofbits/graphtage](https://github.com/trailofbits/graphtage) | 2488 | 2026-09-24T23:12:51Z | LGPL-3.0 | pip-installed structural diff for CSV, JSON, YAML, XML and more, using tree alignment and configurable edit costs. Prefer it for general nested structural comparison; this MVP focuses on strict table keys and Decimal tolerances. |
| [paulfitz/daff](https://github.com/paulfitz/daff) | 927 | 2026-05-27T02:55:16Z | MIT | Table alignment and patch generation with several language installers; more general editing workflow than this read-only key join. |
| [capitalone/datacompy](https://github.com/capitalone/datacompy) | 658 | 2026-10-02T17:47:28Z | Apache-2.0 | DataFrame comparison with numeric tolerances across Pandas/Polars/Spark/Snowflake; preferable when those ecosystems or scale are required. |
| [simonw/csv-diff](https://github.com/simonw/csv-diff) | 342 | 2024-09-06T05:20:04Z | Apache-2.0 | Established pip-installed keyed CSV/JSON CLI; comparison is complementary, not a claim that duplicate validation or tolerances are unavailable. |

README installation and example workflows and available recent issues were inspected. Push time does not prove active support, and mature alternatives cover broader domains. No competitor installations or equivalent performance workloads were measured. Time to first result and runtime performance comparisons are unmeasured. Tests prove only this implementation. Demand is inferred unless an issue is linked explicitly; no users, adoption or results are fabricated.
