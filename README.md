━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  VOICE-TO-CRM AGENT
  Raw audio in. Clean contacts, deals, notes, and follow-up actions
  written into HubSpot — automatically.
  by Hans Stewart · hansstewart.dev

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Architecture    →   hansstewart.github.io/ai-architecture
  Portfolio       →   hansstewart.dev
  GitHub          →   github.com/HansStewart/voice-to-crm

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A transcription and CRM automation system that turns raw audio from
  sales calls, voicemails, and voice notes into clean, structured CRM
  data — written directly into HubSpot without manual entry.

  Upload an audio file. The agent transcribes it through OpenAI Whisper,
  runs GPT-4o over the transcript to extract contact identity, company
  details, deal context, next steps, and follow-up actions, then writes
  the structured output back into HubSpot as a contact record, deal
  record, and timeline notes — all in one automated pass.

  Primary value: eliminates manual CRM logging after calls and voicemails.
  Use cases: sales teams, operators, and voice-first CRM workflows.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND WORKFLOW — 4 STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step 01 — Audio intake
    Receives recorded calls, voicemails, and voice notes via file upload.
    Accepts mp3, mp4, wav, m4a, and webm audio formats.
    Validates the upload and prepares it for transcription.
    Creates request-level metadata for logging and response tracking.
    → Input: Audio file upload

  Step 02 — Transcription layer
    Runs the uploaded audio through OpenAI Whisper.
    Produces a normalized transcript ready for structured extraction.
    Prepares the transcription payload for semantic CRM field mapping.
    → Intermediate: Call transcript

  Step 03 — CRM extraction engine
    Uses GPT-4o to translate transcript content into CRM-specific data
    objects.
    Extracts contact identity, company, deal details, next steps, and
    conversation context.
    Maps extracted content to the fields required by HubSpot.
    Builds a structured object ready for CRM insertion or update.
    → Processing: Transcript → CRM schema

  Step 04 — HubSpot writeback
    Creates or updates the contact record in HubSpot.
    Creates or updates the related deal record and stage context.
    Logs notes and follow-up actions as timeline entries for the sales
    team.
    → Output: Contact + deal + note + JSON summary


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT GETS EXTRACTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Contact identity     Full name, company, title (if stated in the call)
  Deal context         Stage, value signals, timeline, and buying intent
  Next steps           Committed follow-up actions and agreed dates
  Call notes           Summary of conversation for the HubSpot timeline
  Follow-up actions    Tasks logged for sales rep execution


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATA QUALITY NOTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Structured field extraction — not freeform note entry. Every piece of
  data written to HubSpot maps to a specific CRM field rather than being
  dumped into an unstructured notes block.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Language        Python 3.11
  Framework       Flask
  Server          Gunicorn
  Transcription   OpenAI Whisper
  AI Model        OpenAI GPT-4o (extraction and schema mapping)
  CRM             HubSpot API
  Deployment      Google Cloud Run — us-east1


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOCAL DEVELOPMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  git clone https://github.com/HansStewart/voice-to-crm.git
  cd voice-to-crm
  pip install -r requirements.txt
  cp .env.example .env
  → Add OPENAI_API_KEY and HUBSPOT_API_KEY to .env
  python main.py
  → Open http://localhost:8080


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  voice-to-crm/
  ├── main.py
  ├── app/
  │   ├── __init__.py
  │   ├── routes.py
  │   ├── transcriber.py         Whisper audio-to-text
  │   ├── extractor.py           GPT-4o CRM field extraction
  │   └── hubspot.py             HubSpot API writeback
  ├── index.html
  ├── requirements.txt
  ├── Procfile
  └── .env.example               OPENAI_API_KEY= · HUBSPOT_API_KEY=


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Hans Stewart · Marketing Automation Engineer · hansstewart.dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━