import requests
import os
import time

HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")
BASE_URL = "https://api.hubapi.com"

HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_TOKEN}",
    "Content-Type": "application/json"
}

def search_contact_by_email(email):
    url = f"{BASE_URL}/crm/v3/objects/contacts/search"
    payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": email
            }]
        }]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    results = response.json().get("results", [])
    if results:
        return results[0]["id"]
    return None

def create_contact(data):
    url = f"{BASE_URL}/crm/v3/objects/contacts"
    name_parts = (data.get("contact_name") or "Unknown").split(" ", 1)
    firstname = name_parts[0]
    lastname = name_parts[1] if len(name_parts) > 1 else ""

    payload = {
        "properties": {
            "firstname": firstname,
            "lastname": lastname,
            "company": data.get("company") or "",
            "email": data.get("email") or "",
            "phone": data.get("phone") or ""
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json().get("id")

def create_deal(contact_id, data):
    url = f"{BASE_URL}/crm/v3/objects/deals"
    payload = {
        "properties": {
            "dealname": data.get("deal_name") or f"Deal - {data.get('company', 'Unknown')}",
            "dealstage": data.get("deal_stage") or "appointmentscheduled",
            "pipeline": "default"
        },
        "associations": [
            {
                "to": {"id": contact_id},
                "types": [{
                    "associationCategory": "HUBSPOT_DEFINED",
                    "associationTypeId": 3
                }]
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json().get("id")

def create_note(contact_id, deal_id, data):
    url = f"{BASE_URL}/crm/v3/objects/notes"

    action_lines = "\n".join([
        f"- {item.get('action', '')} (Owner: {item.get('owner', 'TBD')})"
        for item in data.get("action_items", [])
    ])

    note_body = f"""CALL SUMMARY
{data.get('summary', 'No summary available.')}

KEY TOPICS
{', '.join(data.get('key_topics', []))}

PAIN POINTS
{', '.join(data.get('pain_points', []))}

ACTION ITEMS
{action_lines}"""

    associations = []
    if contact_id:
        associations.append({
            "to": {"id": contact_id},
            "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 202}]
        })
    if deal_id:
        associations.append({
            "to": {"id": deal_id},
            "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 214}]
        })

    payload = {
        "properties": {
            "hs_note_body": note_body,
            "hs_timestamp": str(int(time.time() * 1000))
        },
        "associations": associations
    }

    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json().get("id")