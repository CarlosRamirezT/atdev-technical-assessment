import os
import pytest
from app.services import email_service
from app.config import config

class DummySMTP:

    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.started_tls = False
        self.logged_in = False
        self.sent_messages = []

    def starttls(self):
        self.started_tls = True

    def login(self, user, password):
        if user == config.SMTP_USER and password == config.SMTP_PASSWORD:
            self.logged_in = True
        else:
            raise Exception("Invalid credentials")
        
    def send_message(self, msg):
        self.sent_messages.append(msg)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):
        pass

@pytest.fixture
def dummy_smtp(monkeypatch):
    dummy = DummySMTP(config.SMTP_SERVER, config.SMTP_PORT)
    monkeypatch.setattr(email_service, "smtplib", type("DummySMTPModule", (), {"SMTP": lambda server, port: dummy}))
    return dummy

def test_send_email_success(tmp_path, dummy_smtp):
    pdf_file = tmp_path / "dummy.pdf"
    pdf_file.write_bytes(b"Dummy PDF content")
    
    try:
        email_service.send_email("test@example.com", str(pdf_file))
    except Exception as e:
        pytest.fail(f"send_email arrojó una excepción inesperada: {e}")
    
    assert dummy_smtp.started_tls is True
    assert dummy_smtp.logged_in is True
    assert len(dummy_smtp.sent_messages) == 1
    
    msg = dummy_smtp.sent_messages[0]
    assert msg["To"] == "test@example.com"

def test_send_email_file_not_found(tmp_path):
    non_existent_file = tmp_path / "nonexistent.pdf"
    with pytest.raises(Exception) as excinfo:
        email_service.send_email("test@example.com", str(non_existent_file))
    assert "No se encontró el archivo PDF" in str(excinfo.value)
