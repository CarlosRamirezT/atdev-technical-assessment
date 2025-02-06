import os
import pdfkit
import jinja2
from lxml import etree
from app.config import config

def get_templates():
    """
        Carga y retorna la plantilla XML (usando Jinja2) y la plantilla XSLT (como cadena).
    """
    
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_dir))
    template_xml = env.get_template("email_template.xml")
    template_xsl_path = os.path.join(base_dir, "email_template.xsl")
    
    with open(template_xsl_path, "r", encoding="utf-8") as f:
        template_xsl_str = f.read()

    return template_xml, template_xsl_str

def generate_pdf(entry, company_name):
    template_xml, template_xsl_str = get_templates()
    
    xml_str = template_xml.render(company_name=company_name, **entry.dict())
    
    try:
        xml_doc = etree.fromstring(xml_str.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        raise Exception(f"Error parseando el XML: {e}")
    
    try:
        xslt_doc = etree.XML(template_xsl_str.encode("utf-8"))
        transform = etree.XSLT(xslt_doc)
    except etree.XMLSyntaxError as e:
        raise Exception(f"Error parseando la plantilla XSLT: {e}")
    
    html_doc = transform(xml_doc)
    html_str = etree.tostring(html_doc, pretty_print=True, encoding="utf-8").decode("utf-8")
    
    pdf_dir = "paystubs"
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    
    pdf_file = os.path.join(pdf_dir, f"{entry.email}.pdf")
    pdfkit.from_string(html_str, pdf_file)
    
    return pdf_file
