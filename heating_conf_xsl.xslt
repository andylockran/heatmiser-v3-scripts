<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:t="http://www.example.org/history">
    <xsl:template match="/">
        <!-- TODO: Auto-generated template -->
        <html>
        <head>
        <title>Heating Configuration</title>
        <link rel="shortcut icon" href="favicon.ico" />
        <link rel="stylesheet" href="heating_status.css"></link>    
        </head>
        <body>
        <a NAME="Top"></a>
        <br/><a HREF="#Bottom">Bottom</a>
        <table border="1" width="100%">
        <tr>
        <th>ident</th>
        <th>address</th>
        <th>vendor</th>
        <th>version</th>
        <th>model</th>
        <th>tempfmt</th>
        <th>switchdiff</th>
        <th>frostprot</th>
        <th>frosttemp</th>
        <th>caloffset</th>
        <th>opdelay</th>
        <th>updwnlimit</th>
        <th>sensormode</th>
        <th>optimstart</th>
        <th>rateofchange<br/>mins/<sup>o</sup>C</th>
        <th>progmode</th>
        <th>roomset</th>
        <th>floormaxenable</th>
        <th>floorlimit</th>
        <th>floorlimiting</th>
        <th>Display</th>
        <th>keylock</th>
        <th>runmode</th>
        <th>Holiday Mode<br></br>Days-Hrs {TotalHrs}</th>
        <th>temphold<sub>mins</sub><br></br>Hrs:Mins</th>
        <th>remtemp</th>
        <th>floortemp</th>
        <th>airtemp</th>
        <th>errcode</th>
        <th>thisdemand</th>
        <th>day</th>
        <th>time (h:m:s)</th>
        </tr>
        <xsl:for-each select="t:poll/t:controller">
            <tr>
                <xsl:call-template name="alternated-row" />
                <td title="location">
                    <xsl:value-of select="./t:locationlong" /><sub><xsl:value-of select="./t:ident" /></sub>
                </td>
                <td title="address">
                    <xsl:value-of select="./t:address" />
                </td>
                <td title="vendor">
                    <xsl:choose>
                        <xsl:when test="./t:vendor = 0">HM</xsl:when>
                        <xsl:when test="./t:vendor = 1">OEM</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="version">
                    <xsl:value-of select="./t:version" />
                </td>
                <td title="model">
                    <xsl:choose>
                        <xsl:when test="./t:model = 0">DT</xsl:when>
                        <xsl:when test="./t:model = 1">DT-E</xsl:when>
                        <xsl:when test="./t:model = 2">PRT</xsl:when>
                        <xsl:when test="./t:model = 3">PRT-E</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="tempfmt">
                    <xsl:choose>
                        <xsl:when test="./t:tempfmt = 0"><sup>o</sup>C</xsl:when>
                        <xsl:when test="./t:tempfmt = 1"><sup>o</sup>F</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="switchdiff">
                    <xsl:value-of select="./t:switchdiff" /><sup>o</sup>
                </td>
                <td title="frostprot">
                    <xsl:choose>
                        <xsl:when test="./t:frostprot = 0">Off</xsl:when>
                        <xsl:when test="./t:frostprot = 1">On</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="frosttemp">
                    <xsl:value-of select="./t:frosttemp" /><sup>o</sup>
                </td>
                <td title="caloffset">
                    <xsl:value-of select="./t:caloffset" />
                </td>
                <td title="opdelay">
                    <xsl:value-of select="./t:opdelay" />
                </td>
                <td title="updwnlimit">
                    <xsl:value-of select="./t:updwnlimit" /><sup>o</sup>
                </td>
                <td title="sensormode">
                    <xsl:choose>
                        <xsl:when test="./t:sensormode = 0"><img src="images/sensor_mode_int.png" alt="IntAir" height="32" width="36"></img></xsl:when>
                        <xsl:when test="./t:sensormode = 1"><img src="images/sensor_mode_rem.png" alt="RemAir" height="32" width="36"></img></xsl:when>
                        <xsl:when test="./t:sensormode = 2"><img src="images/sensor_mode_floor.png" alt="Floor" height="32" width="36"></img></xsl:when>
                        <xsl:when test="./t:sensormode = 3"><img src="images/sensor_mode_int_floor.png" alt="IntAir+Floor" height="32" width="36"></img></xsl:when>
                        <xsl:when test="./t:sensormode = 4"><img src="images/sensor_mode_rem_floor.png" alt="RemAir+Floor" height="32" width="36"></img></xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="optimstart">
                    <xsl:choose>
                        <xsl:when test="./t:optimstart = 0">OFF</xsl:when>
                        <xsl:otherwise><xsl:value-of select="./t:optimstart" /> Hrs</xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="rateofchange">
                    <xsl:value-of select="./t:rateofchange" />
                </td>
                <td title="progmode">
                    <xsl:choose>
                        <xsl:when test="./t:progmode = 0">5/2 Day</xsl:when>
                        <xsl:when test="./t:progmode = 1">7 Day</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="roomset">
                    <xsl:value-of select="./t:roomset" /><sup>o</sup>
                </td>
                <td title="floormaxenable">
                    <xsl:choose>
                        <xsl:when test="./t:floormaxenable = 0">Off</xsl:when>
                        <xsl:when test="./t:floormaxenable = 1">On</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="floorlimit">
                    <xsl:value-of select="./t:floorlimit" /><sup>o</sup>
                </td>
                <td title="floorlimiting">
                    <xsl:choose>
                        <xsl:when test="./t:floorlimiting = 0">No</xsl:when>
                        <xsl:when test="./t:floorlimiting = 1">Yes</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="onoff">
                    <xsl:choose>
                        <xsl:when test="./t:onoff = 0">Off</xsl:when>
                        <xsl:when test="./t:onoff = 1">On</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="keylock">
                    <xsl:choose>
                        <xsl:when test="./t:keylock = 0">Unlock</xsl:when>
                        <xsl:when test="./t:keylock = 1">Locked</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                     
                </td>
                <td title="runmode">
                    <xsl:choose>
                        <xsl:when test="./t:runmode = 0">Normal</xsl:when>
                        <xsl:when test="./t:runmode = 1">Frost</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="holidayhours">
                    <xsl:choose>
                        <xsl:when test="./t:holidayhours = 0">
                            <!-- Holiday Mode is OFF -->
                            OFF
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="floor(./t:holidayhours div 24)" />-<xsl:value-of select="./t:holidayhours mod 24" />
                            {<xsl:value-of select="./t:holidayhours" />}
                        </xsl:otherwise>
                    </xsl:choose>
                </td>
                <td title="tempholdmins">
                    <xsl:choose>
                        <xsl:when test="./t:tempholdmins = 0">
                            <!-- Temp Hold is OFF -->
                            OFF
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:variable name="holdmins"><xsl:value-of select="./t:tempholdmins" /> mins</xsl:variable>
                            <img src="images/clock.png" alt="{$holdmins}" height="24" width="24"></img>
                            <xsl:variable name="holdminsmod60"><xsl:value-of select="./t:tempholdmins  mod 60" /></xsl:variable>
                            (<xsl:value-of select="floor(./t:tempholdmins div 60)" />:<xsl:value-of select='format-number($holdminsmod60, "00")' />)
                        </xsl:otherwise>
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
                <td title="errcode">
                    <xsl:choose>
                        <!-- TODO: Not sure if these are correct error codes -->
                        <xsl:when test="./t:errcode = 0">OK</xsl:when>
                        <xsl:when test="./t:errcode = 224"><img src="images/maintenance.png" alt="IntAir" height="48" width="48"></img>IntAir</xsl:when>
                        <xsl:when test="./t:errcode = 225"><img src="images/maintenance.png" alt="Floor" height="48" width="48"></img>Floor</xsl:when>
                        <xsl:when test="./t:errcode = 225"><img src="images/maintenance.png" alt="RemAir" height="48" width="48"></img>RemAir</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                     
                </td>
                <td title="thisdemand">
                    <xsl:value-of select="./t:thisdemand" />
                </td>
                <td title="day">
                    <xsl:choose>
                        <xsl:when test="./t:time/t:day = 1">Mon</xsl:when>
                        <xsl:when test="./t:time/t:day = 2">Tue</xsl:when>
                        <xsl:when test="./t:time/t:day = 3">Wed</xsl:when>
                        <xsl:when test="./t:time/t:day = 4">Thu</xsl:when>
                        <xsl:when test="./t:time/t:day = 5">Fri</xsl:when>
                        <xsl:when test="./t:time/t:day = 6">Sat</xsl:when>
                        <xsl:when test="./t:time/t:day = 7">Sun</xsl:when>
                        <xsl:otherwise>UNKNWON</xsl:otherwise>
                    </xsl:choose>                    
                </td>
                <td title="time">
                    <xsl:value-of select='format-number(./t:time/t:hour, "00")' />:<xsl:value-of select='format-number(./t:time/t:min, "00")' />:<xsl:value-of select='format-number(./t:time/t:sec, "00")' />
                </td>
            </tr>
                        
        </xsl:for-each>

        <!-- TODO Put another set of th headers here -->
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
