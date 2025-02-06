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
    company_name: str = Query(..., description="Name of the company"),
    country: str = Query(default="do", description="Country code (default: 'do')"),
    file: UploadFile = File(..., description="CSV file containing payroll data")
):
    # Create a temporary directory for file processing if it doesn't exist

    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Save the uploaded file to the temporary directory

    file_path = os.path.join(temp_dir, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving the file: {e}")

    # Process the CSV file to obtain payroll entries

    try:
        entries = process_csv(file_path)
    except Exception as e:
        # Clean up temporary file in case of error
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Error processing CSV file: {e}")

    email_responses = []

    # For each payroll entry, generate a PDF and send it via email

    for entry in entries:
        try:
            pdf_path = generate_pdf(entry, company_name)
            send_email(entry.email, pdf_path)
            email_responses.append({
                "email": entry.email,
                "sent_at": datetime.now().isoformat()
            })
        except Exception as e:
            # Optionally, log or collect errors for individual entries
            email_responses.append({
                "email": entry.email,
                "error": str(e)
            })

    # Clean up: remove the temporary file
    
    if os.path.exists(file_path):
        os.remove(file_path)

    return {"success": True, "emails_sent": email_responses}
