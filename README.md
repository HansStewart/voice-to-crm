# 🎙️ Voice-to-CRM Agent

An AI agent that accepts an audio file (sales call, voicemail, or voice memo), transcribes it using OpenAI Whisper, extracts structured CRM data with GPT-4o, and automatically creates a contact, deal, and note inside HubSpot — zero manual data entry.

**Live API:** https://voice-to-crm-559169459241.us-east1.run.app

---

## Architecture
Audio File Upload (.mp3 / .wav / .m4a)
│
▼
┌─────────────────────────────────┐
│ OpenAI Whisper API │
│ Audio → Full Transcript │
└─────────────┬───────────────────┘
│
▼
┌─────────────────────────────────┐
│ GPT-4o Extractor │
│ Name · Company · Email · Phone │
│ Topics · Pain Points · Actions │
│ Deal Stage · Summary │
└─────────────┬───────────────────┘
│
▼
┌─────────────────────────────────┐
│ HubSpot Private Apps API │
│ Creates Contact + Deal + Note │
│ Auto-populates all fields │
└─────────────────────────────────┘

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Web Framework | Flask 3.1 + Gunicorn |
| Transcription | OpenAI Whisper API |
| AI Extraction | OpenAI GPT-4o |
| CRM | HubSpot Private Apps API |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |

---

## API Reference

### `GET /`
Health check.

**Response:**
```json
{ "status": "healthy", "service": "Voice-to-CRM Agent" }
```

### `POST /process`
Upload an audio file and receive a fully populated HubSpot contact and deal.

**Request:** `multipart/form-data`
file: your_recording.mp3

**Response:**
```json
{
  "success": true,
  "transcript": "Full transcribed text...",
  "extracted_data": {
    "contact_name": "Sarah Johnson",
    "company": "TechFlow Inc",
    "email": "sarah@techflow.com",
    "deal_stage": "qualifiedtobuy",
    "pain_points": ["CRM not being updated", "no pipeline visibility"]
  },
  "hubspot": {
    "contact_id": "12345",
    "deal_id": "67890",
    "note_id": "11121"
  }
}
```