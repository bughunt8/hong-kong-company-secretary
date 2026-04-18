# Hong Kong Agentic Company Secretary Platform

> AI-powered company secretarial compliance for Hong Kong's 1.4 million registered companies — using A2A, MCP, ATXP, and AP2 protocols.

## Overview

This platform productizes the [Hermes HK Company Secretary Advisor](https://github.com/ngronald8/hk-comsec-agent) into a multi-tenant SaaS that automates company secretarial compliance in Hong Kong:

- **Compliance Calendar** — Tracks NAR1, BRC, Profits Tax Return, Employer's Return, SCR deadlines per company
- **Automated Filing** — Pre-fills forms from stored company data, submits via e-Registry
- **WhatsApp-First** — Directors get reminders and approve filings via WhatsApp
- **Agent Economy** — Each company has its own AI agent with an ATXP wallet that pays filing fees autonomously
- **Multi-Agent Network** — Discovers and delegates to accounting agents, legal agents via A2A protocol

## Documents

| Document | Description | Path |
|---|---|---|
| **Complete Package** | All 5 documents in one file | [`docs/COMPLETE_PLANNING_PACKAGE.md`](docs/COMPLETE_PLANNING_PACKAGE.md) |
| **1. PRD** | Product Requirements Definition — features, architecture, data model, APIs | [`docs/prd/01_PRODUCT_REQUIREMENTS.md`](docs/prd/01_PRODUCT_REQUIREMENTS.md) |
| **2. Build Plan** | 48-week phased build plan with tasks, hours, assignees, quality gates | [`docs/build-plan/02_BUILD_PLAN.md`](docs/build-plan/02_BUILD_PLAN.md) |
| **3. Kanban Board** | 72 structured task cards — import into Notion, Linear, or any tracker | [`docs/kanban/03_KANBAN_BOARD.md`](docs/kanban/03_KANBAN_BOARD.md) |
| **4. Marketing Plan** | Brand, website, LinkedIn/Instagram calendars, launch sequence | [`docs/marketing/04_MARKETING_PLAN.md`](docs/marketing/04_MARKETING_PLAN.md) |
| **5. Finance Plan** | Startup costs, cash flow, break-even, government grants, unit economics | [`docs/finance/05_FINANCE_PLAN.md`](docs/finance/05_FINANCE_PLAN.md) |

### Reference Documents

| Document | Description | Path |
|---|---|---|
| Agentic Protocols | Research on UCP, ACP, ATXP, A2A, AP2 protocols | [`docs/AGENTIC_PROTOCOLS_REFERENCE.md`](docs/AGENTIC_PROTOCOLS_REFERENCE.md) |
| HK Platform Use Cases | 8 agentic platform opportunities in Hong Kong | [`docs/HK_PLATFORM_USE_CASES_REFERENCE.md`](docs/HK_PLATFORM_USE_CASES_REFERENCE.md) |
| Shared Context | Founder profile, protocol stack, shared infrastructure | [`docs/SHARED_CONTEXT.md`](docs/SHARED_CONTEXT.md) |

## Protocol Stack

| Protocol | Role in This Platform |
|---|---|
| **A2A** (Google/Linux Foundation) | Agent-to-agent discovery — company agent delegates to accounting/legal agents |
| **MCP** (Anthropic) | Agent-to-data — connects to Companies Registry, IRD, WhatsApp, document storage |
| **ATXP** (Circuit & Chisel) | Agent identity + wallet — each company agent pays its own filing fees |
| **AP2** (Google/PayPal) | Payment authorization — directors pre-approve filing fee payments via Intent Mandates |

## Quick Numbers

| Metric | Value |
|---|---|
| Target market | 1.4M registered HK companies |
| Starting price | HK$200–600/month per company |
| Startup cost | ~HK$149K (self-funded) |
| Break-even | Month 8–10 (35 companies) |
| LTV:CAC | 14.9x |

## Status

**Phase 0 — Foundation** (planning stage)

## License

See [LICENSE](LICENSE) file.
