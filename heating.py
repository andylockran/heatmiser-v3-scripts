#
# Neil Trimboy 2011
# Assume Pyhton 2.7.x
#
import serial
from struct import pack
import time
import sys
import os
import shutil

# Import our own stuff
from stats_defn import *
from hm_constants import *
from hm_utils import *
from mail_utils import *
from comms_settings import *

# CODE STARTS HERE

DATAOFFSET = 9 # ToDO Move this higher up and and define what it is, put in another file

# @todo Define magic numbers used in messages

# Acceptable error in time (s)
TIME_ERR_LIMIT = 60

problem = 0

interval = 600 # 10 mins
interval = str(interval)
interval_mins = float(interval) / 60
heartbeat = str(int(interval) * 2)
rrdfile = 'hmstats.rrd'
if (not os.path.exists(rrdfile)):
    print "Creating file %s" % (rrdfile)
    cmd_create = "rrdtool create %s --step %s" % (rrdfile, interval)
    cmd_create += " DS:outdr:GAUGE:%s:-20:100" % (heartbeat)
    for controller in StatList:
        cmd_create += " DS:%sair:GAUGE:%s:-20:100" % (controller[1], heartbeat)
        cmd_create += " DS:%sflr:GAUGE:%s:-20:100" % (controller[1], heartbeat)
        cmd_create += " DS:%sset:GAUGE:%s:-20:100" % (controller[1], heartbeat)
        cmd_create += " DS:%sdem:GAUGE:%s:0:1" % (controller[1], heartbeat)
    cmd_create +=  ' RRA:AVERAGE:0.5:1:262800'
    cmd_create +=  ' RRA:MAX:0.5:1:262800'

    print cmd_create
    cmd = os.popen4(cmd_create)
    cmd_output = cmd[1].read()
    for fd in cmd: fd.close()
    if len(cmd_output) > 0:
        print cmd_output

# Now one for Optimum Start
interval = 600
interval = str(interval)
interval_mins = float(interval) / 60
heartbeat = str(int(interval) * 2)
rrdrocfile = 'hmoptimstart.rrd'
if (not os.path.exists(rrdrocfile)):
    print "Creating file %s" % (rrdrocfile)
    cmd_create = "rrdtool create %s --step %s" % (rrdrocfile, interval)
    for controller in StatList:
        cmd_create += " DS:%sroc:GAUGE:%s:0:255" % (controller[1], heartbeat)
        cmd_create += " DS:%soptimstart:GAUGE:%s:0:3" % (controller[1], heartbeat)
    cmd_create +=  ' RRA:AVERAGE:0.5:1:262800'

    print cmd_create
    cmd = os.popen4(cmd_create)
    cmd_output = cmd[1].read()
    for fd in cmd: fd.close()
    if len(cmd_output) > 0:
        print cmd_output

# Now one for TimeError
interval = 600
interval = str(interval)
interval_mins = float(interval) / 60
heartbeat = str(int(interval) * 2)
rrdtimeerrfile = 'hmtimedelta.rrd'
if (not os.path.exists(rrdtimeerrfile)):
    print "Creating file %s" % (rrdtimeerrfile)
    cmd_create = "rrdtool create %s --step %s" % (rrdtimeerrfile, interval)
    for controller in StatList:
        cmd_create += " DS:%stimedelta:GAUGE:%s:-172800:172800" % (controller[1], heartbeat)
    cmd_create +=  ' RRA:AVERAGE:0.5:1:262800'

    print cmd_create
    cmd = os.popen4(cmd_create)
    cmd_output = cmd[1].read()
    for fd in cmd: fd.close()
    if len(cmd_output) > 0:
        print cmd_output

# Now one for Load
interval = 600
interval = str(interval)
interval_mins = float(interval) / 60
heartbeat = str(int(interval) * 2)
rrdloadfile = 'hmload.rrd'
if (not os.path.exists(rrdloadfile)):
    print "Creating file %s" % (rrdloadfile)
    cmd_create = "rrdtool create %s --step %s" % (rrdloadfile, interval)
    cmd_create += " DS:zoneload:GAUGE:%s:0:1000" % (heartbeat)
    cmd_create += " DS:circuitload:GAUGE:%s:0:1000" % (heartbeat)
    cmd_create += " DS:areaload:GAUGE:%s:0:1000" % (heartbeat)
    cmd_create +=  ' RRA:MAX:0.5:1:262800'

    print cmd_create
    cmd = os.popen4(cmd_create)
    cmd_output = cmd[1].read()
    for fd in cmd: fd.close()
    if len(cmd_output) > 0:
        print cmd_output

# Generate a RFC2822 format date
# This works with both Excel and Timeline
localtime = time.asctime( time.localtime(time.time()))
polltime = time.time()
polltimet = time.localtime(polltime)
localtime = time.strftime("%d %b %Y %H:%M:%S +0000", polltimet)
localday = time.strftime("%w", polltimet)

d = os.path.join(os.getcwd(),"logs")
if not os.path.exists(d):
    os.makedirs(d)

dbup = os.path.join(os.getcwd(),"backup")
if not os.path.exists(dbup):
    os.makedirs(dbup)

fname = time.strftime("errorlog_%Y%m%d.txt", polltimet)
ffullname = os.path.join(d,fname)

buname = time.strftime("hmstats_%Y%m%d.rrd", polltimet)
bufullname = os.path.join(dbup,buname)
if (not os.path.exists(bufullname)):
    # Backup not yet performed
    print "Looks like a new day"
    startofday = 1
else:
    startofday = 0

#ferr = open(ffullname, 'a')
# TODO Catch file not opened
#sys.stderr = open(ffullname, 'a')  # Redirect stderr



fcsvfile = 'heatmiser_status.csv'

statusfile = 'heatmiser_status.xml'

if startofday == 1:
    if (os.path.exists(rrdrocfile)):
        print "Backing up files"
        shutil.copy2(rrdfile,bufullname)
        buname = time.strftime("hmoptimstart%Y%m%d.rrd", polltimet)
        bufullname = os.path.join(dbup,buname)
        shutil.copy2(rrdrocfile,bufullname)

    if (os.path.exists(fcsvfile)):
        print "Backing up files"
        buname = time.strftime("heatmiser_status%Y%m%d.csv", polltimet)
        bufullname = os.path.join(dbup,buname)
        print buname
        print bufullname
        print fcsvfile
        shutil.copy2(fcsvfile,bufullname)

    if (os.path.exists(statusfile)):
        print "Backing up files"
        buname = time.strftime("heatmiser_status%Y%m%d.xml", polltimet)
        bufullname = os.path.join(dbup,buname)
        print buname
        print bufullname
        print statusfile
        shutil.copy2(statusfile,bufullname)

        # @todo backup load rrd

serport = serial.Serial()
serport.port = COM_PORT
serport.baudrate = COM_BAUD
serport.bytesize = COM_SIZE
serport.parity = COM_PARITY
serport.stopbits = COM_STOP
serport.timeout = COM_TIMEOUT
try:
    serport.open()
except serial.SerialException, e:
        sys.stderr.write("Could not open serial port %s: %s\n" % (serport.portstr, e))
        s= "%s : Could not open serial port %s: %s\n" % (localtime, serport.portstr, e)
        sys.stderr.write(s)
        problem += 1
        mail(email_settings.email_to_addr, "Heatmiser Polling Error ", "Could not open serial port", "errorlog.txt")
        sys.exit(1) # TODO this doesnt seem to exit

print "%s port configuration is %s" % (serport.name, serport.isOpen())
print "%s baud, %s bit, %s parity, with %s stopbits, timeout %s seconds" % (serport.baudrate, serport.bytesize, serport.parity, serport.stopbits, serport.timeout)

number_of_controllers = len(StatList)
print "No of controllers is %d" % (number_of_controllers)
# How initialise good and bad to zero?
#good = 0
#bad = 0
# @todo Remove good and bad
good = [0,0,0,0,0,0,0,0,0,0,0,0,0] #one bigger than size required
bad =  [0,0,0,0,0,0,0,0,0,0,0,0,0]
remoteairtemp = range(number_of_controllers+1)
floortemp = range(number_of_controllers+1)
intairtemp = range(number_of_controllers+1)
demand = range(number_of_controllers+1)
settemp = range(number_of_controllers+1)
result = range(number_of_controllers+1)
sensormode = range(number_of_controllers+1)
badresponse = range(number_of_controllers+1)
unhealthy = range(number_of_controllers+1)
optimstart = range(number_of_controllers+1)
rateofchange = range(number_of_controllers+1)
timeerr = range(number_of_controllers+1)

# CYCLE THROUGH number_of_controllers CONTROLLERS
f = open(statusfile, 'w')

f.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
f.write('<poll xmlns="http://www.example.org/history" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.example.org/history history.xsd ">\n')
f.write('<!-- This is a comment-->\n')
s = '<!-- Generated at ' + localtime + ' -->\n'
f.write(s)
f.write("<polltime>\n")
f.write("<day>" + time.strftime("%d", polltimet) + "</day>\n")
f.write("<month>" + time.strftime("%m", polltimet) + "</month>\n")
f.write("<year>" + time.strftime("%Y", polltimet) + "</year>\n")
f.write("<hour>" + time.strftime("%H", polltimet) + "</hour>\n")
f.write("<minutes>" + time.strftime("%M", polltimet) + "</minutes>\n")
f.write("<seconds>" + time.strftime("%S", polltimet) + "</seconds>\n")
f.write("<unixtime>" + str(polltime) + "</unixtime>\n")
f.write("<readable>" + localtime + "</readable>\n")
f.write("</polltime>\n")
# CYCLE THROUGH ALL CONTROLLERS
for controller in StatList:
    loop = controller[SL_ADDR] #BUG assumes statlist is addresses are 1...n, with no gaps or random
    print
    print loop
    print "Testing control ID %2d in %s *****************************" % (loop, controller[SL_LONG_NAME])
    badresponse[loop] = 0
    unhealthy[loop] = 0
    # TODO is not V3 controller raise error
    destination = controller[SL_ADDR]
    if startofday == 1:
        hmUpdateTime(destination, serport)
    start_low = 0
    start_high = 0
    read_length_high = (RW_LENGTH_ALL & 0xff)
    read_length_low = (RW_LENGTH_ALL >> 8) & 0xff
    # data = [destination, 0x0a, MY_MASTER_ADDR, FUNC_READ, start_low, start_high, read_length_low, read_length_high]
    # There is an implicit read ALL in the hmFormMsgCRC method
    # @todo The 0 below is a magic nmbe which should be replaced
    data = hmFormMsgCRC(destination, controller[SL_CONTR_TYPE], MY_MASTER_ADDR, FUNC_READ, 0, [])
    print data
    # http://stackoverflow.com/questions/180606/how-do-i-convert-a-list-of-ascii-values-to-a-string-in-python
    string = ''.join(map(chr,data))

    #Now try converting it back
    datal = []
    datal = datal + (map(ord,string))
    #print datal
    msgsenttime = time.strftime("%H:%M:%S", time.localtime(time.time()))
    #print msgsenttime
    try:
        written = serport.write(string)  # Write a string
    except serial.SerialTimeoutException, e:
        sys.stderr.write("Write timeout error: %s\n" % (e))
        s= "%s : Write timeout error: %s\n" % (localtime, e)
        sys.stderr.write(s)
        badresponse[loop] += 1
        errortext = "COM Port Error"

    # Now wait for reply
    byteread = serport.read(100)	# NB max return is 75 in 5/2 mode or 159 in 7day mode, this does not yet supt 7 day
    #print "Bytes read %d" % (len(byteread) )
    #TODO checking for correct length here can be removed
    # TODO But we should check for no response
    if (len(byteread)) == 0:
        print  "No reply received"
        badresponse[loop] += 1
        errortext = "No Response"
    else:
        # TODO All this should only happen if correct length reply
        #Now try converting it back to array
        datal = []
        datal = datal + (map(ord,byteread))
        if (hmVerifyMsgCRCOK(MY_MASTER_ADDR, controller[SL_CONTR_TYPE], destination, FUNC_READ, 75, datal) == False):
            badresponse[loop] += 1
            errortext = "Msg check fail"

    if (badresponse[loop]== 0):
        # Should really only be length 75 or TBD at this point as we shouldnt do this if bad resp
        # @todo define magic number 75 in terms of header and possible payload sizes
        # @todo value in next line of 120 is a wrong guess
        # @todo put all the offset constants into other file/constants
        if ((len(byteread)) == 75) or ((len(byteread)) == 120):

            vendor = datal[2+ DATAOFFSET]
            version = datal[3+ DATAOFFSET] & 0x7f
            floorlimiting = datal[3+ DATAOFFSET] >> 7
            model = datal[4+ DATAOFFSET]
            tempfmt = datal[5+ DATAOFFSET]
            switchdiff = datal[6+ DATAOFFSET]
            frostprot = datal[7+ DATAOFFSET]
            cal_h=datal[8+ DATAOFFSET]
            cal_l = datal[9+ DATAOFFSET]
            caloffset = (cal_h*256 + cal_l)
            opdelay = datal[10+ DATAOFFSET]
            address = datal[11+ DATAOFFSET]
            updwnlimit = datal[12+ DATAOFFSET]
            thissensormode = datal[13+ DATAOFFSET]
            optimstart[loop] = datal[14+ DATAOFFSET]
            rateofchange[loop] = datal[15+ DATAOFFSET]
            progmode = datal[16+ DATAOFFSET]
            frosttemp = datal[17+ DATAOFFSET]
            roomset = datal[18+ DATAOFFSET]
            floorlimit = datal[19+ DATAOFFSET]
            floormaxenable = datal[20+ DATAOFFSET]
            onoff = datal[21+ DATAOFFSET]
            keylock = datal[22+ DATAOFFSET]
            runmode = datal[23+ DATAOFFSET]
            holidayhourshigh = datal[24+ DATAOFFSET]
            holidayhourslow = datal[25+ DATAOFFSET]
            holidayhours = (holidayhourshigh*256 + holidayhourslow)
            tempholdminshigh = datal[26+ DATAOFFSET]
            tempholdminslow = datal[27+ DATAOFFSET]
            tempholdmins = (tempholdminshigh*256 + tempholdminslow)
            remoteairtemphigh = datal[28+ DATAOFFSET]
            remoteairtemplow  = datal[29+ DATAOFFSET]
            remoteairtemp[loop] = (remoteairtemphigh*256 + remoteairtemplow)/10.0
            floortemphigh = datal[30+ DATAOFFSET]
            floortemplow  = datal[31+ DATAOFFSET]
            floortemp[loop] = (floortemphigh*256 + floortemplow)/10.0
            intairtemphigh = datal[32+ DATAOFFSET]
            intairtemplow  = datal[33+ DATAOFFSET]
            intairtemp[loop] = (intairtemphigh*256 + intairtemplow)/10.0
            errcode = datal[34+ DATAOFFSET]
            thisdemand = datal[35+ DATAOFFSET]
            currentday = datal[36+ DATAOFFSET]
            currenthour = datal[37+ DATAOFFSET]
            currentmin = datal[38+ DATAOFFSET]
            currentsec = datal[39+ DATAOFFSET]
            wday_t1_hour = datal[40+ DATAOFFSET]
            wday_t1_mins = datal[41+ DATAOFFSET]
            wday_t1_temp = datal[42+ DATAOFFSET]
            wday_t2_hour = datal[43+ DATAOFFSET]
            wday_t2_mins = datal[44+ DATAOFFSET]
            wday_t2_temp = datal[45+ DATAOFFSET]
            wday_t3_hour = datal[46+ DATAOFFSET]
            wday_t3_mins = datal[47+ DATAOFFSET]
            wday_t3_temp = datal[48+ DATAOFFSET]
            wday_t4_hour = datal[49+ DATAOFFSET]
            wday_t4_mins = datal[50+ DATAOFFSET]
            wday_t4_temp = datal[51+ DATAOFFSET]
            wend_t1_hour = datal[52+ DATAOFFSET]
            wend_t1_mins = datal[53+ DATAOFFSET]
            wend_t1_temp = datal[54+ DATAOFFSET]
            wend_t2_hour = datal[55+ DATAOFFSET]
            wend_t2_mins = datal[56+ DATAOFFSET]
            wend_t2_temp = datal[57+ DATAOFFSET]
            wend_t3_hour = datal[58+ DATAOFFSET]
            wend_t3_mins = datal[59+ DATAOFFSET]
            wend_t3_temp = datal[60+ DATAOFFSET]
            wend_t4_hour = datal[61+ DATAOFFSET]
            wend_t4_mins = datal[62+ DATAOFFSET]
            wend_t4_temp = datal[63+ DATAOFFSET]
            result[loop] = datal
            demand[loop] = thisdemand
            settemp[loop] = roomset
            sensormode[loop] = thissensormode
        # @todo next value 120 is a guess
        if ((len(byteread)) == 120):
            # Extract the 7day times
            # @todo put this in 2D array with index for day using for loop
            mon_t1_hour = datal[52+ DATAOFFSET]
            mon_t1_mins = datal[53+ DATAOFFSET]
            mon_t1_temp = datal[54+ DATAOFFSET]
            mon_t2_hour = datal[55+ DATAOFFSET]
            mon_t2_mins = datal[56+ DATAOFFSET]
            mon_t2_temp = datal[57+ DATAOFFSET]
            mon_t3_hour = datal[58+ DATAOFFSET]
            mon_t3_mins = datal[59+ DATAOFFSET]
            mon_t3_temp = datal[60+ DATAOFFSET]
            mon_t4_hour = datal[61+ DATAOFFSET]
            mon_t4_mins = datal[62+ DATAOFFSET]
            mon_t4_temp = datal[63+ DATAOFFSET]
        # Now check for any failure condiions
        #if errcode != 0
        #	print "Controller in error"
        #print "%d %d %d %d %d %d" % (remoteairtemphigh, remoteairtemplow, floortemphigh, floortemplow, intairtemphigh, intairtemplow)
        print "Sensor %d Temp is %.1f and %.1f and %.1f Set to %d Demand %d" % (address, intairtemp[loop], remoteairtemp[loop], floortemp[loop], settemp[loop], thisdemand)
        # Now do same sanity checking
        # Check the time is within range
        # If we only do this at say 1 am then there is no issues/complication of day wrap rounds
        # TODO only do once a day
        # currentday is numbered 1-7 for M-S
        # localday (pyhton) is numbered 0-6 for Sun-Sat
        if (int(localday) != int((currentday%7))):
            s= "%s : Controller %2d : Incorrect day : local is %s, sensor is %s\n" % (localtime, loop, localday, currentday)
            sys.stderr.write(s)
            unhealthy[loop] += 1
            # TODO ++ here
        remoteseconds = (((currenthour * 60) + currentmin) * 60) + currentsec

        nowhours = time.localtime(time.time()).tm_hour
        nowmins = time.localtime(time.time()).tm_min
        nowsecs = time.localtime(time.time()).tm_sec
        nowseconds = (((nowhours * 60) + nowmins) * 60) + nowsecs
        print "Time %d %d" % (remoteseconds, nowseconds)
        timeerr[loop] = nowseconds - remoteseconds
        if (abs(timeerr[loop]) > TIME_ERR_LIMIT):
            s= "%s %s : Controller %2d : Time Error : Greater than %d local is %s, sensor is %s\n" % (startofday, localtime, loop, TIME_ERR_LIMIT, nowseconds, remoteseconds)
            sys.stderr.write(s)
            unhealthy[loop] += 1
            # TODO ++ here

    # END correct length

    print "Controller %2d Good %d Bad %d" % (loop, good[loop], bad[loop])
    if (badresponse[loop]== 0):
        f.write('<controller>\n')
        f.write("<locationlong>" + controller[SL_LONG_NAME] + "</locationlong>\n")
        f.write("<locationshort>" + controller[SL_SHRT_NAME] + "</locationshort>\n")
        f.write("<health>GOOD</health>\n")
        f.write("<ident>" + repr(address) + "</ident>\n")
        f.write("<vendor>" + repr(vendor) + "</vendor>\n")
        f.write("<version>" + repr(version) + "</version>\n")
        f.write("<floorlimiting>" + repr(floorlimiting) + "</floorlimiting>\n")
        f.write("<model>" + repr(model) + "</model>\n")
        f.write("<tempfmt>" + repr(tempfmt) + "</tempfmt>\n")
        f.write("<switchdiff>" + repr(switchdiff) + "</switchdiff>\n")
        f.write("<frostprot>" + repr(frostprot) + "</frostprot>\n")
        f.write("<caloffset>" + repr(caloffset) + "</caloffset>\n")
        f.write("<opdelay>" + repr(opdelay) + "</opdelay>\n")
        f.write("<address>" + repr(address) + "</address>\n")
        f.write("<updwnlimit>" + repr(updwnlimit) + "</updwnlimit>\n")
        f.write("<sensormode>" + repr(thissensormode) + "</sensormode>\n")
        f.write("<optimstart>" + repr(optimstart[loop]) + "</optimstart>\n")
        f.write("<rateofchange>" + repr(rateofchange[loop]) + "</rateofchange>\n")
        f.write("<progmode>" + repr(progmode) + "</progmode>\n")
        f.write("<frosttemp>" + repr(frosttemp) + "</frosttemp>\n")
        f.write("<roomset>" + repr(roomset) + "</roomset>\n")
        f.write("<floorlimit>" + repr(floorlimit) + "</floorlimit>\n")
        f.write("<floormaxenable>" + repr(floormaxenable) + "</floormaxenable>\n")
        f.write("<onoff>" + repr(onoff) + "</onoff>\n")
        f.write("<keylock>" + repr(keylock) + "</keylock>\n")
        f.write("<runmode>" + repr(runmode) + "</runmode>\n")
        f.write("<holidayhours>" + repr(holidayhours) + "</holidayhours>\n")
        f.write("<tempholdmins>" + repr(tempholdmins) + "</tempholdmins>\n")
        f.write("<remtemp>" + repr(remoteairtemp[loop]) + "</remtemp>\n")
        f.write("<floortemp>" + repr(floortemp[loop]) + "</floortemp>\n")
        f.write( "<airtemp>" + repr(intairtemp[loop]) + "</airtemp>\n")
        f.write("<errcode>" + repr(errcode) + "</errcode>\n")
        f.write("<thisdemand>" + repr(thisdemand) + "</thisdemand>\n")
        f.write("<time>\n")
        f.write("<day>" + repr(currentday) + "</day>\n")
        f.write("<hour>" + repr(currenthour) + "</hour>\n")
        f.write("<min>" + repr(currentmin) + "</min>\n")
        f.write("<sec>" + repr(currentsec) + "</sec>\n")
        f.write("</time>\n")
        f.write("<wday_t1_hour>" + repr(wday_t1_hour) + "</wday_t1_hour>\n")
        f.write("<wday_t1_mins>" + repr(wday_t1_mins) + "</wday_t1_mins>\n")
        f.write("<wday_t1_temp>" + repr(wday_t1_temp) + "</wday_t1_temp>\n")
        f.write("<wday_t2_hour>" + repr(wday_t2_hour) + "</wday_t2_hour>\n")
        f.write("<wday_t2_mins>" + repr(wday_t2_mins) + "</wday_t2_mins>\n")
        f.write("<wday_t2_temp>" + repr(wday_t2_temp) + "</wday_t2_temp>\n")
        f.write("<wday_t3_hour>" + repr(wday_t3_hour) + "</wday_t3_hour>\n")
        f.write("<wday_t3_mins>" + repr(wday_t3_mins) + "</wday_t3_mins>\n")
        f.write("<wday_t3_temp>" + repr(wday_t3_temp) + "</wday_t3_temp>\n")
        f.write("<wday_t4_hour>" + repr(wday_t4_hour) + "</wday_t4_hour>\n")
        f.write("<wday_t4_mins>" + repr(wday_t4_mins) + "</wday_t4_mins>\n")
        f.write("<wday_t4_temp>" + repr(wday_t4_temp) + "</wday_t4_temp>\n")
        f.write("<wend_t1_hour>" + repr(wend_t1_hour) + "</wend_t1_hour>\n")
        f.write("<wend_t1_mins>" + repr(wend_t1_mins) + "</wend_t1_mins>\n")
        f.write("<wend_t1_temp>" + repr(wend_t1_temp) + "</wend_t1_temp>\n")
        f.write("<wend_t2_hour>" + repr(wend_t2_hour) + "</wend_t2_hour>\n")
        f.write("<wend_t2_mins>" + repr(wend_t2_mins) + "</wend_t2_mins>\n")
        f.write("<wend_t2_temp>" + repr(wend_t2_temp) + "</wend_t2_temp>\n")
        f.write("<wend_t3_hour>" + repr(wend_t3_hour) + "</wend_t3_hour>\n")
        f.write("<wend_t3_mins>" + repr(wend_t3_mins) + "</wend_t3_mins>\n")
        f.write("<wend_t3_temp>" + repr(wend_t3_temp) + "</wend_t3_temp>\n")
        f.write("<wend_t4_hour>" + repr(wend_t4_hour) + "</wend_t4_hour>\n")
        f.write("<wend_t4_mins>" + repr(wend_t4_mins) + "</wend_t4_mins>\n")
        f.write("<wend_t4_temp>" + repr(wend_t4_temp) + "</wend_t4_temp>\n")
        f.write("</controller>\n")
    else:
        f.write('<controller>\n')
        f.write("<locationlong>" + controller[SL_LONG_NAME] + "</locationlong>\n")
        f.write("<locationshort>" + controller[SL_SHRT_NAME] + "</locationshort>\n")
        f.write("<health reason=\"" + errortext + "\">BAD</health>\n")
        f.write("</controller>\n")
        
    problem += badresponse[loop]
    loop = loop+1 # Change to for loop TODO not used

    time.sleep(2) # sleep for 2 seconds before next controller

# Cycle round controllers complete
f.write('</poll>\n')
f.close()

fcsv = open(fcsvfile, 'a')
s= localtime + ','
fcsv.write(s)

for loop in range(1, number_of_controllers + 1):
    # TODO cope with bad response here
    if(badresponse[loop] == 0):
        print "Sensor %2d Temp is %d and %d and %d" % (loop, intairtemp[loop], remoteairtemp[loop], floortemp[loop])
        s=repr(loop) +',' + repr(intairtemp[loop])  + ',' + repr(remoteairtemp[loop]) + ',' +repr(floortemp[loop]) + ',' + repr(settemp[loop]) +',' + repr(demand[loop]) +','
        fcsv.write(s)
    else:
        print "Sensor %2d is dead" % (loop)
        s=repr(loop) +',' + '#N/A,' + '#N/A,' + '#N/A,' + '#N/A,' + '#N/A,'
        fcsv.write(s)
fcsv.write('x\n')
fcsv.close()


cmd_update =  "rrdtool update %s N:0" % (rrdfile)
for controller in StatList:
    if (badresponse[controller[0]] ==0) :
        if (sensormode[controller[0]] == 3):
            cmd_update += ":%s" % (intairtemp[controller[0]])
        else:
            cmd_update += ":%s" % (remoteairtemp[controller[0]])
        cmd_update += ":%s" % (floortemp[controller[0]])
        cmd_update += ":%s" % (settemp[controller[0]])
        cmd_update += ":%s" % (demand[controller[0]])    
    else:
        cmd_update += ":U:U:U:U"

print cmd_update
cmd = os.popen4(cmd_update)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
    print cmd_output

#Update the rate of change
cmd_update =  "rrdtool update %s N" % (rrdrocfile)
for controller in StatList:
    if (badresponse[controller[0]] == 0) :
        cmd_update += ":%s" % (rateofchange[controller[0]])
        cmd_update += ":%s" % (optimstart[controller[0]])
    else:
        cmd_update += ":U:U"

print cmd_update
cmd = os.popen4(cmd_update)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
    print cmd_output

#Update the time error
cmd_update =  "rrdtool update %s N" % (rrdtimeerrfile)
for controller in StatList:
    if (badresponse[controller[0]] == 0) :
        cmd_update += ":%s" % (timeerr[controller[0]])
    else:
        cmd_update += ":U"

print cmd_update
cmd = os.popen4(cmd_update)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
    print cmd_output

#Update load
cmd_update =  "rrdtool update %s N" % (rrdloadfile)
zoneload = 0
circuitload = 0
areaload = 0
ohdearerror = 0
for controller in StatList:
    print "controller %d" % controller[0]
    if (badresponse[controller[0]] == 0) :
        if (demand[controller[0]] == 1) :
            zoneload += 1
            zone_area = 0
            for circuit in controller[SL_CIRCUITS]:
                circuit_area = 0
                circuitload += 1
                print "Circuit %d %s" % (circuit, CircuitList[circuit-1][CL_SHRT_NAME])
    # Would be best to lookup rather than index here
                for rectangle in CircuitList[circuit-1][CL_RECTANGLES]:
                    print rectangle
                    rect_area = rectangle[0]*rectangle[1]
                    print "rect area %f" % rect_area
                    circuit_area += rect_area
                zone_area += circuit_area
                print "circuit area %f" % circuit_area
            print "zone area %f" % zone_area
            areaload += zone_area
    else:
        ohdearerror = 1

if (ohdearerror == 0) :
    cmd_update += ":%s" % (zoneload)
    cmd_update += ":%s" % (circuitload)
    cmd_update += ":%s" % (areaload)
else :
    cmd_update += ":U:U:U"

print cmd_update
cmd = os.popen4(cmd_update)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
    print cmd_output

#END OF CYCLE THROUGH CONTROLLERS

# Now do some tidying up of loose ends
# @todo still some files to close I think
serport.close() # close port
print "Port is now %s" % serport.isOpen()
#ferr.close()
#

if (problem > 0):
    print "Emailing error reprt"
    mail(email_settings.email_to_addr, "Heatmiser Polling Error ", "A Problem has occurred", ffullname)
