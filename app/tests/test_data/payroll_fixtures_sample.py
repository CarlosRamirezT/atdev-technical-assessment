import jinja2
import os
import pytest
from app.models.payroll_entry import PayrollEntry
from app.services import pdf_generator

# Fixture para el primer ejemplo de entrada
@pytest.fixture
def dummy_entry():
    return PayrollEntry(
        full_name="John Doe",
        email="john@example.com",
        position="Manager",
        health_discount_amount=10.0,
        social_discount_amount=20.0,
        taxes_discount_amount=30.0,
        other_discount_amount=5.0,
        gross_salary=1000.0,
        gross_payment=900.0,
        net_payment=800.0,
        period="2025-01"
    )

# Fixture para el segundo ejemplo de entrada
@pytest.fixture
def dummy_entry_two():
    return PayrollEntry(
        full_name="Jane Smith",
        email="jane@example.com",
        position="Engineer",
        health_discount_amount=5.0,
        social_discount_amount=10.0,
        taxes_discount_amount=15.0,
        other_discount_amount=2.5,
        gross_salary=2000.0,
        gross_payment=1800.0,
        net_payment=1600.0,
        period="2025-02"
    )

# Fixture que parcha la función get_templates para inyectar plantillas dummy
@pytest.fixture(autouse=True)
def patch_templates(monkeypatch):
    dummy_xml_template = jinja2.Template("""<?xml version="1.0" encoding="UTF-8"?>
<paystub>
    <company>{{ company_name }}</company>
    <employee>
        <full_name>{{ full_name }}</full_name>
        <position>{{ position }}</position>
        <gross_salary>{{ gross_salary }}</gross_salary>
        <net_payment>{{ net_payment }}</net_payment>
    </employee>
</paystub>
""")
    dummy_xsl_str = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/paystub">
        <html>
            <head>
                <title>Paystub</title>
            </head>
            <body>
                <h2><xsl:value-of select="company"/></h2>
                <p>Employee: <xsl:value-of select="employee/full_name"/></p>
                <p>Position: <xsl:value-of select="employee/position"/></p>
                <p>Gross Salary: <xsl:value-of select="employee/gross_salary"/></p>
                <p>Net Payment: <xsl:value-of select="employee/net_payment"/></p>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
"""
    monkeypatch.setattr(pdf_generator, "get_templates", lambda: (dummy_xml_template, dummy_xsl_str))

# Creamos una clase dummy para simular pdfkit y capturar las llamadas realizadas.
class DummyPDFKit:
    def __init__(self):
        self.called_with = []

    def from_string(self, html, output_path, *args, **kwargs):
        self.called_with.append((html, output_path))
        # Simulamos la escritura de un archivo PDF.
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write("PDF content simulation")
        return True

# Fixture para parchar pdfkit en el módulo pdf_generator.
@pytest.fixture(autouse=True)
def patch_pdfkit(monkeypatch):
    dummy_pdfkit = DummyPDFKit()
    monkeypatch.setattr(pdf_generator, "pdfkit", dummy_pdfkit)
    return dummy_pdfkit
