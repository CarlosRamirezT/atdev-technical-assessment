import os
import smtplib
from email.message import EmailMessage
from app.config import config

def send_email(to_email: str, pdf_path: str):
    """
    Envía un correo electrónico con el PDF del recibo de pago adjunto.
    
    Parámetros:
      - to_email: Dirección de correo del destinatario.
      - pdf_path: Ruta del archivo PDF a adjuntar.
    """
    subject = "Your Paystub"
    body = "Please find attached your paystub for this period."
    
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config.SMTP_USER
    msg["To"] = to_email
    msg.set_content(body)
    
    try:
        with open(pdf_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(pdf_path)
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    except FileNotFoundError:
        raise Exception(f"No se encontró el archivo PDF en: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error al leer el archivo PDF: {e}")
    
    try:
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()  # Iniciar una conexión TLS para mayor seguridad.
            server.login(config.SMTP_USER, config.SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Error al enviar el correo electrónico: {e}")
