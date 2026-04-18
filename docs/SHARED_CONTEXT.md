# Shared Context for All 3 Platform Document Sets

## About Ronald Ng (The Founder)
- **Current role**: Head of Technology, Core Technology, Hong Kong (Feb 2025–present)
- **Background**: 21+ years IT leadership — IBM, Telstra International, CTO at startups, Head of Infrastructure at crypto startup
- **Education**: EMBA (London Business School), MComm Info Systems (UNSW), BEng Computer Engineering (UNSW)
- **Certifications**: CISSP (2026), TOGAF 9, AWS Solutions Architect Associate, AWS ML Specialty, AWS Security Specialty, AWS Advanced Networking Specialty, BCS IT Service Management
- **In progress**: ISO 42001 Lead Auditor (targeting May–June 2026)
- **Languages**: English (fluent), Cantonese (native), Mandarin (fluent)
- **Existing company**: Profit Rise Consulting (profitriseco.com) — HK-based consulting firm offering Data Resiliency, Cyber Security/ISO 27001, GenAI Workflow Transformation
- **Technical**: OpenClaw expert (built agents), MCP specialist, GitHub: ngronald8, active on Claude AI, agentic AI
- **Already built**: Hermes HK Company Secretary Advisor — OpenClaw WhatsApp bot with 6-file knowledge base, FastAPI webhook server, Docker deployment, auto-deploy on Proxmox VM
- **Contact**: talent@ronald.ng, LinkedIn: linkedin.com/in/RonaldNG
- **Location**: Hong Kong, timezone Asia/Hong_Kong
- **Constraint**: Ronald is currently employed full-time. These platforms will be built as side projects under Profit Rise Consulting, transitioning to full-time once revenue justifies it.

## Agentic Protocol Stack (All 3 Platforms Use These)
- **A2A** (Agent-to-Agent Protocol, Google/Linux Foundation): Agent discovery, task delegation, capability negotiation. Agent Cards at `/.well-known/agent-card.json`. JSON-RPC 2.0 over HTTP/SSE/gRPC. Apache 2.0.
- **MCP** (Model Context Protocol, Anthropic): Agent-to-tools/data vertical integration. Client-server model.
- **ATXP** (Agent Transaction Protocol, Circuit & Chisel): Agent identity, wallet, email, tools, self-registration. `npx atxp agent register`. Nested payments. LLM gateway.
- **UCP** (Universal Commerce Protocol, Google/Shopify): Structured product discovery, checkout, order management. Manifests at `/.well-known/ucp`. Multi-transport: REST, MCP, A2A.
- **AP2** (Agent Payments Protocol): Extension to A2A for cryptographic payment mandates. Cart Mandate, Intent Mandate, Payment Mandate.
- **ACP** (Agentic Commerce Protocol, OpenAI/Stripe): Checkout + payment tokenization. REST API. Apache 2.0.

## Shared Infrastructure Assumptions
- **Primary human interface**: WhatsApp Business API (HK's dominant messaging platform)
- **Payment rails**: FPS (Faster Payment System) for HKD, Alipay HK / WeChat Pay HK for cross-border
- **Hosting**: Proxmox VM (existing), scalable to cloud (AWS HK region or Alibaba Cloud HK)
- **Agent runtime**: OpenClaw (existing expertise)
- **LLM providers**: Claude (primary), GPT-4.1 (secondary), Qwen (for Cantonese/Chinese tasks)
- **Government subsidies available**: Digital Transformation Support Pilot Programme (HK$50K matching), Cyberport incubation, HKSTP Co-Acceleration

## Document Requirements (Apply to ALL 15 Documents)
1. Every document must be self-contained — another LLM or human can act on it without needing context from other documents
2. Ronald should NOT be the bottleneck — documents should assume Ronald works evenings/weekends (15–20 hrs/week) and can hire freelancers/contractors for specific tasks
3. All costs in HKD unless otherwise specified
4. All timelines assume part-time founder (15–20 hrs/week)
5. Include specific tool/service recommendations (not generic "use a payment provider")
6. Marketing plans must be executable by an LLM with access to website builder, Instagram API, and LinkedIn API
7. Finance plans must include month-by-month cash flow projections for 12 months
