import io
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

# Automatically set the environment variables for authentication for all tests in this module.
@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("API_USER", "test_user")
    monkeypatch.setenv("API_PWD", "test_password")

@pytest.fixture
def client():
    return TestClient(app)

def dummy_generate_pdf(entry, company_name, country="en"):
    return f"dummy_paystubs/{entry.email}.pdf"

def dummy_send_email(email, pdf_path):
    return True

def test_process_payroll_api(monkeypatch, client):
    """
    Test the /api/process endpoint with basic authentication.
    """
    monkeypatch.setattr("app.services.pdf_generator.generate_pdf", dummy_generate_pdf)
    monkeypatch.setattr("app.services.email_service.send_email", dummy_send_email)
    monkeypatch.setattr("app.routes.payroll.generate_pdf", dummy_generate_pdf)
    monkeypatch.setattr("app.routes.payroll.send_email", dummy_send_email)
    
    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, "test_data", "test_sample.csv")
    assert os.path.exists(csv_file_path), f"Test file does not exist at: {csv_file_path}"
    
    with open(csv_file_path, "rb") as f:
        csv_content = f.read()
    
    file_like = io.BytesIO(csv_content)
    file_like.name = "test_sample.csv"
    
    # Use the correct query parameter "company" instead of "company_name"
    response = client.post(
        "/api/process?company=TestCompany",
        auth=("test_user", "test_password"),
        files={"file": (file_like.name, file_like, "text/csv")}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "success" in data
    assert data["success"] is True
    assert "emails_sent" in data
    assert isinstance(data["emails_sent"], list)
    assert len(data["emails_sent"]) == 2
    
    for email_info in data["emails_sent"]:
        assert "email" in email_info, f"Missing 'email' in {email_info}"
        assert "sent_at" in email_info, f"Missing 'sent_at' in {email_info}"
        assert "@" in email_info["email"]
    
    temp_dir = "temp"
    if os.path.exists(temp_dir):
        for file in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, file))

