# Finance & Investment Plan

*Extracted from the Complete Planning Package*

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
