# Replication report: the case that the in-house face is NOT a moat

Worker: `replication` · Run: `zf-ashley-moat` · All pages seen 2026-09-23 unless noted. Quotes are verbatim, ≤40 words.

## 1. Summary

The founder's claim that the in-house rendering stack is "the hardest to copy" does not survive contact with the 2026 supply market. At least ten vendors sell real-time, interruptible, photoreal conversational-avatar APIs today, several with claimed end-to-end latencies at or below what "feels human" requires (Anam "180MS avg. agent response time"; Beyond Presence "250 ms speech-to-video latency"; Tavus Phoenix-4 "sub-600ms"). Renting costs $0.04–0.37 per minute, i.e. roughly **$0.80–$7.40 per 20-minute interview**, against Ashley's effective $3.75–$6.00 per interview — so 5+ vendors fit inside Ashley's price with room to spare. Open-source models (MuseTalk 30fps on a V100, MIT; Ditto ~25fps on an RTX 4090, Apache-2.0) make self-hosting cost roughly $0.23 of GPU time per interview. Synthesia — the enterprise avatar incumbent — launched an Interactive Avatar API in July 2026 described as "real-time, interruptible," and ElevenLabs sells avatars at ~$0.11/min. **Verdict: a competitor can field an equivalent face in ~4–8 weeks to demo and ~3–6 months to production by renting (Anam, Hedra, HeyGen LiveAvatar, or ElevenLabs); 6–12 months self-hosting open source. Confidence: high on cost and vendor capability (verified pricing pages), medium on interruption quality and 20-minute identity consistency (marketing claims, not independently tested).**

## 2. Rentable avatar APIs

| Vendor | Real-time / interruptible | Claimed latency | Photorealism approach | Price (verbatim where possible) | Languages | Self-host / on-prem | Hiring / interview use |
|---|---|---|---|---|---|---|---|
| **Tavus** (CVI) | Yes — CVI described as "an end-to-end operating system designed for building responsive, interruptible video agents" (tavus.io research page) | "sub-600ms latency" Phoenix-4 (marktechpost.com, 2026-02-18); "sub-500ms response latency" (daily.co partner page); earlier "end-to-end response times of less than 1 second" (cartesia.ai, Oct 2024) | Photo-driven neural replica; Phoenix-4 is "Gaussian-Diffusion" | Developer plans: Builder $59/mo, 175 min, PAYG "$0.35/min"; Growth $397/mo, 1,300 min, "$0.31/min"; Business $975/mo, 4,000 min, "$0.26/min" (tavus.io/pricing, fetched 2026-09-23). Older table: Starter overage "$0.37/min" CVI | Multi-language via TTS choice | None on pricing page | None found |
| **HeyGen** (Interactive Avatar / LiveAvatar) | Yes — "Avatars can listen and respond instantly through voice, video, or text with minimal delay" (help.heygen.com, 2026-09-09) | "minimal delay" (no ms figure found) | Photo-driven (1080p custom avatar) | "For the price of $475/month, you will receive 6,000 LiveAvatar (LA) Credits. Max session duration: 60 minutes." (help.heygen.com). Third-party: ~2 credits/min Full mode → ≈$0.158/min. General video API: "Avatar $0.99" per minute (help.heygen.com) | 175+ languages claimed site-wide | No | None found; Pipecat ships `HeyGenVideoService` for real-time agents (docs.pipecat.ai) |
| **D-ID** (Agents / streaming) | Yes (streaming agents product) | Not published in fetched pages | Photo-driven ("Self-Hosted Expressive Avatars: Real-Time AI Videos" — d-id.com) | Official API page loads dynamically — GAP. Third-party: "Customer service session (average 8 minutes): ~$0.35–0.55 in avatar streaming costs (roughly $0.04–0.07 per minute)" (gmicloud.ai). Studio: "The length of the video is rounded up to the nearest 15-second interval." (d-id.com/pricing) | Multi-language | **Yes — dedicated self-hosting product** (d-id.com nav: "Self-Hosting") | None found |
| **Anam** | Yes; SDKs incl. LiveKit + Pipecat | "180MS avg. agent response time" and "Our avatars respond faster than you blink." (anam.ai) | Photoreal proprietary (CARA / CARA-4); image-to-avatar | "Real-time AI avatars from $0.04 per minute at scale." Plans: Starter $12/mo, 50 min, "$0.16/min" overage; Growth $299/mo, 2,000 min, "$0.12/min"; Professional $999/mo, 5,000 min, "$0.11/min"; Enterprise "$0.04/min". "You get billed by the second." (anam.ai/pricing) | "over 70 languages" | Not mentioned | None cited; verticals listed are support, sales, tutoring, medical, training |
| **Simli** | Yes (WebRTC) | "<300ms latency requirements" (verda.com, 2025-08-27) | Neural (Trinity-1 "Gaussian Avatar") | Official pricing page 403/404 — GAP. Third-party: "$0.0056–$0.20 per minute, with some configurations including a ~$0.02 startup/session charge" (spatius.ai, 2026-07-05); Trinity-1 "less than $0.01 (a cent) per minute" (aitwin.me) | Unclear | Unclear | None found |
| **Beyond Presence** (bey.dev) | Yes | "250 ms speech-to-video latency and 1-second end-to-end response times" (docs.bey.dev) | "proprietary AI research in computer vision and generative modeling"; "hyper-realistic" | No public pricing on docs — GAP. Third-party: "pay-as-you-go pricing at approximately $6/hour (~$0.10/min)" (globaldev.tech, 2025-03); "$0.20/min after startup + $0.02 startup" (spatius.ai, 2026-07-05) | "multilingual" | No | None found |
| **Synthesia** | Yes — launched Jul 2026: "Today, we're launching the Synthesia Interactive Avatar API to shift from broadcast video to actual conversation: real-time, interruptible" (synthesia.io, 2026-07-15) | Not published in fetched snippets | Photo-driven (240+ avatars, custom from photo/webcam) | Not captured — GAP (API pricing page not fetched) | "160+ languages" | No | None found, but Synthesia already sells into HR/L&D — closest incumbent channel |
| **Soul Machines** | Yes (3D "digital people") | Not published | **3D CG, not photoreal video** | Studio tiers: "Basic – $12.99 per month; Plus – $99 per month; Pro – $2,700 per month" (soulmachines.com via search) | Multi-language | No | None found |
| **UneeQ** | Yes (3D digital human) | Not published | **3D CG** | "$899 per month" (sourceforge.net comparison); enterprise AWS Marketplace contract pricing | Multi-language | Partial (AWS Marketplace deployment) | None found |
| **Hedra** | Yes — "Live Avatars" (Jul 2025) at **$0.05/min**, "claimed ~15x cheaper than existing solutions" (news.aibase.com, 2025-07-23) | Not published | Photo/illustration-driven (Character-3, single image) | $0.05/min (aibase.com) | Multi-language | No | None found |
| **LiveKit / Pipecat** (integration layer) | N/A — frameworks | N/A | N/A | LiveKit: "You can integrate a variety of providers to LiveKit Agents with just a few lines of code." (docs.livekit.io). Third-party: "with a plugin, integration is roughly five lines of code" (docket.io) | N/A | **Both open-source frameworks, self-hostable** | None found |
| **ElevenLabs** (bonus, not in brief list) | Yes (Conversational AI + Avatars) | Not published in fetched snippets | Photo-driven | "Image & Video pricing structure at approximately $0.11/min"; Creator "Includes 275 call minutes / month ($0.08/min for additional)" (elevenlabs.io via search) | 30+ languages | No | None found |

Notes: Anam's FAQ billing rule is the relevant one for cost math: minutes count "from session start until end, 'regardless of whether you are actively speaking or not'" (anam.ai/pricing). Tavus's newer per-minute rates ($0.26–0.35/min) are the closest list-price comparable to a 20-minute session product. The two cheapest verified-rate vendors (Anam at $0.04/min at scale; Hedra at $0.05/min) are both below one-tenth of Ashley's per-interview price.

## 3. Open-source models

| Model | Real-time on what GPU | Quality / notes | Licence | Productionizable in one quarter by a small team? |
|---|---|---|---|---|
| **MuseTalk** (Tencent Music) | "a real-time high quality lip-syncing model (30fps+ on an NVIDIA Tesla V100)" (github.com/TMElyralab/MuseTalk) | Latent inpainting of mouth region on video frames; 25fps recommended | "The code of MuseTalk is released under the MIT License. There is no limitation for both academic and commercial usage." (repo) | **Yes** — this is the classic self-host route (commercial-clean code, modest GPU). Needs a driving video loop + streaming pipeline around it |
| **Ditto** (Ant Group, ACM MM 2025) | ~25 FPS on RTX 4090 (24GB); DiT in "motion space" with "low first-frame latency" (github.com/antgroup/ditto-talkinghead) | Controllable gaze/expression; checkpoints on Hugging Face | "This repository is released under the Apache-2.0 license" (repo) | **Yes** — single-image driven, streaming-oriented design |
| **LivePortrait** (Kuaishou/Kling) | "12.8ms per frame on an RTX 4090" ≈ 78 fps ceiling (repo/HF) | Stitching/retargeting control; weights ~2.14GB, fp16 <300MB VRAM | Code permissive, **but** depends on "InsightFace `buffalo_l` models, which means the model cannot be used commercially" (replicate.com docs) | Speed yes; **commercial blocker** unless InsightFace dependency replaced |
| **OmniAvatar** (Jun 2025) | Not strictly real-time (offline diffusion; 20–50 steps) | Full/half-body + hands from single image | Repo live with weights ("June 24-th, 2025: We released the inference code and model weights!"); licence not confirmed — GAP | Not in one quarter for real-time use |
| **Omni-LiveAvatar** (Aug 2026) | "the first framework for minute-level, real-time streaming joint audio-video avatar generation" (arxiv.org, 2026-08-17) | Research system; ~20.88 FPS on 5×H800 per related coverage | Unknown / research | No — but signals where the frontier is heading |
| **EchoMimicV2** (Ant Group) | No — "about 2.5 hours to generate 45 sec video" reported on AWS GPUs (GitHub issue #131, 2024-08-13) | Semi-body + hands | Apache-2.0 (code) | Not for real-time |
| **Hallo / Hallo2 / Hallo3** (Fudan) | No — diffusion; optimized for "4K, hour-long" offline generation | High visual quality | Code permissive-ish; **model weights governed by CogVideoX licence terms** (Hallo3 repo) | Not for real-time |
| **SadTalker** | No (offline, seconds-plus per clip on 3090/4090) | 3DMM-driven single-image animation | Apache-2.0 (code) | Not for real-time |
| **Wav2Lip** | Yes-ish (very fast, low-res 96×96 lip region) | Dated quality | "the license for the code is changed from MIT to non-commercial/research use only" (GitHub issue #104, 2020-10-08) | **No — commercial use blocked** |
| **NVIDIA Audio2Face-3D / ACE** | Yes — "supporting both pre-recorded files and real-time use cases" (github/NVIDIA, NGC) | 3D mesh animation (not photoreal video); needs a 3D renderer (Unreal/Unity) | Open-sourced Sep 2025; "use of the Audio2Face models is governed by the NVIDIA Open Model License" (NGC catalog) | Yes for a 3D-style interviewer; but 3D look ≠ photoreal claim |

Bottom line: a small team has at least two commercial-clean, real-time-capable open-source paths today (MuseTalk, MIT; Ditto, Apache-2.0), and NVIDIA gives away the 3D variant outright.

## 4. Unit economics

Ashley's realized price per completed interview (from tryashley.ai/pricing, fetched 2026-09-23):
- PAYG: $6.00; Growth: $499/100 = **$4.99** effective ($5.50 overage); Scale: $1499/400 = **$3.75** effective ($5.00 overage).
- Interview length: site says "typically 15–25 minutes" → assume **20 minutes median** (arithmetic uses 20).

**Cost to a rival renting an avatar API, per 20-min interview** (billed on session duration; several vendors — Tavus CVI, Anam, Beyond Presence — bundle STT+LLM+TTS+avatar in that rate, so this is close to all-in):

| Vendor & rate | Arithmetic | Cost/interview | % of Ashley's $4.99 |
|---|---|---|---|
| Anam Enterprise $0.04/min | 0.04 × 20 | **$0.80** | 16% |
| Hedra $0.05/min | 0.05 × 20 | **$1.00** | 20% |
| Simli (third-party mid ~$0.05/min) | 0.05 × 20 | **$1.00** | 20% |
| D-ID ~$0.04–0.07/min (third-party) | 0.055 × 20 | **$1.10** | 22% |
| ElevenLabs ~$0.11/min | 0.11 × 20 | **$2.20** | 44% |
| Anam Growth $0.12/min | 0.12 × 20 | **$2.40** | 48% |
| Beyond Presence ~$0.10–0.20/min | 0.15 × 20 | **$3.00** | 60% |
| HeyGen LiveAvatar $475/6,000 credits ÷ 2 credits/min = $0.158/min | 0.158 × 20 | **$3.17** | 64% |
| Tavus Business $975/4,000 min = $0.244/min | 0.244 × 20 | **$4.88** | 98% |
| Tavus Builder PAYG $0.35/min | 0.35 × 20 | **$7.00** | 140% — not viable |

**Self-hosted open-source GPU cost per interview:**
- RunPod market rates (2026, via search of runpod.io and comparators): RTX 4090 ≈ **$0.69/hr** (down to ~$0.34/hr spot); L40S "$1.09/hr" (runpod.io article, 2025-06-29); A100 PCIe $1.39–1.59/hr (FlexPrice/ComputePrices).
- MuseTalk or Ditto serves one avatar stream on one 4090. A 20-min interview occupies 20/60 hr × $0.69 = **$0.23** GPU time. With TTS/STT/LLM APIs (~$0.10–0.30 per interview for ~4,000 spoken words at commodity ASR/LLM rates) and 50% GPU utilization from imperfect session packing ($0.23 ÷ 0.5 = $0.46), all-in face cost ≈ **$0.56–0.76 per interview** — ~11–15% of Ashley's Growth-tier effective price.
- Even doubling GPU prices (Secure Cloud A100 at $1.59/hr → $0.53 GPU per interview) keeps the self-hosted face under $1.

**Verdict: renting is viable at Ashley's price** with Anam, Hedra, Simli, D-ID, ElevenLabs, or HeyGen LiveAvatar (face cost 16–64% of the interview price), leaving the rival 36–84% gross margin before adding their own ops cost. Only Tavus at list PAYG rates ($0.35/min) fails the test — and Tavus's bundled-minute Business tier ($0.244/min, $4.88/interview) still roughly breaks even against Scale-tier pricing ($5.00 overage).

## 5. Time-to-replicate scenarios

**(a) Startup renting an API — 2–6 weeks to demo, 3–6 months to production.**
Evidence: LiveKit ships avatar-provider plugins ("just a few lines of code", docs.livekit.io); Pipecat ships `HeyGenVideoService`; Anam's SDKs include LiveKit and Pipecat. The interviewer logic (rubric, adaptive follow-ups) is standard LLM work — Ashley's own site concedes the contrast: "a voice on a phone line is a feature that any hiring product can add in a quarter" (tryashley.ai/vision); swapping the rented voice for a rented face does not change that arithmetic. Production-quality risks: barge-in polish (Anam/Tavus claims are marketing, not independently verified), 20-minute identity/expression consistency, vendor rate changes, and building the employer-side workflow (ATS, scorecards). None of these is a multi-year problem.

**(b) Incumbent with an ML team building on open source — 4–8 weeks to demo, 6–12 months to production.**
MuseTalk (MIT, 30fps on V100) and Ditto (Apache-2.0, ~25fps on RTX 4090) are commercially usable today; NVIDIA's Audio2Face-3D is open under the NVIDIA Open Model License for a 3D-style fallback. The hard parts are the same ones Ashley solved — streaming chunking, interruption rollback, latency budgeting across STT→LLM→TTS→render — which is exactly what Tavus/Cartesia published as engineering practice ("sub-90ms" TTS, <1s end-to-end, Oct 2024). A 5–10-person ML+infra team that has shipped streaming inference before can match a small startup's stack; the main risks are hiring, long-session artifact drift, and GPU cost engineering (which is small: ~$0.50/interview).

**(c) Rival acquiring an avatar company — 6–12 months including deal time.**
Precedents: Google acquired avatar startup **Alter** "for about $100 million" (TechCrunch, 2022-10-27); Apple quietly acquired 3D-avatar company **TrueMeeting** in early 2025 (roadtovr.com); Meta acquired **WaveForms AI** (voice-emotion AI) in August 2025 (The Information/SiliconANGLE). A hiring-tech incumbent could also skip M&A entirely and white-label Synthesia's Interactive Avatar API (launched 2026-07-15, "real-time, interruptible") into an existing ATS-embedded product — weeks to demo, leveraging a sales force and compliance bench Ashley cannot match.

## 6. Bear case per moat type

- **Technology (the face).** The central claim — "It is the slowest thing we built and the hardest to copy" (tryashley.ai/vision) — is contradicted by a 2026 market where ten-plus vendors sell real-time interruptible photoreal avatars at $0.04–0.37/min with 180–600ms latencies, where Synthesia launched an interruptible interactive-avatar API in July 2026, and where MIT/Apache-2.0 models run 25–30fps on a $0.69/hr GPU. "Hardest to copy" is a statement about *this team's* calendar, not about the market's. Weakest moat candidate for an early-stage company.
- **Data (transcripts and rubrics).** The vision page's real long-term asset — "a structured, consistent record of how people answer questions about the work" — is genuine, but its value depends on volume Ashley has not demonstrated (two named institutional users). Rubrics are customer-supplied and portable; transcripts can be seeded synthetically or from any incumbent's history. Data moats require scale before they deter anyone; today a rival's first 10k interviews get them to parity. (Validity science is another worker's scope.)
- **Regulatory / compliance.** NYC LL144 and Illinois AIVIA/HB 3773 impose audit and notice duties that any funded competitor can satisfy with the same third-party auditor and counsel. Precedent cuts against tech differentiation: HireVue dropped facial-analysis scoring under public pressure — the winning compliance posture (Ashley's "words-only" scoring) is a policy that can be copied in a release cycle, and Ashley itself frames it as "positioned to support" audits, not as a certification it holds.
- **Brand and candidate trust.** No evidence of consumer-side brand recognition; the trust posture (AI disclosure up front, no auto-rejection, human decides) is copyable policy, not technology. The Greenhouse stat Ashley cites (38% abandonment of bad AI interviews) is category-level and benefits whichever vendor is best — it does not bind candidates to Ashley.
- **Switching costs.** Explicitly near zero by Ashley's own pricing page: "Plans are month-to-month," "Can we cancel anytime? Yes." Per-interview billing and no deep data lock-in (webhooks only "rolling out"; no public API) mean an employer can A/B a rival next month. This is the weakest moat of all, and it is self-inflicted.
- **Network effects.** None visible. Two named users (U.S. Air Force Academy, UF Warrington) are logos, not a network; neither employers nor candidates get more value as more employers join. The data asset is a *scale* effect at best, not a network effect, and only materializes at volume.
- **Distribution.** Currently an anti-moat: "The integration surface is currently guided, not self-serve" with "Public, anonymous API signup ... not available yet" (tryashley.ai/developers) means slower adoption, while incumbents (HireVue; and now Synthesia with an enterprise HR channel) already own ATS ecosystems and procurement. No marketplace, no partner ecosystem, no self-serve funnel.

**Weakest for an early-stage company:** switching costs (month-to-month by design), the face itself (rentable for <$1–3/interview), and network effects (absent). Strongest survivors of this bear case: none of the current assets, alone, clears the 12-month replication bar — which is the point of this report.

## 7. Commoditization trajectory

Evidence that quality is rising and price is falling, 2024–2026:

- **Latency:** Oct 2024 — Tavus/Cartesia demo "end-to-end response times of less than 1 second"; Feb 2026 — Tavus Phoenix-4, "sub-600ms latency ... via WebRTC" (marktechpost.com, 2026-02-18); 2026 — Anam claims "180MS avg. agent response time," Beyond Presence "250 ms speech-to-video." The floor has fallen ~5x in ~18 months.
- **Price:** Hedra entered live avatars at "$0.05 per minute — claimed ~15x cheaper" (aibase.com, 2025-07-23); Anam advertises "from $0.04 per minute at scale" (2026); Simli's Trinity-1 claims "<$0.01 per minute"; Selvia offers "$0.03/min on-demand"; third-party tracking puts effective market rates around "$0.15–0.20/min" (selvia.ai, Jun 2026; spatius.ai, 2026-07-05). For calibration, Tavus's older CVI overage was $0.37/min — today's floor is ~9x lower.
- **Supply:** NVIDIA open-sourced Audio2Face (Sep 2025); ElevenLabs (the voice leader) added avatars at ~$0.11/min; Synthesia (the enterprise avatar leader) launched an Interactive Avatar API on 2026-07-15; the open-source frontier moved from MuseTalk (2024) to Ditto (2025) to Omni-LiveAvatar minute-level streaming (arXiv, 2026-08-17). Market analysts size the category at ~$1.08B in 2026 growing ~32.9% CAGR (Grand View Research) — growth with falling unit prices is the textbook commoditization signature.
- **Implication for "we own the pipeline":** over 12–24 months the photoreal face follows the path of TTS (from premium per-minute API to ~$0.0x/min commodity with open-weight alternatives). Owning the pipeline then confers only a cost/latency edge that rented APIs will underprice, while the engineering slog Ashley paid (the "slowest thing we built") becomes a weekend integration for everyone else. The durable assets are elsewhere: data at volume, validity evidence, distribution, and trust brand — each of which must be built deliberately, because none is implied by owning the renderer.

## 8. Gaps and unverifiable items

- **D-ID official API per-minute rates:** pricing page loads dynamically (two fetch attempts returned nav/FAQ only); only third-party ~$0.04–0.07/min (gmicloud.ai). D-ID does offer a self-hosted product (nav link confirmed).
- **HeyGen LiveAvatar credit burn:** the ~2 credits/min (Full) figure is third-party (medux.io); HeyGen help article with $475/mo–6,000-credit plan was reached only via search snippet; direct doc URLs 404'd.
- **Simli official pricing:** simli.com/pricing 404 and simli.ai/pricing 403; all Simli rates are third-party.
- **Tavus official docs:** maker.tavus.io behind bot check (403 / Cloudflare "Just a moment"); latency figures cited from Tavus marketing/blog and partner pages rather than the docs.
- **Beyond Presence official pricing:** none published on docs.bey.dev; two conflicting third-party figures (~$0.10/min vs ~$0.20/min + $0.02 startup).
- **Synthesia Interactive Avatar API pricing:** launch post found; per-minute rate not captured.
- **Soul Machines / UneeQ per-session pricing:** not publicly listed (subscription/contract only); both are 3D-style, so less directly comparable anyway.
- **Interruption/barge-in quality and 20-minute identity consistency** of any vendor: no independent benchmark was testable in this run; claims are vendor marketing (Anam cites an "Avatar Benchmark (2026)" that I did not independently verify).
- **OmniAvatar repo licence** not confirmed from the repo itself.
- **Ashley traction** (customers, volume, team, runway): unknown by design (director's list); all moat judgments assume an early-stage startup per context.md.

## 9. Assumptions made

1. Median interview length = 20 minutes (site: "typically 15–25 minutes"); arithmetic scales linearly if 15 or 25 is used.
2. Renting vendors bill the full session wall-clock (Anam FAQ confirms; HeyGen/Simli billing basis unverified), so a 20-min interview = 20 billed minutes.
3. Ashley's effective per-interview price is taken as $3.75–$6.00 from published plan math, ignoring free-tier promotions.
4. Self-hosted cost assumes one avatar stream per consumer GPU, ~50% utilization across scheduled sessions, plus commodity STT/LLM/TTS APIs; RunPod rates used as the GPU price reference ($0.69/hr RTX 4090, $1.09/hr L40S, $1.39–1.59/hr A100 PCIe).
5. "One quarter" ≈ 13 weeks; "production quality" means: reliably sub-second turn-taking, interruption recovery, and consistent avatar identity across a 15–25-minute session, at hiring-employer SLA expectations.
6. HeyGen LiveAvatar effective rate = $475 ÷ (6,000 credits ÷ 2 credits/min) = $0.158/min (depends on the third-party 2-credits/min figure; flagged as such).
7. Where a vendor's latency is quoted by a competitor (e.g., Anam vs Tavus comparisons), I preferred the vendor's own page or a launch-coverage source; conflicts are noted inline.
