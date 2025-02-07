<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    
    <xsl:template match="/paystub">
        <html>
            <head>
                <meta charset="UTF-8"/>
                <style>
                    body { font-family: Arial, sans-serif; }
                    table { width: 100%; border-collapse: collapse; }
                    td, th { padding: 8px; border: 1px solid #ddd; }
                    .company-name { font-size: 24px; font-weight: bold; color: #ffcc00; }
                    .section-title { font-weight: bold; background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <td colspan="2" rowspan="3" class="company-name"><xsl:value-of select="employee/company"/></td>
                        <td colspan="2"><h3>Comprobante de pago <xsl:value-of select="employee/period"/></h3></td>
                    </tr>
                    <tr>
                        <td colspan="2"><xsl:value-of select="employee/full_name"/></td>
                    </tr>
                    <tr>
                        <td colspan="2"><xsl:value-of select="employee/position"/></td>
                    </tr>
                    <tr class="section-title">
                        <td><strong>Salario bruto</strong></td>
                        <td><xsl:value-of select="employee/gross_salary"/></td>
                        <td><strong>SFS</strong></td>
                        <td><xsl:value-of select="employee/social_discount"/></td>
                    </tr>
                    <tr>
                        <td><strong>Pago Bruto</strong></td>
                        <td><xsl:value-of select="employee/gross_payment"/></td>
                        <td><strong>AFP</strong></td>
                        <td><xsl:value-of select="employee/health_discount"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td><strong>ISR</strong></td>
                        <td><xsl:value-of select="employee/taxes_discount"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td><strong>Otros</strong></td>
                        <td><xsl:value-of select="employee/other_discount"/></td>
                    </tr>
                    <tr class="section-title">
                        <td></td>
                        <td></td>
                        <td><strong>Total Descuentos</strong></td>
                        <td><xsl:value-of select="employee/total_discount"/></td>
                    </tr>
                    <tr class="section-title">
                        <td>Pago Neto</td>
                        <td><xsl:value-of select="employee/net_payment"/></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
