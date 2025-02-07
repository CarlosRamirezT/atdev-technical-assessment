from lxml import etree
import os
import pdfkit
import jinja2

from app.config import config
from ..utils.translations import translate_template


def get_templates():
    """
    Carga y retorna la plantilla XML (usando Jinja2) y la plantilla XSLT (como cadena).
    """
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_dir))
    template_xml = env.get_template("email_template.xml")
    template_xsl_path = os.path.join(base_dir, "email_template.xsl")

    with open(template_xsl_path, "r", encoding="utf-8") as f:
        template_xsl_str = f.read()

    return template_xml, template_xsl_str


def _get_pdf_values_from_entry(entry):
    values = entry.dict()
    values["total_discount"] = (
        values.get("social_discount", 0)
        + values.get("health_discount", 0)
        + values.get("taxes_discount", 0)
        + values.get("other_discount", 0)
    )
    values["company"] = "FakeClients"
    return values


def generate_pdf(entry, company_name, country="en"):
    template_xml, template_xsl_str = get_templates()

    xml_values = _get_pdf_values_from_entry(entry)

    xml_str = template_xml.render(company_name=company_name, **xml_values)

    try:
        xml_doc = etree.fromstring(xml_str.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        raise Exception(f"Error al parsear el XML: {e}")

    template_xsl_str = translate_template(template_xsl_str, locale=country)

    try:
        xslt_doc = etree.XML(template_xsl_str.encode("utf-8"))
        transform = etree.XSLT(xslt_doc)
    except etree.XMLSyntaxError as e:
        raise Exception(f"Error al parsear la plantilla XSLT: {e}")

    html_doc = transform(xml_doc)
    html_str = etree.tostring(html_doc, pretty_print=True, encoding="utf-8").decode(
        "utf-8"
    )

    pdf_dir = config.FILES_PATH
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_file = os.path.join(pdf_dir, f"{entry.email}.pdf")
    pdfkit.from_string(html_str, pdf_file)

    return pdf_file
