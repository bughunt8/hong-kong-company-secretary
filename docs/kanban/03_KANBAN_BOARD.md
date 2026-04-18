# Kanban / GTD Board

*Extracted from the Complete Planning Package*

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

