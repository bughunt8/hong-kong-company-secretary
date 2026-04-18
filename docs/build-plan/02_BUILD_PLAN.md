# Product Build Plan

*Extracted from the Complete Planning Package*

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

