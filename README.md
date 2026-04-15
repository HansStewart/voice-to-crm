# Voice-to-CRM Agent

> A transcription and CRM automation system that turns raw audio into clean contacts, deals, notes, and follow-up actions inside HubSpot — automatically.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/voice-to-crm)

---

## What It Does

Upload an audio file from a sales call, voicemail, or voice note. The agent transcribes it through OpenAI Whisper, runs GPT-4o over the transcript to extract contact identity, company details, deal context, next steps, and follow-up actions, then writes the structured output back into HubSpot as a contact record, deal record, and timeline notes — all in one automated pass.

**Primary value:** eliminates manual CRM logging after calls and voicemails.  
**Use cases:** sales teams, operators, and voice-first CRM workflows.

---

## Backend Workflow

**Step 1 — Audio intake** `Input: Audio file upload`
Receives recorded calls, voicemails, and voice notes via file upload. Accepts mp3, mp4, wav, m4a, and webm audio formats. Validates the upload and prepares it for transcription.

**Step 2 — Transcription layer** `Intermediate: Call transcript`
Runs the uploaded audio through OpenAI Whisper. Produces a normalized transcript ready for structured extraction. Prepares the transcription payload for semantic CRM field mapping.

**Step 3 — CRM extraction engine** `Processing: Transcript → CRM schema`
Uses GPT-4o to translate transcript content into CRM-specific data objects. Extracts contact identity, company, deal details, next steps, and conversation context. Maps extracted content to the fields required by HubSpot.

**Step 4 — HubSpot writeback** `Output: Contact + deal + note + JSON summary`
Creates or updates the contact record in HubSpot. Creates or updates the related deal record and stage context. Logs notes and follow-up actions as timeline entries for the sales team.

---

## What Gets Extracted

| Field | Description |
|---|---|
| Contact identity | Full name, company, title (if stated in the call) |
| Deal context | Stage, value signals, timeline, and buying intent |
| Next steps | Committed follow-up actions and agreed dates |
| Call notes | Summary of conversation for the HubSpot timeline |
| Follow-up actions | Tasks logged for sales rep execution |

> **Data quality note:** structured field extraction — not freeform note entry. Every piece of data written to HubSpot maps to a specific CRM field rather than being dumped into an unstructured notes block.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| Transcription | OpenAI Whisper |
| AI Model | OpenAI GPT-4o |
| CRM | HubSpot API |
| Deployment | Google Cloud Run — us-east1 |

---

## Local Development

```bash
git clone https://github.com/HansStewart/voice-to-crm.git
cd voice-to-crm
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY and HUBSPOT_API_KEY to .env
python main.py
# Open http://localhost:8080
```

---

## Project Structure

```
voice-to-crm/
├── main.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── transcriber.py     Whisper audio-to-text
│   ├── extractor.py       GPT-4o CRM field extraction
│   └── hubspot.py         HubSpot API writeback
├── index.html
├── requirements.txt
├── Procfile
└── .env.example           OPENAI_API_KEY=  HUBSPOT_API_KEY=
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Whisper transcription + GPT-4o extraction |
| `HUBSPOT_API_KEY` | Yes | HubSpot CRM read and write access |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| AI Content Pipeline | [github.com/HansStewart/ai-content-pipeline](https://github.com/HansStewart/ai-content-pipeline) |
| Pipeline Intelligence Agent | [github.com/HansStewart/pipeline-intelligence-agent](https://github.com/HansStewart/pipeline-intelligence-agent) |
| CRM Automation Agent | [github.com/HansStewart/crm-agent](https://github.com/HansStewart/crm-agent) |
| Multi-Agent BI System | [github.com/HansStewart/multi-agent](https://github.com/HansStewart/multi-agent) |
| AI Data Agent | [github.com/HansStewart/ai-data-agent](https://github.com/HansStewart/ai-data-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**
