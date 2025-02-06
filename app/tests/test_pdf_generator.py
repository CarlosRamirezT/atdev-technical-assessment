import os
import pytest
from app.services import pdf_generator
from app.models import PayrollEntry

from app.tests.data.fixtures import dummy_entry, dummy_entry_two, patch_pdfkit

def test_generate_pdf_structure(dummy_entry, patch_pdfkit):
    company_name = "Test Company"
    pdf_file = pdf_generator.generate_pdf(dummy_entry, company_name)
    
    expected_file = os.path.join("paystubs", f"{dummy_entry.email}.pdf")
    assert pdf_file == expected_file
    assert os.path.exists(pdf_file)
    
    with open(pdf_file, "r") as f:
        content = f.read()
    assert "PDF content simulation" in content

def test_generate_pdf_data_output(dummy_entry, dummy_entry_two, patch_pdfkit):
    company_name = "Another Company"
    pdf_file1 = pdf_generator.generate_pdf(dummy_entry, company_name)
    pdf_file2 = pdf_generator.generate_pdf(dummy_entry_two, company_name)
    
    expected_file1 = os.path.join("paystubs", f"{dummy_entry.email}.pdf")
    expected_file2 = os.path.join("paystubs", f"{dummy_entry_two.email}.pdf")
    
    assert pdf_file1 == expected_file1
    assert pdf_file2 == expected_file2

    calls = patch_pdfkit.called_with
    assert any(company_name in html for html, _ in calls)
