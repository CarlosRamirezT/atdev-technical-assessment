<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/paystub">
        <html>
            <head>
                <title>
                    <xsl:value-of select="concat(company, ' - Paystub')"/>
                </title>
            </head>
            <body>
                <h2><xsl:value-of select="concat(company, ' - Paystub')"/></h2>
                <p>Employee: <xsl:value-of select="employee/full_name"/></p>
                <p>Position: <xsl:value-of select="employee/position"/></p>
                <p>Gross Salary: <xsl:value-of select="employee/gross_salary"/></p>
                <p>Net Payment: <xsl:value-of select="employee/net_payment"/></p>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
