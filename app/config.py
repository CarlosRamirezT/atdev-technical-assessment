import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER", "your-email@example.com")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "yourpassword")
    FILES_PATH = os.getenv("FILES_PATH", "saved_files/")
    API_USER = os.getenv("API_USER", "test_user")
    API_PWD = os.getenv("API_PWD", "test_password")

config = Config()
