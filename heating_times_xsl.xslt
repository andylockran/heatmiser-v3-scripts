<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:t="http://www.example.org/history">
    <xsl:template match="/">
        <!-- TODO: Auto-generated template -->
        <html>
        <head>
        <title>Heating Times</title>
        <link rel="shortcut icon" href="favicon.ico" />
        <link rel="stylesheet" href="heating_status.css"></link>    
        </head>
        <body>
        <a NAME="Top"></a>
        <br/><a HREF="#Bottom">Bottom</a>
        <table border="1" width="100%">
        <tr>
        <th rowspan="3">Unit</th>
        <th colspan="8">Weekday</th>
        <th colspan="8">Weekend</th>
        </tr>
        <tr>
        <th colspan="2">Time1</th>
        <th colspan="2">Time2</th>
        <th colspan="2">Time3</th>
        <th colspan="2">Time4</th>
        <th colspan="2">Time1</th>
        <th colspan="2">Time2</th>
        <th colspan="2">Time3</th>
        <th colspan="2">Time4</th>
        </tr>
        <tr>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        <th>Time</th>
        <th>Temp</th>
        </tr>
        <xsl:for-each select="t:poll/t:controller">
            <tr>
                <xsl:call-template name="alternated-row" />
                <td title="location">
                    <xsl:value-of select="./t:locationlong" /><sub><xsl:value-of select="./t:ident" /></sub>
                </td>
                <td title="idehournt"> 
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wday_t1_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wday_t1_hour, "00")' /> :<xsl:value-of select='format-number(./t:wday_t1_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wday_t1_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wday_t1_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wday_t2_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wday_t2_hour, "00")' /> :<xsl:value-of select='format-number(./t:wday_t2_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wday_t2_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wday_t2_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wday_t3_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wday_t3_hour, "00")' /> :<xsl:value-of select='format-number(./t:wday_t3_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wday_t3_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wday_t3_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wday_t4_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wday_t4_hour, "00")' /> :<xsl:value-of select='format-number(./t:wday_t4_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wday_t4_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wday_t4_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wend_t1_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wend_t1_hour, "00")' /> :<xsl:value-of select='format-number(./t:wend_t1_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wend_t1_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wend_t1_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wend_t2_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wend_t2_hour, "00")' /> :<xsl:value-of select='format-number(./t:wend_t2_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wend_t2_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wend_t2_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <xsl:when test="./t:wend_t3_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wend_t3_hour, "00")' /> :<xsl:value-of select='format-number(./t:wend_t3_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wend_t3_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wend_t3_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="idehournt">
                    <xsl:choose>
                        <!-- A time of 24 means not used -->
                        <xsl:when test="./t:wend_t4_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select='format-number(./t:wend_t4_hour, "00")' /> :<xsl:value-of select='format-number(./t:wend_t4_mins, "00")' /></xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="temp">
                    <xsl:choose>
                        <xsl:when test="./t:wend_t4_hour = 24">-</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:wend_t4_temp" /><sup>o</sup></xsl:otherwise>
                    </xsl:choose>
                </td>
                
                


            </tr>
                        
        </xsl:for-each>
        
        </table>
        
        <br/>Based on Poll Made at <xsl:value-of select="t:poll/t:polltime/t:readable" />

        <br/><a HREF="#Top">Top</a>
        <br/>
        <a NAME="Bottom"></a>
        <a href="heating_status_ss.htm">Status</a> :
        <a href="heating_config_ss.htm">Config</a> :
        <a href="heating_times_ss.htm">Times</a> :
        <a href="mytimeline.htm">Timeline</a> : 
        <a href="graphs">Graphs</a>
        <br/>
        </body>
        </html>
    </xsl:template>
    
    <xsl:template name="alternated-row">
    <!--** Template alternated-row, for alternated rows style in tables -->
       <xsl:choose>
            <xsl:when test="./t:thisdemand = 0">
                <xsl:attribute name="class">
                    <xsl:if test="position() mod 2 = 1">a</xsl:if>
                    <xsl:if test="position() mod 2 = 0">b</xsl:if>
                </xsl:attribute>
            </xsl:when>
            <xsl:when test="./t:thisdemand = 1">
                <xsl:attribute name="class">
                    <xsl:if test="position() mod 2 = 1">ad</xsl:if>
                    <xsl:if test="position() mod 2 = 0">bd</xsl:if>
                </xsl:attribute>
            </xsl:when>
            <xsl:otherwise>
                <xsl:attribute name="class">
                    <xsl:if test="position() mod 2 = 1">a</xsl:if>
                    <xsl:if test="position() mod 2 = 0">b</xsl:if>
                </xsl:attribute>
            </xsl:otherwise>
        </xsl:choose> 
    </xsl:template>
    
</xsl:stylesheet>
