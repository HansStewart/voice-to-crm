🎙️ Voice-to-CRM Agent

An AI agent that accepts an audio file (sales call, voicemail, or voice memo), transcribes it using OpenAI Whisper, extracts structured CRM data with GPT-4o, and automatically creates a contact, deal, and note inside HubSpot — zero manual data entry.

Live API: https://voice-to-crm-559169459241.us-east1.run.app



Overview

The Voice to CRM Agent listens to uploaded voice recordings, runs them through OpenAI Whisper for transcription, then sends the transcript to GPT-4o to extract key sales data including contact details, deal information, and follow-up actions. The extracted data is automatically pushed into HubSpot as structured CRM records — no copy-pasting, no manual entry.



Features

- Accepts audio file uploads in common formats (mp3, mp4, wav, m4a, webm)
- Transcribes audio to text using OpenAI Whisper
- Extracts contact names, company, email, phone, deal value, deal stage, and next steps using GPT-4o
- Creates or updates HubSpot contacts automatically
- Logs call notes and follow-up actions as HubSpot timeline activities
- Returns a structured JSON summary of everything that was logged
- Health check endpoint for uptime monitoring and deployment verification
- Containerized with Docker and deployed on Google Cloud Run



Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Web Framework | Flask 3.0.3 |
| Transcription | OpenAI Whisper |
| AI Engine | OpenAI GPT-4o |
| CRM Integration | HubSpot CRM API v3 |
| HTTP Client | Requests 2.32.3 |
| Environment Config | python-dotenv |
| Production Server | Gunicorn |
| Containerization | Docker |
| Cloud Deployment | Google Cloud Run |
| CI/CD | Google Cloud Build |



Project Structure

```
voice-to-crm-agent/
├── app.py                  Flask app — upload route and response handler
├── transcriber.py          OpenAI Whisper integration — converts audio to text
├── extractor.py            GPT-4o engine — extracts structured CRM data from transcript
├── hubspot_client.py       HubSpot API client — creates contacts and logs activities
├── requirements.txt        Python dependencies
├── Dockerfile              Container configuration
├── .dockerignore           Files excluded from Docker build
├── .env                    Local environment variables (never committed)
├── .env.example            Environment variable template for contributors
└── .gitignore              Git exclusions
```



Setup and Installation

Prerequisites

- Python 3.11+
- Git
- Docker (for containerized deployment)
- Google Cloud SDK (for Cloud Run deployment)
- HubSpot account with Private App access
- OpenAI API key

1. Clone the Repository

```bash
git clone https://github.com/HansStewart/voice-to-crm-agent.git
cd voice-to-crm-agent
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
source venv/bin/activate        # macOS / Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Open `.env` and set your values:

```
OPENAI_API_KEY=your_openai_api_key_here
HUBSPOT_TOKEN=your_hubspot_private_app_token_here
```

5. HubSpot Private App Setup

This agent requires a HubSpot Private App token with the following scopes:

- crm.objects.contacts.write
- crm.objects.contacts.read
- crm.objects.deals.write
- crm.objects.deals.read
- timeline

To generate a token:

1. Go to HubSpot Settings, then Integrations, then Private Apps
2. Click Create a private app
3. Under the Scopes tab, enable the scopes listed above
4. Click Create app and copy the pat- token



Running Locally

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:8080
```

Upload a voice memo using the file upload form. The agent will transcribe the audio, extract the sales data, log it to HubSpot, and return a structured summary of what was created.



Running with Docker

```bash
docker build -t voice-to-crm-agent .
docker run -p 8080:8080 --env-file .env voice-to-crm-agent
```



Deploying to Google Cloud Run

Deploy from Source

```bash
gcloud run deploy voice-to-crm-agent \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --timeout 120
```

Set Environment Variables

```bash
gcloud run services update voice-to-crm-agent \
  --region us-central1 \
  --set-env-vars OPENAI_API_KEY=your_key_here,HUBSPOT_TOKEN=your_token_here
```



API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | File upload interface |
| POST | /upload | Accepts audio file, runs transcription and CRM logging |
| GET | /health | Returns agent status for uptime monitoring |

Health Check Response

```json
{
  "status": "ok",
  "agent": "voice-to-crm-agent"
}
```

Upload Response Example

```json
{
  "transcript": "Hey just got off a call with Marcus at Apex Solutions...",
  "extracted_data": {
    "contact_name": "Marcus Johnson",
    "company": "Apex Solutions",
    "email": "marcus@apexsolutions.com",
    "phone": "555-210-4400",
    "deal_value": "12000",
    "deal_stage": "Proposal Sent",
    "next_steps": "Send contract by Friday, follow up Monday"
  },
  "hubspot": {
    "contact_id": "98234",
    "note_id": "77621",
    "status": "logged"
  }
}
```



Security Notes

- Never commit your .env file — it is excluded via .gitignore
- Use Google Cloud Secret Manager for production-grade secret management
- The HubSpot token used is a scoped Private App token with only the minimum required permissions
- Cloud Run services can be restricted to authenticated access by removing --allow-unauthenticated



Roadmap

- Add real-time streaming transcription for live call recording
- Add duplicate contact detection before creating new HubSpot records
- Support batch processing of multiple audio files in one upload
- Add a post-call email summary sent automatically via HubSpot sequences
- Integrate with Zoom and Google Meet for direct call recording ingestion



Author

Hans Stewart

[GitHub](https://github.com/HansStewart)



Built with Python, OpenAI Whisper, GPT-4o, HubSpot API, and Google Cloud Run.