# Automated RTI Info Assistant — README

## Overview
An **Automated RTI (Right to Information) Assistant** is a tool — usually a chatbot, web app, or workflow automation system — that helps citizens draft, file, track, and understand RTI applications under India's Right to Information Act, 2005 (or equivalent transparency laws in other countries). It reduces the friction of navigating bureaucratic procedures by automating repetitive, rule-based parts of the RTI process.

## Problem It Solves
Filing an RTI application manually requires knowing:
- Which Public Information Officer (PIO) / department to address
- The correct format and mandatory fields
- Applicable fees and exemptions (e.g., BPL waivers)
- Timelines (30 days normal, 48 hours for life/liberty matters)
- Appeal procedures if no response or an unsatisfactory response is received

Most first-time applicants find this confusing. An automated assistant simplifies it.

## Core Features
1. **Query Understanding** — Takes a plain-language question ("Why hasn't my road repair request been addressed?") and identifies the relevant department/authority.
2. **Application Drafting** — Auto-generates a properly formatted RTI application with mandatory clauses, addressee details, and applicant info.
3. **PIO/Department Lookup** — Maintains or fetches a database of Public Information Officers by department/region.
4. **Fee & Exemption Guidance** — Tells users the correct fee, payment mode, and BPL exemption rules.
5. **Submission Routing** — Optionally integrates with the RTI Online portal (rtionline.gov.in, Government of India) for direct e-filing, or generates a postable PDF.
6. **Tracking & Reminders** — Tracks the 30-day statutory deadline and reminds the user to file a First Appeal if no response arrives.
7. **First/Second Appeal Drafting** — Auto-drafts appeal letters to the appellate authority or Information Commission if the response is delayed, denied, or incomplete.
8. **Multilingual Support** — Since RTI is used widely in regional contexts, supporting Hindi and other regional languages is a common requirement.

## Typical Architecture
```
User Query (chat/voice/form)
        |
        v
Intent & Entity Extraction (NLP)
        |
        v
Department/PIO Lookup (structured DB or scraped govt data)
        |
        v
Template Engine (fills legal RTI format)
        |
        v
Output: PDF/Doc -> Manual post OR API submission to RTI portal
        |
        v
Tracking Module (deadline reminders, status updates)
```

## Key Components to Build

| Component | Purpose |
|---|---|
| NLP/LLM layer | Understand user intent, extract department & subject |
| PIO Directory | Structured database of departments and information officers |
| Template Generator | Produces legally compliant RTI application text |
| Document Export | PDF/Word generation for print or postal filing |
| Status Tracker | Monitors deadlines, sends reminders |
| Appeal Module | Drafts First/Second Appeal on non-response |

## Legal Considerations
- RTI applications must cite the RTI Act, 2005 and follow prescribed formats per state (each Indian state has its own RTI rules with minor format variations).
- The assistant should **not** provide legal advice — only procedural/drafting assistance — and should clarify this to users.
- Personal data of applicants should be handled securely; RTI applications often contain PII.

## Possible Tech Stack
- **Backend**: Python/Node.js
- **NLP**: An LLM (like Claude) for intent extraction and drafting
- **Database**: PostgreSQL/MongoDB for PIO directories and application tracking
- **Frontend**: Web app or WhatsApp/Telegram bot (high reach for citizen-facing tools)
- **Document generation**: PDF libraries (e.g., reportlab, docx generation)

## Limitations to Flag to Users
- Cannot guarantee a response from government departments — it only helps file/track requests.
- State-specific RTI rules vary; the directory needs regular updates.
- Should not be relied on for time-critical legal deadlines without human double-checking.

## Next Steps
If building this as an actual project, useful next steps include:
- Scaffolding the app structure
- Designing the PIO database schema
- Writing the RTI template generator
- Setting up the tracking/reminder module
