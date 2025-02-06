# atdev-technical-assessment

Notification Automation Project in FastAPI for ATDEV Technical Assessment.

# Paystub Notifier API

## Description

Paystub Notifier API is a RESTful application developed in Python using FastAPI. Its purpose is to process CSV files containing payroll data, generate paystub PDFs for each employee, and send these PDFs via email. The project is built with a modular, scalable architecture following best practices for file handling and security, and it is container-ready (including ARM support for Mac M1/M2).

## Scope

- **CSV Processing:** Convert CSV files with payroll data into Python objects.
- **PDF Generation:** Create paystub PDFs using XML templates and XSLT transformations.
- **Email Sending:** Dispatch the generated PDFs as email attachments.
- **Containerization:** Preconfigured for Docker and Docker Compose with ARM support.
- **Automated Testing:** Unit tests for individual services and integration tests for the API.
- **Security:** Secure configuration management using environment variables.

## Features

- **CSV Handling:** Efficiently processes payroll CSV files.
- **PDF Generation:** Produces paystubs from XML/XSLT templates.
- **Email Integration:** Sends out emails via SMTP with PDF attachments.
- **Modular Architecture:** Organized into models, routes, services, and utilities.
- **Container-Ready:** Fully configured for Docker and Docker Compose.
- **ARM Support:** Compatible with ARM architectures (ideal for Mac M1/M2).
- **Automated Testing:** Comprehensive unit and integration tests.

## Project Structure

```plaintext
atdev-technical-assessment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   └── models.py
│   ├── routes/
│   │   └── payroll.py
│   ├── services/
│   │   ├── email_service.py
│   │   ├── file_handler.py
│   │   └── pdf_generator.py
│   ├── utils/
│   │   └── security.py
│   └── tests/
│       ├── data/
│       │   └── fixtures.py
│       ├── test_api.py
│       ├── test_file_handler.py
│       ├── test_pdf_generator.py
│       ├── test_security.py
│       └── test_data/
│           └── test_sample.csv
├── templates/
│   ├── template.xml
│   └── template.xsl
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md