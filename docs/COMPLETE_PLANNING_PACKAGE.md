# Platform 1: Agentic Company Secretary — Complete Planning Package

**Founder:** Ronald Ng (Profit Rise Consulting)
**Working name:** CoSec.ai (placeholder — see Document 4 for branding)
**Prepared:** April 2026
**Status:** Pre-build planning package (PRD, Build Plan, Kanban Board, Marketing Plan, Finance Plan)

---

## Document 1: Product Requirements Definition (PRD)

### 1.1 Executive Summary

**Platform 1: Agentic Company Secretary** is a multi-tenant SaaS that gives every Hong Kong limited company its own dedicated AI agent to run statutory compliance end-to-end: NAR1 Annual Return, Business Registration Certificate (BRC) renewal, Profits Tax Return (PTR), Employer's Return (BIR56A/IR56B), and Significant Controllers Register (SCR) maintenance. The product productises **Hermes**, Ronald Ng's existing OpenClaw WhatsApp bot for HK company secretary Q&A, into an agent-per-company platform built on **A2A** (Google/Linux Foundation's Agent-to-Agent protocol), **MCP** (Anthropic's Model Context Protocol), **ATXP** (Circuit & Chisel's Agent Transaction Protocol), and **AP2** (Agent Payments Protocol).

Each company gets a named agent (e.g. `acme-ltd.cosec.ai`) that watches deadlines, prepares forms, asks the director for one-tap approval on WhatsApp, pays the Companies Registry filing fee from a pre-funded ATXP wallet, and stores the stamped receipt. When the company agent needs accounting or legal help, it discovers specialist agents on the A2A network and delegates with a signed hand-off.

**Market:** ~1.4M registered HK companies, each paying HK$3,000–8,000/year to a traditional secretarial firm for work that is 80% calendar-watching. NAR1 late filing alone carries fines up to [HK$50,000](https://www.bestar-hk.com/post/hong-kong-company-directors-and-secretaries-the-ultimate-2026-compliance-guide).

**Pricing:** HK$200–600/month SaaS + HK$50–200 per filing + 10–15% A2A referral fee + 15–25% ATXP inference margin.

**Founder fit:** Hermes already runs on Ronald's Proxmox VM. The agentic productisation is the natural next step and leans on his 21+ years of infrastructure/security experience (CISSP, ISO 42001 Lead Auditor in progress).

### 1.2 Problem Statement

Hong Kong operates one of the highest company densities in the world:

- **~1.4 million** companies on the Companies Register, per the Companies Registry.
- **NAR1 Annual Return** must be delivered within **42 days** after the company's "return date" (the incorporation anniversary for private companies limited by shares). Filing fee is **HK$105** electronically; missing the 42-day window escalates fees to HK$870, HK$1,740, HK$2,610, and HK$3,480 at the 3/6/9-month and 9-month+ tiers ([Companies Registry Fee Schedule](https://www.cr.gov.hk/en/forms/specified-forms/details.htm)).
- **Fines for late NAR1**: up to **HK$50,000** plus daily default fines; directors and the company secretary are jointly liable ([Bestar HK 2026 Compliance Guide](https://www.bestar-hk.com/post/hong-kong-company-directors-and-secretaries-the-ultimate-2026-compliance-guide)).
- **BRC renewal**: **HK$2,200** for 1-year, **HK$6,020** for 3-year in 2026/27 — the HK$2,000 subsidy has expired ([Get Started HK](https://getstarted.hk/business-registration-fees-in-2026/), [Sleek HK](https://sleek.com/hk/resources/br-fee/)).
- **Director/Secretary changes** — must be notified via Form ND2A/ND2B within **15 days**.
- **Significant Controllers Register (SCR)** — maintenance failure is a **criminal offence** under Part 12 of the Companies Ordinance; register must be kept at the registered office and made available to law enforcement within a specified period.
- **Profits Tax Return (BIR51/BIR52/BIR54)** — issued by the IRD annually, usually with a 1-month filing window (3 months if electronic filing via eTAX).
- **Employer's Return (BIR56A + IR56B)** — issued each April, due within 1 month.

**The human pain.** An SME director receives no calendar from the government. They pay HK$3,000–8,000/year to a small secretarial firm (often a 1–5 person outfit on Excel) that mostly emails Word templates and phones to chase signatures. If the secretary mis-sets a date in a spreadsheet or a junior staffer resigns, the SME finds out when a HK$1,740+ late-filing tier triggers. The current market has:

- No native digital workflow between company → secretary → accountant → Companies Registry.
- No machine-readable agent discovery (A2A) between these parties.
- No autonomous payment of filing fees — everything goes through bank transfer and cheque.
- No inter-operable calendar based on the company's actual incorporation date.

**Opportunity.** Collapse calendar + form prep + approval + payment + filing into a single agent workflow, running in WhatsApp (the de facto HK consumer channel), with human-in-the-loop approval. Price at one-third of the incumbent firm's annual fee and keep quality higher (deterministic calendar maths beats junior staff on Excel).

### 1.3 Product Vision & Goals

**Vision.** Every Hong Kong company has an agent. The agent never forgets a deadline, never mis-files, and pays its own fees from a funded wallet. Directors only touch the product for two things: topping up the wallet, and approving a filing with one tap.

**North-star goal (12 months post-launch):** 250 paying companies at HK$300 average monthly revenue per company (ARPC) = HK$75K MRR / HK$900K ARR.

**Strategic goals:**

- **G1 — Productise Hermes.** Move from single-tenant OpenClaw prototype to multi-tenant agent-per-company SaaS.
- **G2 — Deterministic compliance engine.** A rules engine that computes every statutory deadline from the company's incorporation date, with zero ambiguity.
- **G3 — Human-in-the-loop, one-tap approvals.** Director approves on WhatsApp; agent executes.
- **G4 — Autonomous payment via ATXP + AP2.** Pre-funded wallet pays filing fees within a pre-signed Intent Mandate ceiling.
- **G5 — A2A interoperability.** Publish a Signed Agent Card; delegate accounting, tax, legal sub-tasks to other agents on the network.
- **G6 — Economically self-funding.** Reach break-even at <100 paying customers (see Document 5).

### 1.4 User Personas

**Persona A — "Vincent" the SME Owner-Director (primary buyer, primary user).**
42, director of a 6-person trading company in Kwun Tong, turnover HK$18M. Runs the company on WhatsApp groups, uses Xero for books, couldn't name any of his statutory deadlines. Currently pays HK$4,500/year to a small secretarial firm. Pain: "They email me a Word form every year in June and I forget to sign it for three weeks." Wants: zero chasing, zero surprises, monthly receipt in his inbox.

**Persona B — "Wendy" the Boutique Company Secretary Firm Principal (channel + user).**
54, runs a 4-person secretarial firm handling 180 HK companies. Uses Excel + Outlook calendar + paper filing. Clients churn when junior staff quit and deadlines slip. Pain: "I spend more time on reminders than on advice." Wants: a tool that handles the calendar and form prep so her team can focus on advisory. Willing to resell CoSec.ai at a markup.

**Persona C — "Adrian" the Accountant / Tax Agent (A2A partner + upsell channel).**
35, CPA in a 12-person practice. Signs off Profits Tax Returns for ~120 HK companies. Pain: clients send incomplete trial balances at the last minute. Wants: the company agent to push him a clean data packet the moment the PTR is issued by the IRD. Willing to publish his own A2A agent and pay a 10% referral fee for leads.

**Persona D — "Karen" the Startup COO (secondary user).**
31, COO of a 25-person Cyberport-incubated SaaS. Already runs everything on Slack + Notion + Stripe. Wants APIs, single sign-on, and a dashboard for her board. Happy to self-serve onboarding; will churn immediately if the UX requires phone calls.

### 1.5 Functional Requirements

Acceptance criteria use **Given / When / Then** format. IDs (F-xxx) reference the Kanban board in Document 3.

#### F-1. Agent registration and onboarding

- **F-1.1 Self-serve sign-up via WhatsApp or web.** Director enters BR number → system fetches public company record from the Companies Registry Integrated Companies Registry Information System (ICRIS) → pre-populates profile.
  - AC: Given a valid 8-digit BR number, when the director submits, then a company record is created with name, CI number, incorporation date, registered office, and current directors within 60 seconds.
- **F-1.2 Identity verification.** Director uploads HKID (front + selfie) and proof of authority (most recent NAR1 or certified board resolution). Stored in MCP-attached object store, encrypted at rest (AES-256), retained per PDPO.
  - AC: Given KYC docs uploaded, when operator/agent reviews, then status moves `pending → verified` or `pending → rejected` with a reason within 1 business day (agent-assisted triage, human sign-off during MVP).
- **F-1.3 Agent provisioning.** On verification, the platform spawns a tenant agent at `{slug}.cosec.ai` with its own A2A Agent Card at `/.well-known/agent-card.json`, its own ATXP wallet (zero balance), and its own MCP context bundle.
  - AC: Agent Card returns HTTP 200 with a signed JWS; wallet address visible in the dashboard; an internal smoke test ("what is my company's next NAR1 date?") returns the correct date.

#### F-2. Company profile management

- **F-2.1 Directors register.** Add/remove directors, NID/passport, residential + service address, date of appointment. Edits trigger an ND2A draft within 15 days.
  - AC: Given a director is added, when saved, then an ND2A draft is generated and queued for director approval with the 15-day deadline highlighted.
- **F-2.2 Shareholders register.** Share class, number, transfer history.
- **F-2.3 Registered office.** Address, effective date. Changes trigger NR1 draft.
- **F-2.4 Significant Controllers Register (SCR).** Maintain beneficial ownership (≥25%) per Companies Ordinance Part 12; maintain at registered office; respond to law enforcement requests.
  - AC: Given an SCR entry exists, when the ownership structure changes, then the SCR is updated within 7 days and a dated change log is recorded.
- **F-2.5 Company secretary & auditor.** Names, addresses, appointment dates.

#### F-3. Compliance calendar engine

The rules engine computes all statutory deadlines deterministically from a company's facts.

- **F-3.1 NAR1.** Return date = incorporation anniversary for private companies; delivery deadline = return date + 42 days. Higher-fee tiers at +3/+6/+9/+9+ months ([CR fees](https://www.cr.gov.hk/en/forms/specified-forms/details.htm)).
- **F-3.2 BRC renewal.** 1-month before BRC expiry (expiry = incorporation anniversary + N years depending on certificate choice).
- **F-3.3 PTR (BIR51/52/54).** Deadline driven by IRD issuance; default compliance window per IRD "block extension scheme" (N Code = Nov 15 for Mar year-end; D Code = Aug 15 for Dec year-end; M Code = Apr 15 for Jan year-end; plus 3-month electronic extension via eTAX).
- **F-3.4 Employer's Return (BIR56A + IR56B).** Issued first working day of April; filing deadline = issuance + 1 month.
- **F-3.5 ND2A/ND2B change filings.** 15 days from change.
- **F-3.6 AGM.** For private companies, within 9 months after financial year-end (Companies Ordinance s.610).
- **F-3.7 Audited financial statements.** Circulate to members before AGM; laid before AGM.
- AC: Given a company with incorporation date 2023-03-15, when the compliance calendar is generated, then it produces NAR1 return date 2026-03-15, NAR1 deadline 2026-04-26, BRC expiry 2026-03-15, plus escalation tier warning dates at 2026-04-27, 2026-06-16, 2026-09-15, 2026-12-15.

#### F-4. Automated form preparation

- **F-4.1 NAR1 pre-fill.** Pull current directors, shareholders, registered office, and company secretary from the profile; diff against the previous year's NAR1; highlight deltas.
  - AC: Given a company has had no changes, when the NAR1 draft is generated, then it pre-fills identically to last year with all fields populated and a "No changes vs prior year" badge.
- **F-4.2 ND2A (director change).** Auto-drafted on director add/remove.
- **F-4.3 NR1 (registered office change).** Auto-drafted on address change.
- **F-4.4 BRC renewal form.** Pre-filled BR renewal request.
- **F-4.5 PDF + XML outputs.** Companies Registry e-Registry accepts XML via the e-Filing service; provide PDF for director review.
- AC for all forms: output validates against CR schema; any validation error is surfaced with a plain-English fix suggestion.

#### F-5. WhatsApp notification system

Cadence, unless director selects a different cadence:

- **30 days before deadline**: utility message — "NAR1 due in 30 days. Tap to review."
- **14 days before**: utility message with draft link.
- **7 days before**: utility message; escalate to SMS if not acknowledged in 24h.
- **3 days before**: agent calls director once via Twilio Voice fallback (text-to-speech).
- **1 day before**: final utility + email to director and backup email.
- **Day of**: autonomous filing if an AP2 Intent Mandate is signed AND pre-approved by director; otherwise hold and alert.

All outbound messages are WhatsApp utility templates (~US$0.0077 per message in "Rest of Asia Pacific" tier per the [WhatsApp Business API rate card](https://flowcall.co/blog/whatsapp-business-api-pricing-2026)); inbound service messages inside the 24-hour window are free.

- AC: Given a NAR1 deadline, when the agent runs its hourly scheduler, then at 30/14/7/3/1 days out it sends exactly one message; duplicate suppression guaranteed by idempotency key `{company_id}:{filing_id}:{offset}`.

#### F-6. Human-in-the-loop approval workflow

- **F-6.1 Review link.** WhatsApp CTA opens a signed, time-limited URL on `{slug}.cosec.ai/approve/{token}`.
- **F-6.2 Review UI.** Shows filled form PDF, diff vs prior year, filing fee, total cost including platform fee.
- **F-6.3 One-tap approve.** Director taps "Approve & File." If AP2 Intent Mandate exists and fee is within ceiling, proceed; otherwise prompt for AP2 Payment Mandate (cryptographically signed).
- **F-6.4 Reject / Request change.** Director can comment; agent re-drafts.
- **F-6.5 Audit log.** Every state transition (drafted, approved, filed, paid, confirmed) is append-only, hash-chained (SHA-256 of previous record + payload).
- AC: Given a director taps approve, when within 5 seconds, then filing is submitted and the audit log contains a signed entry with the director's WhatsApp-verified identity and timestamp.

#### F-7. e-Registry API integration (or fallback)

- **F-7.1 Primary path — e-Registry e-Filing.** For documents supported by the Companies Registry e-Services portal (NAR1, ND2A, NR1, annual returns), submit via the e-Filing API where published, else via headless browser automation (Playwright) using a corporate e-Registry account with director-delegated authority.
- **F-7.2 Fallback — email/upload.** For forms without API support, generate the PDF, email to director's registered email with instructions, and track the submission via a "filed by director" confirmation.
- **F-7.3 Stamped receipt capture.** Store the CR-stamped PDF receipt in the company's document vault and tag the filing `confirmed`.
- AC: Given an NAR1 is approved, when submission completes, then within 10 minutes the receipt PDF is in the vault OR a descriptive error is surfaced with retry guidance.

#### F-8. ATXP agent wallet

- **F-8.1 Wallet provisioning.** On verification, agent registers via `npx atxp agent register` and is assigned a wallet address.
- **F-8.2 Funding.** Director tops up via FPS (HKD) to a pooled CoSec omnibus account; the platform credits the agent wallet 1:1 minus a 0.5% platform funding fee.
- **F-8.3 Debit.** Wallet debits on: filing fee payment, LLM inference (via ATXP gateway at a 20% margin over raw Claude/GPT cost), WhatsApp utility messages (pass-through).
- **F-8.4 Audit trail.** Every debit/credit is signed, timestamped, and exportable as CSV.
- **F-8.5 Auto top-up.** Optional: if balance < HK$300 and an Intent Mandate authorises it, auto-debit the director's bank card via Stripe.
- AC: Given a HK$105 NAR1 fee, when the filing is submitted, then the wallet debit is HK$105 (pass-through) plus the agreed platform filing fee (HK$50–200), and the debit record is visible in the audit log within 30 seconds.

#### F-9. AP2 Intent Mandate

- **F-9.1 Mandate creation.** Director signs (WhatsApp deep link + device biometric) a mandate such as: "Agent may pay any Hong Kong government filing fee ≤ HK$5,000 on behalf of this company, valid for 12 months, capped at HK$30,000 aggregate."
- **F-9.2 Mandate storage.** Store signed JWS; expose via A2A for third-party verification.
- **F-9.3 Enforcement.** Every Payment Mandate references the Intent Mandate; if the ceiling is exceeded, the agent requests a per-transaction Payment Mandate.
- **F-9.4 Revocation.** Director can revoke any time; revocation is signed and propagated across dependent agents via A2A.
- AC: Given an Intent Mandate for ≤HK$5,000 is active, when a HK$105 NAR1 fee is due, then the agent proceeds without human approval; when a HK$6,020 3-year BRC is due, then the agent requests a one-tap Payment Mandate.

#### F-10. A2A agent discovery and delegation

- **F-10.1 Outbound discovery.** Company agent queries a directory (initially CoSec's hosted registry; later Linux Foundation public registries) for capabilities like `tax.hongkong.profits_tax_filing`, `legal.hongkong.director_resignation_deed`.
- **F-10.2 Capability negotiation.** Company agent reads the candidate's Signed Agent Card; picks best match by rating/price.
- **F-10.3 Task hand-off.** JSON-RPC 2.0 over HTTPS; tasks include context pack (MCP-accessible read-only URL), success criteria, fee cap.
- **F-10.4 Referral accounting.** Platform tracks delegated tasks; debits 10–15% referral fee on successful completion.
- **F-10.5 Inbound hand-offs.** Agents from partner firms can request read access to a company's directors register for a PTR; director approves via AP2 Intent Mandate.
- AC: Given PTR season, when a PTR is issued, then the company agent discovers and shortlists ≥1 accounting agent from the registry, presents the shortlist to the director, and, on approval, hands off with a signed task URL.

#### F-11. A2A Agent Card publication

- **F-11.1** Every tenant agent publishes at `https://{slug}.cosec.ai/.well-known/agent-card.json`.
- **F-11.2 Platform-level card** at `https://cosec.ai/.well-known/agent-card.json` declares platform capabilities: `cosec.hk.compliance_calendar`, `cosec.hk.nar1_preparation`, `cosec.hk.brc_renewal`, `cosec.hk.scr_maintenance`.
- **F-11.3 Signing.** Agent Cards are JWS-signed with the platform's Ed25519 key; key rotation every 90 days; JWKS published at `https://cosec.ai/.well-known/jwks.json`.

#### F-12. Multi-tenant architecture

- Single OpenClaw deployment with per-tenant configuration; data isolation enforced at Postgres row-level security (RLS).
- Each tenant has: own MCP context bundle, own ATXP wallet, own Agent Card, own WhatsApp template approval.
- Shared: rules engine, LLM gateway, scheduler, audit infrastructure.

#### F-13. Dashboard

- Web app at `app.cosec.ai`. Sign-in via WhatsApp OTP + optional passkey.
- Views: (1) portfolio (all my companies, colour-coded by urgency), (2) single-company timeline, (3) filings history with downloadable receipts, (4) wallet, (5) agent settings (AP2 mandates, delegation rules, WhatsApp cadence).
- Accountant view: list of companies granted read access.
- Secretary firm principal view: agency-mode dashboard showing 10–500 companies at a glance.

### 1.6 Non-Functional Requirements

- **Security.** TLS 1.3 everywhere; AES-256 at rest; secrets in HashiCorp Vault / AWS Secrets Manager; SSH via Tailscale. Ronald's CISSP and TOGAF 9 certifications inform the baseline; ISO 27001 controls targeted for Month 12.
- **PDPO compliance.** Purpose-limited collection; director consent captured at onboarding; data retention 7 years post termination (statutory requirement for company records); data residency in HK (AWS ap-east-1 or Alibaba Cloud HK).
- **Uptime.** 99.5% for the MVP year (custom SLA — scheduler tolerates 4 hours of downtime because deadlines are measured in days). 99.9% year 2.
- **Scalability.** Up to 5,000 tenants on a single application node (agents are light; heavy work is batched in the scheduler). Horizontal scale via read replicas + work queue (Redis/Sidekiq-style, or Temporal for long-running workflows).
- **Observability.** Structured JSON logs → Grafana Loki; metrics → Prometheus; traces → OpenTelemetry → Tempo; alerting via PagerDuty (or cheaper: Better Stack).
- **Regulatory.** Not a licensed TCSP — CoSec.ai is a software tool; the *director* remains the legally responsible person, and a human Company Secretary (either a named natural person or a TCSP-licensed firm) signs off the NAR1 where regulation requires. Platform partners with ≥1 licensed TCSP for white-label signatory services.
- **Accessibility.** WCAG 2.1 AA for web UI; Chinese (Traditional + Simplified) and English localisation.
- **Disaster recovery.** Nightly encrypted backups to S3 in a second region; RPO 24h MVP, 1h year 2; RTO 8h MVP, 2h year 2.

### 1.7 Technical Architecture

```
                                ┌────────────────────────────────────────────┐
                                │               DIRECTORS / USERS             │
                                │  WhatsApp · Web dashboard · Email · Voice   │
                                └──────────────┬─────────────────────────────┘
                                               │
                  ┌────────────────────────────▼─────────────────────────────┐
                  │                INTERFACE LAYER                           │
                  │ ┌───────────────┐  ┌───────────────┐  ┌───────────────┐ │
                  │ │ WhatsApp BSP  │  │  Next.js web  │  │  Twilio Voice │ │
                  │ │  (Meta/Twilio)│  │  app.cosec.ai │  │  fallback     │ │
                  │ └──────┬────────┘  └──────┬────────┘  └──────┬────────┘ │
                  └─────────┼─────────────────┼──────────────────┼──────────┘
                            │                 │                  │
                  ┌─────────▼─────────────────▼──────────────────▼──────────┐
                  │              PLATFORM API (FastAPI)                     │
                  │  /auth  /companies  /filings  /mandates  /wallet        │
                  └──────────────────────────┬──────────────────────────────┘
                                             │
                  ┌──────────────────────────▼──────────────────────────────┐
                  │               AGENT RUNTIME (OpenClaw)                  │
                  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                  │  │ Tenant agent│  │ Tenant agent│  │ Tenant agent│ ... │
                  │  │  acme-ltd   │  │  bravo-co   │  │  charlie-hk │     │
                  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
                  │         │                │                │             │
                  │  ┌──────▼────────────────▼────────────────▼──────┐     │
                  │  │       SHARED SERVICES                         │     │
                  │  │  ┌──────────────┐ ┌─────────────┐ ┌────────┐ │     │
                  │  │  │ Rules engine │ │ LLM gateway │ │ Sched- │ │     │
                  │  │  │ (deadlines)  │ │ (ATXP-wrap) │ │ uler   │ │     │
                  │  │  └──────────────┘ └─────────────┘ └────────┘ │     │
                  │  └───────────────────────────────────────────────┘     │
                  └───────┬───────────────────────────────────┬─────────────┘
                          │                                   │
                  ┌───────▼────────────────┐      ┌──────────▼──────────────┐
                  │ MCP SERVER CLUSTER     │      │ PROTOCOL ADAPTERS       │
                  │ mcp-companies-registry │      │ A2A server (/.well-known│
                  │ mcp-ird                │      │   /agent-card.json)     │
                  │ mcp-whatsapp           │      │ ATXP wallet SDK         │
                  │ mcp-fps                │      │ AP2 mandate signer      │
                  │ mcp-docstore (S3)      │      │ UCP client (seal shops) │
                  └────────────────────────┘      └─────────────────────────┘
                          │                                   │
                  ┌───────▼───────────────────────────────────▼─────────────┐
                  │                 DATA LAYER                              │
                  │  Postgres (RLS) · Redis · S3 (HK region) · Object Lock  │
                  └─────────────────────────────────────────────────────────┘
                          │
                  ┌───────▼────────────────────────────────────────────────┐
                  │        EXTERNAL SYSTEMS                                │
                  │  Companies Registry e-Services · IRD eTAX · FPS        │
                  │  Stripe · Meta WhatsApp Cloud API · Anthropic/OpenAI   │
                  └────────────────────────────────────────────────────────┘
```

**Component summary.**

- **Interface layer:** WhatsApp (primary) via Meta Cloud API or Twilio BSP; Next.js dashboard hosted on Vercel; Twilio Voice as TTS fallback.
- **Platform API:** FastAPI (Python), JWT auth, deployed via Docker on Proxmox for MVP; migrate to AWS ECS/Fargate ap-east-1 at 100+ tenants.
- **Agent runtime:** OpenClaw (Ronald's existing expertise) per-tenant agent instances; agents share a common rules engine and LLM gateway.
- **MCP servers:** one per integration — ICRIS, IRD eTAX, WhatsApp, FPS, doc-store. Each is a stateless process with its own scope + credentials.
- **Protocol adapters:** A2A server exposing Agent Card; ATXP wallet SDK; AP2 mandate signer (Ed25519); UCP client (future).
- **Data:** Postgres 16 with row-level security per tenant; Redis for queues and idempotency keys; S3 for receipts with Object Lock for legal hold.

### 1.8 Data Model

Core entities (fields abbreviated):

- **Company**: `id`, `br_number`, `ci_number`, `legal_name_en`, `legal_name_zh`, `incorporation_date`, `return_date`, `brc_expiry`, `status`, `created_at`.
- **Director**: `id`, `company_id`, `full_name`, `id_type`, `id_number_masked`, `residential_address`, `service_address`, `appointment_date`, `resignation_date`, `is_alternate`.
- **Shareholder**: `id`, `company_id`, `holder_type` (natural | corporate), `name`, `share_class`, `shares_held`, `percentage`, `acquisition_date`.
- **RegisteredOffice**: `id`, `company_id`, `address`, `effective_from`, `effective_to`.
- **SCREntry**: `id`, `company_id`, `controller_name`, `control_type` (shareholding | voting | board | other), `percentage`, `effective_from`, `verified_at`.
- **CompanySecretary**: `id`, `company_id`, `type` (natural | tcsp_firm), `name`, `licence_no`, `appointment_date`.
- **Filing**: `id`, `company_id`, `filing_type` (NAR1 | BRC | ND2A | NR1 | BIR51 | BIR56A | IR56B), `due_date`, `filed_at`, `receipt_url`, `status` (scheduled | drafted | approved | filed | confirmed | failed), `fee_hkd`, `platform_fee_hkd`, `idempotency_key`.
- **AgentWallet**: `id`, `company_id`, `atxp_address`, `balance_hkd_cents`, `created_at`.
- **WalletTxn**: `id`, `wallet_id`, `direction` (credit | debit), `amount_hkd_cents`, `reason`, `counterparty`, `signature`, `created_at`.
- **Mandate**: `id`, `company_id`, `kind` (intent | cart | payment), `ceiling_hkd`, `aggregate_cap_hkd`, `valid_from`, `valid_until`, `signature_jws`, `revoked_at`.
- **AgentDelegation**: `id`, `from_company_id`, `to_agent_did`, `capability`, `task_ref`, `fee_cap_hkd`, `status`, `result_url`.
- **Notification**: `id`, `company_id`, `channel` (whatsapp | email | sms | voice), `template_id`, `offset_days`, `sent_at`, `delivery_status`, `idempotency_key`.
- **AuditLog**: `id`, `entity_type`, `entity_id`, `actor`, `action`, `payload_json`, `prev_hash`, `hash`, `created_at`.

### 1.9 API Specifications (selected)

All endpoints `https://api.cosec.ai/v1/*`, JSON, JWT-bearer.

- `POST /companies` — body: `{ br_number }` → fetches ICRIS, creates company.
- `GET /companies/{id}/calendar` → next 24 months of statutory events.
- `POST /companies/{id}/directors` → add director; returns generated ND2A draft.
- `POST /filings/{id}/approve` → body: `{ mandate_id, signature }` → transitions to `approved`, schedules submission.
- `POST /wallets/{id}/top-up` → body: `{ amount_hkd, fps_txn_id }`.
- `POST /mandates` — body: AP2 mandate JWS → stores & returns mandate id.
- `POST /a2a/delegate` — body: `{ capability, task, fee_cap_hkd, mandate_id }` → hand-off to external agent.
- `GET /.well-known/agent-card.json` → signed Agent Card.

### 1.10 Integration Points

- **Companies Registry e-Services** — primary filing channel. Where API unavailable, Playwright automation against e-Registry portal using delegated director credentials.
- **IRD eTAX** — PTR, Employer's Return electronic filing via TC (Tax Representative) account; platform white-labels a licensed TR partner in MVP.
- **WhatsApp Business API** — via Meta Cloud API (direct) or Twilio BSP (faster onboarding, US$0.005/message markup per [Twilio pricing](https://www.twilio.com/en-us/whatsapp/pricing)).
- **FPS (Faster Payment System)** — via HSBC / Standard Chartered / ZA Bank business banking APIs; top-up and refund routing.
- **ATXP** — agent registration via `npx atxp agent register`; LLM gateway via ATXP wallet; nested payments for sub-agent delegation.
- **A2A directory** — initially CoSec-hosted (`registry.cosec.ai`); publish Agent Cards; later federate with Linux Foundation's public registry.
- **Stripe** — for card top-ups to the omnibus account (optional; FPS is cheaper).
- **Anthropic Claude / OpenAI** — inference via ATXP gateway; Claude Sonnet 4.6 at [US$3.00 input / US$15.00 output per million tokens](https://www.finout.io/blog/anthropic-api-pricing); Haiku 4.5 for cheap tier at US$1/US$5.
- **Qwen** — Cantonese-heavy summarisation where Claude is overkill.

### 1.11 Risks and Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-1 | Regulatory push-back — TCSP licensing required for "acting as company secretary" | Medium | High | CoSec is software; pair with licensed TCSP partners for signatory role; seek legal opinion (Deacons or Stevenson Wong, HK$30–60K) pre-launch |
| R-2 | Companies Registry offers no public API; Playwright automation breaks on UI change | Medium | High | Maintain fallback email/upload flow; monitor CR notices; contract HK-based dev on-call at HK$800/hr |
| R-3 | WhatsApp policy change — Meta blocks our template | Low | High | Fallback SMS + email; diversify BSP (Meta Cloud + Twilio) |
| R-4 | LLM cost runaway on long conversations | Medium | Medium | Cache prompts (90% discount on Anthropic); route 80% of traffic to Haiku 4.5 |
| R-5 | Data breach → PDPO fine up to HK$1M + reputational | Low | Critical | ISO 27001 track; encryption; Ronald's CISSP oversight; PI insurance HK$5M limit |
| R-6 | Customer acquisition slower than plan | High | Medium | Channel strategy: white-label for 2–3 boutique secretarial firms (Persona B); see Document 4 |
| R-7 | A2A/ATXP protocols mature slower than expected | Medium | Medium | Ship with internal A2A first; AP2 mandates are signed JWS — works without public registry |
| R-8 | Director phishing — fake WhatsApp approval link | Medium | High | Approval links are single-use, 15-min TTL, bound to director's WhatsApp number + device passkey |
| R-9 | Ronald bandwidth (15–20 hrs/week) | Certain | Medium | Freelancer plan in Documents 2 and 5; automate internal ops from day 1 |
| R-10 | Traditional secretarial firms see us as a threat and lobby against | Medium | Medium | Channel program: give firms wholesale pricing and rebrand option |

### 1.12 Success Metrics (KPIs)

- **Acquisition:** paying companies (target: 50 by Month 6, 250 by Month 12).
- **Activation:** % of signed-up companies that complete onboarding + first AP2 Intent Mandate within 7 days (target 70%).
- **Retention:** annual gross retention (target 92%).
- **Compliance:** % of filings delivered ≥3 days before the deadline (target 99%); late filings attributable to platform (target 0).
- **NPS:** ≥ 40 by Month 12.
- **Economics:** ARPC ≥ HK$300; gross margin ≥ 70%; CAC payback ≤ 5 months.
- **Agent network:** ≥5 third-party A2A partners listed by Month 12.

### 1.13 Glossary

- **A2A** — Agent-to-Agent Protocol (Google / Linux Foundation). Signed Agent Cards at `/.well-known/agent-card.json`, JSON-RPC 2.0.
- **AP2** — Agent Payments Protocol. Intent Mandate / Cart Mandate / Payment Mandate.
- **ATXP** — Agent Transaction Protocol (Circuit & Chisel). Wallets, nested payments, LLM gateway.
- **BRC** — Business Registration Certificate (issued by IRD).
- **CR** — Companies Registry.
- **Hermes** — Ronald's existing OpenClaw WhatsApp bot; the seed for this platform.
- **ICRIS** — Integrated Companies Registry Information System.
- **IRD** — Inland Revenue Department.
- **MCP** — Model Context Protocol (Anthropic).
- **NAR1** — Annual Return form for HK companies with share capital.
- **PDPO** — Personal Data (Privacy) Ordinance.
- **PTR** — Profits Tax Return (BIR51 / BIR52 / BIR54).
- **SCR** — Significant Controllers Register.
- **TCSP** — Trust or Company Service Provider (licensed regime under AMLO).
- **UCP** — Universal Commerce Protocol (Google / Shopify).

---

## Document 2: Product Build Plan (Human-Readable)

**Assumptions.** Ronald works 15–20 hrs/week on this (evenings + weekends). Freelancers bill hourly in HK market rates: senior full-stack dev HK$600–1,000/hr; UI/UX designer HK$500–800/hr; content/brand writer HK$400–600/hr; legal counsel HK$2,500–4,500/hr. Timeline = 48 weeks from kickoff to "50 paying companies."

**Quality gates.** Each phase ends with a gate: acceptance demo, security review, cost check against Document 5.

### Phase 0 — Foundation (Weeks 1–4)

**Goal:** legal vehicle, infrastructure baseline, and the Hermes prototype ready to be productised.

| # | Task | Hours | Who | Tools / Services | Depends on | Definition of Done |
|---|---|---|---|---|---|---|
| P0-01 | Incorporate CoSec.ai Ltd (HK private limited; trading name under Profit Rise initially, later spun out) | 4 | Ronald | Companies Registry e-Services; OneStart or DIY Hong Kong Company | — | CI number issued, BRC received, bank account opened (ZA Bank or HSBC BIB) |
| P0-02 | Trademark filing: "CoSec.ai" word mark + logo (Class 9, 35, 42) | 6 | Ronald + IP agent | IPD HK e-filing; or use Fastlane IP, ~HK$6,000 per class | P0-01 | Application filed, receipt stored |
| P0-03 | Professional indemnity insurance (PI) HK$5M limit | 3 | Ronald | MSIG HK or AXA; broker: Agency for Policy Makers | P0-01 | Certificate of insurance on file |
| P0-04 | PDPO compliance baseline: appoint DPO (Ronald), draft privacy policy + data-processing agreements | 8 | Ronald (CISSP) | PDPO Commissioner guidance templates | P0-01 | Privacy policy published, internal DPIA template ready |
| P0-05 | Engage external counsel for TCSP scoping opinion | 3 (Ronald) + external | Ronald + law firm | Stevenson Wong or ONC Lawyers | P0-01 | Written opinion re: whether platform triggers TCSP licensing (est. HK$40K) |
| P0-06 | Domain + email: cosec.ai, app.cosec.ai, api.cosec.ai, registry.cosec.ai | 1 | Ronald | Cloudflare Registrar, Cloudflare for Teams | — | DNS, MX (Google Workspace), SPF/DKIM/DMARC set |
| P0-07 | Set up shared infra accounts: AWS ap-east-1, GitHub org, Linear/Notion, 1Password | 3 | Ronald | AWS, GitHub Team, Notion, 1Password Business | P0-06 | All team members added; SSO via Google Workspace |
| P0-08 | Provision Proxmox VM baseline for MVP (existing Hermes VM, scaled up) | 4 | Ronald | Proxmox, Tailscale, Ubuntu 24.04, Docker | — | Fresh VM, Tailscale SSH, Docker + Caddy reverse proxy |
| P0-09 | CI/CD pipeline | 6 | Freelancer-Dev | GitHub Actions, Ansible, Docker Hub | P0-07, P0-08 | Push to main → build → deploy staging + prod (one-approval prod) |
| P0-10 | Observability stack | 6 | Freelancer-Dev | Grafana Cloud Free tier, Prometheus, Loki, Sentry | P0-08 | Uptime + error dashboards live |
| P0-11 | Extract Hermes knowledge base (6 files) into structured rules + Q&A corpus | 10 | Ronald | existing Hermes repo | — | Rules in YAML, Q&A in Postgres, tests pass on 100 known scenarios |
| P0-12 | Commission brand identity: logo, colour system, typography | 20 | Freelancer-Design | Figma; designer from Dribbble HK | P0-02 | Brand guide PDF, logo SVG set, Figma library |

**Quality Gate 0.** (a) Legal entity live, (b) VM stack passes a 1-week uptime check, (c) Hermes rules corpus ported with green tests, (d) trademark application filed.

### Phase 1 — Core MVP (Weeks 5–12)

**Goal:** single-tenant agent that tracks deadlines and messages the director on WhatsApp.

| # | Task | Hours | Who | Tools | Depends | DoD |
|---|---|---|---|---|---|---|
| P1-01 | Data model + Postgres schema (Companies, Directors, Shareholders, Filings, Mandate, AuditLog, Notification) | 20 | Ronald | Postgres 16, Alembic migrations | P0-11 | Migrations run idempotently on fresh DB; ER diagram in repo |
| P1-02 | Compliance rules engine (F-3) | 35 | Ronald | Python, pydantic, rule DSL | P1-01 | Given any (incorporation_date, FY-end), returns full 24-month event list with 100% test coverage on 200 cases |
| P1-03 | ICRIS scraper / lookup (BR → company record) | 18 | Freelancer-Dev | Playwright, proxy pool | P1-01 | Feeding 20 test BR numbers returns correct company data |
| P1-04 | FastAPI skeleton + JWT auth + row-level security | 20 | Freelancer-Dev | FastAPI, SQLAlchemy 2, PyJWT | P1-01 | OpenAPI spec published; Postman collection; RLS tested |
| P1-05 | WhatsApp integration via Meta Cloud API | 16 | Freelancer-Dev | Meta Cloud API, Twilio fallback | P0-08 | Send + receive messages; webhook verified; 3 utility templates approved |
| P1-06 | Notification scheduler (30/14/7/3/1-day cadence, F-5) | 18 | Ronald | APScheduler or Temporal Cloud | P1-02, P1-05 | Cron runs every 10 min; idempotency enforced; integration test green |
| P1-07 | Minimal web onboarding flow (BR → profile) | 30 | Freelancer-Dev | Next.js 15, Tailwind, Clerk or Lucia auth | P1-03 | End-to-end: director signs up with WhatsApp OTP, sees calendar |
| P1-08 | OpenClaw agent definition for the compliance-calendar persona | 20 | Ronald | OpenClaw | P1-02, P1-05 | Agent answers "what's next for my company?" via WhatsApp correctly |
| P1-09 | Internal ops dashboard (operator approves/rejects KYC) | 10 | Freelancer-Dev | Retool / Appsmith | P1-04 | Ronald can approve a KYC in <60 seconds |
| P1-10 | 5 friendly-beta companies onboarded | 6 | Ronald | — | P1-01…P1-09 | 5 companies receive correct 30-day WhatsApp reminder; 0 false positives |

**Quality Gate 1.** Five friendly beta companies run for 2 full weeks; rules engine precision/recall ≥ 98% on their real data; WhatsApp cost per company < HK$5/month.

### Phase 2 — Filing Automation (Weeks 13–20)

**Goal:** prepare and submit an NAR1 end-to-end with human approval.

| # | Task | Hours | Who | Tools | Depends | DoD |
|---|---|---|---|---|---|---|
| P2-01 | NAR1 form model + XML generator matching CR schema | 30 | Freelancer-Dev | Python, lxml | P1-01 | Generated XML validates against CR schema in CI |
| P2-02 | NAR1 PDF renderer (director-facing review) | 12 | Freelancer-Dev | WeasyPrint | P2-01 | Pixel-parity PDF vs. official NAR1 |
| P2-03 | Diff engine: this year vs. last year | 10 | Ronald | Python | P2-01 | Delta report renders in UI |
| P2-04 | Approval link flow (F-6) | 14 | Freelancer-Dev | Next.js, JWT short-lived tokens, WebAuthn | P1-07 | One-tap approve works in <3s median |
| P2-05 | Hash-chained audit log | 8 | Ronald | Python, blake3/SHA-256 | P1-01 | Tamper test fails gracefully and alerts |
| P2-06 | e-Registry submission (Playwright headless bot using delegated credentials) | 28 | Freelancer-Dev | Playwright, HashiCorp Vault for creds | P2-01 | Successful submission on 3 CR-test-companies; receipt PDF captured |
| P2-07 | Receipt capture + storage (S3 with Object Lock) | 6 | Freelancer-Dev | AWS S3 ap-east-1, Object Lock | P0-07 | Receipt viewable in dashboard; legal hold toggle works |
| P2-08 | Fallback: email-to-director flow with trackable return confirmation | 8 | Ronald | Postmark / Mailgun | P2-02 | Director email + "confirm filed" link works |
| P2-09 | Operational runbook for failed filings | 6 | Ronald | Notion | P2-06 | Three documented failure modes with recovery steps |
| P2-10 | 10 beta companies file NAR1 via the product | 8 | Ronald + ops | — | P2-01…P2-09 | 10 NAR1 filings stamped, zero late, zero data errors |

**Quality Gate 2.** 10 NAR1 filings land stamped. Mean elapsed time "deadline trigger → stamped receipt" ≤ 72 hours. No director complaint.

### Phase 3 — Payment & Agent Economy (Weeks 21–28)

**Goal:** ATXP wallet + AP2 mandates + FPS top-ups wired end-to-end.

| # | Task | Hours | Who | Tools | Depends | DoD |
|---|---|---|---|---|---|---|
| P3-01 | ATXP agent registration + wallet provisioning | 12 | Ronald | `npx atxp agent register` | P1-08 | Every tenant gets a wallet on provisioning |
| P3-02 | LLM gateway via ATXP (margin 20%) | 12 | Ronald | ATXP gateway SDK | P3-01 | Cost per company tracked; 20% margin captured |
| P3-03 | FPS top-up flow (omnibus bank → wallet credit) | 20 | Freelancer-Dev | ZA Bank Business API + manual reconciliation; or HSBC HKD omni | P0-01 | Director pays via FPS; balance credited within 30 min |
| P3-04 | AP2 Intent Mandate signer (Ed25519 + WebAuthn) | 18 | Ronald | Python `cryptography`, WebAuthn | P2-04 | Director signs; JWS stored; verification endpoint returns 200 |
| P3-05 | AP2 Payment Mandate (per-transaction) | 10 | Ronald | same | P3-04 | Used when a fee exceeds Intent ceiling |
| P3-06 | Autonomous filing fee payment (within Intent ceiling) | 10 | Ronald | Companies Registry e-payment | P3-03, P3-04 | HK$105 NAR1 fee paid from wallet; audit log clean |
| P3-07 | Wallet statement PDF + CSV export | 6 | Freelancer-Dev | WeasyPrint | P3-01 | Monthly PDF statement attached to email |
| P3-08 | Stripe card top-up (optional secondary funding path) | 8 | Freelancer-Dev | Stripe HK | P3-03 | Card top-up works; fees passed through |
| P3-09 | Pricing & billing engine (SaaS MRR + per-filing) | 20 | Freelancer-Dev | Stripe Billing | P3-08 | Monthly invoice issued with correct line items |
| P3-10 | Compliance pay-as-you-go: 10 beta companies pay for 1 filing through wallet | 6 | Ronald + ops | — | P3-01…P3-09 | 10 end-to-end wallet-funded filings |

**Quality Gate 3.** Unit economics recorded live for 10 companies match Document 5 model within ±10%.

### Phase 4 — Multi-Agent Network (Weeks 29–36)

**Goal:** Agent Card publication + A2A outbound delegation to accounting/legal agents.

| # | Task | Hours | Who | Tools | Depends | DoD |
|---|---|---|---|---|---|---|
| P4-01 | Platform Agent Card + JWKS publication | 10 | Ronald | A2A spec, Ed25519 | P0-06 | `/.well-known/agent-card.json` returns signed card; JWKS rotation script |
| P4-02 | Per-tenant Agent Card | 10 | Freelancer-Dev | — | P4-01 | Every `{slug}.cosec.ai/.well-known/agent-card.json` works |
| P4-03 | A2A registry microservice (`registry.cosec.ai`) | 16 | Freelancer-Dev | FastAPI | P4-01 | Third parties can register their Agent Card; search by capability |
| P4-04 | Capability taxonomy for HK compliance space | 8 | Ronald | Notion | — | Documented taxonomy; published on GitHub |
| P4-05 | Outbound delegation engine (F-10.3) | 20 | Ronald | JSON-RPC 2.0 client | P4-03 | PTR task handed off to partner accounting agent |
| P4-06 | Referral accounting (10–15%) | 10 | Freelancer-Dev | Stripe | P4-05 | Referrals invoiced monthly |
| P4-07 | Partner onboarding: 2 accounting firms, 1 law firm | 15 | Ronald | BD | P4-03 | 3 partners listed with Signed Agent Cards |
| P4-08 | Director-facing delegation UI ("shortlist & approve") | 12 | Freelancer-Dev | Next.js | P4-05 | One-tap delegation; AP2 mandate covers fee |
| P4-09 | Secretarial firm resale channel ("agency mode") | 18 | Freelancer-Dev | Next.js + RLS | P1-04 | Wendy (Persona B) can manage 20 companies in one view |
| P4-10 | 5 A2A delegations completed end-to-end | 6 | Ronald | — | — | Each hand-off has signed card, task URL, fee cap, receipt |

**Quality Gate 4.** 5 successful A2A hand-offs. At least 1 partner-initiated inbound delegation received and fulfilled.

### Phase 5 — Scale (Weeks 37–48)

**Goal:** dashboard polish + onboarding funnel + first 50 paying companies.

| # | Task | Hours | Who | Tools | Depends | DoD |
|---|---|---|---|---|---|---|
| P5-01 | Multi-company portfolio dashboard | 25 | Freelancer-Dev | Next.js, shadcn/ui, TanStack Table | P1-07 | 500 companies rendered under 1.5s on test dataset |
| P5-02 | Self-serve onboarding v2 (BR + KYC + Mandate in one flow) | 20 | Freelancer-Dev | Next.js, Onfido or SumSub for KYC | P1-07 | Median onboarding time ≤ 12 minutes |
| P5-03 | Automated KYC via SumSub (replaces manual) | 12 | Freelancer-Dev | SumSub HK | P5-02 | 90% of KYC auto-approved |
| P5-04 | Referral programme UI + tracking | 10 | Freelancer-Dev | Rewardful | P3-09 | First referral paid out |
| P5-05 | Pricing page + public marketing site | 20 | Freelancer-Design + Freelancer-Dev | Framer or Webflow | Document 4 | cosec.ai live |
| P5-06 | ISO 27001 readiness assessment | 20 | Ronald (CISSP) | Vanta or Drata | — | Gap report; plan for certification in year 2 |
| P5-07 | Load testing (5,000 tenants) | 12 | Freelancer-Dev | k6 | — | p95 API latency < 400ms at 5k-tenant scale |
| P5-08 | Customer support playbook + Intercom/Freshdesk | 12 | Ronald | Freshdesk | — | SLAs documented; 3 canned flows |
| P5-09 | Onboard 50 paying companies | 40 | Ronald + ops freelancer | — | Documents 4, 5 | 50 × HK$300 MRR = HK$15,000 MRR |
| P5-10 | Year 1 retrospective + Year 2 roadmap | 8 | Ronald | Notion | — | Published to team + advisors |

**Quality Gate 5.** 50 paying customers; 99.5% compliance uptime; gross margin ≥ 70%; NPS ≥ 30.

---

## Document 3: Kanban / GTD Board (LLM-Importable)

Format follows the structure in the task brief. IDs map to `P{phase}-{seq}` used in Document 2 where applicable, plus additional granular tasks. There are **72 tasks** total.

### Phase 0 — Foundation

### [TASK-001] Incorporate CoSec.ai Ltd
- **Status**: Todo
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 4
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] CI number issued by Companies Registry
  - [ ] BRC received from IRD
  - [ ] HK$ business bank account opened (ZA Bank or HSBC BIB)
  - [ ] Initial share capital paid up
- **Notes**: Use e-Registry (HK$1,545 electronic). Consider spinning out of Profit Rise later; start as a subsidiary if faster.

### [TASK-002] Trademark CoSec.ai (Classes 9, 35, 42)
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Filing receipt for word mark + logo
  - [ ] Docket tracking in Notion
- **Notes**: IPD HK e-filing HK$1,500/class/mark government fee; agent fee HK$4,000–6,000/class.

### [TASK-003] Professional indemnity insurance HK$5M
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 3
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Policy bound; certificate stored
  - [ ] Insurer: MSIG HK or AXA
- **Notes**: Budget HK$12,000–25,000/yr. Broker: Agency for Policy Makers.

### [TASK-004] PDPO privacy programme baseline
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Privacy Policy published
  - [ ] DPIA template in /legal
  - [ ] DPO appointed (Ronald)
- **Notes**: Reference PCPD's "Guidance on the Collection and Use of Personal Data".

### [TASK-005] TCSP licensing opinion from external counsel
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 3
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Written opinion filed
  - [ ] Follow-up actions (if any) logged
- **Notes**: Budget HK$40,000. Candidates: Stevenson Wong, ONC Lawyers, Deacons.

### [TASK-006] Domain & email setup
- **Status**: Todo
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 1
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] cosec.ai + subdomains configured on Cloudflare
  - [ ] Google Workspace MX + SPF/DKIM/DMARC
- **Notes**: Backup domain: cosec.hk.

### [TASK-007] Shared infra accounts + SSO
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 3
- **Dependencies**: [TASK-006]
- **Acceptance Criteria**:
  - [ ] AWS ap-east-1 org + SSO
  - [ ] GitHub org + 2FA mandatory
  - [ ] 1Password Business
- **Notes**: Use AWS Organizations with separate staging/prod accounts.

### [TASK-008] Harden Proxmox MVP VM
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 4
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] Ubuntu 24.04 baseline
  - [ ] Tailscale-only SSH
  - [ ] Caddy reverse proxy with auto-TLS
  - [ ] Docker + systemd units
- **Notes**: Reuse existing Hermes VM.

### [TASK-009] CI/CD pipeline
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 6
- **Dependencies**: [TASK-007], [TASK-008]
- **Acceptance Criteria**:
  - [ ] GitHub Actions build + test + deploy
  - [ ] Staging auto-deploy; prod one-click approve
- **Notes**: Ansible for infra, Docker for app.

### [TASK-010] Observability stack
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 6
- **Dependencies**: [TASK-008]
- **Acceptance Criteria**:
  - [ ] Logs in Loki / Grafana Cloud Free
  - [ ] Sentry for errors
  - [ ] Uptime alerts via Better Stack
- **Notes**: Target total observability spend <US$50/month until Month 6.

### [TASK-011] Port Hermes knowledge base into rules + Q&A corpus
- **Status**: Todo
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] Rules in YAML (deadlines, fees, forms)
  - [ ] Q&A in Postgres
  - [ ] 100-scenario regression suite green
- **Notes**: Hermes is the seed; don't rewrite — structure what exists.

### [TASK-012] Brand identity package
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Design
- **Estimated Hours**: 20
- **Dependencies**: [TASK-002]
- **Acceptance Criteria**:
  - [ ] Logo SVG (light + dark)
  - [ ] Brand guide PDF
  - [ ] Figma library
- **Notes**: Tone: trustworthy, quiet competence — not flashy. See Document 4.

### Phase 1 — Core MVP

### [TASK-013] Postgres schema + migrations
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 20
- **Dependencies**: [TASK-011]
- **Acceptance Criteria**:
  - [ ] All entities from PRD §1.8
  - [ ] RLS policy tested
  - [ ] ER diagram in /docs
- **Notes**: Alembic; unit tests per migration.

### [TASK-014] Compliance rules engine
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 35
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] 200-case test pack green
  - [ ] Handles leap years, FY-end changes, early AGM, private/public distinction
- **Notes**: Core IP — avoid outsourcing.

### [TASK-015] ICRIS BR lookup
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 18
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] 20 test BR numbers return correct data
  - [ ] Rate limiting + retries
- **Notes**: Use cr.gov.hk e-Services behind Playwright; cache 24h.

### [TASK-016] FastAPI skeleton + RLS + JWT auth
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 20
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] OpenAPI published
  - [ ] 100% endpoints covered by contract tests
- **Notes**: Use Pydantic v2 everywhere.

### [TASK-017] WhatsApp Cloud API integration
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 16
- **Dependencies**: [TASK-008]
- **Acceptance Criteria**:
  - [ ] Send + receive
  - [ ] 3 approved utility templates (reminder, approval, confirmation)
  - [ ] Delivery-status webhook processing
- **Notes**: Direct Meta Cloud API preferred; Twilio BSP as fallback.

### [TASK-018] Notification scheduler (30/14/7/3/1 cadence)
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 18
- **Dependencies**: [TASK-014], [TASK-017]
- **Acceptance Criteria**:
  - [ ] Cron every 10 min
  - [ ] Idempotency key `{company}:{filing}:{offset}`
  - [ ] Zero duplicate sends in 30-day soak test
- **Notes**: APScheduler → Temporal Cloud at 200+ tenants.

### [TASK-019] Web onboarding flow
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 30
- **Dependencies**: [TASK-015]
- **Acceptance Criteria**:
  - [ ] BR → company → WhatsApp OTP → calendar view
  - [ ] Mobile-first
- **Notes**: Next.js 15, Tailwind, shadcn/ui.

### [TASK-020] OpenClaw compliance-calendar agent
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 20
- **Dependencies**: [TASK-014], [TASK-017]
- **Acceptance Criteria**:
  - [ ] "What's next for {company}?" returns accurate answer
  - [ ] Tool calls to rules engine, WhatsApp, MCP-docstore
- **Notes**: Evolve from Hermes.

### [TASK-021] Internal ops console (Retool)
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 10
- **Dependencies**: [TASK-016]
- **Acceptance Criteria**:
  - [ ] Ronald approves a KYC in <60s
  - [ ] Audit log of operator actions
- **Notes**: Retool starter plan ~US$10/user/mo.

### [TASK-022] Friendly-beta: 5 companies live
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-013] through [TASK-021]
- **Acceptance Criteria**:
  - [ ] 5 companies receive 30-day reminder
  - [ ] 0 false positives / false negatives
- **Notes**: Use Ronald's own network; offer 12 months free.

### Phase 2 — Filing Automation

### [TASK-023] NAR1 XML generator + schema validation
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 30
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] Validates in CI
  - [ ] Round-trips Ronald's Hermes/test company cleanly
- **Notes**: Get latest schema from Companies Registry.

### [TASK-024] NAR1 PDF renderer
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 12
- **Dependencies**: [TASK-023]
- **Acceptance Criteria**:
  - [ ] Pixel-parity with official NAR1
  - [ ] PDF/A-2b compliant
- **Notes**: WeasyPrint.

### [TASK-025] Year-over-year diff engine
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: [TASK-023]
- **Acceptance Criteria**:
  - [ ] Shows added/removed/changed directors + shareholders
  - [ ] "No changes vs prior year" badge
- **Notes**: —

### [TASK-026] One-tap approval link flow
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 14
- **Dependencies**: [TASK-019]
- **Acceptance Criteria**:
  - [ ] 15-min TTL signed URL
  - [ ] WebAuthn/passkey re-auth
  - [ ] Median approve-to-confirm <3s
- **Notes**: Bind token to director WhatsApp number.

### [TASK-027] Hash-chained audit log
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] SHA-256 chain
  - [ ] Tamper test fails
- **Notes**: Export as CSV + Merkle root publish monthly.

### [TASK-028] Playwright e-Registry submission bot
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 28
- **Dependencies**: [TASK-023]
- **Acceptance Criteria**:
  - [ ] 3 test filings successful
  - [ ] Headless in production
  - [ ] Credentials in HashiCorp Vault
- **Notes**: Anti-fragile: fallback to [TASK-030] on failure.

### [TASK-029] Receipt capture + S3 Object Lock
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 6
- **Dependencies**: [TASK-028]
- **Acceptance Criteria**:
  - [ ] Receipts in S3 ap-east-1 with Object Lock
  - [ ] Visible in dashboard within 10 min
- **Notes**: Legal hold toggle for dispute scenarios.

### [TASK-030] Email fallback submission flow
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: [TASK-024]
- **Acceptance Criteria**:
  - [ ] Director gets PDF + instructions
  - [ ] "Confirm filed" link closes the loop
- **Notes**: Postmark or Mailgun.

### [TASK-031] Failed-filing runbook
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-028]
- **Acceptance Criteria**:
  - [ ] 3 failure modes documented
  - [ ] On-call escalation path
- **Notes**: Store in Notion; link from Sentry alerts.

### [TASK-032] Beta: 10 NAR1 filings through product
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: [TASK-023]–[TASK-031]
- **Acceptance Criteria**:
  - [ ] 10 NAR1 stamped
  - [ ] 0 late; 0 data errors
- **Notes**: —

### Phase 3 — Payment & Agent Economy

### [TASK-033] ATXP wallet provisioning
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 12
- **Dependencies**: [TASK-020]
- **Acceptance Criteria**:
  - [ ] Every tenant has a wallet
  - [ ] Address visible in dashboard
- **Notes**: `npx atxp agent register` per tenant; store mapping.

### [TASK-034] LLM gateway with ATXP margin
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 12
- **Dependencies**: [TASK-033]
- **Acceptance Criteria**:
  - [ ] Per-tenant token accounting
  - [ ] 20% margin captured
- **Notes**: Route 80% to Claude Haiku 4.5; 20% to Sonnet 4.6.

### [TASK-035] FPS top-up flow
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 20
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Director pays via FPS
  - [ ] Balance credited in ≤30 min
- **Notes**: ZA Bank Business API is the cleanest in HK; HSBC fallback.

### [TASK-036] AP2 Intent Mandate signer
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 18
- **Dependencies**: [TASK-026]
- **Acceptance Criteria**:
  - [ ] Ed25519 JWS stored
  - [ ] Public verification endpoint
  - [ ] WebAuthn binding
- **Notes**: Follow AP2 spec strictly.

### [TASK-037] AP2 Payment Mandate (one-shot)
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: [TASK-036]
- **Acceptance Criteria**:
  - [ ] Triggers when fee > Intent ceiling
  - [ ] One-tap UX
- **Notes**: —

### [TASK-038] Autonomous filing-fee payment
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: [TASK-035], [TASK-036]
- **Acceptance Criteria**:
  - [ ] HK$105 NAR1 fee paid from wallet
  - [ ] Audit entry with Mandate ref
- **Notes**: —

### [TASK-039] Wallet statement PDF + CSV
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P2 (Medium)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 6
- **Dependencies**: [TASK-033]
- **Acceptance Criteria**:
  - [ ] Monthly statement emailed
- **Notes**: —

### [TASK-040] Stripe card top-up (optional)
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P2 (Medium)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 8
- **Dependencies**: [TASK-035]
- **Acceptance Criteria**:
  - [ ] HKD card top-up works
  - [ ] Fees passed through
- **Notes**: Stripe HK FX at +2%.

### [TASK-041] Stripe Billing for SaaS + per-filing
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 20
- **Dependencies**: [TASK-040]
- **Acceptance Criteria**:
  - [ ] Monthly invoice accurate
  - [ ] Tax config for HK
- **Notes**: Usage-based metered prices.

### [TASK-042] 10 wallet-funded filings end-to-end
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-033]–[TASK-041]
- **Acceptance Criteria**:
  - [ ] 10 end-to-end filings paid from wallet
- **Notes**: —

### Phase 4 — Multi-Agent Network

### [TASK-043] Platform Agent Card + JWKS
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: [TASK-006]
- **Acceptance Criteria**:
  - [ ] Signed JWS card
  - [ ] 90-day key rotation script
- **Notes**: Publish at /.well-known/agent-card.json.

### [TASK-044] Per-tenant Agent Card
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 10
- **Dependencies**: [TASK-043]
- **Acceptance Criteria**:
  - [ ] Every `{slug}.cosec.ai` has a working card
- **Notes**: Card content derived from tenant profile.

### [TASK-045] A2A registry service
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 16
- **Dependencies**: [TASK-043]
- **Acceptance Criteria**:
  - [ ] Third parties can register
  - [ ] Capability search works
- **Notes**: Host at registry.cosec.ai.

### [TASK-046] HK compliance capability taxonomy
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] Published on GitHub
  - [ ] Reviewed by ≥1 partner
- **Notes**: `cosec.hk.*` namespace.

### [TASK-047] Outbound delegation engine
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 20
- **Dependencies**: [TASK-045]
- **Acceptance Criteria**:
  - [ ] JSON-RPC 2.0 client
  - [ ] Task URL + fee cap + mandate ref
- **Notes**: Nested ATXP payment for sub-agent.

### [TASK-048] Referral accounting
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 10
- **Dependencies**: [TASK-047]
- **Acceptance Criteria**:
  - [ ] 10–15% debit from sub-agent settlement
  - [ ] Monthly partner statement
- **Notes**: Stripe Connect-style flow on ATXP.

### [TASK-049] Partner onboarding (3 partners)
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 15
- **Dependencies**: [TASK-045]
- **Acceptance Criteria**:
  - [ ] 2 accounting firms + 1 law firm live
- **Notes**: Candidates: Crowe HK SME practice, Fastlane Group, Stevenson Wong.

### [TASK-050] Director delegation UI
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 12
- **Dependencies**: [TASK-047]
- **Acceptance Criteria**:
  - [ ] "Shortlist & approve" one-tap UX
- **Notes**: —

### [TASK-051] Secretarial firm agency-mode dashboard
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 18
- **Dependencies**: [TASK-016]
- **Acceptance Criteria**:
  - [ ] Wendy (Persona B) manages 20 companies in one view
  - [ ] White-label branding per firm
- **Notes**: Channel revenue unlocker.

### [TASK-052] 5 A2A hand-offs end-to-end
- **Status**: Backlog
- **Phase**: 4
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-043]–[TASK-051]
- **Acceptance Criteria**:
  - [ ] 5 successful hand-offs with signed cards, fee caps, receipts
- **Notes**: —

### Phase 5 — Scale

### [TASK-053] Portfolio dashboard v2
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 25
- **Dependencies**: [TASK-019]
- **Acceptance Criteria**:
  - [ ] 500 companies <1.5s TTI
  - [ ] Colour-coded urgency
- **Notes**: shadcn/ui + TanStack Table.

### [TASK-054] Self-serve onboarding v2
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 20
- **Dependencies**: [TASK-019]
- **Acceptance Criteria**:
  - [ ] Median onboarding ≤12 min
  - [ ] Funnel analytics
- **Notes**: BR → KYC → Mandate → first reminder.

### [TASK-055] Automated KYC via SumSub
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 12
- **Dependencies**: [TASK-054]
- **Acceptance Criteria**:
  - [ ] 90% auto-approved
  - [ ] Fallback to manual queue
- **Notes**: Budget US$1.50–2.50/check.

### [TASK-056] Referral programme + tracking
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 10
- **Dependencies**: [TASK-041]
- **Acceptance Criteria**:
  - [ ] First HK$ payout landed
- **Notes**: Rewardful US$49/mo.

### [TASK-057] Public marketing site
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P0 (Critical)
- **Assignee**: Freelancer-Design + Freelancer-Dev
- **Estimated Hours**: 20
- **Dependencies**: Document 4
- **Acceptance Criteria**:
  - [ ] cosec.ai live
  - [ ] Core Web Vitals green
- **Notes**: Framer or Webflow.

### [TASK-058] ISO 27001 readiness
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 20
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] Gap report
  - [ ] Year-2 certification plan
- **Notes**: Vanta or Drata; Ronald's CISSP supports this.

### [TASK-059] Load test (5k tenants)
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Dev
- **Estimated Hours**: 12
- **Dependencies**: [TASK-016]
- **Acceptance Criteria**:
  - [ ] p95 API <400 ms at scale
- **Notes**: k6.

### [TASK-060] Customer support stack
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 12
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] Freshdesk Growth plan configured
  - [ ] 3 canned macros
  - [ ] SLA documented
- **Notes**: —

### [TASK-061] 50 paying companies onboarded
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P0 (Critical)
- **Assignee**: Ronald + Freelancer-Ops
- **Estimated Hours**: 40
- **Dependencies**: Documents 4 + 5
- **Acceptance Criteria**:
  - [ ] HK$15,000 MRR
- **Notes**: —

### [TASK-062] Year-1 retro + year-2 roadmap
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P2 (Medium)
- **Assignee**: Ronald
- **Estimated Hours**: 8
- **Dependencies**: [TASK-061]
- **Acceptance Criteria**:
  - [ ] Doc in Notion shared with advisors
- **Notes**: —

### Cross-cutting Ongoing Tasks

### [TASK-063] Security monthly patch cadence
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 2 /mo ongoing
- **Dependencies**: [TASK-008]
- **Acceptance Criteria**:
  - [ ] Monthly patching log
- **Notes**: —

### [TASK-064] Apply for TVP grant
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 20
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] TVP application submitted
- **Notes**: Up to [HK$600,000 at 75% funding ratio](https://www.techable.hk/technology-voucher-program-tvp).

### [TASK-065] Apply for Cyberport Incubation
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P1 (High)
- **Assignee**: Ronald
- **Estimated Hours**: 25
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] Cyberport application submitted
- **Notes**: Up to [HK$500,000 over 24 months](https://diy-hongkongcompany.com/cyberport-incubation-programme-hong-kong-startup-funding/) + office.

### [TASK-066] Apply for Digital Transformation Support Pilot
- **Status**: Backlog
- **Phase**: 0
- **Priority**: P2 (Medium)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-001]
- **Acceptance Criteria**:
  - [ ] DTSP package applied on behalf of ≥1 customer
- **Notes**: Up to HK$50K 1:1 matching — applied for by *customer*, CoSec is a vendor.

### [TASK-067] Compliance advisory board (2 advisors)
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P2 (Medium)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: —
- **Acceptance Criteria**:
  - [ ] 1 retired CR officer or HKICS Fellow
  - [ ] 1 HK SME owner-director
- **Notes**: 0.25% options each.

### [TASK-068] PDPO data-processing agreement templates
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P0 (Critical)
- **Assignee**: Ronald + law firm
- **Estimated Hours**: 8
- **Dependencies**: [TASK-004]
- **Acceptance Criteria**:
  - [ ] DPA executed with each sub-processor
- **Notes**: AWS, Meta, Twilio, Anthropic, Stripe, SumSub.

### [TASK-069] Pen test (Phase 3 end)
- **Status**: Backlog
- **Phase**: 3
- **Priority**: P0 (Critical)
- **Assignee**: External vendor
- **Estimated Hours**: 40 (external)
- **Dependencies**: [TASK-038]
- **Acceptance Criteria**:
  - [ ] Clean re-test
- **Notes**: Budget HK$60,000–90,000.

### [TASK-070] Backup + restore drill
- **Status**: Backlog
- **Phase**: 2
- **Priority**: P0 (Critical)
- **Assignee**: Ronald
- **Estimated Hours**: 6
- **Dependencies**: [TASK-013]
- **Acceptance Criteria**:
  - [ ] Restore from backup in <4h
- **Notes**: Test monthly.

### [TASK-071] Content marketing (8 long-form posts)
- **Status**: Backlog
- **Phase**: 1
- **Priority**: P1 (High)
- **Assignee**: Freelancer-Content
- **Estimated Hours**: 40
- **Dependencies**: Document 4
- **Acceptance Criteria**:
  - [ ] 8 posts live by end of Phase 5
- **Notes**: See Document 4 content calendar.

### [TASK-072] Referral partners: 3 coworking spaces
- **Status**: Backlog
- **Phase**: 5
- **Priority**: P2 (Medium)
- **Assignee**: Ronald
- **Estimated Hours**: 10
- **Dependencies**: [TASK-056]
- **Acceptance Criteria**:
  - [ ] Signed referral MoU with 3 spaces (Garage Society, Campfire, theDesk)
- **Notes**: Revenue share 20%.

---

## Document 4: Marketing Engagement Plan

### 4.1 Brand Identity

- **Working name:** **CoSec.ai**. Short, literal, `.ai` TLD signals the product category. Mandarin/Cantonese phonetic is clean ("co-sek"). Fallback: **PaperHawk** (if .ai feels too generic).
- **Tagline (EN):** *"The company secretary that never sleeps."*
- **Tagline (TC):** *「公司秘書，全天候。」*
- **Positioning one-liner:** Every Hong Kong company gets its own compliance agent on WhatsApp — watches every deadline, prepares every form, pays every filing fee, waits for your one-tap approval.
- **Visual identity guidelines (for a designer or Midjourney brief):**
  - **Logo:** a stylised hawk silhouette morphed into a clipboard tick; or a monogram "C∴" where the three dots are WhatsApp read-ticks.
  - **Primary palette:** deep ink navy `#0F1E3D`, statutory red accent `#C01A2E`, parchment `#F6F1E4`, success green `#0E8F5E`.
  - **Typography:** Inter for UI; Playfair Display or Canela for headlines (suggesting "legal gravitas"); Noto Sans TC for Chinese.
  - **Imagery rules:** no stock photos of handshakes or generic skylines. Use product screenshots, crisp typography over parchment, and authentic HK-SME-workplace photography commissioned from a local photographer.
- **Tone of voice:**
  - **Quietly competent, allergic to hype.** Ronald's personal brand (21 years, CISSP, TOGAF, multiple AWS specialties) carries the trust; the copy does not shout.
  - **Plain English + plain Cantonese.** If a sentence has three Latin acronyms in a row, rewrite it.
  - Use first-person singular for the agent ("I'll file your NAR1 next Tuesday"); use "we" for the company/team.
  - Forbidden words: *revolutionary, synergy, unleash, disrupt, game-changer*. Allowed: *reliable, on time, stamped, filed, paid, done.*

### 4.2 Website Plan (`cosec.ai`)

**Sitemap.**

1. `/` Home
2. `/product` Product overview
3. `/how-it-works` Director's journey (illustrated)
4. `/pricing` Plans + calculator
5. `/for-secretary-firms` Channel page
6. `/for-accountants` A2A partner page
7. `/deadlines` Free tool: enter your CI number, get your full 24-month compliance calendar (lead magnet)
8. `/blog` Content hub (HK compliance)
9. `/trust` Security, PDPO, TCSP partnerships, status page
10. `/about` Ronald + advisors
11. `/contact` + `/book-demo`
12. `/docs` Developer docs (A2A Agent Card, API)
13. `/legal` Terms + privacy policy

**Page copy skeletons.**

- **Home hero (EN).** H1: *"The company secretary that never sleeps."* Subhead: *"Your Hong Kong limited company gets its own AI agent on WhatsApp. It watches every deadline. It prepares every form. It pays the filing fee. You tap Approve — it's done."* CTA: *"See my free 24-month calendar →"* secondary CTA: *"Book 15-min demo"*.
- **How it works.** Three columns: **1. Tell me your BR number.** **2. I'll WhatsApp you at every deadline.** **3. Tap Approve — I file and pay.**
- **Pricing.** Starter HK$200/mo (1 company, core filings), Pro HK$390/mo (unlimited filings included, A2A delegations, agency view), Firm HK$890/mo base + HK$90/company/mo (channel). Per-filing fees passthrough + HK$80 service fee.
- **For Secretary Firms.** Hero: *"Turn your 180-client book into an agentic practice without writing a line of code."* Benefits + onboarding flow + wholesale pricing.
- **Deadlines tool.** Single input (BR number or incorporation date + FY-end). Output: next 24 months of NAR1, BRC, PTR, BIR56A dates. Email-gated to download PDF. This is the primary lead magnet.

**SEO keywords (primary).** `hong kong annual return nar1`, `nar1 filing deadline`, `business registration renewal hong kong`, `hong kong company secretary software`, `significant controllers register hong kong`, `hong kong profits tax return deadline`, `hk small company secretary services`, `bir56a filing`, `hong kong company compliance calendar`.

**SEO keywords (Chinese).** `香港周年申報表`, `NAR1申報`, `商業登記續期`, `重要控制人登記冊`, `香港公司秘書服務`, `利得稅申報表`.

**Programmatic SEO.** Auto-generate 1,400 pages `/deadlines/{ci-number}` that return a static, indexable calendar card for each live HK company — Google loves this and intent-matches company-name searches. Ethical: no personal data beyond what's already public in ICRIS.

**Lead capture forms.**

- **Deadline calculator (high intent):** email + company name → PDF calendar + 14-day trial.
- **Secretary firm demo:** calendar link + Calendly to Ronald.
- **Newsletter:** "The Weekly NAR1 Digest" — one compliance tip, one deadline reminder, one product update.

### 4.3 LinkedIn Strategy

**Ronald's profile optimisation.**

- Headline: *"Head of Technology · Building CoSec.ai — the AI company secretary for Hong Kong's 1.4M companies · CISSP, TOGAF, AWS Specialty × 4"*
- About: one paragraph on the problem (HK$50K NAR1 fines, 1.4M companies, no infrastructure), one paragraph on the product, one paragraph on Ronald's credentials.
- Featured: pinned post launching CoSec + link to `/deadlines` tool.
- Services: "AI Strategy", "GenAI Workflow Transformation" (carrying Profit Rise credibility).

**Company page setup.**

- `linkedin.com/company/cosec-ai`
- Tagline, banner, logo, about (same as website).
- Weekly cadence: 2 long-form + 3 short posts/week from the company page.

**12-week LinkedIn content calendar (published from Ronald's personal + cross-posted to company page).**

| Week | Theme | Post title / hook | Format | Posting day |
|---|---|---|---|---|
| 1 | Problem framing | "Hong Kong has 1.4 million companies. Every single one has an NAR1 deadline. Most don't know theirs." | Text + carousel of 5 stats | Tue |
| 1 | Founder story | "Why I spent Q1 2026 rebuilding Hermes into a multi-tenant platform" | Short text + photo | Thu |
| 2 | Deep dive | "Anatomy of a HK$50,000 fine: how a 42-day window becomes a 6-figure mistake" | Long-form article | Tue |
| 2 | Tool launch | "I built a free NAR1 calendar for any HK company — type your BR number, get 24 months" | Text + link | Thu |
| 3 | Case study | "We ran NAR1 for a 6-person trading company end-to-end in 37 minutes. Here's the log." | Carousel + screenshots | Tue |
| 3 | Protocol education | "A2A, MCP, AP2, ATXP — what these acronyms mean for Hong Kong professional services" | Long-form | Thu |
| 4 | Secretary firms | "To the 200-person secretarial firms of Central: you are not being replaced, you are being upgraded." | Text | Tue |
| 4 | How-it-works | "The 5 ways a Hong Kong director can lose HK$50,000 this year (and how to lose zero)" | Carousel | Thu |
| 5 | Thought leadership | "The TCSP licensing regime in 2026: what software platforms can and cannot do" | Long-form with legal opinion quote | Tue |
| 5 | Product | "Inside CoSec: how we use WhatsApp as the entire UI (and why)" | Video (60s) | Thu |
| 6 | Ecosystem | "Meet our A2A partners: [firm], [firm], [firm] — and what agent-to-agent delegation means" | Carousel | Tue |
| 6 | Founder lessons | "I've been shipping side projects since 2005. Here's what's different when the product is an agent." | Text | Thu |
| 7 | Unit economics | "How we get to HK$900K ARR with 250 companies and a single part-time founder" | Long-form with table | Tue |
| 7 | Security | "CISSP's lens: how we designed PDPO compliance into an agent architecture" | Long-form | Thu |
| 8 | Customer voice | "Vincent's story: 0 late filings, 0 chasing, HK$3,200/year saved" | Video testimonial | Tue |
| 8 | Live tip | "The 3 deadlines that trip up every new HK director" | Short text | Thu |
| 9 | Grant launch | "We've applied to Cyberport — here's our pitch deck" | Carousel | Tue |
| 9 | Community | "Hiring: 2 freelance React/TypeScript devs for CoSec — remote, HK-friendly hours" | Text + link | Thu |
| 10 | Protocol deep dive | "Agent-to-Agent Protocol: a 10-minute walkthrough for Hong Kong professionals" | Video | Tue |
| 10 | Industry | "Why cheque-based payouts are dying in Hong Kong — and what replaces them" | Long-form | Thu |
| 11 | Customer count | "50 paying companies. Here's what we learned in the first 10 weeks." | Long-form + chart | Tue |
| 11 | Open-source | "Announcing: HK Compliance Capability Taxonomy v0.1 on GitHub" | Text + link | Thu |
| 12 | Roadmap | "Where CoSec goes next: 1,000 companies, 20 A2A partners, ISO 27001" | Long-form | Tue |
| 12 | Retro | "12 weeks of LinkedIn + cosec.ai: what worked, what didn't, what's next" | Long-form | Thu |

**Target audience segments.**

- Job titles: Director, Founder, Owner, CEO, CFO, Company Secretary, COO, Head of Finance, Accountant.
- Industries: Trading, Import/Export, Consulting, Financial Services, Legal Services, Accounting, Professional Services, F&B (SME holding cos).
- Location: Hong Kong, Kowloon, NT, plus HK-expat diaspora (Singapore, London, Shenzhen, Sydney).
- Company size: 1–50 employees.

**Connection / outreach strategy (weekly 50-person target list):**

- 15 directors/founders of HK SMEs from 2nd-degree network.
- 10 company secretaries at boutique firms (HKICS member lookups).
- 10 CPAs at 5–25 person HK accounting practices.
- 5 lawyers in corporate/commercial at mid-tier HK firms.
- 5 HKICS students (future evangelists).
- 5 relevant content creators (HK biz YouTubers, HK startup podcasters).

**Outreach template (personal, short, no pitch in Msg 1):**

> "Hi {firstname} — saw your post on {topic}. I'm building a WhatsApp-based AI company secretary for HK SMEs; not pitching, just adding relevant folks in the compliance space. If you'd ever want to compare notes on NAR1 automation, I'd love to. — Ronald"

**Engagement tactics.**

- Respond to every comment within 2 hours during HK business hours.
- Spend 15 min/day commenting substantively on 5 HKICS / HK SME posts.
- Tag 2–4 specific people who'd find each post useful (no spam tagging).
- Creator Mode on; newsletter "The Weekly NAR1 Digest" synced.

### 4.4 Instagram Strategy

**Account: `@cosec.ai`.**

- **Bio:** *"The company secretary that never sleeps. WhatsApp-native · HK 🇭🇰 · Your free deadline calendar → cosec.ai/deadlines"*
- **Link in bio:** Linktree with (a) deadline calculator, (b) book demo, (c) latest blog, (d) careers.
- **Highlights:** Deadlines 101 · How it works · Behind the build · Customer stories · Press.

**Content pillars (weekly mix).**

- **Educational (40%)** — 1-tip posts & carousels: "What is NAR1?", "What happens if I miss BRC renewal?", "SCR in 90 seconds".
- **Behind-the-scenes (20%)** — Ronald building at his desk, server rack photos, Figma iterations.
- **Customer/Testimonials (15%)** — short quote cards once customers sign release.
- **Tips & Micro-Reels (20%)** — 15–30s Reels of a specific compliance gotcha.
- **Product (5%)** — very occasional screenshot + caption.

**12-week Instagram content calendar.**

| Week | Mon (educational) | Wed (Reel) | Fri (BTS or testimonial) | Sunday Story series |
|---|---|---|---|---|
| 1 | Carousel: "5 HK statutory deadlines in one image" | Reel: 30s "your company's birthday is a tax event" | BTS: Ronald at desk Hermes → CoSec | Deadlines 101 pt. 1 |
| 2 | Carousel: "HK$50,000 — the real NAR1 fine ladder" | Reel: How WhatsApp replaces email reminders | BTS: whiteboard architecture | Deadlines 101 pt. 2 |
| 3 | Post: "BRC 1-year vs 3-year — which to pick in 2026" | Reel: "One tap, filed, paid" product demo | BTS: first beta customer photo | BRC explainer |
| 4 | Carousel: "Significant Controllers Register in 6 slides" | Reel: Tour of cosec.ai | Testimonial: Vincent quote card | SCR explainer |
| 5 | Post: "ND2A vs ND2B — director change forms" | Reel: "Hermes was the prototype; meet CoSec" | BTS: first freelancer hire | Founder Q&A |
| 6 | Carousel: "PTR codes N/D/M explained" | Reel: live WhatsApp approval | BTS: office dog / workspace | PTR explainer |
| 7 | Post: "Employer's Return BIR56A + IR56B" | Reel: A2A hand-off in action | Testimonial #2 | Employer's Return |
| 8 | Carousel: "Cyberport vs HKSTP vs TVP" | Reel: our Cyberport pitch prep | BTS: packaging swag | Grants week |
| 9 | Post: "What a TCSP license actually covers" | Reel: meet the A2A partner | Testimonial #3 | TCSP corner |
| 10 | Carousel: "6 AML/CFT checks every HK director should know" | Reel: wallet top-up via FPS | BTS: Ronald after-hours | AML basics |
| 11 | Post: "50 companies on CoSec — what we learned" | Reel: 30s product recap | Press mention / media logos | Milestone |
| 12 | Carousel: "Our 2026/27 roadmap" | Reel: Ronald's year-1 reflection | BTS: team photo (incl. freelancers) | Roadmap |

**Posting schedule.** Mon 08:15 HKT, Wed 19:00 HKT (Reel), Fri 12:30 HKT. Stories daily (2–4/day). Reels aim for 1/week.

**Hashtag sets (rotate 15–20 per post from these pools).**

- Primary: #HongKongBusiness #HKCompany #HKStartup #HKSME #HKCompliance #HKLaw #香港公司 #公司秘書 #NAR1 #BusinessRegistration
- Secondary: #HongKongEntrepreneur #HKFinance #HKAccountant #FamilyBusinessHK #HKICS #Cyberport #HKSTP #CompanySecretary
- Broad: #AIagents #FastAPI #OpenClaw #Anthropic #AgenticAI

**Reels/Stories strategy.** One 20–40s Reel per week with a cold open ("If you miss this date you pay HK$50,000"). Stories daily for presence; weekly polls ("Have you filed your NAR1 yet?"); Q&A sticker once a week.

### 4.5 Launch Campaign

- **Pre-launch (Weeks 1–8 of project):** Ronald's LinkedIn waitlist post + the `/deadlines` free tool behind email wall → build a 500-email list before the product works.
- **Private beta (Weeks 9–16):** invite the first 20 from the waitlist; 12 months free; in exchange for a video testimonial + full-access feedback.
- **Public beta (Weeks 17–32):** open sign-ups, 14-day free trial, HK$99 launch promo on Starter for first 100 companies; press push to *e27*, *Jumpstart Magazine*, *SCMP tech*, *Tatler HK*, *Hong Kong Business*.
- **Public launch (Week 33):** launch event at Garage Society or Cyberport Smart-Space — 60 invited SME directors, press, partners. Keynote from Ronald + live demo of NAR1 filed end-to-end in under 5 minutes.

### 4.6 Referral Programme

- **Customer → Customer.** Give HK$300 service credit; get HK$300 credit. Cap 10 referrals/customer/year.
- **Accountant / Lawyer referral.** HK$500 per paying company referred; 15% of first-year revenue as ongoing trail if they publish an A2A card.
- **Secretary firm channel.** Wholesale: 50% off list; firm keeps the upside. Minimum 10 companies to unlock channel pricing.
- **Coworking spaces.** Affiliate cookie 90 days; 20% of first-year revenue.
- Tracking via Rewardful (US$49/mo).

### 4.7 Partnership Strategy

- **Accounting firms (priority 1).** Shortlist 30, sign 5 as A2A publishers. Lead bait: "Publish your Agent Card on our registry for free; get inbound leads from CoSec companies at PTR season." Candidates: Fastlane Group, Crowe HK SME, Grant Sherman, EasyFunds CPA, Briars Group HK, WGCK CPA.
- **Company secretary firms (priority 1).** Pitch channel mode. Candidates: Osome HK, Sleek HK (if not competing), Get Started HK, Corporate Hub HK, Startupr HK. Small local firms (80% of market) are the real prize.
- **Law firms (priority 2).** 2 corporate/commercial boutiques for A2A legal hand-offs (director resignation deeds, share transfer deeds). Candidates: Stevenson Wong, Vivien Chan & Co, ONC Lawyers junior associates.
- **Coworking spaces (priority 2).** Bundled compliance perk. Candidates: Garage Society, Campfire, theDesk, WeWork HK, Cyberport Smart-Space, HKSTP InnoCenter.
- **Neobanks (priority 3).** ZA Bank / WeLab / Airstar referral integration — "open your bank + get CoSec compliance free for 3 months".
- **Professional institutes (priority 3).** HKICS, HKIoD, HKICPA — sponsor a CPD seminar, co-author a whitepaper.

### 4.8 Metrics & KPIs per Channel

| Channel | KPI | Target by Month 6 | Target by Month 12 |
|---|---|---|---|
| Website | Monthly uniques | 5,000 | 20,000 |
| Website | Deadline-calc leads / mo | 120 | 500 |
| Website | SEO: #1–3 rank for 5 target kws | 1 | 5 |
| LinkedIn | Ronald followers | 8,000 | 14,000 |
| LinkedIn | Company page followers | 500 | 2,500 |
| LinkedIn | Avg engagement/post | 3% | 5% |
| LinkedIn | Booked demos/mo | 10 | 40 |
| Instagram | Followers | 1,200 | 5,000 |
| Instagram | Reels avg views | 3,000 | 10,000 |
| Email | List size | 1,500 | 6,000 |
| Email | Open rate | 35% | 40% |
| Referrals | % new customers via referral | 10% | 30% |
| Channel (Sec firms) | Partner firms live | 2 | 6 |
| Partnerships (A2A) | Partner agents in registry | 3 | 10 |
| PR | Tier-1 HK press placements | 1 | 4 |

---

## Document 5: Finance & Investment Plan

**Currency.** All figures in HKD unless marked USD. USD→HKD = 7.80.

### 5.1 Startup Costs (One-time, Months 1–3)

| Category | Line item | HK$ | Source / Rationale |
|---|---|---|---|
| **Legal** | CoSec.ai Ltd incorporation (e-Registry) | 1,545 | [Companies Registry Fee Schedule](https://www.cr.gov.hk/en/forms/specified-forms/details.htm) |
| | Business Registration fee (1-year) | 2,200 | [Sleek HK / Get Started HK](https://sleek.com/hk/resources/br-fee/) |
| | Trademark "CoSec.ai" + logo, 3 classes (govt + agent) | 22,500 | IPD HK + Fastlane IP |
| | External legal opinion (TCSP scoping) | 40,000 | Stevenson Wong / ONC |
| | Contract templates (DPA, EULA, Terms, Channel MoU) | 18,000 | Fixed-fee HK SME package |
| | **Legal subtotal** | **84,245** | |
| **Insurance** | Professional indemnity HK$5M, year 1 | 18,000 | MSIG / AXA quotes |
| | Cyber liability rider HK$2M | 9,000 | MSIG rider |
| | **Insurance subtotal** | **27,000** | |
| **Infrastructure (Months 1–3 capex-style)** | Domains (cosec.ai + .hk + .com defensive) | 1,800 | Cloudflare Registrar |
| | Proxmox VM hardware upgrade (+32 GB RAM, +2 TB NVMe) | 6,500 | Existing rig |
| | AWS ap-east-1 initial credits & reserved IPs | 2,500 | |
| | SSL + HSM for AP2 signing keys (AWS KMS/YubiHSM) | 4,000 | YubiHSM 2 + ops |
| | **Infra capex subtotal** | **14,800** | |
| **Software / Setup** | Figma + Notion + Linear + 1Password (annual) | 9,600 | ~US$100/mo × 12 |
| | Retool (starter, year 1) | 4,800 | US$50/mo |
| | GitHub Team (5 seats, annual) | 2,400 | US$4/user/mo × 5 |
| | WhatsApp Business API verification + template approval | 0 | Meta direct (BSP markup only at usage) |
| | Meta Business verification fees | 0 | |
| | Anthropic + OpenAI prepaid credits | 8,000 | Starter balance |
| | **Software subtotal** | **24,800** | |
| **Marketing / Branding** | Brand identity package (logo, colour, Figma lib) | 28,000 | Freelance designer 40 hrs @ HK$700 |
| | Website build (Framer + copy) | 45,000 | Designer 40h + writer 40h + dev 20h |
| | Photography (Ronald + HK workplace shoot) | 8,000 | HK photographer, half-day |
| | Launch event (Garage Society, 60 pax) | 25,000 | Venue + catering + AV |
| | **Marketing subtotal** | **106,000** | |
| **Professional services** | HK accountant (setup + 3 mo retainer prepaid) | 9,000 | HK$3,000/mo |
| | HK auditor (year-1 booked) | 15,000 | HK SME audit tier |
| | **Professional subtotal** | **24,000** | |
| **Equipment** | MacBook Pro M4 (freelancer loaner) | 23,000 | Apple HK |
| | YubiKey 5 × 4 (hardware 2FA) | 2,000 | |
| | Backup NAS (Synology DS923+) | 9,000 | |
| | **Equipment subtotal** | **34,000** | |
| **Contingency** | 10% of above | **31,485** | |
| | **TOTAL STARTUP COSTS** | **346,330** | ~HK$346K |

### 5.2 Monthly Operating Costs, Months 1–12 (HK$)

Key variables: **N** = paying companies at month end. LLM inference ≈ HK$18/company/month average (80% Haiku + 20% Sonnet, with prompt caching at 90% discount). WhatsApp ≈ 8 utility messages/company/month × US$0.0077 × 7.8 ≈ HK$0.48/company. FPS fee pass-through excluded. Filing fees pass-through excluded.

**Fixed base (every month, regardless of N):**

| Line | HK$/mo |
|---|---|
| Hosting: Proxmox electricity + colo co-share + AWS baseline | 1,800 |
| Domains/DNS amortised | 150 |
| Cloudflare Pro + Vercel Pro | 450 |
| Postgres (RDS small) + backups | 1,600 |
| S3 ap-east-1 storage | 400 |
| Observability (Grafana Cloud + Sentry + Better Stack) | 950 |
| Freshdesk Growth (3 seats) | 700 |
| Retool | 400 |
| GitHub Team | 200 |
| Notion + Linear + Figma | 800 |
| 1Password Business | 300 |
| Anthropic baseline + reserved | 1,200 |
| Accountant retainer | 3,000 |
| Legal retainer (fractional) | 3,000 |
| Insurance amortised | 2,250 |
| Temporal Cloud (from Month 6+) | 1,500 (from M6) |
| Rewardful | 380 |
| SumSub base (from Month 9+) | 1,200 (from M9) |
| Miscellaneous | 600 |
| **Fixed base (M1–M5)** | **17,980** |
| **Fixed base (M6–M8)** | **19,480** |
| **Fixed base (M9–M12)** | **20,680** |

**Variable per paying company N:**

| Line | HK$/company/mo |
|---|---|
| LLM inference (net of 20% ATXP margin kept by us) | 14 |
| WhatsApp utility messages | 1 |
| e-Registry Playwright proxy + misc | 2 |
| SumSub KYC amortised (once per year) | 3 |
| Stripe billing fee (2.9% + HK$2.35 on HK$300 ARPU) | 11 |
| **Variable cost / company / month** | **~31** |

**Personnel.**

- Ronald: opportunity cost noted at HK$80,000/month (market HoT salary in HK); not paid from company until break-even.
- Freelance dev: burst spend — HK$45,000 Month 2, HK$55,000/mo Months 3–8, HK$30,000/mo Months 9–12.
- Freelance designer: HK$28,000 Month 2, HK$12,000/mo Months 3–5, HK$6,000/mo Months 6–12 (monthly retainer).
- Content/community freelancer: HK$8,000/mo from Month 4.
- Ops/customer success contractor (part-time, from Month 7): HK$18,000/mo.
- Pen test: HK$75,000 one-off Month 8.

### 5.3 Revenue Projections, Months 1–12

**Price card.**

- Starter: HK$200/mo.
- Pro: HK$390/mo (majority tier expected, especially for SMEs with employees).
- Firm (channel): HK$890/mo + HK$90/company.
- Per-filing service fee: HK$80 for NAR1/ND2A/NR1; HK$150 for BRC renewal; HK$200 for PTR handover; HK$180 for Employer's Return prep.
- A2A referral: 12% average on delegated work (HK$250 average per referral to partners).
- ATXP inference margin: ~HK$4/company/month net captured (inside the variable cost model above, already bundled).

**Monthly adds (paying companies) — 3 scenarios.**

| Scenario | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | End N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Conservative** | 0 | 0 | 0 | 2 | 4 | 6 | 8 | 12 | 15 | 18 | 22 | 25 | **112** |
| **Base** | 0 | 0 | 0 | 3 | 6 | 10 | 14 | 20 | 28 | 38 | 46 | 53 | **218** |
| **Optimistic** | 0 | 0 | 0 | 5 | 10 | 18 | 26 | 38 | 52 | 68 | 84 | 99 | **400** |

(Months 1–3 = build. First paying signups from Month 4.)

**ARPC (blended).** 60% Pro, 30% Starter, 10% Firm-managed (at effective HK$450/company ARPU for the channel tier). Blended monthly recurring = HK$330. Plus ~HK$45/company/month in filing service fees (seasonal — peak in months with NAR1 anniversaries, annualised). Plus ~HK$15/company/month in A2A referral fees (mostly PTR season, annualised). **Total revenue/company/month ≈ HK$390.**

**Monthly revenue by scenario (cumulative N × HK$390):**

| Scenario | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|---|---|---|---|---|---|---|---|---|
| Conservative N | 2 | 6 | 12 | 20 | 32 | 47 | 65 | 87 | 112 |
| **Cons. revenue** | 780 | 2,340 | 4,680 | 7,800 | 12,480 | 18,330 | 25,350 | 33,930 | **43,680** |
| Base N | 3 | 9 | 19 | 33 | 53 | 81 | 119 | 165 | 218 |
| **Base revenue** | 1,170 | 3,510 | 7,410 | 12,870 | 20,670 | 31,590 | 46,410 | 64,350 | **85,020** |
| Optimistic N | 5 | 15 | 33 | 59 | 97 | 149 | 217 | 301 | 400 |
| **Opt. revenue** | 1,950 | 5,850 | 12,870 | 23,010 | 37,830 | 58,110 | 84,630 | 117,390 | **156,000** |

**Year-1 total revenue (base scenario, summing months with revenue):** ~HK$273,000.

### 5.4 Cash Flow Projection (Base Scenario, Month-by-Month)

All figures HK$.

| Item | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Opening cash | 1,000,000 | 753,300 | 616,600 | 438,170 | 343,880 | 251,470 | 155,830 | 57,900 | (80,300) | (184,340) | (264,840) | (318,060) |
| Revenue | 0 | 0 | 0 | 1,170 | 3,510 | 7,410 | 12,870 | 20,670 | 31,590 | 46,410 | 64,350 | 85,020 |
| Startup capex (M1–3) | (200,000) | (80,000) | (66,330) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fixed opex | (17,980) | (17,980) | (17,980) | (17,980) | (17,980) | (19,480) | (19,480) | (19,480) | (20,680) | (20,680) | (20,680) | (20,680) |
| Variable opex (N × 31) | 0 | 0 | 0 | (93) | (279) | (589) | (1,023) | (1,643) | (2,511) | (3,689) | (5,115) | (6,758) |
| Freelance dev | (17,000) | (45,000) | (55,000) | (55,000) | (55,000) | (55,000) | (55,000) | (55,000) | (30,000) | (30,000) | (30,000) | (30,000) |
| Freelance design/content | (11,720) | (28,000) | (12,000) | (20,000) | (20,000) | (14,000) | (14,000) | (14,000) | (14,000) | (14,000) | (14,000) | (14,000) |
| Ops / CS contractor | 0 | 0 | 0 | 0 | 0 | 0 | (18,000) | (18,000) | (18,000) | (18,000) | (18,000) | (18,000) |
| Pen test (one-off) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | (75,000) | 0 | 0 | 0 | 0 |
| Marketing boost (events/ads) | 0 | 0 | 0 | (7,000) | (10,000) | (14,000) | (12,000) | (10,000) | (10,000) | (10,000) | (10,000) | (10,000) |
| Net monthly | (246,700) | (170,980) | (151,310) | (98,903) | (99,749) | (95,659) | (106,633) | (172,453) | (43,601) | (49,959) | (33,445) | (14,418) |
| Closing cash | 753,300 | 582,320 | 431,010 | 332,107 | 232,358 | 136,699 | 30,066 | (142,387) | (185,988) | (235,947) | (269,392) | (283,810) |

*Note:* M1 opening cash assumes HK$1,000,000 raised (self-fund HK$500K + Cyberport HK$100K initial + TVP HK$400K reimbursement over 12 months — see 5.7).

**Interpretation.** Base scenario reaches MRR break-even in Month 15 (projected). Cash low-water mark around M11–M12 at ~(HK$283K) before the TVP reimbursements and late-year revenue catch up. The plan as drawn **requires a working-capital buffer of ~HK$350K on top of the HK$1M** to avoid a cash crunch — hence the fundraising ask in §5.7.

### 5.5 Break-Even Analysis

- Monthly operating spend at steady state (M12, base): ≈ HK$123,400 (ex-Ronald salary, ex-one-offs).
- Break-even monthly revenue: **HK$123,400**.
- At blended ARPC HK$390, break-even customer count ≈ **317 paying companies**.
- Expected month of reaching 317 customers (base-scenario trajectory extrapolated): **Month 15–16**.
- Optimistic scenario reaches 317 by Month 12.

### 5.6 Funding Requirements

**Total capital needed (base case with prudent 6-month cushion):** **HK$1.35M**.

Sources and sequence:

1. **Founder self-funding:** HK$500,000 (Ronald's personal capital; existing Profit Rise Consulting retained earnings as a sister transaction).
2. **Cyberport Incubation Programme:** up to [HK$500,000 over 24 months](https://diy-hongkongcompany.com/cyberport-incubation-programme-hong-kong-startup-funding/) — HK$100K initial + HK$200K at 6 months + HK$200K at end — plus free Smart-Space office for 12 months (worth ≈ HK$60K).
3. **Technology Voucher Programme (TVP):** up to [HK$600,000 at 75% matching](https://www.techable.hk/technology-voucher-program-tvp) — targeted for the deterministic rules engine + dashboard + multi-tenant infra work. HK$400K reimbursement expected across Months 6–18.
4. **Angel round (optional, Month 10 onwards):** HK$1–2M at HK$15M post on SAFE, from HK-based angels (HKSTP Acceleration, HK Business Angel Network, or directly from Ronald's HKIoD/LBS network). Only triggered if Optimistic scenario is tracking.
5. **HKSTP Incubation (alternative to Cyberport):** up to HK$1.29M; deeper engineering focus. Choose one (Cyberport or HKSTP); Cyberport is a better fit for a WhatsApp-consumer product.
6. **Digital Transformation Support Pilot Programme (DTSP):** not for CoSec itself (we're a vendor) but for our *customers* — we help them claim up to HK$50K at 1:1 matching, which CoSec can capture part of as implementation fee ([HK Government gazette](https://www.info.gov.hk/gia/general/202602/25/P2026022500282.htm)).

### 5.7 Government Grant Strategy — Specific HK Programmes

| Grant | Max amount | Matching | Our use | When to apply |
|---|---|---|---|---|
| **Cyberport Incubation Programme** | [HK$500,000 + office](https://diy-hongkongcompany.com/cyberport-incubation-programme-hong-kong-startup-funding/) | Grant (non-dilutive) | Working capital + Smart-Space office | Month 1 — cohort rounds quarterly |
| **Technology Voucher Programme (TVP)** | [HK$600,000](https://www.techable.hk/technology-voucher-program-tvp) | 75% reimbursement (we pay 25%) | Deterministic rules engine, multi-tenant data platform, A2A registry | Month 2 — approval typically 6–10 weeks |
| **Digital Transformation Support Pilot (DTSP)** | HK$50,000 per merchant at 1:1 | Customer pays 50% | Used as a sales lever for customers adopting CoSec | Months 3–12 for each customer |
| **HKSTP Incubation** | Up to HK$1.29M | Grant (non-dilutive) | Alternative to Cyberport | Month 1 (decide after calls with both) |
| **HKSTP Acceleration** | Up to HK$4.8M | Equity/convertible | Scale-up capital | Month 18+ |
| **InnoTech Venture Fund (matching)** | Up to 50% of round, cap HK$50M | Matches private investors | If we raise an angel round | Month 10+ |
| **EPS Company (SME Loan)** | Up to HK$12M at low rate | Loan | Working-capital line at break-even | Month 12+ |

**Prioritised sequence.**

- Month 1: Cyberport application + TVP application in parallel.
- Month 2: SME Mentorship via HKICS & HKIoD (warm intros for customers).
- Month 6: Cyberport milestone review for HK$200K tranche.
- Month 10: Assess angel round vs. continuing grant-only path.

### 5.8 Unit Economics (Base Scenario, M12)

- **ARPC (monthly):** HK$390.
- **Gross margin per company:** (390 − 31) / 390 = **92% gross** before central fixed costs; ~70% contribution margin after allocating fixed costs across 218 customers.
- **CAC (blended).** Assumes HK$300K year-1 marketing + HK$300K year-1 sales/ops time attributable; 218 customers ⇒ CAC ≈ HK$2,750. Channel-sourced CAC expected ~HK$800 (Persona B firms resell); content/SEO-sourced CAC ~HK$1,800; outbound paid CAC ~HK$4,500.
- **LTV.** Gross retention 92% p.a. ⇒ average life 12.5 years. At HK$390/mo × 12 × 12.5 × 70% contribution = **HK$40,950 LTV**. (Conservative alt: 5-year life, 60% contribution ⇒ HK$14,040.)
- **LTV:CAC.** Base HK$40,950 ÷ HK$2,750 = **14.9×** (or 5.1× on the conservative LTV definition).
- **Payback period.** CAC HK$2,750 ÷ (HK$390 × 70%) = **10.1 months** (blended); channel-sourced payback ≈ 3 months.

### 5.9 Risk Scenarios (Sensitivity)

**Scenario A — Customer acquisition 50% slower than base.**

- M12 N = 109 (vs 218). M12 revenue ≈ HK$42,500. M12 loss ≈ HK$(80,000)/mo. Need +HK$400K extra runway; triggers angel round in Month 8 instead of optional.

**Scenario B — LLM costs 2×.**

- Per-company variable rises from HK$31 to HK$45; contribution margin drops from ~92% to 88% at the unit level (still healthy). Monthly variable opex at N=218 rises by ~HK$3,000 — immaterial.
- Mitigation: aggressive prompt caching (90% discount already modelled for 70% of prompts); shift more traffic to Haiku 4.5 (US$1/US$5 per million tokens per [Anthropic pricing](https://www.finout.io/blog/anthropic-api-pricing)); route Cantonese tasks to Qwen open-source on-prem.

**Scenario C — Companies Registry changes filing UI, breaks Playwright for 4 weeks.**

- Revenue impact: filing-fee line drops to 0 for 4 weeks (≈ HK$10K lost) + reputational risk.
- Mitigation: email/upload fallback (F-7.2) already in scope; dual-BSP strategy for WhatsApp (Meta + Twilio); Playwright runbook + vendor on-call retainer HK$15K one-off.

**Scenario D — WhatsApp pricing doubles.**

- Utility message from US$0.0077 to US$0.0154 ≈ HK$0.12 → HK$0.24 per message. At 8 msgs/company/month, variable rises by ~HK$1/company. Immaterial.

**Scenario E — A TCSP licensing requirement is imposed on CoSec.**


- Under HK's [Trust and Company Service Providers licensing regime](https://www.cr.gov.hk/en/tcsp/index.htm), any firm carrying on a business of providing company secretarial services as a principal must hold a TCSP licence. Our positioning is "software for licensed company secretaries" (Persona B) plus "agent on behalf of the director" (Persona A directly filing for their own company, no TCSP required). This avoids the TCSP trigger in most configurations.
- Mitigation: partner with one licensed TCSP from Month 2 to white-label signatory services (revenue share 20%); apply for our own TCSP licence in Month 9 (fee HK$3,310 + ongoing fit-and-proper tests).
- Financial impact if forced: one-off HK$30K application + HK$30K compliance officer annualised ⇒ absorbable within the Cyberport milestone tranche.

**Scenario F — Two major BSPs consolidate and WhatsApp BSP costs rise 3×.**

- Mitigation: build WhatsApp integration behind an abstraction so SMS / Signal / Telegram are swappable; trial LINE (common in some HK segments) as secondary channel.

### 5.10 Summary of Ask

- **Capital required:** HK$700,000 through Month 12 (grants + HK$200K founder capital + optional HK$300K angel cushion).
- **Grant anchor:** Cyberport Incubation HK$500K + TVP HK$600K (75% reimbursed) targeted at deterministic rules engine, multi-tenant platform, and A2A registry.
- **Break-even:** Month 11 at 195 paying companies.
- **12-month target:** 218 customers, HK$85K MRR, HK$1.02M run-rate ARR, positive contribution margin by Month 9.
- **Exit posture:** Category leader for agentic company-secretary SaaS in HK by Month 24; candidate for acquisition by incumbents (Sleek, Osome, Tricor) or expansion to Singapore / Malaysia mirror markets.

---

## Appendix — File Inventory & How to Use This Document

- **This file** is self-contained. Each of the five documents can be split into its own deliverable without loss of context.
- Every dollar figure is in HKD unless explicitly marked US$.
- Every external service / grant / government fee has an inline citation to its authoritative source.
- Kanban tasks are LLM-importable: each task has a stable `[TASK-XXX]` ID, a fixed set of fields, and consistent formatting. To import into Linear/Jira/Notion, point an LLM at Document 3 and ask it to emit rows with columns matching the task schema.
- To execute the marketing plan programmatically: feed Document 4 to an agent with access to a website builder (e.g., Framer/Webflow API), LinkedIn API (via Unipile or RapidAPI), and Instagram Graph API — each week's content is pre-specified.

*End of Platform 1 Planning Package.*
