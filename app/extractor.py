import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_crm_data(transcript):
    prompt = f"""You are a CRM data extraction assistant. Analyze this sales call transcript and extract structured data.

Transcript:
{transcript}

Return a JSON object with these exact fields:
{{
  "contact_name": "full name or null",
  "company": "company name or null",
  "email": "email address or null",
  "phone": "phone number or null",
  "key_topics": ["topic1", "topic2"],
  "pain_points": ["pain point 1", "pain point 2"],
  "action_items": [
    {{"action": "description", "owner": "person responsible"}}
  ],
  "deal_stage": "one of: appointmentscheduled, qualifiedtobuy, presentationscheduled, contractsent, closedwon, closedlost",
  "deal_name": "company name + brief deal description",
  "summary": "2-3 sentence summary of the conversation"
}}

Return only valid JSON. No markdown. No extra text."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)