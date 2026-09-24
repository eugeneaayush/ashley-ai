# Ashley.Ai competitive moat design

Date: 2026-09-23. Status: approved in brainstorming, awaiting owner review of this document.
Owner: Aayush Tuli (Helen Labs, Inc.). Product: Ashley.Ai, https://www.tryashley.ai.

## 1. Context and constraints

- Ashley is an AI interviewer for high-volume hiring: a live, photoreal avatar rendered by an in-house
  real-time stack, adaptive questions, transcript-only scoring on the employer's rubric, a human makes
  every decision, 11 languages. Pricing is per interview: $6 pay as you go, $499/month for 100,
  $1,499/month for 400, month to month.
- Stage (owner's answers, 2026-09-23): pilots and pre-revenue; beachhead is high-volume hourly hiring;
  one or two technical founders with a short runway; the goal is actual defensibility against a
  funded copycat or an incumbent adding a face within a year, not a fundraising story.
- The owner's starting belief was that the in-house avatar stack is the moat. The research below says it
  is not, and this design places the moat elsewhere.

## 2. What the research established

Five Z.ai research workers produced the reports in `2026-09-23-competitive-moat-research/`. The facts
the design rests on were re-fetched from primary pages by the director; status is marked per item.

1. **The face is rentable.** Anam advertises "Real-time AI avatars from $0.04 per minute at scale"
   (anam.ai/pricing, verified). A rival's 20-minute interview therefore costs about $0.80 in avatar
   fees at scale, or $2.40 on Anam's $0.12/minute Growth tier, against Ashley's effective $3.75 to
   $6.00 per interview. MuseTalk is "released under the MIT License. There is no limitation for both
   academic and commercial usage" and runs "30fps+ on an NVIDIA Tesla V100" (github.com/TMElyralab/
   MuseTalk, verified). Worker estimate: 4 to 8 weeks to a demo, 3 to 6 months to production by
   renting; 6 to 12 months self-hosting. Synthesia's interruptible Interactive Avatar API (July 2026)
   is worker-sourced, not re-fetched.
2. **Distribution is the asymmetry.** Ribbon's homepage shows "1M+ interviews completed", "Syncs with
   60+ ATS out of the box", "SOC 2 Type I Certified With Type II in observation", and "NYC Local Law
   AI Bias Audit Last audited: 2025" (ribbon.ai, verified). Alex shows "33+ officially supported ATS
   integrations" and 30 languages (alex.com, verified); its $17M Series A led by Peak XV is
   worker-sourced. HireVue reported customers conducting "over 1 million video interviews in just
   30 days" (hirevue.com press release, verified). Workday acquired Paradox in 2025 (worker-sourced,
   consistent with director knowledge). Ashley's own compare pages understate Ribbon and Alex.
3. **Compliance is table stakes as posture, a partial moat as product.** "Sapia.ai is the first AI
   interview company to achieve ISO 42001 certification" (sapia.ai, published 2025-10-07, verified).
   EU AI Act high-risk employment obligations now apply from 2 December 2027 ("Starting on 2 December
   2027, high-risk AI systems will be subject to strict obligations", digital-strategy.ec.europa.eu,
   verified; artificialintelligenceact.eu timeline, verified). NYC Local Law 144, Illinois AIVIA and
   HB 3773, California's FEHA automated-decision rules, and Texas TRAIGA are in force
   (worker-sourced law-firm summaries). The regulatory worker's verdict: compliance alone is a tax;
   productized audit infrastructure, pre-audited configurations, and certification timing are a
   partial moat. A photoreal face raises the compliance bar (biometric consent, synthetic-content
   disclosure, the EU prohibition on workplace emotion recognition), which is an advantage only for the
   vendor built to clear it.
4. **Data compounds only with outcome labels.** Transcripts and rubrics are commodities; incumbents
   hold millions of transcripts. What compounds is hire, retention, and performance labels joined to
   transcripts on a stable, versioned instrument. Worker estimate from validation statistics: about
   1,000 to 2,000 labeled hires per role family are needed to prove a proprietary model beats a good
   rubric plus a frontier model; at 10,000 interviews a month that is 1 to 4 years; at 1,000 a month it
   is effectively unreachable. Candidate-side "interview once, reuse everywhere" networks have failed
   repeatedly in HR tech (Triplebyte, Hired) and are explicitly out of scope.
5. **Moat ranking.** The moat-playbook worker's top three for an early-stage company: a trust-posture
   counter-position with published audits, a self-serve month-to-month pricing counter-position, and
   ATS-embedded switching costs. The rendering stack ranked fourth as process power that decays as
   avatar APIs commoditize.

## 3. Decision

Build approach 1, the embedded and instrumented interview layer for hourly hiring, with the cheap parts
of approach 2, the audit-grade interviewer, layered on. The rendering stack is reframed as a cost and
latency advantage, not the defense. Rejected: leading with certification spend (approach 2 alone),
deepening the rendering stack as the moat (approach 3), and any candidate-side network.

## 4. Design

### 4.1 Positioning (the counter-position)

Ashley is the interview step for hourly hiring teams with no procurement department: self-serve,
per-interview pricing, month to month, disclosed AI, words-only scoring, a human decides. Incumbents
whose revenue runs on $30k to $100k implementations cannot match this without cannibalizing their sales
motion. The face stays in the story as the reason candidates finish and prefer the interview. The
beachhead is one flagship multi-location operator (a QSR or retail franchise group, or a staffing
agency on Bullhorn) whose rollout becomes the referenceable case study. Everything below exists to make
that customer expensive to leave.

### 4.2 The embedded layer

Four components, all engineering, none needing cash:

- **Two-way ATS integration.** Interviews trigger from an ATS stage change; results write back as
  structured fields: per-question rubric scores, transcript link, recommendation, rubric version. The
  first two integrations are chosen by where the flagship's applicants already live. Candidates from
  the research: Ashby (open Assessments framework), Greenhouse, iCIMS, Bullhorn for staffing.
  Hourly-native systems (Workstream, Fountain, Harri) were not researched and need a quick check.
  Paradox is Workday's and is treated as a rival channel.
- **Outcome webhooks coming in.** Hire decision, 30, 90, and 365-day retention, and any manager rating,
  keyed to the interview session id. This is the only data that compounds and it cannot be retrofitted.
- **A stable instrument per role family.** Fixed core question batteries and anchored rubrics for six to
  ten hourly role families, versioned on every score row. Custom avatars are allowed; custom instruments
  are not, because rows stop pooling.
- **Per-customer calibration.** Once a customer has a few hundred labeled outcomes, show how their rubric
  predicts their own retention. Legally uncontroversial and sticky.

Switching costs come from the four together: the integration, the accumulated labeled history, the
calibrated rubrics, and the audit trail from 4.4.

### 4.3 Data and instrumentation

- **Append-only event log** per session: every question text, rubric, prompt, and model version stamped
  on each score row, plus the outcome events. Scoring prompts are never hot-patched silently.
- **Panel scoring by default**: several model ratings per answer, aggregated; rating disagreement is
  kept as a signal.
- **Consent architecture for pooling.** Consent to record is unchanged. A separate, optional,
  plain-language toggle at interview start covers pseudonymized cross-employer improvement of scoring.
  Per-customer learning runs without it; cross-customer learning runs only on opted-in rows. Enterprise
  terms default to customer-owns-data with opt-in pooled learning.
- **Deletion that propagates.** Illinois AIVIA 30-day deletion and GDPR erasure reach derived features:
  deletable feature-store rows, retraining windows, deletions logged into audit exports.
- **Frozen benchmark per role family.** Human double-rated transcripts with eventual outcome labels, held
  out; every rubric or model change is scored on criterion validity and the four-fifths adverse-impact
  ratio before shipping. The methodology is published; the data stays private.

### 4.4 Compliance layer

- **Disclosure receipts.** Timestamped record that Ashley identified herself as an AI and the candidate
  consented, attached to every session.
- **Audit exports.** One-click packs for NYC Local Law 144 selection-rate reporting, Illinois AIVIA and
  HB 3773 notices and deletion logs, and California automated-decision rules, generated from the event
  log. Default for every tier, not only Enterprise.
- **First independent bias audit** when cash allows, roughly $25k to $75k a year, published with
  methodology. Ribbon already advertises a 2025 audit, so this closes a gap; publishing methodology and
  results is the differentiating part.
- **ISO 42001: start the clock, defer the spend.** Document the AI management system now as a byproduct
  of the event log and consent design; certify only when a customer demands it.
- **Hard rule: never score expression.** Words only, stated publicly. The EU prohibition on workplace
  emotion recognition is the nearest cliff for a product with a face.

### 4.5 Sequencing

| Quarter | Build | Proof point |
|---|---|---|
| Q4 2026 | Event log; versioned instrument for 6 to 10 hourly role families; disclosure receipts; first two-way ATS integration chosen by the flagship's stack; outcome webhooks in | Flagship signed on per-interview pricing; first outcome labels flowing |
| Q1 2027 | Audit export packs; panel scoring; consent toggle for pooling; second ATS or Bullhorn integration; first marketplace listing | Flagship rollout to more locations; per-customer calibration shown to them |
| Q2 2027 | Frozen benchmark per role family; published methodology; first independent audit if cash allows; second flagship in a different chain | Public validity and fairness page; case study |
| H2 2027 | ISO 42001 only on customer demand; cross-customer model only on opted-in rows | Labeled outcomes above about 1,500 per top role family |

Each quarter carries one integration and one proof point, because two founders cannot run marketplace
programs, audits, and sales at once.

## 5. Success criteria at 12 months

A rival with a rented face can match the demo but not this: at least two multi-location customers whose
scores, transcripts, and labeled outcomes live in Ashley's event log, integrated into their ATS, on a
versioned instrument, with published audit methodology. Leaving requires re-integrating, re-calibrating,
and abandoning the audit trail.

## 6. Risks and kill criteria

- **Paradox inside Workday, or Ribbon, ships a face and owns the hourly funnel first.** Mitigation: the
  flagship and the outcome loop, which distribution alone does not provide, and speed on the first
  integration.
- **No outcome labels.** If the ATS loop never closes, Ashley accumulates only transcripts. This is the
  largest failure mode and the reason outcome webhooks are in the first quarter.
- **Instrument drift** from bespoke per-customer questions. Custom avatars yes, custom instruments no.
- **Pooling without consent** converts the asset into a liability. The consent toggle and propagating
  deletion are mandatory, not optional.
- **Founder bandwidth.** If a quarter's integration and proof point both slip, cut scope rather than add
  a second integration.

## 7. Assumptions and open questions

- Interview length assumed at 20 minutes median for the rental cost arithmetic (site says 15 to 25).
- Labeling rate assumed at 5 to 15 percent of interviewed candidates hired, with 6-month label lag, in the
  volume estimates.
- The hourly-native ATS landscape (Workstream, Fountain, Harri) was not researched; the first integration
  choice depends on the flagship's actual stack.
- The $17M Alex Series A, Synthesia's July 2026 API launch, the Workday acquisition of Paradox, the
  HireVue Illinois BIPA settlement (2026), and the law-firm summaries of state AI-hiring rules are
  worker-sourced from pages the director could not re-read (JavaScript-only or moved). None of them
  changes the decision.
- The Digital Omnibus law-firm URL cited by the regulatory worker is dead; the 2 December 2027 date was
  confirmed from the European Commission's AI Act page and the AI Act implementation timeline instead.

## 8. Provenance

Research run `zf-ashley-moat` (five Z.ai workers, 2026-09-23): units replication, competitors,
moat-playbook, regulatory, data-outcomes; all completed on the first attempt. Briefs and the shared
context file are in `~/zai-fleet-runs/zf-ashley-moat/`; the five reports are copied beside this document.
Verification by the director: at least two claims per unit re-fetched from the source page with caching
disabled; results recorded per item in section 2.
