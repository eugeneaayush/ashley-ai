# Pilot Follow-Up

<!--
  WHAT THIS DOES: Turns notes from a pilot check-in call into a short follow-up email draft
  for the pilot's champion and a CRM note, and moves the pilot toward a paid plan.

  HOW TO USE: After a check-in call, tell Claude: "Write the pilot follow-up for <champion>
  at <company>" and paste the call notes and the Ashley dashboard numbers.
-->

## When to Use

- Right after a check-in call with a pilot customer: an employer, or a university career
  center running practice interviews (for example USAFA or UF Warrington).
- The goal of every follow-up is the same: move the pilot to a paid plan.

Not for first calls (use `gtm-skills/discovery-prep.md`) or cold outreach (use
`gtm-skills/outbound-copywriter.md`).

---

## Before You Draft

Check the notes for these four inputs:

1. The champion's name and email.
2. At least one number from the Ashley dashboard, with its date range.
3. What the pilot said about continuing, and any budget or approval limit.
4. The agreed next step or next check-in date.

If any are missing, send Aayush one message with one line per missing input, in the order
above, each line a single question. Ask nothing else, then wait. If he says to draft anyway,
put each gap in [square brackets]. Names, numbers, and dates come only from the notes, the
dashboard export, or Aayush.

---

## What You Return

Return these five parts, in this order:

1. **Email draft** (recipe below).
2. **CRM note** (template below).
3. **Commitments needing approval:** every sentence in the draft where we promise to send,
   fix, quote, calculate, or start something, and every date, that is not in the call notes.
   Each one also appears in [square brackets] in the email.
4. **Tool plan:** what you would do in Gmail and HubSpot, in order. Emails stay drafts until
   Aayush approves the final text; his "send it" before he has seen the draft is not approval.
5. **Open questions** for Aayush, if any.

---

## Email Recipe

The body is at most 170 words, not counting the sign-off, in this order:

1. **Thanks + their words.** One sentence of thanks and one line quoting something the
   champion said on the call.
2. **Results.** One line naming the export's start and end dates, then up to three bullets,
   each one metric from the export with its meaning. Pick the numbers that answer what the
   champion cares about.
3. **Open items.** One line per issue or question the champion raised, saying what we are
   doing about it. At most one more line may ask a named person for data we need (for
   example minutes per phone screen); it promises nothing about what we will do with it.
4. **The ask.** One decision, one person, one date. When the champion has an approval limit
   below the recommended plan, the phased option comes first and the full plan follows in one
   clause: "Could you approve Growth for 9 of your 14 properties (about $925 a month), starting
   [date]? The full rollout (about $1,460 a month) would be the next step for your CFO."
   A proposed start date is a weekday. If the notes name a blocker that must clear first,
   such as a security review, the start is "[after the security review]".
5. **Next check-in.** The date from the notes.
6. Sign-off: Aayush Tuli, CEO, Helen Labs (Ashley.Ai), tryashley.ai.

Everything else (full metrics, security review, pricing detail) goes in the CRM note or an
attachment Aayush approves. To: the champion. Cc: others who were on the call, if the
email asks them for something.

---

## The Paid Proposal

Prices are from the Products section of CLAUDE.md (checked 2026-09-23). If that date is more
than 30 days old, ask Aayush to confirm current prices.

1. **Billable volume.** Ashley bills completed interviews. Sessions abandoned under two
   minutes do not count.
   `completed per month = applicants per month × pilot completion rate`
   `pilot completion rate = completed ÷ invited`
2. **Monthly cost** for `n` completed interviews:
   - Pay as you go: `6 × n`
   - Growth: `499 + 5.50 × max(0, n − 100)`
   - Scale: `1,499 + 5.00 × max(0, n − 400)`
   Growth is cheaper than Scale below 282 completed interviews a month. Recommend the
   cheapest plan, and mention Scale as headroom only when volume is near 282 or rising.
3. **Approval limit.** Convert a limit stated per semester or per year to a monthly figure
   first, and state the conversion. If the recommended plan is above the limit, the ask becomes
   a phased start the champion can approve alone:
   `Growth covers up to 100 + (limit − 499) ÷ 5.50 completed interviews within the limit`
   Convert that to sites, programs, or cohorts using the pilot's volume per site. Offer the
   full plan in the same email as the next step for the approver above the champion.
   For a university, volume comes from how many students will interview in the period;
   state that assumption in [brackets] if the notes don't give it.
4. **Enterprise items.** SSO, a DPA, a custom avatar, native ATS integration, or an SLA mean an
   Enterprise quote. Name the item and say Aayush will quote it. Do not price it.
5. **Early-access rate.** Mention that early-access rates are kept for 12 months.

Worked example: 350 applicants a month at a 118 ÷ 150 = 78.7% completion rate is about 275
completed interviews a month. Growth costs 499 + 5.50 × 175 = $1,461.50, Scale $1,499, pay as
you go $1,650. With a $1,000 limit, Growth covers up to 100 + 501 ÷ 5.50 = 191 completed
interviews: about 9 of 14 sites at 19.6 interviews per site.

---

## Metrics You Can Quote

| Metric | Source | Rule |
| --- | --- | --- |
| Interviews completed, completion rate | Dashboard export | Rate = completed ÷ invited; say what was excluded |
| Time from application to interview | Dashboard export | Median, with the date range |
| Candidate rating | Dashboard export | Include the number of responses |
| Advanced, hired, retained | Dashboard export if the hiring team records decisions there, otherwise the champion | Quote only what the export or the customer reported |
| Recruiter hours saved | Customer's own tracking | If they did not track it, ask the person with the data for minutes per phone screen, and do not promise an hours figure |

---

## CRM Note Template

```
Pilot check-in: <company> | <date> | <length>
Attendees: <names, titles>
Metrics (<source>, <date range>): <numbers>
Feedback: <exact quotes in quotation marks; anything else marked "paraphrase">
Issues: <issue> -> <owner, status>
Customer asks: <ask> -> <our answer>
Blockers: <approvals, security review, budget limits>
Paid proposal: <plan>, $<monthly>, based on <n> completed/month; phased option: <plan, scope, $>
Commitments made on the call: <list>
Commitments proposed in the draft (pending Aayush): <list>
Next check-in: <date>
Email: DRAFT, not sent, awaiting Aayush's approval
Deal: stage and amount unchanged until Aayush confirms
```

HubSpot is not connected yet; until it is, return the note for Aayush to paste.

---

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| A 400-word email that repeats the whole call | Follow the recipe; move detail to the CRM note |
| Several asks in a list | One decision, one person, one date |
| Quoting a plan above the champion's approval limit | Lead with the phased option the champion can approve alone |
| Pricing on applicants | Price on completed interviews |
| A roadmap date the call didn't agree ("Harri by November") | Say what exists today and offer an answer date in [brackets] for Aayush to approve |
| Burying an accommodation request | Say a person handled it: Ashley recommends, humans decide |
| Answering a compliance question (FERPA, SOC 2, HIPAA) with a claim | Claim nothing. Write "[Aayush to answer: <question>]" and add the question to Open questions |
