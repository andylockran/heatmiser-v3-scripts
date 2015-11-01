<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:t="http://www.example.org/history">
    <xsl:template match="/">
        <!-- TODO: Auto-generated template -->
        <html>
        <head>
        <title>Heating Status</title>
        <link rel="shortcut icon" href="favicon.ico" />
        <link rel="stylesheet" href="heating_status.css"></link>    
        </head>

        <body>
        <a NAME="Top"></a>
        <br/><a HREF="#Bottom">Bottom</a>
        <table border="1" width="100%">
        <tr>
        <th>Location</th>
        <th>Graphs</th>
        <th>Air</th>
        <th>Remote</th>
        <th>Floor</th>
        <th>Set</th>
        <th>Status</th>
        </tr>
        <xsl:for-each select="t:poll/t:controller">
            <tr>
                <xsl:call-template name="alternated-row" />
                <td title="location">
                    <xsl:value-of select="./t:locationlong" /><sub><xsl:value-of select="./t:ident" /></sub>
                </td>
                <td title="graphs">
                    <xsl:variable name="grname24"><xsl:value-of select="./t:locationshort" />_24hrs.png</xsl:variable>
                    <a href="graphs/{$grname24}"><img src="images/graph_24.png" alt="Graphs" height="20" width="20"></img></a>
                    <xsl:variable name="grname7"><xsl:value-of select="./t:locationshort" />_7days.png</xsl:variable>
                    <a href="graphs/{$grname7}"><img src="images/graph_7.png" alt="Graphs" height="20" width="20"></img></a>
                    <xsl:variable name="grname4"><xsl:value-of select="./t:locationshort" />_4weeks.png</xsl:variable>
                    <a href="graphs/{$grname4}"><img src="images/graph_4.png" alt="Graphs" height="20" width="20"></img></a>
                    <xsl:variable name="grname8"><xsl:value-of select="./t:locationshort" />_8weeks.png</xsl:variable>
                    <a href="graphs/{$grname8}"><img src="images/graph_8.png" alt="Graphs" height="20" width="20"></img></a>
                    <xsl:variable name="grname12"><xsl:value-of select="./t:locationshort" />_12weeks.png</xsl:variable>
                    <a href="graphs/{$grname12}"><img src="images/graph_12.png" alt="Graphs" height="20" width="20"></img></a>
                    <xsl:variable name="grname52"><xsl:value-of select="./t:locationshort" />_52weeks.png</xsl:variable>
                    <a href="graphs/{$grname52}"><img src="images/graph_52.png" alt="Graphs" height="20" width="20"></img></a>
                </td>
                <td title="air">
                    <xsl:choose>
                        <xsl:when test="./t:sensormode = 0">
                            <!-- Air Only -->
                            <xsl:value-of select="./t:airtemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 1">
                            <!-- Remote Air Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 2">
                            <!-- Floor Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 3">
                            <!-- Air and floor -->
                            <xsl:value-of select="./t:airtemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 4">
                            <!-- Remote and floor -->
                            -
                        </xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="remote">
                    <xsl:choose>
                        <xsl:when test="./t:sensormode = 0">
                            <!-- Air Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 1">
                            <!-- Remote Air Only -->
                            <xsl:value-of select="./t:remtemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 2">
                            <!-- Floor Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 3">
                            <!-- Air and floor -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 4">
                            <!-- Remote and floor -->
                            <xsl:value-of select="./t:remtemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="floor">
                    <xsl:choose>
                        <xsl:when test="./t:sensormode = 0">
                            <!-- Air Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 1">
                            <!-- Remote Air Only -->
                            -
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 2">
                            <!-- Floor Only -->
                            <xsl:value-of select="./t:floortemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 3">
                            <!-- Air and floor -->
                            <xsl:value-of select="./t:floortemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:when test="./t:sensormode = 4">
                            <!-- Remote and floor -->
                            <xsl:value-of select="./t:floortemp" /><sup>o</sup>
                        </xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="roomset">
                    <xsl:choose>
                        <xsl:when test="./t:onoff = 0">OFF <small>(<xsl:value-of select="./t:roomset" /><sup>o</sup>)</small></xsl:when>
                        <xsl:when test="./t:onoff = 1">
                            <xsl:choose>
                                <xsl:when test="./t:runmode = 0"><xsl:value-of select="./t:roomset" /><sup>o</sup></xsl:when>
                                <xsl:when test="./t:runmode = 1">FROST <small>(<xsl:value-of select="./t:frosttemp" /><sup>o</sup>)</small></xsl:when>
                                <xsl:otherwise>UNKNWON</xsl:otherwise>
                            </xsl:choose>
                        </xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                    <xsl:if test="./t:tempholdmins > 0">
                        &#160;
                        <xsl:variable name="holdmins"><xsl:value-of select="./t:tempholdmins" /> mins</xsl:variable>
                        <img src="images/clock.png" alt="{$holdmins}" height="24" width="24"></img>
                        <xsl:variable name="holdminsmod60"><xsl:value-of select="./t:tempholdmins  mod 60" /></xsl:variable>
                        <small>(<xsl:value-of select="floor(./t:tempholdmins div 60)" />:<xsl:value-of select='format-number($holdminsmod60, "00")' />)</small>
                    </xsl:if>
                </td>
                <td title="thisdemand">
                    <xsl:choose>
                        <xsl:when test="./t:thisdemand = 0">-</xsl:when>
                        <xsl:when test="./t:thisdemand = 1"><img src="images/flame.png" alt="Heating" height="25" width="18"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <xsl:when test="./t:keylock = 0"><img src="images/unlocked.png" alt="UnLocked" height="24" width="32"></img></xsl:when>
                        <xsl:when test="./t:keylock = 1"><img src="images/locked.png" alt="Locked" height="24" width="32"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <xsl:when test="./t:runmode = 0">-</xsl:when>
                        <xsl:when test="./t:runmode = 1"><img src="images/frost.png" alt="Frost" height="32" width="32"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <xsl:when test="./t:floorlimiting = 0">-</xsl:when>
                        <xsl:when test="./t:floorlimiting = 1"><img src="images/limit.png" alt="FloorLimiting" height="24" width="24"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <xsl:when test="./t:tempholdmins = 0">-</xsl:when>
                        <xsl:when test="./t:tempholdmins > 0"><xsl:variable name="holdmins"><xsl:value-of select="./t:tempholdmins" /> mins</xsl:variable>
                        <img src="images/clock.png" alt="{$holdmins}" height="24" width="24"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <xsl:when test="./t:holidayhours = 0">-</xsl:when>
                        <xsl:when test="./t:holidayhours > 0"><img src="images/holiday.png" alt="Holiday" height="24" width="32"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>
                    <xsl:choose>
                        <!-- TODO: Not sure if these are correct error codes -->
                        <xsl:when test="./t:errcode = 0">-</xsl:when>
                        <xsl:when test="./t:errcode = 224"><img src="images/maintenance.png" alt="IntAir" height="48" width="48"></img></xsl:when>
                        <xsl:when test="./t:errcode = 225"><img src="images/maintenance.png" alt="Floor" height="48" width="48"></img></xsl:when>
                        <xsl:when test="./t:errcode = 225"><img src="images/maintenance.png" alt="RemAir" height="48" width="48"></img></xsl:when>
                        <xsl:otherwise>U</xsl:otherwise>
                    </xsl:choose>                    
                </td>
            </tr>
                        
        </xsl:for-each>
        <tr>
        <th>Location</th>
        <th>Graphs</th>
        <th>Air</th>
        <th>Remote</th>
        <th>Floor</th>
        <th>Set</th>
        <th>Status</th>
        </tr>
        
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
