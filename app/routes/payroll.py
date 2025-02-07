import os
import shutil
from datetime import datetime
from fastapi import APIRouter, File, UploadFile, Query, HTTPException
from app.services.file_handler import process_csv
from app.services.pdf_generator import generate_pdf
from app.services.email_service import send_email

router = APIRouter()


@router.post("/process", summary="Process payroll CSV file and send paystub PDFs")
async def process_payroll(
    company: str = Query(..., description="Name of the company"),
    country: str = Query(default="do", description="Country code (default: 'do')"),
    file: UploadFile = File(..., description="CSV file containing payroll data"),
):
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    file_path = os.path.join(temp_dir, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving the file: {e}")

    try:
        entries = process_csv(file_path)
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Error processing CSV file: {e}")

    email_responses = []

    for entry in entries:
        try:
            pdf_path = generate_pdf(entry, company, country)
            send_email(entry.email, pdf_path)
            email_responses.append(
                {"email": entry.email, "sent_at": datetime.now().isoformat()}
            )
        except Exception as e:
            email_responses.append({"email": entry.email, "error": str(e)})

    if os.path.exists(file_path):
        os.remove(file_path)

    return {"success": True, "emails_sent": email_responses}
