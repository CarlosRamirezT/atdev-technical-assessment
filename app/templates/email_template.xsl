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
                        <td colspan="2" rowspan="3" class="company-name">
                            <xsl:value-of select="employee/company"/>
                        </td>
                        <td colspan="2">
                            <h3>{paystub_payment} <xsl:value-of select="employee/period"/></h3>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <xsl:value-of select="employee/full_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <xsl:value-of select="employee/position"/>
                        </td>
                    </tr>
                    <tr class="section-title">
                        <td><strong>{gross_salary}</strong></td>
                        <td><xsl:value-of select="employee/gross_salary"/></td>
                        <td><strong>{health_insurance}</strong></td>
                        <td><xsl:value-of select="employee/social_discount"/></td>
                    </tr>
                    <tr>
                        <td><strong>{gross_payment}</strong></td>
                        <td><xsl:value-of select="employee/gross_payment"/></td>
                        <td><strong>{social_security}</strong></td>
                        <td><xsl:value-of select="employee/health_discount"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td><strong>{taxes}</strong></td>
                        <td><xsl:value-of select="employee/taxes_discount"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td><strong>{others}</strong></td>
                        <td><xsl:value-of select="employee/other_discount"/></td>
                    </tr>
                    <tr class="section-title">
                        <td></td>
                        <td></td>
                        <td><strong>{total_discount}</strong></td>
                        <td><xsl:value-of select="employee/total_discount"/></td>
                    </tr>
                    <tr class="section-title">
                        <td>{net_payment}</td>
                        <td><xsl:value-of select="employee/net_payment"/></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
