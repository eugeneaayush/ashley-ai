# Moat Playbook — Ashley.Ai (Helen Labs, Inc.)

Unit: `moat-playbook` · All sources fetched 2026-09-23 via web search. Where the search engine
returned a domain-level link rather than an article path, the source_url is the domain and is
flagged as such. Quotes are verbatim from the cited page as returned in search results (≤40 words);
items marked *(paraphrase)* were summarized by the search layer and should be re-verified before
external use.

## 1. Summary

Ashley has one real asset today — the in-house real-time rendering stack (process power) — but a
moat must be built where competitors rent nothing: business-model counter-positioning, embedded
workflow switching costs, and trust-posture branding. The HR-tech record is unambiguous on what
fails: candidate-side "interview once, reuse everywhere" pools (Triplebyte, Hired) die on privacy
backlash and marketplace economics, and assessment-science moats alone (Pymetrics) end up
acquired, not dominant. What compounds: system-of-record gravity plus certification walls
(Workday, SAP), ecosystem lock-in (Greenhouse), compliance-as-product embedding (Checkr, $5B peak
valuation), published-science trust brands (Sapia.ai), and distribution through franchise/staffing
channels (Paradox, Fountain) — Paradox converting a partnership into a Workday acquisition
(announced 2025-08-21, completed 2025-10-01). For an early-stage company this quarter, the
affordable moves are: price/contracting counter-position, a words-only + published-audit trust
position incumbents cannot credibly copy, and marketplace/embedding distribution that converts
into switching costs. Top three to pursue first: **(1) trust-posture counter-position with
published bias audits, (2) self-serve month-to-month pricing counter-position defended by
inference-cost scale economies, (3) ATS-embedded switching costs via marketplace listings and
webhook/score write-back depth.**

## 2. Powers applied to Ashley

Framework: Hamilton Helmer's 7 Powers, plus data and distribution/embedding moats. For each:
what Ashley could do in the next two quarters, what it takes, and the precedent that shows the
mechanism working.

### 2.1 Scale economies
- **What to do:** treat inference cost per completed interview as the strategic metric. Negotiate
  committed-use GPU pricing as volume grows, distill/route models per language, cache rendering
  primitives, and publish a falling $/interview curve that keeps the $499–$1,499 tiers and $5–6
  overage profitable while enterprise incumbents bill $30K–$100K+ implementations.
- **What it takes:** volume first — scale economies are *scale-dependent* and weak at Ashley's
  current (unknown, assumed small) volume; GPU supply is market-priced (RunPod), so the advantage
  is operational, not structural, until volume is meaningful.
- **Precedent:** HireVue reached 24M+ hosted interviews, but scale alone did not protect it from
  the 2021 facial-analysis backlash — evidence that scale economies without trust posture underperform.
  Counter-example on price: Checkr's API-first scale ($679M raised, ~$800M revenue claimed by a
  competitor's page) let it productize cheap per-check pricing (see §3.5).

### 2.2 Network economies
- **What to do:** the only network effect reachable in two quarters is *data-network*: a
  consented, anonymized cross-employer benchmark of structured answers by role ("what a strong
  candidate sounds like"), which improves scoring for every customer as employers join. Pure
  two-sided candidate↔employer networks (§5) are not buildable at this stage.
- **What it takes:** consent architecture (opt-in sharing, GDPR/CCPA-clean), enough employers per
  role-family for benchmarks to be non-trivial, and discipline not to overclaim validity (the
  `data-outcomes` worker owns the science).
- **Precedent:** Eightfold positioned its "talent intelligence" data network (100+ data fields,
  $400M+ raised) as the core differentiator; Handshake shows the full two-sided version works only
  at institutional scale (12M+ students, 750K+ employers, §3.13).

### 2.3 Counter-positioning (2 candidates below; rank #1 and #2)
- **(a) Trust-posture counter-position:** words-only transcript scoring, AI disclosure at the
  start of every interview, no auto-rejection, human decision, published bias-audit support, and a
  public "you won't be ghosted" candidate commitment. An incumbent whose flagship product was
  built on video/facial scoring and enterprise sales cannot copy this *credibly*: HireVue's
  facial-analysis removal followed an FTC complaint (§3.1), so "we're the transparent one" from
  that lineage reads as retrofit. Ashley's site already claims this posture; the moat step is
  *proof*: publish recurring third-party-aligned audits and candidate-experience stats.
- **(b) Business-model counter-position:** self-serve, pay-per-interview, month-to-month, no
  implementation fee, vs. the category's $25K–$75K+ implementation enterprise motion (§3.2).
  Copying it forces incumbents to cannibalize their sales-led pricing and channel — the Helmer
  test for true counter-positioning.
- **What it takes:** (a) audit budget (~$25–75K/yr for annual third-party audits, comparable to
  NYC LL144 audit norms) and publication discipline; (b) discipline to stay self-serve while
  enterprise deals tempt.
- **Precedents:** HireVue/EPIC (§3.1), Sapia.ai published science (§3.3), Paradox pricing (§3.2).

### 2.4 Switching costs
- **What to do:** make Ashley the *system of record for first-round evidence*: per-role rubric
  libraries and interview archives that accumulate hiring history; webhook + ATS score write-back
  so transcripts/scores live in the ATS; custom-branded avatars (enterprise tier) that a
  competitor must re-create; funnel analytics baselines that break when the tool is swapped.
- **What it takes:** ship the "rolling out" webhooks to stable contract, add 2–3 native ATS
  integrations (Ashby Assessments framework, Greenhouse, iCIMS), and persist per-customer
  calibration data. Cost is engineering time, not cash.
- **Precedents:** Greenhouse ecosystem lock-in (§3.6); Workday/SAP system-of-record gravity
  (§3.8); Checkr embedding via API + continuous monitoring at $1.70/person/month (§3.5).

### 2.5 Branding
- **What to do:** own "the AI interviewer candidates don't hate" — publish candidate NPS and
  completion rates next to the industry's 38%-abandoned stat the site already cites; make
  disclosure and no-ghosting signature claims; cultivate the university/defense early users
  (USAFA, UF Warrington per the site) as named references if permissions allow.
- **What it takes:** consistent publication, reference customers, and never being the company in
  a candidate-backlash story — brand here is fragile and binary.
- **Precedents:** Sapia.ai built a science-and-fairness brand on a million-interview research
  base (§3.3); Karat branded interview consistency via "Interview Engineers" (§3.14).

### 2.6 Cornered resource
- **What to do:** the in-house real-time rendering/inference stack and the team that tuned ASR +
  LLM + voice + face against one latency budget is today's cornered resource. Sustain it with
  key-person retention (vesting, publication constraints) and by deepening the stack (interruption
  handling, 11-language coverage) faster than avatar-API renters improve.
- **What it takes:** hiring market for the 3–5 people who can do this; note the `replication`
  worker owns the bear case on how long this holds — treat it as a 12–24 month head start, not a
  permanent moat.
- **Precedent:** none of the studied companies defended on proprietary rendering; the closest
  analog of a proprietary-asset moat is Eightfold's data asset (§3.9).

### 2.7 Process power
- **What to do:** codify the operational knowledge of running live photoreal interviews at
  conversational latency — Helmer's process power is embedded, coordination-heavy know-how that
  stays hard even when visible. Instrument it: publish uptime/latency/quality benchmarks
  competitors renting APIs cannot match.
- **What it takes:** measurement infrastructure and a culture of tuning the whole pipeline
  against the latency budget, which the site says already happened once.
- **Precedent:** Paradox's conversational-scheduling ops at franchise scale (95% task automation
  claims, Deloitte Fast 500) reflect process power in deployment, not just code (§3.2).

### 2.8 Data moat (adjacent to `data-outcomes` scope)
- **What to do (moat mechanics only):** consented transcripts + rubric scores per role become an
  asset only if (i) collection is consent-clean, (ii) scores are joined to outcomes (hired/not,
  performance), and (iii) aggregation crosses employers. First step this quarter: contract terms
  + consent flows that permit anonymized cross-employer benchmarking, else the corpus is
  per-customer and confers only switching costs.
- **Precedents:** Eightfold (§3.9), Sapia.ai (§3.3), HireVue's 700-customer × 24M-interview
  corpus (§3.1) — all show data assets accruing to whoever already had distribution.

### 2.9 Distribution / embedding moat
- **What to do:** a certification sweep — Ashby Assessments integration, Greenhouse and iCIMS
  marketplace listings, Lever marketplace, SAP/Workday later (§4). Each listing alone is weak;
  the moat is the *sum*: embedded in the customer's ATS on day 1, webhook-native, certified.
  Parallel non-ATS channels: staffing/RPO via Bullhorn, franchise brands directly.
- **What it takes:** integration reviews (weeks–months each), security review packages, and for
  Workday/SAP an enterprise-customer pull. This is the highest-leverage use of the next two
  quarters of engineering capacity.
- **Precedents:** Paradox was Workday's preferred text-recruiting/scheduling partner *before*
  Workday acquired it (§3.2); Fountain distributed through the ADP Marketplace (§4).

## 3. Precedents (researched, with sources)

### 3.1 HireVue — scale and enterprise contracts could not save facial analysis
Defensibility was enterprise contracts + hosted scale (700+ customers incl. over one-third of the
Fortune 100; 24M+ video interviews). In January 2021, facing an EPIC FTC complaint, it dropped
facial analysis; assessments now score transcripts only.
- Carlyle majority investment, Sep 2019: quote: "Its more than 700 customers worldwide include
  over one-third of the Fortune 100 and leading brands such as Unilever, Hilton, JP Morgan Chase…"
  source: https://www.carlyle.com (Sep 3, 2019; domain-level link from search)
- Scale: "HireVue has hosted more than 24 million video interviews and 150M chat-based candidate
  engagements for over 700 pioneering customers" — https://www.hirevue.com (Oct 19, 2021)
- Facial analysis: "HireVue, Facing FTC Complaint From EPIC, Halts Use of Facial Analysis" —
  https://epic.org (Jan 12, 2021); "HireVue… has removed the facial analysis component from its
  screening assessments" — https://www.shrm.org (Feb 3, 2021); also https://www.wired.com
  (Jan 12, 2021) and https://fortune.com (Jan 19, 2021), all domain-level links.
- **Lesson for Ashley:** incumbents' trust retrofits are reactive; a born-transparent posture is
  claimable space, and words-only scoring is now table stakes HireVue validated for the category.

### 3.2 Paradox / Olivia — conversational ATS won hourly + franchise distribution, then sold to Workday
- Series B $40M led by Brighton Park Capital, May 2020 — https://voicebot.ai (domain-level).
- Later Thoma Bravo-backed; franchise offering "supports 50,000+ locations and owner-operators,"
  customers include 7-Eleven, Nestlé, Marriott — https://www.hiretruffle.com (2026; domain-level).
- Pricing under Workday ownership now typically "$30K–$100K+"
  (https://www.hiretruffle.com, 2026) with implementation fees "$25k–$75k"
  (https://www.noon.ai, Aug 26, 2026) — *(paraphrase from review pages; verify before quoting)*.
- Acquisition: "The addition of Paradox will give Workday an AI-powered talent acquisition suite
  to help customers more efficiently find, hire, and onboard…" — https://newsroom.workday.com
  (Aug 21, 2025); completed Oct 1, 2025 — https://investor.workday.com; analysis:
  https://joshbersin.com ("A Bigger Deal Than You Think").
- Pre-acquisition, "Paradox was already the preferred Workday text recruiting and scheduling
  partner" *(paraphrase of paradox.ai positioning seen in search)*.
- **Lesson:** partnership → distribution → acquisition is the canonical exit path; franchise
  brands are a repeatable channel; but the enterprise pricing model it grew into is exactly what
  Ashley can counter-position against.

### 3.3 Sapia.ai — published science and interview-count claims as a trust brand
Chat-based structured interviews; research base of 1M+ interviews; regulatory filings cite 2M+
interviews; Starbucks deployment described by CEO Barb Hyman using 3.7M interviews of proprietary
de-identified data.
- "Analyzing over a million interviews and 11 million words of candidate feedback, the findings
  make clear that responsibly designed AI has the…" — https://www.businesswire.com (Sep 18, 2025)
- 3.7M interviews / Starbucks — https://flexos.work (Apr 2024, domain-level); "more than 2
  million interviews" in regulatory comments (Sanford Heisler summary); "1 million candidates and
  8 million interviews" on sapia.ai (domain-level). Counts vary 1M–8M by source and date.
- **Lesson:** publishing research on your own corpus creates a fairness brand that competitors
  without corpora cannot match; Ashley's transcript corpus could support the same play once
  consent-clean.

### 3.4 Pymetrics → Harver — assessment science alone was not a standalone moat
Acquired by Harver in August 2022 (not 2023); neuroscience-game assessments folded into Harver's
volume-hiring suite.
- AlleyWatch (Aug 15, 2022) — https://alleywatch.com (domain-level); ETS investor note:
  pymetrics adds "groundbreaking, behavioral-based AI methodology" — https://harver.com
  (domain-level); corroborated by https://www.graduatesfirst.com (domain-level).
- **Lesson:** behavioral-science differentiation gets absorbed into suites; standalone science
  needs distribution or a compliance lock to stay independent.

### 3.5 Checkr — compliance as product; embedding + continuous monitoring
- "Checkr was valued at $5B following its $250M Series E round led by Durable Capital Partners in
  September 2021" — https://sacra.com; ~$679M total raised —
  https://research.contrary.com (Feb 2025).
- Continuous monitoring product at "$1.70/person/month" — https://checkthat.ai (domain-level);
  ">100,000 employers… more than $800 million in revenue" — https://www.accusourcehr.com
  (competitor page; treat with caution); Forrester TEI: "169% ROI over three years" —
  https://checkr.com (domain-level).
- **Lesson:** turn the compliance burden into product surface (monitoring, audit exports, APIs)
  and you get paid monthly for defensibility. Ashley's LL144/AIVIA audit exports are the same
  play at seed scale.

### 3.6 Greenhouse & Lever — workflow lock-in via partner marketplaces
- Greenhouse runs the most extensive mid-market partner marketplace; technology partners must
  pass an integration review — https://outsail.co (Jul 24, 2026) and
  https://partner-program-directory.partnerfleet.io / https://xamplify.com (domain-level;
  *(paraphrase of requirements)*); official page: https://www.greenhouse.com (partner program
  guide gated behind a form).
- Lever maintains a marketplace across HRIS/assessments/background checks — https://lever.co
  (domain-level).
- **Lesson:** the ATS marketplace is the modern integration review moat; being *listed* is
  distribution, being *embedded in the workflow* is switching cost.

### 3.7 iCIMS — certified marketplace with AI-interview vendors already listed
- Official marketplace: "Discover and compare trusted Assessment partners that best fit your
  hiring needs." — https://marketplace.icims.com (seen 2026-09-23).
- Listed/integrating AI-interview vendors per third-party roundups: HireVue, Tenzo, Classet,
  Noon, Skima — https://skima.ai (Aug 2025), https://www.tenzo.ai, https://www.classet.ai
  (May 2026), https://www.noon.ai (2026) — *(paraphrase; roundups, not iCIMs official listings)*.
- **Lesson:** a competitor can be listed in weeks; the moat is depth (score write-back,
  certifications), not presence.

### 3.8 Workday & SAP SuccessFactors — system of record + certification walls
- Workday Marketplace confers a "Workday Certified" badge; listings without it "do not signify a
  fully tested and customer ready integration" —
  https://marketplace.workday.com/en-US/apps/653288/jay-cloud (seen 2026-09-23). Certified
  partners "have to meet and follow enterprise standards" (performance, safety, scalability) —
  https://www.edume.com/blog/benefits-of-partnering-with-a-workday-certified-software-partner
- SAP: "Integration certification provides technical and integration testing for partner
  applications aligned with SAP's strategic platform direction" — https://www.sap.com
  (domain-level); Gold-tier consulting partners need "at least 10 certified solution consultants,
  2 certified project managers, and 2 certified platform experts" —
  https://spadoom.com (Oct 10, 2025) *(paraphrase)*.
- **Lesson:** these are the highest, slowest walls in HR tech — realistically entered only with an
  enterprise customer pulling Ashley through; plan for 6–18 months.

### 3.9 Eightfold — talent-data network as the asset
- Raised >$400M total — https://startupintros.com (domain-level); est. revenue ~$189M and "over
  100 data fields" — https://www.appsruntheworld.com (domain-level).
- **Lesson:** "more customers → more talent data → better matching" is the HR-tech data-flywheel
  template; it begins paying only after multi-customer scale (rank accordingly).

### 3.10 Mercor — AI interview + marketplace monetization (candidate-side pool that worked, sideways)
- "Today, we're announcing our $350 million Series C funding, led by Felicis with participation
  from Benchmark, General Catalyst…" — https://www.mercor.com (Oct 27, 2025); $10B valuation,
  ~5x its ~$2B Feb 2025 mark; reportedly in talks at $20B — https://www.techbuzz.ai (Jul 9,
  2026); seed $3.6M Jan 2024.
- Model: AI-conducted interviews vet experts, who are then supplied (with payments/matching) to
  AI labs — monetizing the vetted candidate pool against AI-lab demand, not employer hiring.
- **Lesson:** the reusable candidate record works when a *second market* (AI data work) pays for
  vetted people; it is not evidence that employers will accept shared interview records.

### 3.11 micro1 — from AI-recruiter (Zara) to AI-data supply
- Series A "$35M led by 01 Advisors at a $500M valuation" (Sep 2025); founder raised "over $100
  million" total — https://www.forbes.com (seen 2026-09-23; article ~Sep 22, 2026): "At the
  beginning of last year, Ali Ansari's company, Micro1, was a recruiting business generating $7
  million in ARR."
- Growth "$100M to $500M gross run rate in ~8 months" — https://techcrunch.com (Aug 2026,
  domain-level); called a Scale AI competitor by Reuters.
- **Lesson:** same as Mercor — AI-interview vetting monetized through AI-lab demand dwarfed the
  hiring-tool business. (Relevant only if Ashley ever pivots the asset; not a moat for employer
  hiring.)

### 3.12 Handshake — the two-sided network that did work
- $3.5B valuation (Jan 2022) — https://www.builtinsf.com (domain-level); network: 12M+ active
  students, 1,400+ university partners, 750,000+ employers — https://equitybee.com
  (domain-level); $40M Series C Oct 2018 — https://techcrunch.com (domain-level).
- Network-effect evidence: "By connecting universities to a network, Handshake increases the
  number of opportunities employers choose to post to an institution by 300% on average" —
  https://joinhandshake.com (domain-level).
- **Lesson:** the third side (universities/institutions) created lock-in candidates can't route
  around; it took ~8 years and institutional sales. Not replicable by Ashley in 2 quarters, but
  validates that institutional anchors (Ashley's USAFA/UF footprints) can seed networks.

### 3.13 Indeed — distribution giant, cautious product surface
- "View candidate resumes, schedule and conduct interviews, and take notes all in one place with
  Indeed's virtual interview platform." — https://www.indeed.com (seen 2026-09-23).
- Retired its one-way interview feature — https://www.hiretruffle.com (2026; domain-level);
  virtual hiring events launched Jul 30, 2020 — https://www.hrdive.com (Aug 17, 2020,
  domain-level).
- **Lesson:** Indeed's scheduling/assessment surface is distribution-led; it retires products
  that candidates dislike. A "candidate-preferred" interviewer could ride job-board distribution
  without competing on it.

### 3.14 Karat & Triplebyte — human interviewers as a service; the "interview once" failure
- Karat's Interview Cloud: trained humans conduct 60-minute technical interviews 24/7 for clients
  incl. Indeed, Atlassian, Intuit, Peloton, NYT, Wayfair — https://karat.com /
  https://www.businesswire.com (Oct 2021, domain-level); ~21% pass rate per candidate guides;
  "Partners of Brilliance" program hires via Karat Academy — https://karat.com (domain-level).
- "Karat acquires Triplebyte's adaptive assessment technology to help companies eliminate resume
  bias, reduce candidate drop-off…" — https://karat.com (Mar 16, 2023).
- Triplebyte shutdown: "Yesterday, Karat announced a shutdown of Triplebyte with less than 2
  weeks notice." — https://news.ycombinator.com (Mar 16, 2023; the acquisition was an asset
  purchase; services wound down Mar 31, 2023 per https://techcrunch.com, domain-level).
- **Lesson:** outsourcing the first-round interview is a durable *service* business; the
  cross-company reusable assessment was the part that died (see §5).

## 4. Channels (does a partner program exist, requirements, who's listed)

| Channel | Partner program / certification? | Requirements & typical timeline | AI-interview vendors already listed (evidence) |
|---|---|---|---|
| Workday | Yes — Workday Marketplace; "Workday Certified" badge tier | Enterprise standards (performance/safety/scalability), security review, typically an enterprise-customer pull; realistically 6–18 months (EduMe: https://www.edume.com/blog/benefits-of-partnering-with-a-workday-certified-software-partner; badge quote: https://marketplace.workday.com/en-US/apps/653288/jay-cloud) | Paradox (owned by Workday since Oct 2025) — https://newsroom.workday.com |
| SAP SuccessFactors | Yes — SAP integration certification | "technical and integration testing for partner applications aligned with SAP's strategic platform direction" (https://www.sap.com); personnel thresholds for partner tiers (https://spadoom.com); months | Not evidenced in this run — gap |
| iCIMS | Yes — iCIMS Marketplace, Assessment partner category | Listing + integration; weeks–months (https://marketplace.icims.com) | HireVue, Tenzo, Classet, Noon, Skima per third-party roundups (https://skima.ai Aug 2025) — verify on official marketplace |
| Greenhouse | Yes — partner program with integration review for tech partners | Integration review; guide gated behind form (https://www.greenhouse.com); weeks–months | "Most extensive" mid-market marketplace (https://outsail.co Jul 24, 2026); specific AI-interview listings not enumerated — gap |
| Lever | Yes — Lever Marketplace | Integration + listing (https://lever.co); weeks | Not enumerated — gap |
| Ashby | Yes — Assessments integration framework + 200+ partners | "Ashby's Assessments framework allows third party assessment providers to integrate with Ashby and allow users to initiate skills tests, reference checks…" (https://developers.ashbyhq.com); API-driven, weeks | CodeSignal, Criteria Corp, Metaview commonly listed (https://pin.com, domain-level roundups) |
| Bullhorn (staffing) | Yes — Bullhorn Marketplace | REST API + webhook subscriptions + agency-tenant data model; API call limits (per https://jobcannon.io, domain-level *(paraphrase)*); weeks–months | Texting/AI-screening integrations common (https://www.whippy.ai roundup) — no named AI-interview vendor confirmed |
| Indeed | Product surface, not a classic marketplace | Indeed Interview platform + job-ad distribution (https://www.indeed.com) | Indeed itself competes/retires features (one-way interview retired per https://www.hiretruffle.com) |
| ADP Marketplace | Yes — app marketplace | Partner app review; Fountain precedent (https://apps.adp.com, domain-level) | Fountain (hourly hiring) — adjacent category |
| RPO / staffing agencies / PEOs | Indirect channel | Paradox marketed Olivia to staffing agencies, RPOs, PEOs, exec search (https://americanstaffing.net, domain-level); Bullhorn is the system of record for this channel | Paradox (channel proven) |
| BPOs | Indirect channel | Not evidenced in this run — gap | — |
| Franchise brands | Direct enterprise motion | Paradox: "50,000+ locations and owner-operators," 7-Eleven, Nestlé, Marriott (https://www.hiretruffle.com); Fountain: UPS, Amazon DSP, Sweetgreen (https://www.workstream.us Apr 29, 2026) | Paradox, Fountain (category precedents) |

## 5. Candidate-side options ("interview once, reuse across employers")

What the record shows:
- **Triplebyte (failed):** "one interview, many companies" fast-tracking; 2020 privacy backlash
  when profiles were surfaced beyond candidate expectations ("We will not share any information
  about you with companies [without permission]" — https://news.ycombinator.com, May 23, 2020);
  marketplace monetized companies only (https://news.ycombinator.com "Rethinking Triplebyte," Jun
  17, 2021); assets sold to Karat, services shut down Mar 31, 2023 with <2 weeks notice
  (https://news.ycombinator.com Mar 16, 2023; https://techcrunch.com).
- **Hired (failed):** tech-job marketplace once valued at $500M began winding down ~2020
  (https://www.theinformation.com, Nov 2020, domain-level); final shutdown by LHH (Adecco) noted
  Jun 2024 (https://news.ycombinator.com).
- **Karat:** durable as a *service* (outsourced interview capacity), not as a reusable candidate
  record; its Triplebyte asset purchase absorbed the "interview once" IP without reviving the
  consumer-facing pool (https://karat.com, Mar 16, 2023).
- **Byteboard:** no evidence retrieved this run — see §7.
- **Vervoe:** employer-side job simulations with AI grading/ranking; not a candidate-side pool
  (https://vervoe.com, Sep 13, 2026).
- **HackerRank / LinkedIn Skills:** lightweight verified-skill signals work as *discovery*
  garnish: "When skills are validated you can showcase your proficiency and become more
  discoverable to opportunities" (https://www.linkedin.com, domain-level) — but neither created a
  cross-employer interview record.
- **Mercor / micro1 (worked, differently):** reusable vetting pools pay when the buyer is AI
  labs' data-work demand, not employers (§3.10–3.11).
- **Handshake (worked):** only with an institutional third side and ~a decade of building
  (§3.12).

**Privacy and consent constraints for any Ashley candidate record:** GDPR/CCPA purpose-limitation
(each employer's interview was collected for *that* application; reuse needs fresh, opt-in
consent — Triplebyte's 2020 backlash is the cautionary tale); Ashley's own published posture
("You can ask the hiring company to delete your data at any time," https://www.tryashley.ai/candidates,
fetched 2026-09-23) sets a candidate-ownership expectation a reuse pool would have to be designed
around; NYC LL144-style bias-audit duties attach to the *employer using* an automated employment
decision tool, so a shared portable record shifts audit burden onto every consuming employer — a
sale-killer for cautious ones. **Verdict: do not build the cross-employer pool now; build the
consent architecture so it remains possible later.**

## 6. Ranked moat candidates

Strength scale: ●○○ weak / ●●○ moderate / ●●● strong. CP = counter-positioning idea (two
required, present at #1 and #2).

| # | Moat candidate | Mechanism (power) | First step this quarter | Cost & time to value | Scale-dependent? | 12-mo | 36-mo | Precedent |
|---|---|---|---|---|---|---|---|---|
| 1 | **Trust-posture CP: words-only + disclosed AI + human decision + published audits** (CP) | Incumbents can't credibly copy a born-transparent position (HireVue retrofit took an FTC complaint) | Commission and publish first bias/validity audit; publish candidate-experience stats | $25–75K/yr audits; value in weeks (differentiation) | Low | ●●● | ●●● | HireVue/EPIC §3.1; Sapia §3.3 |
| 2 | **Self-serve/month-to-month pricing CP** (CP) | Copying forces incumbents to cannibalize $30K–$100K+ enterprise motion | Keep self-serve core; publish comparison pages (already live); hold list price discipline | ~$0 (positioning); value now | Low | ●●● | ●●○ (erodes if enterprise pull wins) | Paradox pricing §3.2 |
| 3 | **ATS embedding + switching costs** (switching costs, embedding) | Webhooks, score write-back, rubric/calibration archives, custom avatar | Ship webhooks stable; Ashby Assessments integration; Greenhouse listing | Eng-months; value in 1–2 quarters | Medium | ●●○ | ●●● | Greenhouse §3.6; Workday §3.8; Checkr §3.5 |
| 4 | **Rendering-stack process power** (process power, cornered resource) | In-house real-time pipeline + latency tuning API-renters can't match quickly | Publish latency/reliability benchmarks; retain key staff; keep deepening | Ongoing eng; already built once | Low-Med | ●●○ | ●●○ | No direct precedent; Eightfold analog §3.9 |
| 5 | **Compliance-as-product** (switching costs, counter-position) | LL144/AIVIA audit exports, notice workflows, retention/deletion automation | Ship "compliance pack" (already Enterprise-tier promise) as productized exports | Low eng cost; value this quarter (regulated buyers) | Low | ●●○ | ●●● | Checkr §3.5 |
| 6 | **Staffing/RPO channel via Bullhorn** (distribution) | Agencies resell screening capacity under their brand | Bullhorn Marketplace integration (REST + webhooks + agency-tenant) | 1 eng-month + listing; value 1–2 quarters | Medium | ●●○ | ●●○ | Paradox/ASA §3.2; Bullhorn §4 |
| 7 | **Franchise/brand-portfolio flagship** (distribution, branding) | One flagship franchise brand → referenceable multi-location rollout | Target 1–2 franchise/QSR operators with the $6-per-interview pitch | Sales time; value 2–4 quarters | Medium-High | ●●○ | ●●● | Paradox §3.2; Fountain §4 |
| 8 | **Brand: "candidate-preferred interviewer"** (branding) | Own the anti-backlash position with published stats | Instrument candidate NPS; publish vs. the 38%-abandonment stat | Near $0; compounding | Low | ●●○ | ●●● | Sapia §3.3; Handshake brand §3.12 |
| 9 | **Inference-cost scale economies** (scale economies) | Falling $/interview sustains price CP | Negotiate committed GPU pricing; measure $/interview weekly | Ops focus; value as volume grows | High | ●○○ | ●●○ | Checkr pricing §3.5 |
| 10 | **Consented cross-employer benchmark data** (data network) | "What a strong candidate sounds like" per role improves with each customer | Consent flows + contract terms enabling anonymized aggregation | Legal + eng; value ≥4 quarters | High | ●○○ | ●●● | Eightfold §3.9; Sapia §3.3 |
| 11 | **University/institutional anchor accounts** (network seed, branding) | Institutional third side seeds network gravity (Handshake lesson) | Convert USAFA/UF relationships into named case studies + edu pricing | Near $0; value 2–3 quarters | Medium | ●○○ | ●●○ | Handshake §3.12 |
| 12 | **Portable candidate record (opt-in)** (network economies) | "Interview once, reuse" | *Do not build*; build consent architecture so it stays possible later | Deferred | Very high | ●○○ | ●○○ (history says fail) | Triplebyte §3.14; Hired §5 |

**Top-three justification**
1. **Trust-posture counter-position (#1).** Cheapest, fastest, and the only position that
   *strengthens* as regulation (NYC LL144, Illinois AIVIA/HB 3773) spreads: every new audit duty
   is free marketing for the vendor already publishing audits. HireVue's forced retreat proves
   incumbents move only under pressure, and Sapia shows the publishing flywheel compounds. Ashley's
   product already embodies the posture; the moat arrives the day it is *evidenced* publicly.
2. **Self-serve pricing counter-position (#2).** A structural Helmer counter-position: incumbents
   whose revenue runs on $25K–$75K implementations cannot match $499/month month-to-month without
   breaking their sales model. It pairs with #1 (trust + price = "the safe default for teams
   without a procurement department") and decays only if Ashley itself abandons self-serve.
3. **ATS embedding and switching costs (#3).** Distribution that converts to retention: Ashby's
   open Assessments framework is buildable this quarter, Greenhouse/iCIMS listings follow, and
   accumulated rubric/calibration history plus ATS write-back makes churn costly. This is the
   channel that turned Paradox from partner to acquisition target and the mechanism behind
   Checkr's and Greenhouse's durability.

## 7. Gaps and unverifiable items
- **Byteboard:** no search evidence retrieved; excluded from findings rather than assumed.
- **SAP SuccessFactors / Greenhouse / Lever:** exact AI-interview vendors listed not enumerated
  (marketplace pages not directly fetched; partner guides gated behind forms).
- **Workday Marketplace listing timelines:** no published SLA; 6–18-month estimate is my
  inference from certification scope, not a sourced number.
- **Bullhorn marketplace requirements:** single third-party source (jobcannon.io, paraphrased);
  re-verify against Bullhorn's official partner docs.
- **Sapia.ai interview counts:** sources range 1M–8M depending on date; recorded as a range.
- **HireVue current (2026) customer count:** latest confirmed figure located is 700+ (2019–2021
  press); 33M interviews as of Nov 2022 (https://www.hirevue.com, domain-level).
- **Paradox implementation-fee figures:** two review sources disagree ($25–75K vs $30–100K+);
  both cited, neither primary.
- **Several URLs are domain-level** (returned that way by search); article-level paths not
  captured. All quotes marked *(paraphrase)* are search-layer summaries, not verified verbatim
  text.
- **Mercor/micro1 interview mechanics** (format, scoring) not deeply sourced — funding and model
  only.

## 8. Assumptions made
1. Ashley is an early-stage startup (small team, months not years of runway, unknown traction),
   per the run context's instruction to assume this absent evidence.
2. GTM is US-first; NYC LL144 / Illinois AIVIA are the operative audit regimes for planning
   (validity-science and legal-scope questions belong to the `regulatory` and `data-outcomes`
   workers; product-landscape to `competitors`; avatar-replication bear case to `replication`).
3. "Two quarters" budget assumes ~2–4 engineers of capacity and low-seven-figures annual spend
   ceiling; audit cost estimate ($25–75K/yr) is an order-of-magnitude planning number, not a
   quote.
4. The vision-page framing of a long-term structured-interview corpus is treated as strategy,
   not as an existing dataset of unknown-employer scale.
5. Where sources conflicted (Paradox pricing, Sapia counts), both figures are reported and
   flagged rather than averaged.
