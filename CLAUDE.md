# CLAUDE.md -- Helen Labs (Ashley.Ai) Company OS

<!-- Filled in from the owner interview on 2026-09-27. Items still open are marked
     "TODO: fill in later". Keep this file the hub: move detail into blueprint/ files. -->

## What This Is

This is the Company OS for **Helen Labs, Inc.**, maker of **Ashley.Ai** (https://www.tryashley.ai). It gives Claude full business context: who we are, how we operate, our tools, our processes, and our rules.

**Owner:** Aayush Tuli (8xblbcdas9dpcxtttkjwxfiqzw5cat@gmail.com)
**Repo:** eugeneaayush/ashley-ai (private)
**Local path:** /Users/eugenekainly/ashley-ai

---


## Company Identity

**Company:** Helen Labs, Inc. (product: Ashley.Ai)
**What we do:** The AI interviewer for high-volume hiring: a live, photoreal interviewer that gives every applicant a real first-round conversation, scored on the employer's rubric.
**Industry:** HR tech, AI recruiting software
**Stage:** Pre-revenue, running pilots (U.S. Air Force Academy; University of Florida Warrington College of Business)
**Team size:** 3 co-founders (one business, two technical)

### Mission
Give every applicant a real conversation, and help every company hire the best person rather than the best resume.

### Core Values
- **Candidates always know.** Ashley discloses she is an AI. No one is evaluated by AI without knowing it.
- **Humans decide.** Ashley recommends; a person makes every hiring decision. No candidate is auto-rejected.
- **Judge the words.** Score what people say against the rubric, never appearance, accent, or background.
- **Nobody gets ghosted.** Every applicant gets a real conversation and a timely outcome.

### Key People

| Name | Role | Notes |
|------|------|-------|
| Aayush Tuli | CEO & co-founder (business) | Primary operator. All Claude actions serve this person. |
| TODO: fill in later | Technical co-founder | Engineering: in-house avatar models and real-time rendering stack. TODO: name and focus. |
| TODO: fill in later | Technical co-founder | Engineering: in-house avatar models and real-time rendering stack. TODO: name and focus. |

---


## Products / Services / What We Do

Prices and features from tryashley.ai, checked 2026-09-23. Strategy and positioning: `blueprint/wiki/moat-decisions.md`.

### Ashley AI Interviewer
The core product. Live, photoreal video interviews rendered in real time by our own stack, not a rented avatar API. Adaptive, role-specific follow-up questions in 11 languages, with live captions. Scores the transcript against the employer's rubric and keeps transcripts and recordings for every interview. Ashley introduces herself as an AI at the start.

### Enterprise interviewer
Custom-branded interviewer (avatar, voice, and tone), compliance pack (audit exports and notice workflows), SSO, DPA and security review, dedicated capacity with an SLA, and native ATS integration support.

### Self-serve plans
Pay per completed interview, not per seat. Starter is free for 10 interviews. Pay as you go is $6 per interview. Growth is $499/month for 100 interviews ($5.50 overage). Scale is $1,499/month for 400 interviews ($5.00 overage). Month to month; early-access rates are kept for 12 months.

### Hiring team dashboard
Candidate job dashboard, per-interview analytics, score reports with CSV export, new-candidate email digests, and webhooks into the customer's stack (rolling out).

---


## Behavior Rules

- **Tone:** Direct, concise, no filler. Professional but not corporate.
- **Initiative:** Take action within safe boundaries. Ask only when genuinely stuck or when the action is irreversible.
- **No sycophantic filler.** Skip "Great question!" and "Absolutely!" -- just do the work.
- **Session startup:** At the start of every session, mentally load context from brain files before taking action.
- **Writing rules:**
  - No em dashes. Use commas, periods, or parentheses.
  - Avoid: leverage, utilize, streamline, comprehensive, robust, revolutionary.
  - Short sentences. Active voice. Write like a human.
- **When updating context:** Always evaluate whether a change should update brain files, and commit changes after updating.

---


## Safety Guard (CRITICAL)

Enforced by the PreToolUse hook `.claude/hooks/safety-guard.sh`, wired in `.claude/settings.json`.

**When a tool call would be blocked:**
1. Tell Aayush Tuli exactly what you were about to do (recipient, content, target system)
2. Ask for explicit approval
3. Only retry after confirmation
4. NEVER circumvent the guard (e.g., using Bash to call an API directly instead of the blocked MCP tool)

### Blocked Categories

1. **External messaging** -- Never send emails, Slack messages, LinkedIn messages, or DMs, or activate outbound sequences, without approval
   <!-- Covers: Gmail sends and drafts, Slack posts, LinkedIn messages, Apollo sequences -->

2. **Financial operations** -- Never create invoices, process payments, or modify billing

3. **Destructive deletes** -- Never delete records, campaigns, contacts, issues, pages, or accounts
   <!-- Covers: HubSpot and Apollo records, Linear issues, Notion pages -->

4. **Database mutations** -- Never run raw SQL, apply migrations, or modify schemas
   <!-- Covers: Supabase, any direct database access -->

5. **Git push / deploy** -- Never push to remote, merge PRs, or trigger deployments
   <!-- Covers: git push, gh pr merge, Cloudflare deploys, RunPod endpoint changes -->

6. **Calendar mutations** -- Never create, delete, or modify calendar events
   <!-- Covers: Google Calendar, Calendly -->

---


## Tool Ecosystem

### Core Tools

| Tool | Purpose | How We Use It |
|------|---------|---------------|
| Google Workspace | Email, calendar, docs | Gmail, Google Calendar, and Drive for the founders |
| Slack | Team chat | Founder coordination and deal alerts |
| Notion | Docs and wiki | Internal notes and planning |
| Linear | Issue tracking | Product and engineering roadmap |
| LinkedIn Sales Navigator | Prospecting | Find hiring leaders at high-volume employers |
| Apollo | Enrichment and sequences | Enrich leads and run outbound sequences |
| HubSpot | CRM | Pipeline, pilots, and deals |
| Calendly | Scheduling | Demo booking |
| GitHub | Code | Repositories, pull requests, issues |
| Cloudflare | Web and edge | tryashley.ai and networking (Cloudflare for Startups) |
| RunPod | GPU compute | Real-time rendering and model inference |
| Supabase | Database and auth | Application data with row-level security |

### How Tools Connect (Data Flow)

```
LinkedIn Sales Navigator (find hiring leaders) -> Apollo (enrich, sequence) -> HubSpot (track deals) -> Slack (alerts)
Customer ATS (stage change) -> Ashley interview -> score write-back to the ATS; outcome webhooks -> Ashley   (planned: contracts/WEBHOOKS.md)
```

---


## MCP Server Registry

Connectors available in Claude desktop sessions as of 2026-09-27. Claude.ai connectors may be absent in CLI or headless sessions.

| MCP Server | Type | Purpose |
|------------|------|---------|
| github | stdio | Repository management, PRs, issues, code search |
| Gmail | HTTP/OAuth (claude.ai connector) | Read and draft email; sending is blocked by the safety guard |
| Google Calendar | HTTP/OAuth (claude.ai connector) | Read availability; changes are blocked by the safety guard |
| Google Drive | HTTP/OAuth (claude.ai connector) | Search and read shared docs |
| Apollo | HTTP/OAuth (claude.ai connector) | Prospect search, enrichment, sequences |
| Linear | HTTP/OAuth (claude.ai connector) | Issues, projects, and cycles |

Not yet connected: HubSpot (needs authorization), Slack, Notion, Supabase, Cloudflare, Calendly.

---


## Skill Routing Table

| User Intent | Skill File | Description |
|-------------|-----------|-------------|
| "Write a cold email" | gtm-skills/outbound-copywriter.md | Cold email sequences using the SPARK framework |
| "Draft a LinkedIn post" | gtm-skills/linkedin-post-writer.md | LinkedIn content in your brand voice |
| "Build an ICP" | gtm-skills/icp-modeller.md | Ideal Customer Profile with scoring criteria |
| "Design our GTM motion" | gtm-skills/gtm-strategist.md | Go-to-market strategy and channel planning |
| "Prep me for a call" | gtm-skills/discovery-prep.md | Pre-call research briefs and conversation starters |
| "Follow up with a pilot" | gtm-skills/pilot-follow-up.md (TODO: create) | Updates and next steps for pilot customers such as USAFA and UF |

Workflow commands (installed in `.claude/commands/workflows/`): `/workflows:plan`, `/workflows:work`, `/workflows:review`, `/workflows:swarm`, `/workflows:brainstorm`, `/workflows:compound`.

---


## Brain File Structure

Start with CLAUDE.md and `blueprint/company/overview.md`. The files under `blueprint/company/` and `blueprint/wiki/` are still templates except `moat-decisions.md`; fill them in as you go.

```
ashley-ai/
├── CLAUDE.md                  # This file (the hub)
├── blueprint/
│   ├── INDEX.md               # Content catalog
│   ├── company/               # overview, team, accounts, gtm-stack, voice, design-system (TODO: fill in later)
│   ├── wiki/                  # moat-decisions (filled), outbound-playbook, processes, onboarding
│   ├── skills/, archive/, raw/ # guides for skills, finished work, raw inputs
│   └── hooks/                 # source copies of the installed hooks
├── gtm-skills/                # AI skill definitions (5 starters)
├── contracts/                 # Interview data contracts: JSON Schemas, fixtures, reference tools
├── docs/                      # moat/ working docs; superpowers/ specs and plans
├── plugin/                    # Source of the /workflows commands
├── tests/                     # pytest suite for contracts/ and docs
└── .claude/                   # settings.json, hooks/, commands/workflows/
```

### Importing Other Files

You can reference other files directly in CLAUDE.md using the `@path/to/file` syntax. Claude will read the referenced file when it loads this one. Example:

```
@blueprint/company/overview.md
@blueprint/company/voice.md
```

This keeps CLAUDE.md lean while still pulling in key context at load time.

### Path-Specific Rules

Use `.claude/rules/` for rules that only apply to certain file types or directories. Each rule file can include a frontmatter `globs` field to scope it (for example `globs: "contracts/**"`).

---


## Update Routing Rules

All updates go in this repo. Commit after every meaningful change.

**Update this repo when:**
- Company processes, SOPs, or workflows change
- Tool configurations or integrations are added/modified
- Customer or account changes (new customer, churn, status shift)
- Team structure changes
- Brand guidelines evolve
- New skills or playbooks are created

**Never put in this repo:**
- Personal credentials or API keys (use environment variables or a secrets manager)
- Personal opinions about specific people
- Anything you wouldn't want a team member to see

---


## Credentials and Secrets

This section is an index. Never put actual keys, passwords, or tokens in this repo.

| Service | Where Stored | Notes |
|---------|-------------|-------|
| RunPod, Cloudflare, Supabase | Provider secret stores and environment variables | Never committed; `.env` files are gitignored |
| Shared founder logins | 1Password | Claude never reads or types passwords |
| GitHub, Gmail, Google Calendar, Google Drive, Apollo, Linear | MCP connectors handle auth | No manual credential needed |

---


## Quick Start Checklist

- [x] Run interactive setup (owner interview, 2026-09-27)
- [x] Set up at least one MCP server (GitHub plus claude.ai connectors)
- [ ] Add the two technical co-founders' names to Key People
- [ ] Fill in `blueprint/company/overview.md` with company background
- [ ] Fill in `blueprint/company/voice.md` with writing style guidelines
- [ ] Create the first custom skill: `gtm-skills/pilot-follow-up.md`
- [ ] Update `.claude/hooks/safety-guard.sh` with the real connector tool names (its list uses generic names such as `mcp__gmail__send_email`)
- [ ] Test: ask Claude "What do you know about us?" in a new session and verify the answer
- [ ] Iterate: add more context files as you notice gaps
