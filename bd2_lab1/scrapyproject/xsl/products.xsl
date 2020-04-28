<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h1>Products</h1>
                <xsl:for-each select="products/product">
                    <hr></hr>
                    <h3>Name:</h3>
                    <p>
                        <xsl:value-of select="name"/>
                    </p>
                    <h3>Price:</h3>
                    <p>
                        <xsl:value-of select="price"/>
                    </p>
                    <h3>Description:</h3>
                    <p>
                        <xsl:value-of select="description"/>
                    </p>
                    <h3>Image:</h3>
                    <xsl:element name="img">
                        <xsl:attribute name="src">
                            <xsl:value-of select="image"/>
                        </xsl:attribute>
                    </xsl:element>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>


</xsl:stylesheet>