# Data and validity moat — is a structured-interview data asset real?

Unit: `data-outcomes` · Run: zf-ashley-moat · All items seen 2026-09-23 unless noted.
Method: web search (Z.ai built-in) + direct fetch of key abstracts. Several academic/vendor sources
resolved at domain level in search results rather than full article URLs; pinpoint citations are given
in prose so the director can retrieve them. Flagged in §8 where a quote comes from a search snippet
rather than a fetched page.

---

## 1. Summary

- "Valid" in this market means criterion-related validity against job performance, demonstrated with
  real labeled outcomes, plus adverse-impact monitoring under the EEOC Uniform Guidelines. The
  structured interview is the best-validated common procedure: r = .51 (Schmidt & Hunter 1998),
  revised to r = .42, top-ranked, in Sackett et al. 2022.
- LLM-scored interviews are a live research area (2023–2026), not settled science: evidence shows
  usable reliability when multiple LLM ratings are aggregated, but documented accent/cultural scoring
  bias and high prompt sensitivity. No large-scale criterion-validity study of LLM interview scoring
  with real hiring outcomes is publicly available yet.
- Vendors' "science" is mostly internal technical manuals, self-published reports, and volume claims
  (HireVue: 1M+ interviews/month at peak; Sapia.ai: 6.7M+ cumulative). Independent verification is
  thin — one external audit of HireVue's manual, peer-reviewed studies of game-based assessments,
  and essentially nothing for Paradox.
- Transcripts do not compound — incumbents already have millions. What compounds is **outcome labels**
  (hired / retained / performance-rated) linked to transcripts, pooled across customers, on a stable
  instrument. That loop closes via ATS/HRIS integrations, which competitors can also build.
- Pooling is legally constrained (GDPR purpose limitation, Illinois AIVIA 30-day deletion, customer
  data-ownership terms) but doable with consent architecture designed in advance.
- Volume math: at 1,000 interviews/month a cross-customer model per role family is ~a decade away;
  at 10,000/month it is 1–4 years for top role families; at 100,000/month it arrives within the
  first year. No published hiring-specific learning curve exists; estimates below are derived from
  validation-statistics first principles.
- **Verdict: a data moat is real but slow and conditional.** It is not achievable in the next 12
  months at Ashley's plausible early volumes; the near-term defensible asset is per-customer outcome
  instrumentation plus a published validation methodology, which converts into a cross-customer model
  only at roughly sustained 10k+ interviews/month.

---

## 2. Validity requirements

What a legally defensible, predictive structured interview requires, with exact figures.

**Meta-analytic validity (the headline numbers any RFP will ask for):**

| Source | Figure | Quote / note | source_url |
|---|---|---|---|
| Schmidt & Hunter (1998), *Psychological Bulletin*, 85 years of research | Structured interview r = .51; unstructured r = .38; GMA r = .51; work sample r = .54 | Both structured interviews and GMA "had a validity of .51" (search-synthesized); "cited by 8014" | https://psycnet.apa.org (search-domain; citation: Schmidt & Hunter, 1998, 124(2), 262–274) |
| Sackett et al. (2022), *Journal of Applied Psychology* re-analysis | Structured interview mean validity **.42**, top-ranked of all procedures; GMA falls to .31; 80% credibility interval .18–.66 (later Lievens et al. update: .24–.66) | "Structured interviews emerged as the top-ranked selection procedure. validity estimates of .42 for structured interviews" | https://gwern.net (hosts paper discussion) and PubMed (search-domain; citation: Sackett, Zhang, Berry & Lievens, 2022) |

The Sackett revision matters strategically: it corrected older over-corrections (range restriction,
unreliability), which *lowered* every estimate but *promoted* the structured interview to #1. The
product Ashley already is (structured, same questions, same rubric, transcript-only scoring) sits on
the single best-validated selection procedure in I/O psychology — the rubric quality itself is most
of the validity, before any proprietary data.

**Legal defensibility (US):**

- EEOC **Uniform Guidelines on Employee Selection Procedures** (29 CFR Part 1607, adopted 1978;
  clarifying Q&A Mar 1, 1979). Three validation routes: criterion-related, content, construct.
  Criterion-related validity "should consist of empirical data demonstrating that the selection
  procedure is predictive of or significantly correlated with important elements of work behavior"
  (paraphrase of 29 CFR 1607.5(b); search-snippet level). source_url: https://www.uniformguidelines.com
  and https://www.eeoc.gov
- **Four-fifths rule** (29 CFR 1607.4(D)): a selection rate for any race, sex, or ethnic group less
  than 4/5 (80%) of the highest group's rate "will generally be regarded as evidence of adverse
  impact." A rule of thumb, not a safe harbor — small samples can mask impact, large samples can make
  trivial gaps significant. source_url: https://www.law.cornell.edu (29 CFR 1607.4)
- **Sample sizes:** the Uniform Guidelines set **no fixed minimum N** but endorse validity
  generalization and note "technical feasibility" for small samples. Practitioner guidance: "sample
  sizes be at least 30 and need not be larger than 500 (at 500, sample error will not exceed 10
  percent of the standard...)". source_url: https://iosolutions.com (search-snippet). In practice,
  litigation-defensible criterion studies for a single employer rarely run below N ≈ 100–200 hires;
  transportability arguments (validity generalization) are used below that.
- **Reliability** is a precondition: inter-rater reliability of human structured-interview raters is
  commonly r ≈ .54–.79 for single raters (see §3, Wiley paper) — the benchmark an automated rater
  must meet or beat.

**Implication for Ashley:** the bar for "our data makes scoring better" is not "we have N
interviews." It is "our scores predict outcomes incumbents' scores don't, at N large enough to
survive a challenge, with adverse-impact ratios logged continuously."

---

## 3. LLM-scored interview evidence (2023–2026)

| Study | Venue / date | What it found | Key quote (≤40 words) | source_url |
|---|---|---|---|---|
| "Scoring Employment Interviews With Large Language Models: Evaluation Design Components, Validity Investigations, and Best Practice Recommendations" (Stockdale et al., U. Houston) | *Journal of Applied Psychology*, online Jun 2026 | Investigated prompt design, model selection, hyperparameters, and number of LLM raters; examined intrarater reliability, convergent/discriminant/criterion validity, and group differences; panel-of-LLM-raters aggregation improves reliability (panel-interview analogy) | "We investigated the effects of several LLM rater evaluation practices—specifically, prompt design, model selection, hyperparameters, and number..." (snippet, truncated) | https://www.researchgate.net and https://read.qxmd.com (paywalled; no effect sizes retrievable — see §8) |
| "Invisible Filters: Cultural Bias in Hiring Evaluations Using Large Language Models" (Rao, Venkatesan, Cherubini, Jayagopi) | arXiv:2508.16673, Aug 2025; AIES 2025 (fetched directly) | LLM scores on 100 UK + 100 Indian interview transcripts: consistent penalty to Indian-accented transcripts, persisting under anonymization, mediated by sentence complexity/lexical diversity; name/caste/region swaps alone NOT significant | "Indian transcripts receive consistently lower scores than UK transcripts, even when they were anonymized" | https://arxiv.org/abs/2508.16673 |
| "Inter-Rater Reliability of AI Scores: A Call to Move [Beyond Single Correlations]" | Wiley (journal), 2024–25 | Review of LLM-as-rater reliability studies; benchmark context: single human rater reliability 0.54–0.79, often lower for panels in field | Human single-rater reliability "ranged from 0.54–0.79" (snippet paraphrase) | https://onlinelibrary.wiley.com (search-domain) |
| Wang (2025), "Evaluating LLMs as raters in large-scale assessments" | ScienceDirect, cited by 42 | LLMs adequate at relative ranking, weaker at absolute standards; Claude-family models scored best | "LLMs perform adequately for relative ranking tasks but remain less reliable for absolute standard judgments" | https://www.sciencedirect.com (search-domain) |
| Zhang (2024), "Can Large Language Models Serve as Data Collectors?" (VU Amsterdam) | 2024, cited by 66 | Validity, reliability, fairness, and rating patterns of GPT-3.5/GPT-4 as survey/rating instruments | (not quoted — snippet-level only) | https://research.vu.nl (search-domain) |
| "Investigation of the Inter-Rater Reliability between Large Language Models" (ChatGPT-4o vs 4.5-preview) | arXiv, Aug 20 2025 | LLM-vs-LLM agreement in rating tasks | (not quoted — title-level only) | https://arxiv.org (search-domain) |
| Panfilova et al., "The AI interviewer: multi-faceted evaluation of adaptive [interviewing]" | Nature-family journal, 2026, cited by 3 | Six LLMs as adaptive semi-structured interviewers over a 54-question battery; controlled evaluation of the interviewer (not scorer) role | "conducts semi-structured interviews over a fixed battery of 54 main questions" (snippet) | https://www.nature.com (search-domain) |
| Bloomberg investigation (Mar 2024) | Journalism | GPT models ranked résumés by name with racial bias — "serious risk for automated discrimination at scale" (snippet) | as quoted (snippet) | via search; original bloomberg.com article not directly fetched |
| Accent-bias meta-analysis | *J. Applied Psychology* / Wiley, Jan 2025 | "Hiring interview evaluations consistently favor standard-accented (SA) over non-standard-accented (NSA) applicants" (snippet) — the human baseline Ashley's transcript-only scoring must beat | as quoted | https://onlinelibrary.wiley.com (search-domain) |

**Synthesis for the moat question:**
1. **Reliability is solvable today** (aggregate multiple ratings — panel-of-raters), so a competitor
   with a frontier LLM and a good rubric gets near-human-rater reliability *without any proprietary
   data*. That sets a high, moving baseline for any data-derived advantage.
2. **Bias is the live risk**: the accent penalty survives anonymization (Invisible Filters), and it
   is linguistic, not name-based — exactly the risk of "scoring the words only." Cross-customer
   outcome labels are the only way to *detect and correct* systematic bias against groups whose
   language differs; that is a genuine data-asset argument.
3. **Prompt sensitivity** (Stockdale et al.) means unversioned prompt changes destroy score
   comparability — instrument governance is a prerequisite for compounding (see §7).
4. I found **no published study with criterion validity of LLM-scored interviews against real job
   performance at employer scale**. Whoever runs that study first — on their own labeled data —
   owns the only evidence that matters. This is the actual scarcity.

---

## 4. Vendor science claims

| Vendor | Published claim | Quote / figure | Independently verified? | source_url |
|---|---|---|---|---|
| **HireVue** | Volume: "HireVue customers conduct over 1 million video interviews in just 30 days" (Sept 2021 peak); ~12M cumulative by 2019 (WaPo: "700 companies... nearly 12 million interviews"); 1.46M in Q1 2025 per third party | "over 1 million video interviews in just 30 days" | Volume: press release + journalists; not audited | https://www.hirevue.com/press-release/hirevue-customers-conduct-over-1-million-video-interviews-in-just-30-days ; Washington Post 2019 via search |
| HireVue (science) | External review by Dr. Richard Landers (Apr 2021) of the technical manual's adverse-impact analyses | review "did not indicate any significant adverse impact" (snippet) | Partially — an external I/O review of an *internal, gated* manual; data not public | https://www.hirevue.com |
| HireVue (retreat) | Removed facial-analysis scoring Jan 2021 amid EPIC complaint and audit | Per EPIC: "10% to 30% of a candidate's score was based on facial expressions" | Yes — SHRM, Fortune, AI Incident Database | https://www.shrm.org ; https://epic.org ; https://incidentdatabase.ai |
| **Sapia.ai** | Volume/experience: 2025 Candidate Experience Report on "6.7M+ completed chat interviews," satisfaction 9.05/10 | "6.7M+ completed chat interviews" (snippet) | No — company-sponsored (Businesswire, Sept 2025) | https://sapia.ai and Businesswire via search |
| Sapia.ai (science) | Adverse-impact testing described in own ebook via an MTurk study; claims language signals "reliably predict job performance"; MIT-Tech-Review-adjacent coverage notes it claims to predict "job hopping" from interview answers | claims it can "predict job hopping from interview answers" (snippet) | No peer-reviewed validation of the product found | https://sapia.ai ; MIT Tech Review piece via search |
| **Pymetrics / Harver** | Harver acquired pymetrics Aug 2022; 12–16 neuroscience mini-games, 70+/91 traits; models must pass accuracy/recall ≥65% and bias audits pre-deployment; 98% assessment completion | (figures from vendor/third-party summaries) | Partially — bias-audit-before-deployment practice is real and notable; specific validity coefficients not published peer-reviewed under the pymetrics name | https://harver.com (press) |
| pymetrics-adjacent (peer-reviewed) | Leutner et al. 2023, *Frontiers in Psychology*: ML-scored game-based cognitive assessment — convergent validity r = .5, test–retest r = .68, fairness maintained in separate applicant sample N = 3,107 | "The assessment has convergent validity (r = 0.5) and test–retest reliability (r = 0.68)" (snippet) | Yes — peer-reviewed (authorship/vendor affiliation not confirmed) | https://www.frontiersin.org ; https://pmc.ncbi.nlm.nih.gov |
| **Paradox** | No peer-reviewed validity study found for Olivia chat assessments; screening is mostly knockout questions in chat; entered assessments by acquiring Traitify (2021) | (absence of evidence — see §8) | No | https://www.paradox.ai ; https://recruitingtechreviews.com ; https://joshbersin.com |
| **SHL** | Publishes "Guidance for the Interpretation of Validity Coefficients" and gated technical manuals; OPQ criterion validity "confirmed by dozens of studies" (~5,000 participants per third-party summaries) | (third-party summary, unverified count) | Manuals exist and are gated; counts not independently verified | https://www.shl.com |

**Read-across:** every serious vendor wraps an I/O-psychology evidence layer around a volume engine.
The evidence layer is mostly self-published and gated; the volume engine is real. Nobody in this set
publishes a *replicable* criterion study of AI-scored interviews with open methodology. The
differentiator available to a small player is transparency, not volume.

---

## 5. What compounds and what does not

**Does not compound (commodity within ~12 months):**
- **Transcripts alone.** HireVue reported 1M+ interviews in a single month; Sapia claims 6.7M+
  cumulative. Frontier LLMs already read transcripts at near-human reliability with a good rubric
  (§3). A competitor gets equivalent transcript-scoring by renting a model. Ashley's transcript
  corpus, on its own, is worth little to anyone.
- **Rubrics and question banks.** Explicit knowledge, copiable on sight, and vendors (HireVue
  Builder) auto-generate them from job title already (§4, hirevue.com Aug 2021).
- **Reaction/experience data** (completion, satisfaction) — nice for sales, weak for validity.

**Compounds (proprietary, hard to copy):**
- **Outcome labels**: which interviewed candidate was hired, was still there at 90/365 days, and was
  rated well by their manager — joined to the interview transcript and per-question scores at the
  row level. This is the only data that (a) competitors cannot buy or scrape, (b) improves scoring
  against the criterion the law cares about, and (c) enables bias detection/correction with real
  base rates.
- **The join itself.** The loop closes through integrations: ATS stage-change + hire-decision
  webhooks (Greenhouse/L Workday-style), HRIS retention events, performance-review exports. Each
  customer's loop is contractually theirs — a competitor signing the same ATS integration gets the
  same loop for *their* customers. The moat is not the plumbing; it is having instrumented it years
  earlier so the labels exist.
- **A stable measurement instrument** (fixed core question batteries + anchored rubrics, versioned)
  across customers and time. Without stable items, pooled data is noise (see §7).

**Per-customer vs cross-customer learning:**
- Per-customer learning (this employer's hires vs misses) works at small N, is uncontroversial
  legally, and is genuinely sticky — it makes Ashley's scoring calibrated to outcomes the customer
  themselves validated. But it is not exclusive: the customer knows it too, and any vendor plugged
  into the same ATS can offer it.
- Cross-customer learning (pool all employers' labeled interviews to model "what a strong candidate
  sounds like" per role family) is where scale economics live — and where the law bites:
  - **GDPR Art. 5(1)(b)** purpose limitation: data collected for "assessing this application" reused
    to train cross-employer models is a *further purpose* needing the Art. 6(4) compatibility test
    or fresh consent. EDPB Guidelines 4/2019: "The controller should not connect datasets or perform
    any further processing for new incompatible purposes" (edpb.europa.eu). Recruitment guidance for
    staffing agencies treats sharing a candidate across employers as requiring consent in practice.
    source_url: https://gdpr-info.eu ; https://www.edpb.europa.eu ; https://ico.org.uk
  - **Enterprise contract norms** run against pooling: customers increasingly demand zero-training
    clauses ("AI vendors may seek rights to use customer data... contracts must restrict this" —
    Morgan Lewis, Jun 2026, morganlewis.com via search). Ashley's enterprise DPA posture must decide
    this explicitly.
  - **Illinois AIVIA** (820 ILCS 42): 30-day deletion of AI-analyzed video interviews on candidate
    request — imposes "transparency, consent, and data destruction" duties (Davis Wright Tremaine
    snippet). The 2024 SB 3311 litigation-hold amendment did not advance; BIPA reform SB 2979 was
    signed Aug 2, 2024 (single-accrual). A deletion that must propagate into pooled training
    features requires ML pipeline design (deletable feature stores / retraining windows), not a
    cron job. source_url: https://www.dwt.com and https://www.consumerfinancialserviceslawmonitor.com (search-domains)
  - Practical consequence: **pool only pseudonymized feature/label rows**, never raw identity;
    segregate EU/UK; take a distinct, optional, plain-language candidate consent at interview start
    ("help improve scoring for everyone") — which most candidates will accept and which competitors
    who did not ask for it early can never retro-fit.

---

## 6. Volume estimates (reasoning shown)

**Baseline to beat:** rubric + frontier LLM, which per §3 already delivers near-single-human-rater
reliability (~.54–.79) and inherits every frontier-model upgrade for free. A proprietary model must
beat it *on criterion validity* (prediction of hire/retention/performance), and the advantage must be
statistically demonstrable, not vibes.

**Step 1 — labeled-sample statistics.** Standard error of a Fisher-z validity estimate is 1/√(N−3).
- N = 200 labeled hires → SE(z) ≈ .071 → 95% CI on r roughly ±.14 at r ≈ .30. Enough to *claim*
  validity in line with industry practice (cf. §2 guidance: N ≥ 30 floor, 500 ceiling for precision).
- To show a model *beats* the rubric baseline by Δr ≈ .05–.10 (dependent correlations, predictor
  inter-correlation ~.5), 80% power needs on the order of **N ≈ 1,000–2,000 labeled hires per role
  family**. That is the defensible threshold; below it, "our data makes us better" is not provable.

**Step 2 — label sparsity and lag.** High-volume funnels hire roughly 5–15% of interviewed candidates
(assumption, §9). Performance/retention labels mature at 3–12 months. So labeled outcomes accrue at
~0.05–0.15× interview volume, delayed 6 months on average.

**Step 3 — role-family fragmentation.** Cross-customer models are per role family (retail associate ≠
support ≠ sales). Assume volume concentrates in ~6–10 families (assumption, §9), helped by Ashley's
fixed structured format.

**Scenarios** (using 10% labeling, 6-month lag, 8 role families):

| Interview volume | Labeled hires/yr | Per role family/yr | Time to 1,000–2,000/family | Verdict |
|---|---|---|---|---|
| 1,000/mo | ~1,200 | ~150 | **7–13 years** | Cross-customer model effectively unreachable; per-customer learning only for the largest single accounts |
| 10,000/mo | ~12,000 | ~1,500 | **~1–2 years for top families; 2–4 years broadly** | Moat becomes real in year 2–3 if instrumentation started day one |
| 100,000/mo | ~120,000 | ~15,000 | **1–3 months after label lag (top families)** | Cross-customer model defensible within year 1; HireVue-class asset |

**Learning curves:** I found **no published learning curve for interview-scoring or selection-model
accuracy vs labeled volume** (recorded in §8). The estimates above therefore use validation-statistics
thresholds, not curve-fitting. General ML experience (improvement roughly log-linear in labeled data,
steep early gains, long tail) suggests the first ~500 labels per family capture most of the rubric-
calibration gain, and the last mile of criterion-validity advantage is what takes thousands. Also note
the treadmill: the rubric+frontier-LLM baseline improves with every model release, so the proprietary
increment must be re-earned against a moving target — argue increments (Δr), not absolutes.

**Cross-check against incumbents:** HireVue needed years at ~1M interviews/month to build the corpus
it markets science on (§4). Sapia's 6.7M cumulative took ~8 years. Ashley should plan on the 10k/mo
row as the realistic medium-term case.

---

## 7. Design recommendations

**Instrument from day one (this quarter):**
1. **Outcome webhooks in, not just out.** Ashley's webhooks currently push results to customers
   (site: "Webhook delivery of interview results into customer systems is rolling out"). Add the
   reverse feed: ATS stage-change/hire-decision events and later HRIS retention + manager ratings,
   keyed to `interview_session_id`. Store as an append-only event log (offer → hire, 30/90/365-day
   retention, performance rating, manager-ad-hoc "good hire" flag). This is cheap now, impossible to
   retrofit.
2. **Stable, versioned instrument.** Fixed core question batteries per role family with anchored
   rubrics; every question text, rubric, prompt, and model version stamped on each score row. The
   structured interview's .42–.51 validity *is* standardization; instrument drift is the number-one
   way pooled data becomes worthless. Never hot-patch a scoring prompt silently (prompt sensitivity:
   Stockdale et al., §3).
3. **Consent architecture for pooling.** A distinct, optional, plain-language toggle at interview
   start for pseudonymized cross-employer improvement of scoring; separate from consent to record.
   Per-customer learning runs without it; cross-customer learning runs only on opted-in rows.
   Enterprise terms default customer-owns-data with opt-in pooled learning — sells better than a
   buried training-rights clause and survives GDPR Art. 6(4) scrutiny.
4. **Deletion that propagates.** Illinois AIVIA's 30-day deletion and GDPR erasure must reach
   derived features: design the feature store so a candidate's rows (and their influence via
   retraining windows) can be expunged; log deletions in the audit exports Ashley already promises
   for NYC LL144/AIVIA.
5. **Panel-of-raters scoring** (multiple LLM ratings aggregated, per Stockdale et al.) as the default
   scorer — best reliability today, and the per-rating disagreement is itself a useful feature.
6. **A frozen benchmark per role family:** human double-rated transcripts + eventual outcome labels,
   held out, against which every model/rubric change is scored (criterion Δr + 4/5-ratio impact).
   Publish the methodology even if the data stays private — the credibility gap in §4 is an opening.
7. **Continuous adverse-impact telemetry:** per-question score distributions by demographic where
   lawfully held, four-fifths ratios computed on every customer's live funnel. The Invisible Filters
   accent result (§3) means words-only scoring still carries linguistic proxy bias; being the vendor
   who *measures and publishes* that is both a moat and a defense.

**The two or three things that would make the data asset worthless:**
1. **No outcome labels.** If the ATS loop is never built, Ashley accumulates transcripts — a
   commodity incumbents already hold in the millions, and the vision-page asset never exists.
2. **Instrument drift / full per-customer customization.** If every enterprise customer gets bespoke
   questions and rubrics with silent prompt changes, rows never pool, and "what a strong candidate
   sounds like" is unmeasurable across customers. (Custom avatars are fine; custom *instruments*
   are the poison.)
3. **Legal overreach on pooling.** Training cross-customer models on non-consented data, or failing
   AIVIA/GDPR deletion inside pooled stores, converts the asset into liability — the HireVue facial-
   analysis retreat (§4) is the canonical demonstration that a scoring feature can become a crisis.

---

## 8. Gaps and unverifiable items

- **No published learning curve** for selection-model validity vs labeled-outcome volume was found;
  §6 is derived from validation statistics, flagged as such.
- **Stockdale et al. (JAP, 2026)** — could not retrieve effect sizes (paywalled); quotes are from
  search snippets; reliability/validity magnitudes unverified.
- **Sapia.ai** — no independent peer-reviewed validation of the chat-interview product found; all
  figures (6.7M, 9.05/10, MTurk adverse-impact study) are company-published.
- **Paradox** — no peer-reviewed validity study found (absence of evidence; may exist in gated
  technical material).
- **SHL OPQ "dozens of studies, ~5,000 participants"** — third-party summary count; SHL manuals are
  gated; not independently verified.
- **HireVue cumulative-interview counts vary wildly across sources** (12M in 2019 → 600M+ claimed on
  a review site); I used the press-release and Washington Post figures only. The "1M in 30 days"
  figure is a Sept 2021 peak, not a steady state; Q1-2025 third-party figure (1.46M) suggests lower
  recent run-rates.
- Several URLs resolved at **domain level** in search results (psycnet.apa.org, onlinelibrary.wiley.com,
  sciencedirect.com, nature.com, research.vu.nl, frontiersin.org, edpb.europa.eu); pinpoint citations
  are given in prose. Quotes marked "(snippet)" came from search-result extracts, not full fetched
  pages — treat as near-verbatim pending fetch.
- **Bloomberg (Mar 2024) résumé-name-bias item** — surfaced via search summary only; original article
  not fetched.
- Bloomberg/CDT critiques of HireVue explainability (CDT, Sept 2022: "mostly fails") seen at headline
  level only.

## 9. Assumptions made

- Ashley is early-stage with unknown traction; volumes (1k / 10k / 100k interviews per month) are
  the brief's stipulated scenarios, not observed figures.
- Hire rate from interviewed candidate to hire assumed 5–15% (used 10%); performance/retention labels
  assumed to mature at 3–12 months (used 6-month average lag); volume assumed to concentrate in ~6–10
  role families (used 8). None verified from Ashley data — all flagged in-line in §6.
- "Well-written rubric + frontier LLM" baseline assumed to deliver near-single-human-rater
  reliability, extrapolating from the Wiley IRR review (0.54–0.79) plus panel-of-raters findings;
  no direct head-to-head benchmark of rubric+LLM vs humans on interview transcripts was found.
- The brief's "Paradox" was interpreted as Paradox.ai (conversational recruiting), not Harrison
  Assessments' "Paradox Theory," which a literal search also surfaces.
- Vendor volume claims taken as published, not audited; dates are as reported by the sources.
