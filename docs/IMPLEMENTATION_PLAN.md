# CoSec.ai — Implementation & Testing Plan

*Greenfield build from planning documentation. 48-week roadmap, part-time founder (15–20 hrs/week), freelancer-augmented.*

---

## Table of Contents

1. [Repository Structure](#1-repository-structure)
2. [Tech Stack Decisions](#2-tech-stack-decisions)
3. [Testing Infrastructure](#3-testing-infrastructure)
4. [Phase 0 — Foundation (Weeks 1–4)](#4-phase-0--foundation-weeks-14)
5. [Phase 1 — Core MVP (Weeks 5–12)](#5-phase-1--core-mvp-weeks-512)
6. [Phase 2 — Filing Automation (Weeks 13–20)](#6-phase-2--filing-automation-weeks-1320)
7. [Phase 3 — Payment & Agent Economy (Weeks 21–28)](#7-phase-3--payment--agent-economy-weeks-2128)
8. [Phase 4 — Multi-Agent Network (Weeks 29–36)](#8-phase-4--multi-agent-network-weeks-2936)
9. [Phase 5 — Scale (Weeks 37–48)](#9-phase-5--scale-weeks-3748)
10. [Cross-Cutting: Security & Compliance Testing](#10-cross-cutting-security--compliance-testing)
11. [Cross-Cutting: PDPO & Data Governance](#11-cross-cutting-pdpo--data-governance)
12. [Phase Summary Table](#12-phase-summary-table)
13. [Open Risks & Protocol Dependencies](#13-open-risks--protocol-dependencies)

---

## 1. Repository Structure

Single **monorepo** at `hong-kong-company-secretary/`.

```
hong-kong-company-secretary/
├── apps/
│   ├── api/                  # FastAPI backend (Python 3.12)
│   │   ├── routers/          # One file per resource
│   │   ├── services/         # Business logic
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic I/O schemas
│   │   ├── middleware/       # Tenant context, auth, logging
│   │   └── tests/
│   │       ├── unit/
│   │       └── integration/
│   ├── web/                  # Next.js 15 dashboard (app.cosec.ai)
│   │   ├── app/              # App Router pages
│   │   ├── components/       # shadcn/ui + custom components
│   │   └── tests/            # Vitest + Playwright
│   ├── agent/                # OpenClaw per-tenant agent runtime
│   │   ├── personas/         # Agent system prompts + tool configs
│   │   └── services/         # Delegation, mandate checking
│   └── registry/             # A2A registry microservice (registry.cosec.ai)
│       ├── routers/
│       └── tests/
├── packages/
│   ├── rules-engine/         # Compliance calendar (pure Python, zero I/O)
│   │   ├── src/
│   │   │   ├── models.py     # CompanyFacts, StatutoryEvent (Pydantic)
│   │   │   ├── rules.yaml    # Deadline rules DSL
│   │   │   └── engine.py     # Calendar computation
│   │   └── tests/            # 200-case test pack
│   ├── mcp-servers/          # Individual MCP server processes
│   │   ├── mcp-icris/        # ICRIS BR lookup (Playwright scraper)
│   │   ├── mcp-ird/          # IRD eTAX integration
│   │   ├── mcp-whatsapp/     # Meta Cloud API + Twilio BSP
│   │   ├── mcp-fps/          # FPS reconciliation webhook handler
│   │   └── mcp-docstore/     # S3 document vault
│   └── shared-types/         # Pydantic models (Python) + generated TS types
│       ├── python/
│       └── typescript/       # Auto-generated from Pydantic via datamodel-code-generator
├── infra/
│   ├── docker/               # Compose files (dev, staging, prod-lite)
│   ├── ansible/              # Proxmox VM provisioning playbooks
│   └── k8s/                  # Helm charts (Phase 5, AWS ECS/Fargate migration)
├── tests/
│   ├── e2e/                  # Playwright full-stack E2E tests
│   ├── load/                 # k6 load test scripts
│   └── security/             # Bandit config, Trivy ignores
├── tools/
│   └── verify_audit_chain.py # Audit log integrity checker
├── docs/                     # All planning documents
└── .github/
    └── workflows/
        ├── ci.yml            # PR: lint, unit, contract, SAST, container scan
        ├── staging.yml       # push main: deploy staging + integration tests
        ├── prod.yml          # manual (one-click approve): deploy prod
        ├── load-test.yml     # manual: k6 against staging
        └── nightly.yml       # backup drill, security scan, uptime check
```

---

## 2. Tech Stack Decisions

| Layer | Choice | Rationale |
|---|---|---|
| Backend language | Python 3.12 | PRD requirement; Ronald's existing stack (Hermes) |
| Web framework | FastAPI | PRD requirement; async-native; auto OpenAPI |
| ORM / migrations | SQLAlchemy 2 (async) + Alembic | Async-capable; RLS-compatible via `execute()` |
| Data validation | Pydantic v2 | PRD requirement; used everywhere |
| Database | PostgreSQL 16 | PRD requirement; Row-Level Security per tenant |
| Cache / queue | Redis 7 | Idempotency keys, scheduler state, session tokens |
| Long-running workflows | APScheduler (MVP) → Temporal Cloud (200+ tenants) | PRD requirement; migrate path documented |
| Agent runtime | OpenClaw | Ronald's existing expertise; Hermes is built on it |
| Frontend | Next.js 15 (App Router) | PRD requirement |
| UI components | Tailwind CSS + shadcn/ui | PRD requirement |
| Auth | Clerk (managed) or Lucia (self-hosted) + WhatsApp OTP | PRD requirement; passkey / WebAuthn support |
| File storage | AWS S3 ap-east-1 with Object Lock | PRD requirement; legal hold; HK data residency |
| Secrets | HashiCorp Vault | PRD requirement |
| Headless browser | Playwright (Chromium) | PRD requirement for e-Registry bot |
| Email | Postmark | Transactional; reliable HK delivery |
| PDF generation | WeasyPrint + Jinja2 + Noto CJK fonts | PRD requirement; PDF/A-2b output |
| XML generation | lxml | NAR1 schema validation in CI |
| Mandate signing | Python `cryptography` (Ed25519) | AP2 spec; WebAuthn binding |
| CI/CD | GitHub Actions + Ansible + Docker | PRD requirement |
| Observability | Grafana Cloud Free + Prometheus + Loki + Sentry + OpenTelemetry + Better Stack | PRD requirement |
| Testing — Python | pytest + pytest-asyncio + httpx[async] | Standard FastAPI testing stack |
| Testing — TypeScript | Vitest + Playwright | Next.js standard |
| API contract testing | Schemathesis | Auto-tests all FastAPI routes against OpenAPI spec |
| Load testing | k6 | PRD requirement (Phase 5) |
| SAST — Python | Bandit | GitHub Actions, every PR |
| SAST — TypeScript | ESLint security plugin | GitHub Actions, every PR |
| Dependency scanning | pip-audit + npm audit | GitHub Actions, every PR |
| Container scanning | Trivy | GitHub Actions, every image build |
| KYC (Phase 5) | SumSub | PRD requirement; HK HKID support |

---

## 3. Testing Infrastructure

### 3.1 GitHub Actions Workflows

**`ci.yml`** — runs on every pull request:
1. Python lint: `ruff check` + `black --check`
2. TypeScript lint: `eslint` + `prettier --check`
3. Rules engine unit tests: `pytest packages/rules-engine/tests/ -v --cov --cov-fail-under=100`
4. API unit tests: `pytest apps/api/tests/unit/ -v --cov --cov-fail-under=90`
5. Registry unit tests: `pytest apps/registry/tests/ -v`
6. Web unit tests: `cd apps/web && vitest run`
7. API contract tests: `schemathesis run openapi.json --stateful=links --checks all`
8. SAST: `bandit -r apps/ packages/ -ll` + ESLint security
9. Dependency scan: `pip-audit` + `npm audit --audit-level=high`
10. Container scan: `trivy image cosec-api:$SHA`

**`staging.yml`** — runs on push to `main`:
1. Build and push Docker images
2. Ansible deploy to staging VM
3. Integration test suite: `pytest apps/api/tests/integration/ -v` (requires live DB + Redis)
4. Playwright E2E smoke: `playwright test --project=chromium tests/e2e/smoke/`

**`prod.yml`** — manual trigger with one-click approval gate:
1. Same build as staging
2. Ansible deploy to production VM
3. Post-deploy smoke test against prod

**`load-test.yml`** — manual trigger, runs against staging:
1. `k6 run tests/load/5k-tenants.js --vus=5000 --duration=20m`

**`nightly.yml`** — runs at 02:00 HKT:
1. Backup/restore drill: snapshot DB → restore to temp schema → verify row counts
2. Audit chain verification: `python tools/verify_audit_chain.py`
3. Security scan: Trivy on latest prod image
4. Better Stack uptime check assertion

### 3.2 Test Execution Reference

| Suite | Command | Environment |
|---|---|---|
| Rules engine | `pytest packages/rules-engine/tests/ -v --cov` | Local / CI |
| API unit | `pytest apps/api/tests/unit/ -v --cov` | Local / CI |
| API integration | `pytest apps/api/tests/integration/ -v` | CI staging (Docker Compose) |
| API contract | `schemathesis run http://localhost:8000/openapi.json --stateful=links` | CI staging |
| Web unit | `cd apps/web && vitest run` | Local / CI |
| E2E smoke | `playwright test tests/e2e/smoke/` | CI staging |
| E2E full | `playwright test tests/e2e/` | Manual / pre-release |
| Load | `k6 run tests/load/5k-tenants.js` | Manual / staging |
| Audit chain | `python tools/verify_audit_chain.py` | Nightly |

### 3.3 Coverage Targets

| Package | Target |
|---|---|
| `packages/rules-engine` | 100% branch coverage (core IP) |
| `apps/api` — services layer | ≥ 90% |
| `apps/api` — routers | ≥ 85% (contract tests cover the rest) |
| `apps/web` — utility functions | ≥ 80% |

---

## 4. Phase 0 — Foundation (Weeks 1–4)

### 4.1 Goal

Legal vehicle live, infrastructure baseline running, Hermes knowledge base ported to structured rules.

### 4.2 Implementation Tasks

#### Legal & Business (Ronald, sequential)

| Task | What | Key Output |
|---|---|---|
| TASK-001 | Incorporate CoSec.ai Ltd via e-Registry (HK$1,545 electronic) | CI number, BRC, ZA Bank or HSBC BIB account |
| TASK-002 | Trademark filing — "CoSec.ai" word mark + logo (Classes 9, 35, 42) via IPD HK e-filing | Filing receipt; docket in Notion |
| TASK-003 | Professional indemnity insurance HK$5M (MSIG HK or AXA; budget HK$12K–25K/yr) | Certificate of insurance on file |
| TASK-004 | PDPO baseline — appoint DPO (Ronald), draft privacy policy + DPIA template | Privacy policy published at `cosec.ai/privacy`; DPIA template in `/legal` |
| TASK-005 | TCSP licensing opinion (Stevenson Wong / ONC / Deacons; budget HK$40K) | Written opinion; follow-up actions logged |
| TASK-064 | TVP grant application (up to HK$600K at 75% funding ratio) | Application submitted |
| TASK-065 | Cyberport Incubation application (up to HK$500K + office over 24 months) | Application submitted |

#### Infrastructure (Ronald + Freelancer-Dev, parallelisable after TASK-006)

**TASK-006 — Domain & email setup**

- Register `cosec.ai` on Cloudflare Registrar (backup: `cosec.hk`)
- Subdomains on Cloudflare: `app.cosec.ai`, `api.cosec.ai`, `registry.cosec.ai`
- Google Workspace: MX records, SPF (`v=spf1 include:_spf.google.com ~all`), DKIM, DMARC (`p=quarantine`)
- Wildcard subdomain: `*.cosec.ai` → proxied to API (for per-tenant agent cards)

**TASK-007 — Shared infrastructure accounts**

- AWS: create Organization with separate `staging` and `prod` accounts under `ap-east-1`
- Enable AWS SSO via Google Workspace IdP
- GitHub org: enable 2FA mandatory + branch protection on `main`
- 1Password Business: vault per team role (dev, ops, finance)

**TASK-008 — Harden Proxmox MVP VM**

```
# Reuse existing Hermes VM; clean install Ubuntu 24.04 LTS
# Tailscale-only SSH (disable password auth, disable public SSH port)
# Caddy reverse proxy with auto-TLS (HTTPS for all subdomains)
# Docker Engine + Docker Compose v2
# systemd units for each service (api, web, agent, registry, redis, postgres)
```

**TASK-009 — CI/CD pipeline**

GitHub Actions workflows as described in §3.1. Ansible playbook (`infra/ansible/deploy.yml`) handles:
- `docker pull` latest image
- `docker compose up -d --no-deps <service>`
- Health check polling before marking deploy complete
- Rollback: re-pull previous tag if health check fails

**TASK-010 — Observability stack**

- Grafana Cloud Free tier: Loki (logs), Prometheus (metrics), Tempo (traces)
- OpenTelemetry Collector sidecar in Docker Compose
- Sentry DSN set for FastAPI (Python SDK) and Next.js (browser + server)
- Better Stack uptime monitor for `api.cosec.ai/health`, `app.cosec.ai`, `registry.cosec.ai`
- Alert targets: PagerDuty (or Better Stack on-call) for P0 alerts

**TASK-011 — Port Hermes knowledge base**

Extract from existing Hermes 6-file knowledge base:

1. Deadline rules → `packages/rules-engine/src/rules.yaml`

```yaml
# Example structure
nar1:
  description: Annual Return (NAR1)
  return_date: incorporation_anniversary
  deadline_offset_days: 42
  escalation_tiers:
    - months: 3
      fee_hkd: 870
    - months: 6
      fee_hkd: 1740
    - months: 9
      fee_hkd: 2610
    - months: 9
      fee_hkd: 3480
      tier_label: "9+ months"
  base_fee_hkd: 105
```

2. Compliance Q&A → Postgres `knowledge_qa` table (question, answer, tags, source_citation)
3. Build 100-scenario regression test pack at `packages/rules-engine/tests/test_scenarios.py`

**TASK-012 — Brand identity**

Freelancer-Design (Dribbble HK). Deliverables: logo SVG (light + dark), brand guide PDF, Figma component library. Tone: trustworthy, quiet competence.

### 4.3 Testing (Phase 0)

| What | Command / Method | Pass Criteria |
|---|---|---|
| VM uptime | Better Stack monitor; 7-day soak test | 100% uptime (zero alerts) |
| CI/CD pipeline | Push trivial commit → verify staging deploys; push tagged release → verify prod gate prompts | Both flows complete within 10 min |
| Hermes rules regression | `pytest packages/rules-engine/tests/ -v` | 100/100 green |
| TLS + domain | `curl -Iv https://cosec.ai` and all subdomains | HTTP 200; TLS 1.3; `Strict-Transport-Security` header present |
| Docker baseline | `docker compose -f infra/docker/dev.yml up` | All services start; all health checks pass within 60s |

### 4.4 Quality Gate 0

- [ ] CI number issued and BRC received
- [ ] VM passes 7-day uptime soak
- [ ] Hermes rules corpus ported: 100/100 regression tests green
- [ ] Trademark application filed
- [ ] PDPO privacy policy published

---

## 5. Phase 1 — Core MVP (Weeks 5–12)

### 5.1 Goal

Single-tenant-capable agent that tracks statutory deadlines and messages the director on WhatsApp.

### 5.2 Implementation Tasks

#### TASK-013 — PostgreSQL schema + Alembic migrations (`apps/api/`)

Implement all entities from PRD §1.8. Key implementation notes:

**Row-Level Security (RLS):**

```sql
-- Enable RLS on every tenant-scoped table
ALTER TABLE companies ENABLE ROW LEVEL SECURITY;
ALTER TABLE directors ENABLE ROW LEVEL SECURITY;
-- ... (all tables with company_id)

-- Policy: each request sets the tenant context
CREATE POLICY tenant_isolation ON companies
  USING (id = current_setting('app.tenant_id', true)::uuid);

-- For child tables:
CREATE POLICY tenant_isolation ON directors
  USING (company_id = current_setting('app.tenant_id', true)::uuid);
```

**Middleware** (`apps/api/middleware/tenant.py`): On each request, extract `company_id` from JWT claims → run `SET LOCAL app.tenant_id = ?` inside the SQLAlchemy session. Operator/admin role bypasses RLS via a separate Postgres role.

**Migration naming convention:** `YYYYMMDDHHMMSS_description.py`

#### TASK-014 — Compliance rules engine (`packages/rules-engine/`)

Pure-Python library. Zero I/O, zero DB calls. Import and test in isolation.

**Interface:**

```python
# packages/rules-engine/src/engine.py

from rules_engine.models import CompanyFacts, StatutoryEvent

def compute_calendar(facts: CompanyFacts, months_ahead: int = 24) -> list[StatutoryEvent]:
    """Return all statutory events for the next N months, sorted by due_date."""
    ...
```

**`CompanyFacts` fields:** `incorporation_date`, `financial_year_end` (month), `brc_choice` (1yr | 3yr), `is_private_company`, `has_employees`, `ptr_code` (N | D | M), `ptr_issue_date` (optional).

**`StatutoryEvent` fields:** `event_type`, `form_name`, `due_date`, `fee_hkd`, `escalation_tiers`, `description_en`, `description_zh`.

**PRD acceptance criteria test** (must be in test pack):
```python
# incorporation_date = 2023-03-15
# Expected:
# NAR1 return date = 2026-03-15
# NAR1 deadline = 2026-04-26 (return_date + 42 days)
# BRC expiry = 2026-03-15
# Escalation tiers: 2026-04-27, 2026-06-16, 2026-09-15, 2026-12-15
```

**Edge cases to cover in 200-case test pack:**
- Leap year: incorporation on Feb 29 → return date calculation
- FY-end change mid-year → AGM recalculation
- Private vs public company distinction
- PTR block extension codes (N, D, M)
- eTAX electronic +3-month extension
- Company with no employees (skip BIR56A)
- 1yr vs 3yr BRC choice
- Early AGM filed
- Multiple directors changing in same window

#### TASK-015 — ICRIS BR lookup (`packages/mcp-servers/mcp-icris/`)

Playwright-based stateless MCP server.

```python
# Cache key: f"icris:br:{br_number}"
# Cache TTL: 86400 seconds (24 hours)
# Rate limit: 1 request per 5 seconds per IP (Redis token bucket)
# Retries: 3 attempts with exponential backoff (1s, 2s, 4s) + jitter
```

Returns: `LegalName` (EN + ZH), `CINumber`, `IncorporationDate`, `RegisteredOffice`, `Directors[]`, `CompanyType`, `Status`.

Store raw HTML snapshot in S3 for audit (`icris-snapshots-{date}/{br_number}.html`).

#### TASK-016 — FastAPI skeleton + RLS + JWT auth (`apps/api/`)

```
apps/api/
├── main.py              # App factory; mounts all routers; registers middleware
├── routers/
│   ├── auth.py          # POST /auth/token, POST /auth/refresh
│   ├── companies.py     # POST /companies, GET /companies/{id}/calendar
│   ├── directors.py     # POST /companies/{id}/directors, DELETE ...
│   ├── filings.py       # GET /filings, POST /filings/{id}/approve
│   ├── mandates.py      # POST /mandates, GET /mandates/{id}/verify
│   ├── wallets.py       # POST /wallets/{id}/top-up
│   ├── a2a.py           # POST /a2a/delegate, GET /.well-known/agent-card.json
│   └── webhooks.py      # POST /webhooks/whatsapp, POST /webhooks/fps
├── middleware/
│   ├── tenant.py        # SET LOCAL app.tenant_id per request
│   └── logging.py       # Structured JSON logs → Loki
├── services/            # Business logic (called by routers)
├── models/              # SQLAlchemy async models
└── schemas/             # Pydantic v2 request/response schemas
```

JWT: RS256 (asymmetric). Key pair generated at startup if absent; rotated every 90 days. Access token TTL: 15 minutes. Refresh token TTL: 30 days (stored in `HttpOnly` cookie).

#### TASK-017 — WhatsApp Cloud API (`packages/mcp-servers/mcp-whatsapp/`)

**Webhook handler** (`POST /webhooks/whatsapp`):
1. Verify `X-Hub-Signature-256` HMAC header against `WHATSAPP_APP_SECRET`
2. Parse message payload; route to OpenClaw agent via internal API
3. Return HTTP 200 within 2 seconds (async; offload processing to queue)

**Three utility templates to pre-approve with Meta:**

| Template Name | Variables | When Sent |
|---|---|---|
| `cosec_reminder_n_days` | `{{company_name}}`, `{{deadline_date}}`, `{{filing_type}}`, `{{days_remaining}}`, `{{approval_url}}` | 30 / 14 / 7 days before deadline |
| `cosec_approval_request` | `{{company_name}}`, `{{filing_type}}`, `{{fee_hkd}}`, `{{approval_url}}` | Day of approval request |
| `cosec_filing_confirmed` | `{{company_name}}`, `{{filing_type}}`, `{{filed_date}}`, `{{receipt_url}}` | On confirmed filing |

Twilio BSP configured as fallback (same template names, BSP prefix). Auto-switch if Meta Cloud API returns 5xx three times in 60 seconds.

#### TASK-018 — Notification scheduler (`apps/api/services/scheduler.py`)

```python
# APScheduler AsyncIOScheduler
# Job: check_upcoming_deadlines — runs every 10 minutes
# For each filing with status in (scheduled, drafted):
#   for offset_days in [30, 14, 7, 3, 1]:
#     if (due_date - today).days == offset_days:
#       key = f"notif:{company_id}:{filing_id}:{offset_days}"
#       if not redis.exists(key):
#         send_whatsapp(template, company_id, filing_id, offset_days)
#         redis.setex(key, 172800, "sent")  # 48h TTL
```

Escalation logic:
- 7 days: if no read-receipt within 24h → also send SMS (Twilio)
- 3 days: Twilio Voice TTS call (text-to-speech; director's registered phone)
- 1 day: also send email via Postmark to director + backup email
- Day of: if AP2 Intent Mandate active and fee ≤ ceiling → proceed autonomously; else hold + alert

Migration to Temporal Cloud at 200+ tenants: wrap each notification send in a Temporal activity; the `check_upcoming_deadlines` job becomes a Temporal workflow. Interface is identical to scheduler.

#### TASK-019 — Web onboarding flow (`apps/web/`)

Next.js 15 App Router. Route: `/onboard`.

**Onboarding steps (single-page wizard):**
1. Enter BR number → validate format (8 digits)
2. ICRIS lookup (show spinner; poll `/companies/lookup?br={br}`)
3. Confirm pre-filled company profile (legal name EN/ZH, incorporation date, registered office)
4. Enter director WhatsApp number → send OTP via Twilio Verify
5. Verify OTP → create account
6. Sign AP2 Intent Mandate (Phase 3; shown as "skip for now" in Phase 1)
7. Show compliance calendar

Mobile-first: all forms work on 390px viewport. Tailwind CSS breakpoints. shadcn/ui `Form`, `Input`, `Button`, `Calendar` components.

#### TASK-020 — OpenClaw compliance-calendar agent (`apps/agent/`)

Per-tenant OpenClaw agent instance. Shared runtime, per-tenant config.

**System prompt template** (`apps/agent/personas/cosec_calendar.md`):
```
You are the CoSec.ai compliance agent for {company_name} (BR: {br_number}).
Your role: remind the director of statutory deadlines, answer compliance questions,
and guide them through form approvals. Always be concise and direct.
Company incorporation date: {incorporation_date}
Next filing: {next_event_type} due {next_event_date} (fee: HK${next_event_fee})
```

**Tool calls:**
- `get_compliance_calendar(company_id)` → calls rules engine via API
- `send_whatsapp_message(to, template, variables)` → calls mcp-whatsapp
- `get_document(document_id)` → calls mcp-docstore (S3)
- `query_company_profile(company_id)` → calls API `/companies/{id}`
- `get_approval_status(filing_id)` → calls API `/filings/{id}`

#### TASK-021 — Internal ops console (Retool)

Tables and actions:
- **KYC queue**: list pending companies; button "Approve" / "Reject with reason"; audit log written on each action. Target: approve in < 60 seconds.
- **Filings**: list all filings by status; filter by date range; link to receipt.
- **Notifications log**: view sent notifications; resend button for failed deliveries.

All operator actions write to `AuditLog` with `actor = operator:{email}`.

#### TASK-022 — Friendly beta: 5 companies

Ronald onboards 5 companies from personal network. Offer 12 months free. Monitor for 14 days.

### 5.3 Testing (Phase 1)

| What | Command | Pass Criteria |
|---|---|---|
| Rules engine unit tests | `pytest packages/rules-engine/tests/ -v --cov --cov-fail-under=100` | 200/200 green; 100% branch coverage |
| PRD acceptance criteria | Specific test: `test_prd_acceptance_nar1_2023_03_15` | Exact date match on all 6 expected events |
| Leap year: Feb 29 | `test_leap_year_feb29_incorporation` | NAR1 return date = Feb 28 in non-leap years |
| API contract tests | `schemathesis run http://localhost:8000/openapi.json --stateful=links --checks all` | No schema violations; no unhandled 500s |
| RLS isolation | `test_rls_cross_tenant_isolation`: create 2 companies; query from each JWT; assert no cross-tenant rows | Zero cross-tenant data leakage |
| WhatsApp webhook HMAC | Replay 10 sample payloads (5 valid, 5 tampered signatures) | 5 accepted; 5 return HTTP 403 |
| Notification idempotency soak | Mock clock; advance 30 days; assert each `{company_id}:{filing_id}:{offset}` key SET exactly once | Zero duplicates over 30-day window |
| ICRIS scraper | Feed 20 test BR numbers (including: dissolved company, multi-director, Chinese-name-only company) | 20/20 return correct structured data |
| Agent response accuracy | 10 natural-language queries to OpenClaw agent; compare with expected responses | ≥ 9/10 correct and actionable |
| Beta gate | 5 companies monitored for 14 days | 5/5 receive correct 30-day reminder; 0 false positives; 0 false negatives |

### 5.4 Quality Gate 1

- [ ] 5 beta companies run 14 days; rules engine precision/recall ≥ 98% on real data
- [ ] WhatsApp cost per company < HK$5/month
- [ ] 200-case rules test pack green
- [ ] API OpenAPI spec published and contract tests passing

---

## 6. Phase 2 — Filing Automation (Weeks 13–20)

### 6.1 Goal

Prepare and submit an NAR1 end-to-end with human approval: draft → approve → file → receipt.

### 6.2 Implementation Tasks

#### TASK-023 — NAR1 XML generator (`apps/api/services/filing/nar1_generator.py`)

1. Download latest NAR1 XML schema from Companies Registry and store at `packages/shared-types/schemas/cr/nar1_v{N}.xsd`
2. Schema version pinned in `config.py`; version checked on startup; alert if mismatch
3. Generator: `generate_nar1_xml(company_id: UUID, filing_id: UUID) -> bytes`
4. Calls: `Company`, all `Directors`, all `Shareholders`, `RegisteredOffice`, `CompanySecretary`
5. Produces XML; validates with `lxml.etree.XMLSchema`
6. On validation error: log field path + value; surface to operator dashboard with plain-English fix suggestion
7. Schema validation runs in CI on every PR against 10 fixture companies

#### TASK-024 — NAR1 PDF renderer (`apps/api/services/filing/nar1_pdf.py`)

- WeasyPrint + Jinja2 HTML template
- Fonts: Noto Sans CJK TC (Traditional Chinese), Noto Sans (English) — embed in PDF
- Output: PDF/A-2b compliant
- Template pixel-matched to official CR NAR1 layout (verify using PDF screenshot diff)
- Called as: `render_nar1_pdf(xml_bytes: bytes) -> bytes`

#### TASK-025 — Year-over-year diff engine (`apps/api/services/filing/diff_engine.py`)

```python
def compute_diff(current: CompanySnapshot, prior: CompanySnapshot) -> DiffResult:
    """
    DiffResult:
      directors_added: list[Director]
      directors_removed: list[Director]
      directors_changed: list[DirectorDelta]
      shareholders_changed: list[ShareholderDelta]
      registered_office_changed: bool
      has_changes: bool  # False → "No changes vs prior year" badge
    """
```

`CompanySnapshot` is serialised to `Filing.snapshot_json` at the time of NAR1 draft generation. Prior snapshot loaded from last year's `Filing` record.

#### TASK-026 — One-tap approval link flow

**Backend** (`apps/api/routers/filings.py`):

```
POST /filings/{id}/send-approval-link
  → generate JWT: { sub: director_whatsapp_number, aud: f"{company_id}:{filing_id}", exp: now+900 }
  → store token hash in Redis (key: f"approval_token:{hash}", TTL: 900s, value: "pending")
  → send WhatsApp cosec_approval_request template with URL
  → return { sent: true }

POST /filings/{id}/approve
  body: { token: str, webauthn_assertion: dict }
  → validate JWT (signature, expiry, audience)
  → check Redis key exists and value == "pending" (not "consumed")
  → verify WebAuthn assertion against stored credential for director
  → SET Redis key value = "consumed"
  → transition Filing.status = "approved"
  → enqueue submission job
  → return { status: "approved", submission_eta_seconds: 300 }
```

**Frontend** (`apps/web/app/approve/[token]/page.tsx`):
- Show PDF preview (PDF.js)
- Show diff report (colour-coded: green = added, red = removed, amber = changed)
- Show fee breakdown: filing fee (CR) + platform fee + total
- "Approve & File" button → triggers WebAuthn `navigator.credentials.get()` → POST to API
- "Request Change" button → comment field → POST to `/filings/{id}/request-change`

Security requirements:
- Token is single-use (consumed on first successful approval)
- Token is bound to director WhatsApp number (checked against company record)
- 15-minute TTL
- No filing ID or company data in the URL (only opaque token)

#### TASK-027 — Hash-chained audit log (`apps/api/services/audit.py`)

```python
def append_audit(
    entity_type: str,
    entity_id: UUID,
    actor: str,  # "director:{whatsapp_number}" | "operator:{email}" | "agent:{company_slug}"
    action: str,
    payload: dict,
    db: AsyncSession,
) -> AuditLog:
    prev = await db.execute(
        select(AuditLog).order_by(AuditLog.created_at.desc()).limit(1)
    )
    prev_hash = prev.scalar_one_or_none()?.hash or "genesis"
    payload_json = json.dumps(payload, sort_keys=True)
    new_hash = sha256(f"{prev_hash}|{payload_json}".encode()).hexdigest()
    record = AuditLog(
        entity_type=entity_type, entity_id=entity_id, actor=actor, action=action,
        payload_json=payload_json, prev_hash=prev_hash, hash=new_hash,
    )
    db.add(record)
    return record
```

Monthly: run `tools/verify_audit_chain.py` → compute Merkle root → publish to public GitHub Gist as tamper-evident public record.

#### TASK-028 — Playwright e-Registry submission bot (`apps/api/services/filing/eregistry_bot.py`)

```python
async def submit_nar1(company_id: UUID, filing_id: UUID, xml_bytes: bytes) -> ReceiptResult:
    # 1. Fetch e-Registry credentials from HashiCorp Vault
    creds = await vault.get_secret(f"eregistry/company/{company_id}")
    # 2. Launch Playwright headless Chromium
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # 3. Login, navigate to e-Filing, upload XML, confirm submission
        # 4. Capture stamped receipt PDF (screenshot or download)
        # 5. Return ReceiptResult(receipt_pdf_bytes, submission_reference, filed_at)
    # On failure after 3 retries → trigger email fallback (TASK-030) + PagerDuty alert
```

Credentials in HashiCorp Vault: path `secret/eregistry/{company_id}`, fields `username`, `password`, `delegation_code`. Credentials never logged; masked in Sentry breadcrumbs.

**Anti-fragile design:** if bot fails 3 times within 30 minutes, automatically:
1. Trigger email fallback flow (TASK-030)
2. Set `Filing.status = "fallback:email"`
3. Send PagerDuty page to on-call

#### TASK-029 — S3 receipt storage (`apps/api/services/storage.py`)

```python
# Bucket: cosec-receipts-prod (ap-east-1)
# Object Lock: governance mode, 7-year retention
# Key format: {company_id}/{filing_id}/{filing_type}_{filed_at}.pdf
# Tags: company_id, filing_id, filing_type, filed_at
# ACL: private (no public access)
# Pre-signed URL TTL for dashboard display: 3600 seconds
```

#### TASK-030 — Email fallback submission flow

Postmark template `filing_instructions`:
- Attached: pre-filled PDF NAR1
- Body: step-by-step instructions for manual e-Registry submission in English + Traditional Chinese
- CTA: "I have submitted this filing" → signed token URL → `POST /filings/{id}/confirm-self-filed`

`confirm-self-filed` endpoint:
- Validates token
- Sets `Filing.status = "filed:self-reported"`
- Sets `Filing.filed_at = now()`
- Appends audit log entry

#### TASK-031 — Failed-filing runbook (`docs/runbooks/failed-filing.md`)

Three documented failure modes:

1. **e-Registry bot timeout / UI change**
   - Detection: Playwright `TimeoutError` or element not found after 3 retries
   - Response: auto-trigger email fallback; PagerDuty page on-call
   - Fix: update bot selectors; re-test against staging CR account; re-run submission

2. **HashiCorp Vault credential expiry / rotation failure**
   - Detection: Vault returns 403; alert fires in Sentry
   - Response: auto-rotation script triggered; if script fails → PagerDuty escalation
   - Fix: manually rotate credentials in e-Registry portal; update Vault secret

3. **Receipt PDF not captured**
   - Detection: S3 object missing 10 minutes after `Filed` status set
   - Response: re-scrape e-Registry submission history for the reference number
   - Fix: manual download from e-Registry portal; upload to correct S3 path; update `Filing.receipt_url`

SLA: on-call must acknowledge within 30 minutes; resolve within 2 hours for same-day deadline filings.

### 6.3 Testing (Phase 2)

| What | Command / Method | Pass Criteria |
|---|---|---|
| NAR1 XML schema validation | CI job: `pytest apps/api/tests/unit/test_nar1_generator.py` — generates XML for 10 fixture companies; validates each against CR XSD | All 10 validate; zero schema violations |
| NAR1 XML round-trip | Parse generated XML back into dict; compare with source `Company` object | Zero field discrepancies |
| PDF pixel-parity | Generate PDF → `pdf2image` → `Pillow` SSIM comparison vs reference image | SSIM ≥ 0.99 on all tested pages |
| Diff engine | 8 parametrised test cases: no changes, director added, director removed, shareholder % changed, address changed, combined director + shareholder change, 3 new directors, empty prior year | 8/8 correct; `has_changes` flag matches expected |
| Approval token — valid flow | Integration test: generate token → approve within 15 min with valid WebAuthn → verify `status = approved` and median latency < 3s | Pass |
| Approval token — expired | Attempt approval with 20-min-old token | HTTP 401 |
| Approval token — reuse | Approve once successfully; attempt second approval with same token | HTTP 409 |
| Approval token — wrong director | Use token with a different director WhatsApp number | HTTP 403 |
| Audit chain — normal | Append 100 records; run `verify_audit_chain.py` | Reports chain valid |
| Audit chain — tamper | Mutate `payload_json` of record #50; run `verify_audit_chain.py` | Reports exactly 1 broken link at position 50 |
| e-Registry bot | Run against 3 CR staging/test companies | 3 successful submissions; 3 receipt PDFs captured in S3 |
| S3 Object Lock | Upload receipt; attempt `delete-object`; attempt `delete-object --version-id` | Both deletions rejected with `AccessDenied` |
| Receipt visibility | Upload receipt; check dashboard API returns pre-signed URL within 10 min | URL accessible; PDF renders |
| Email fallback | Trigger fallback flow; director clicks "I have submitted"; verify `status = filed:self-reported` | Status updated; audit log entry present |
| Backup/restore drill (TASK-070) | Full runbook execution: snapshot → restore → row count comparison | Restore completes in < 4h; row counts match |

### 6.4 Quality Gate 2

- [ ] 10 NAR1 filings land stamped; zero late; zero data errors
- [ ] Mean elapsed time "deadline trigger → stamped receipt" ≤ 72 hours
- [ ] No director complaints

---

## 7. Phase 3 — Payment & Agent Economy (Weeks 21–28)

### 7.1 Goal

ATXP wallet + AP2 mandates + FPS top-ups wired end-to-end; every filing fee paid autonomously.

### 7.2 Implementation Tasks

#### TASK-033 — ATXP wallet provisioning (`apps/api/services/wallet.py`)

On company verification (KYC approved):

```python
async def provision_wallet(company_id: UUID) -> str:
    # Run: npx atxp agent register --non-interactive
    # Pass: company slug, platform credentials via env vars
    # Returns: wallet_address (DID or hex address)
    result = await run_subprocess(["npx", "atxp", "agent", "register", "--json"])
    wallet_address = json.loads(result.stdout)["address"]
    await db.execute(
        insert(AgentWallet).values(company_id=company_id, atxp_address=wallet_address, balance_hkd_cents=0)
    )
    return wallet_address
```

#### TASK-034 — LLM gateway with ATXP margin (`apps/api/services/llm_gateway.py`)

```python
# Routing:
#   Complexity score < 0.7 → Claude Haiku 4.5 (80% of traffic)
#   Complexity score ≥ 0.7 → Claude Sonnet 4.6 (20% of traffic)
#
# Per-call accounting:
#   raw_cost = input_tokens * model_input_rate + output_tokens * model_output_rate
#   platform_cost = raw_cost * 1.20  # 20% margin
#   debit_wallet(company_id, platform_cost, reason="llm_inference")
#
# ATXP gateway SDK routes the actual LLM call and handles nested payment
```

Per-tenant token usage tracked in `WalletTxn` with `reason = "llm_inference:{model}:{request_id}"`.

#### TASK-035 — FPS top-up flow (`packages/mcp-servers/mcp-fps/`)

Flow:
1. Director initiates top-up on dashboard → `POST /wallets/{id}/initiate-topup` → returns unique FPS reference (12-char alphanumeric, stored in Redis with 24h TTL)
2. Director sends HKD via FPS to CoSec omnibus account using the reference
3. ZA Bank webhook fires `POST /webhooks/fps` with transaction details
4. Match FPS reference → company wallet; verify amount ≥ minimum (HK$100)
5. Credit `AgentWallet.balance_hkd_cents` by `amount * 0.995` (deduct 0.5% funding fee)
6. Write `WalletTxn` (credit, signed, timestamped)
7. Push WhatsApp `cosec_wallet_topped_up` notification

**Fallback:** HSBC Business Banking API if ZA Bank API is unavailable. Manual reconciliation: nightly job checks FPS transactions against unmatched references.

#### TASK-036 — AP2 Intent Mandate signer (`apps/api/services/mandates.py`)

**Mandate creation flow:**
1. Director opens mandate setup page
2. Selects ceiling (default HK$5,000) and aggregate cap (default HK$30,000) and validity period (default 12 months)
3. "Sign Mandate" button triggers `navigator.credentials.get()` (WebAuthn passkey)
4. Frontend sends: `{ mandate_payload_json, webauthn_assertion }` to `POST /mandates`
5. Backend constructs AP2 Intent Mandate JWS:

```json
{
  "iss": "https://cosec.ai",
  "sub": "did:cosec:{company_slug}",
  "aud": "https://api.cosec.ai",
  "iat": 1234567890,
  "exp": 1266103890,
  "mandate_type": "intent",
  "ceiling_hkd": 5000,
  "aggregate_cap_hkd": 30000,
  "purpose": "hongkong_government_filing_fees",
  "valid_until": "2027-04-18"
}
```

6. Sign JWS with company's Ed25519 key pair (generated per-tenant at provisioning)
7. Store in `Mandate` table
8. Return `{ mandate_id, verification_url }`

**Public verification endpoint:** `GET /mandates/{id}/verify` — fetches mandate, verifies JWS signature, returns `{ valid: bool, remaining_headroom_hkd: float, expires_at: datetime }`.

**Revocation:** `DELETE /mandates/{id}` — director re-authenticates with WebAuthn; sets `Mandate.revoked_at = now()`; signs revocation notice and propagates to dependent agents via A2A events.

#### TASK-037 — AP2 Payment Mandate (per-transaction)

Triggered when `filing.fee_hkd > active_intent_mandate.ceiling_hkd`.

One-tap WhatsApp CTA → approval page showing:
- Filing type and description
- Exact fee amount
- "This payment exceeds your pre-approved ceiling of HK${ceiling}"
- "Approve this one-time payment" → WebAuthn sign → `POST /mandates` with `mandate_type=payment`, single-use, expires in 30 minutes.

#### TASK-038 — Autonomous filing fee payment

```python
async def execute_filing_payment(filing_id: UUID) -> PaymentResult:
    filing = await get_filing(filing_id)
    mandate = await get_active_intent_mandate(filing.company_id)

    if mandate and filing.fee_hkd <= mandate.ceiling_hkd:
        remaining = mandate.aggregate_cap_hkd - mandate.used_hkd
        if filing.fee_hkd <= remaining:
            await debit_wallet(filing.company_id, filing.fee_hkd + filing.platform_fee_hkd, mandate_id=mandate.id)
            await append_audit(..., action="autonomous_payment", payload={"mandate_ref": mandate.id, "fee_hkd": filing.fee_hkd})
            return PaymentResult(autonomous=True)

    # Fee exceeds ceiling or aggregate cap exhausted → request Payment Mandate
    await request_payment_mandate(filing_id)
    return PaymentResult(autonomous=False, mandate_request_sent=True)
```

#### TASK-041 — Stripe Billing (`apps/api/services/billing.py`)

Stripe Products:
1. `cosec_saas_starter` (HK$200/month) — ≤3 companies
2. `cosec_saas_growth` (HK$400/month) — 4–20 companies
3. `cosec_saas_pro` (HK$600/month) — 21+ companies
4. `cosec_filing_fee` — usage-based metered price (HK$50–200 per filing)

Invoice generation: Stripe Billing handles subscription renewals monthly. Filing fees added as usage records via `stripe.SubscriptionItem.create_usage_record`. Tax: HK has no GST/VAT — set Stripe tax config to `tax_behavior: inclusive` with HK tax rate 0%.

### 7.3 Testing (Phase 3)

| What | Command / Method | Pass Criteria |
|---|---|---|
| Wallet debit — normal | `test_wallet_debit_within_balance`: debit HK$100 from HK$500 balance → balance = HK$400 | Pass |
| Wallet debit — insufficient funds | `test_wallet_debit_insufficient`: debit HK$600 from HK$500 balance → raises `InsufficientFundsError` | Correct error; no partial debit |
| Wallet debit — concurrent | `test_wallet_concurrent_debits`: 10 concurrent debits of HK$50 from HK$500 balance → final balance = HK$0, not negative | Serialised via Postgres `SELECT FOR UPDATE`; exactly 10 debits succeed |
| ATXP provisioning | Provision 3 test wallets; verify addresses in DB and dashboard | 3/3 addresses present and non-null |
| FPS reconciliation | Mock ZA Bank webhook: 5 valid FPS transactions, 1 wrong reference, 1 duplicate, 1 zero amount, 1 exceeds max | 5 correctly credited; 4 edge cases handled without crediting |
| AP2 mandate — create and verify | Create mandate → call `GET /mandates/{id}/verify` | Returns `valid: true` |
| AP2 mandate — tamper | Create mandate → mutate `ceiling_hkd` in DB → call verify | Returns `valid: false` (signature mismatch) |
| AP2 mandate — revoke | Revoke mandate → attempt payment → rejected | Payment rejected; `revoked_at` set |
| Intent ceiling enforcement | File HK$105 NAR1 against ceiling-5000 mandate → autonomous. File HK$6,020 BRC → Payment Mandate requested. | Both paths taken correctly |
| Aggregate cap enforcement | Spend HK$25,000 aggregate; attempt HK$6,000 more → blocked | Blocked; Payment Mandate requested |
| LLM gateway margin | Send 100 requests; compare wallet debits vs raw API costs | 20% margin captured (±1%) |
| Stripe billing | Create test subscription; simulate month rollover via Stripe test clock; verify invoice | Line items correct: SaaS fee + filing usage |
| External penetration test (TASK-069) | Vendor scope: API auth bypass, mandate forgery, wallet manipulation, RLS bypass, injection | Clean re-test; zero critical or high findings |

### 7.4 Quality Gate 3

- [ ] Unit economics for 10 companies match Document 5 model within ±10%
- [ ] 10 end-to-end wallet-funded filings completed
- [ ] Pentest clean re-test certificate

---

## 8. Phase 4 — Multi-Agent Network (Weeks 29–36)

### 8.1 Goal

Platform and per-tenant Agent Cards published; A2A registry live; outbound delegation to accounting/legal agents working.

### 8.2 Implementation Tasks

#### TASK-043 — Platform Agent Card + JWKS (`apps/api/routers/a2a.py`)

**Agent Card structure** (per A2A spec):

```json
{
  "name": "CoSec.ai Company Secretary Platform",
  "description": "Automated HK statutory compliance: NAR1, BRC, PTR, SCR, Employer's Return",
  "url": "https://cosec.ai",
  "version": "1.0.0",
  "capabilities": [
    { "id": "cosec.hk.compliance_calendar", "description": "Generate 24-month statutory compliance calendar" },
    { "id": "cosec.hk.nar1_preparation", "description": "Prepare and file Annual Return (NAR1)" },
    { "id": "cosec.hk.brc_renewal", "description": "Prepare and file BRC renewal" },
    { "id": "cosec.hk.scr_maintenance", "description": "Maintain Significant Controllers Register" }
  ],
  "authentication": { "type": "bearer", "scheme": "JWT", "jwks_uri": "https://cosec.ai/.well-known/jwks.json" }
}
```

Signed as JWS (compact serialization) with platform Ed25519 key.

**Key rotation script** (`tools/rotate_agent_card_keys.py`):
1. Generate new Ed25519 keypair
2. Add to JWKS (keep old key for 24h overlap window)
3. Re-sign all Agent Cards (platform + all tenant cards)
4. Update `CURRENT_SIGNING_KEY_ID` in config
5. After 24h: remove old key from JWKS
6. Run as cron job every 90 days; send Slack/email notification on completion

#### TASK-044 — Per-tenant Agent Card

Dynamic route: `GET https://{slug}.cosec.ai/.well-known/agent-card.json`

Caddy wildcard: `*.cosec.ai` proxied to API. API extracts `slug` from `Host` header, looks up company, generates and signs tenant-specific card.

Tenant card includes company-specific subset of capabilities, plus `sub` = `did:cosec:{slug}`.

#### TASK-045 — A2A registry service (`apps/registry/`)

FastAPI microservice at `registry.cosec.ai`.

**Endpoints:**

```
POST /agents
  body: { agent_card_jws: str }
  → validate JWS signature using JWKS from agent_card.authentication.jwks_uri
  → extract capabilities, name, url, did
  → insert into registered_agents (if new) or upsert (if same DID)
  → return { agent_id, registered_at }

GET /agents?capability=tax.hongkong.profits_tax_filing&limit=10
  → full-text search on capabilities JSON array
  → return list sorted by rating desc, response_time_ms asc

GET /agents/{did}
  → return latest agent card JWS for the DID

DELETE /agents/{did}
  → must present signed ownership proof (JWS with same key as the card)
```

Rate limiting: 100 requests/minute per IP (Redis sliding window). Abuse prevention: require `domain_verified: true` for cards to appear in search results (DNS TXT record verification).

#### TASK-046 — HK compliance capability taxonomy

Namespace: `cosec.hk.*`

```yaml
cosec.hk.compliance_calendar:   "Generate HK statutory compliance calendar"
cosec.hk.nar1_preparation:      "Prepare Annual Return (NAR1)"
cosec.hk.nar1_filing:           "File Annual Return with Companies Registry"
cosec.hk.brc_renewal:           "Renew Business Registration Certificate"
cosec.hk.nd2a_filing:           "File director change notification (ND2A)"
cosec.hk.scr_maintenance:       "Maintain Significant Controllers Register"
tax.hongkong.profits_tax_filing: "File Profits Tax Return (BIR51/52/54)"
tax.hongkong.employer_return:    "File Employer's Return (BIR56A + IR56B)"
legal.hongkong.director_deed:    "Draft director resignation deed"
legal.hongkong.board_resolution: "Draft board resolution"
```

Published to GitHub (`docs/capability-taxonomy.md`) and `registry.cosec.ai/taxonomy`.

#### TASK-047 — Outbound delegation engine (`apps/agent/services/delegation.py`)

```python
async def delegate_task(
    from_company_id: UUID,
    capability: str,
    task_description: str,
    context_url: str,
    fee_cap_hkd: Decimal,
    mandate_id: UUID,
) -> DelegationResult:
    # 1. Query registry for capability
    candidates = await registry_client.search(capability=capability, limit=5)
    # 2. Filter by: valid JWS signature, rating ≥ 4.0, fee_cap within range
    # 3. Present shortlist to director (WhatsApp + web)
    # 4. On director approval (AP2 mandate):
    #    POST to partner agent JSON-RPC endpoint:
    #    { jsonrpc: "2.0", method: "execute_task",
    #      params: { capability, context_url, fee_cap_hkd, mandate_jws } }
    # 5. Poll for result (exponential backoff, max 24h)
    # 6. On success: debit 10–15% referral fee; store AgentDelegation record
```

#### TASK-051 — Secretarial firm agency-mode dashboard (`apps/web/app/agency/`)

**New Postgres table:** `agency_memberships (agency_user_id, company_id, role)`

**RLS extension:** agency users can read (but not write) companies in their `agency_memberships`.

**Dashboard features:**
- Overview table: all N companies, columns: urgency indicator, company name, next deadline, filing status, wallet balance
- Bulk acknowledge: mark multiple reminder notifications as reviewed
- Per-firm white-label: `agency_settings (agency_id, logo_url, brand_color, custom_domain)`

### 8.3 Testing (Phase 4)

| What | Command / Method | Pass Criteria |
|---|---|---|
| Agent Card signature | Fetch card; verify JWS using JWKS endpoint | Valid |
| Agent Card tamper | Mutate one field in card; re-verify | Returns invalid |
| JWKS rotation | Run rotation script; verify old key valid during 24h window; verify old key rejected after 24h | Both assertions pass |
| A2A registry CRUD | Register 5 test cards; search by each capability; deregister one | All operations correct; deregistered card not in search results |
| Outbound delegation — mock partner | Point delegation engine at wiremock JSON-RPC stub; verify discovery → shortlist → hand-off → result capture | Full flow; fee deducted |
| Referral fee accounting | 3 mock delegations at HK$1,000 each; verify 10–15% deducted from settlement | Amounts within ±1 HKD |
| Agency-mode RLS | Log in as agency user; verify she sees exactly her N companies and no others | Zero cross-agency data leakage |
| Per-tenant Agent Card | Request `{slug}.cosec.ai/.well-known/agent-card.json` for 10 tenant slugs | All return HTTP 200 with valid signed JWS |
| Live A2A hand-offs (TASK-052) | 5 real delegations to ≥1 live partner accounting agent | 5/5 signed cards, task URLs, fee caps, receipts captured |

### 8.4 Quality Gate 4

- [ ] 5 successful A2A hand-offs with signed cards, task URLs, fee caps, and receipts
- [ ] ≥1 partner-initiated inbound delegation received and fulfilled
- [ ] 3 partner agents (2 accounting + 1 law firm) listed in registry with verified cards

---

## 9. Phase 5 — Scale (Weeks 37–48)

### 9.1 Goal

Dashboard polish, self-serve onboarding with automated KYC, load-tested to 5,000 tenants, 50 paying companies.

### 9.2 Implementation Tasks

#### TASK-053 — Portfolio dashboard v2 (`apps/web/app/dashboard/`)

- TanStack Table with virtualised rows (handles 500+ companies without jitter)
- Server-side pagination: `GET /companies?page={n}&sort=urgency&order=asc`
- Urgency colour coding: red (due < 7 days), amber (7–30 days), green (> 30 days)
- Columns: company name, next filing type, due date, status, wallet balance, agent status
- Global search: company name or BR number (debounced 300ms)
- Performance target: TTI < 1.5s on 500-company dataset (measured via Playwright `performance.timing`)

#### TASK-054 — Self-serve onboarding v2

Revised onboarding funnel with analytics (PostHog):
```
Step 1: BR entry          [event: onboard_step_br_entered]
Step 2: Company confirmed [event: onboard_step_company_confirmed]
Step 3: KYC submitted     [event: onboard_step_kyc_submitted]
Step 4: Mandate signed    [event: onboard_step_mandate_signed]
Step 5: First reminder    [event: onboard_completed]
```

Funnel drop-off visible in PostHog. Target: median completion ≤ 12 minutes.

#### TASK-055 — SumSub automated KYC

SumSub SDK embedded in onboarding Step 3. Applicant submits HKID (front + selfie). SumSub webhook `applicant.reviewed`:
- `reviewResult.reviewAnswer == GREEN` → `company.kyc_status = verified`
- `reviewResult.reviewAnswer == RED` → `company.kyc_status = rejected`; send rejection reason via WhatsApp
- `reviewResult.reviewAnswer == PENDING` → queue for manual review in ops console

Target: 90% auto-approved. Budget: US$1.50–2.50/check.

#### TASK-057 — Public marketing site (`cosec.ai`)

Framer or Webflow. Pages: Home, Pricing, How It Works, Blog, Contact.

Core Web Vitals targets enforced via Lighthouse CI in GitHub Actions:
- LCP < 2.5s
- CLS < 0.1
- INP < 200ms

Localisation: English + Traditional Chinese (Framer/Webflow L10n feature).

#### TASK-059 — Load test (k6)

```javascript
// tests/load/5k-tenants.js
import http from "k6/http";
import { check } from "k6";

export const options = {
  stages: [
    { duration: "10m", target: 5000 },  // ramp up
    { duration: "20m", target: 5000 },  // steady state
    { duration: "5m",  target: 0 },     // ramp down
  ],
  thresholds: {
    "http_req_duration": ["p(95)<400"],  // p95 < 400ms
    "http_req_failed": ["rate<0.001"],   // error rate < 0.1%
  },
};

export default function () {
  const res = http.get(`${__ENV.API_URL}/companies/${randomCompanyId()}/calendar`, {
    headers: { Authorization: `Bearer ${__ENV.TEST_JWT}` },
  });
  check(res, { "status 200": (r) => r.status === 200 });
}
```

Pre-load staging DB with 5,000 synthetic tenant companies using `tools/seed_load_test.py`.

Migration to AWS ECS/Fargate triggered if load test reveals single-VM limitations. Helm charts in `infra/k8s/` ready for this migration.

#### TASK-058 — ISO 27001 readiness

Vanta or Drata auto-scan + manual control mapping. Ronald's CISSP informs the baseline. Target controls to close before year-end: A.8.2 (data classification), A.9.4 (access control), A.12.6 (patch management), A.13.2 (information transfer), A.16.1 (incident management). Year-2 certification plan documented in Notion.

### 9.3 Testing (Phase 5)

| What | Command / Method | Pass Criteria |
|---|---|---|
| Portfolio dashboard TTI | `playwright test tests/e2e/performance/dashboard-tti.spec.ts` — load 500-company dataset, measure TTI | TTI < 1.5s on Chromium |
| Onboarding E2E | `playwright test tests/e2e/onboarding/full-flow.spec.ts` — BR entry → KYC (mocked SumSub) → mandate signing → first reminder fires | Median < 12 min; zero broken steps |
| SumSub auto-approval | Submit 20 test KYC applications to SumSub sandbox (15 pass, 5 fail) | 15 verified, 5 rejected; webhook correctly updates `kyc_status` |
| Core Web Vitals | Lighthouse CI: `lighthouse https://cosec.ai --output=json` | LCP < 2.5s, CLS < 0.1, INP < 200ms |
| k6 load test | `k6 run tests/load/5k-tenants.js` against staging | p95 < 400ms; error rate < 0.1% |
| Full E2E regression | `playwright test tests/e2e/` — all flows: onboard → calendar → approve → file → receipt → wallet | All steps green |
| WCAG 2.1 AA | `axe-playwright` on: home, dashboard, onboarding, approval, wallet pages | Zero critical violations |
| ISO 27001 gap | Vanta/Drata scan + manual | Gap report produced; year-2 plan drafted |

### 9.4 Quality Gate 5

- [ ] 50 paying companies; HK$15,000 MRR (50 × HK$300 ARPC)
- [ ] 99.5% compliance uptime (scheduler delivers ≥ 99.5% of reminders on time)
- [ ] Gross margin ≥ 70%
- [ ] NPS ≥ 30
- [ ] p95 API latency < 400ms at 5k-tenant scale

---

## 10. Cross-Cutting: Security & Compliance Testing

| Cadence | What | Method | Owner |
|---|---|---|---|
| Every PR | Python SAST | `bandit -r apps/ packages/ -ll` (fail on medium+) | CI |
| Every PR | TypeScript SAST | ESLint `plugin:security/recommended` | CI |
| Every PR | Python dependency scan | `pip-audit --requirement requirements.txt` | CI |
| Every PR | Node dependency scan | `npm audit --audit-level=high` | CI |
| Every image build | Container vulnerability scan | `trivy image cosec-api:$SHA --exit-code 1 --severity HIGH,CRITICAL` | CI |
| Pre-commit (local) | Secret detection | GitLeaks pre-commit hook | Dev local |
| Monthly | Git history secret scan | TruffleHog on full git history | Nightly CI |
| Phase 3 end | External penetration test | Scope: API auth bypass, mandate forgery, wallet manipulation, RLS bypass, injection, XSS, CSRF. Budget: HK$60K–90K. | External vendor |
| Monthly | Backup/restore drill | Runbook: snapshot → restore → row count comparison → confirm RTO < 4h | Ronald |
| Monthly | OS + dependency patching | Apply patches; log in Notion patch register | Ronald |
| Phase 5 | ISO 27001 readiness | Vanta/Drata gap assessment + manual review | Ronald (CISSP) |

---

## 11. Cross-Cutting: PDPO & Data Governance

| Control | When Implemented | Verification |
|---|---|---|
| HKID masking | Phase 1 schema | `id_number_masked` stores last 4 chars only; unit test asserts no plaintext HKID in logs |
| Data residency (HK) | Phase 1 deployment | All Postgres + S3 buckets in `ap-east-1`; AWS Config rule `APPROVED_AMIS_BY_ID` + S3 bucket location check |
| AES-256 encryption at rest | Phase 0 infrastructure | AWS RDS + S3 default encryption; Vault secrets encrypted |
| TLS 1.3 in transit | Phase 0 Caddy setup | Caddy default; verified with `testssl.sh` |
| Data retention 7 years | Phase 2 S3 storage | S3 Object Lock governance mode, 7-year retention; lifecycle rule for non-legal-hold objects |
| Consent capture | Phase 1 onboarding | `Company.privacy_consent_version` + `Company.privacy_consent_at` stored at sign-up |
| DPA execution (TASK-068) | Phase 1 | Signed DPAs on file with: AWS, Meta, Twilio, Anthropic, Stripe, SumSub |
| Director consent for A2A data access | Phase 4 | AP2 Intent Mandate required before any data shared with partner agents |
| Right to erasure | Phase 5 | `DELETE /companies/{id}` — soft delete with anonymisation; HKID + residential address zeroed; 7-year statutory records retained per CO |
| Incident notification | All phases | Sentry alert → PagerDuty → notify PCPD within 3 days of confirmed data breach (per PDPO Amendment 2021) |

---

## 12. Phase Summary Table

| Phase | Weeks | Key Deliverable | Testing Gate |
|---|---|---|---|
| 0 — Foundation | 1–4 | Legal entity, infra baseline, Hermes rules ported | 100-scenario regression; 7-day VM uptime |
| 1 — Core MVP | 5–12 | Compliance engine, WhatsApp agent, 5 beta companies | 200-case rules tests; 5 beta companies 14 days |
| 2 — Filing Automation | 13–20 | NAR1 end-to-end, audit log, e-Registry bot | 10 NAR1 filings stamped; tamper-proof audit log |
| 3 — Payment & Agent Economy | 21–28 | ATXP wallets, AP2 mandates, FPS top-up, billing | Pentest clean; 10 wallet-funded filings |
| 4 — Multi-Agent Network | 29–36 | Agent Cards, A2A registry, delegation engine | 5 A2A hand-offs; 3 partner agents live |
| 5 — Scale | 37–48 | Portfolio dashboard, SumSub KYC, load test, 50 paying companies | p95 < 400ms at 5k tenants; 50 × HK$300 MRR; NPS ≥ 30 |

---

## 13. Open Risks & Protocol Dependencies

### R-1: e-Registry API availability

**Risk:** Companies Registry offers no public API. Playwright automation is the primary filing path and breaks if CR redesigns its UI.

**Mitigation in this plan:**
- Email fallback (TASK-030) auto-triggers on 3 consecutive bot failures
- Dedicated monitoring job checks bot against a test company weekly
- HK-based on-call dev (HK$800/hr) on retainer for UI fix turnaround < 48h
- If CR publishes an official API at any point, the bot (`eregistry_bot.py`) should be refactored to use it; the interface (`submit_nar1`) stays identical

### R-2: ATXP SDK maturity

**Risk:** ATXP (`npx atxp agent register`) is a newer protocol and may be pre-production or breaking-change-prone at Phase 3.

**Mitigation in this plan:**
- Pin ATXP SDK to a specific version in `package.json`
- If ATXP SDK is not stable by Phase 3 start: implement a shim wallet using manually-signed Ed25519 JWTs stored in Postgres; expose the same `AgentWallet` interface; migrate to ATXP natively when SDK is stable
- Flag this as a Phase 3 kickoff decision point

### R-3: AP2 spec changes

**Risk:** AP2 mandate spec may evolve between Phase 3 development and production use.

**Mitigation in this plan:**
- Capture the AP2 spec version used in `IMPLEMENTATION_NOTES.md` at Phase 3 start
- `Mandate.spec_version` column stores the AP2 version of each signed mandate
- `GET /mandates/{id}/verify` returns the spec version it was verified against
- If spec changes: add a migration path (`migrate_mandate_v1_to_v2.py`) rather than rejecting old mandates

### R-4: TCSP licensing (R-1 from PRD)

**Risk:** Legal opinion (TASK-005) may conclude that the platform triggers TCSP licensing requirements.

**Mitigation in this plan:**
- TASK-005 is a Phase 0 blocker — no filing automation ships until opinion is received
- If licensing is required: partner with ≥1 licensed TCSP firm for the signatory role; platform acts as software tool only; director + TCSP firm remain legally responsible
- This does not change the technical architecture but does require a TCSP co-signer API integration (Phase 2 scope expansion)

---

*Last updated: 2026-04-18. Maintained alongside planning documents in `docs/`.*
