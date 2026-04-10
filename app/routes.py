from flask import Blueprint, request, jsonify
import os
import tempfile
from app.whisper_client import transcribe_audio
from app.extractor import extract_crm_data
from app.hubspot_client import (
    search_contact_by_email,
    create_contact,
    create_deal,
    create_note
)

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Voice-to-CRM Agent",
        "powered_by": "OpenAI Whisper + GPT-4o + HubSpot API",
        "endpoints": {
            "POST /process": "Upload audio file, get HubSpot contact + deal created automatically"
        }
    })

@main.route("/process", methods=["POST"])
def process_audio():
    if "file" not in request.files:
        return jsonify({"error": "No audio file provided. Send a file with key 'file'."}), 400

    audio_file = request.files["file"]

    if audio_file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    suffix = os.path.splitext(audio_file.filename)[1] or ".mp3"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        audio_file.save(tmp.name)
        tmp_path = tmp.name

    try:
        transcript = transcribe_audio(tmp_path)
        crm_data = extract_crm_data(transcript)

        contact_id = None
        if crm_data.get("email"):
            contact_id = search_contact_by_email(crm_data["email"])

        if not contact_id:
            contact_id = create_contact(crm_data)

        deal_id = create_deal(contact_id, crm_data)
        note_id = create_note(contact_id, deal_id, crm_data)

        return jsonify({
            "success": True,
            "transcript": transcript,
            "extracted_data": crm_data,
            "hubspot": {
                "contact_id": contact_id,
                "deal_id": deal_id,
                "note_id": note_id
            }
        })

    finally:
        os.unlink(tmp_path)