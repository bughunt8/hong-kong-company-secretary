# Product Requirements Definition (PRD)

*Extracted from the Complete Planning Package*

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

