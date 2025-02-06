import os
from app.services.file_handler import process_csv
from app.models.payroll_entry import PayrollEntry
import pytest

def test_process_csv_success():
    
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "test_data", "test_sample.csv")
    
    assert os.path.exists(file_path), f"El archivo de prueba no existe en: {file_path}"
    
    entries = process_csv(file_path)
    
    assert isinstance(entries, list)
    assert len(entries) == 2

    for entry in entries:
        assert isinstance(entry, PayrollEntry)

    first = entries[0]
    assert first.full_name == "John Doe"
    assert first.email == "john@example.com"
    assert first.position == "Manager"
    assert first.gross_salary == 1000.0
    assert first.period == "2025-01"

    second = entries[1]
    assert second.full_name == "Jane Smith"
    assert second.email == "jane@example.com"
    assert second.position == "Engineer"
    assert second.gross_salary == 2000.0
    assert second.period == "2025-01"
