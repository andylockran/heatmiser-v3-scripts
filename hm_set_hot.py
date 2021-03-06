#
# Neil Trimboy 2011
#
# Sets all controllers to Locked
#
# Despite Heatmiser V3 protocol document stating that current day/h/m/s is on 4 separate addresses [43,46]
# Tests showed that it was not possible to write to individual value anf that all 4 values must be written in a single command
import serial
from struct import pack
import time
import sys
import os

from stats_defn import *
from hm_constants import *
from hm_utils import *
from comms_settings import *

# CODE STARTS HERE

problem = 0

#ferr = open('errorlog2.txt', 'a')
sys.stderr = open('errorlog.txt', 'a') # Redirect stderr

# Generate a RFC2822 format date
localtime = time.asctime( time.localtime(time.time()))
polltime  = time.time()
polltimet = time.localtime(polltime)
localtime = time.strftime("%d %b %Y %H:%M:%S +0000", polltimet)
localday  = time.strftime("%w", polltimet)

#serport = serial.Serial()
serport = serial.serial_for_url("socket://192.168.1.155:1001/logging=debug")
serport.close()
#serport.port = COM_PORT
serport.baudrate = COM_BAUD
serport.bytesize = COM_SIZE
serport.parity = COM_PARITY
serport.stopbits = COM_STOP
serport.timeout = COM_TIMEOUT
try:
    serport.open()
except serial.SerialException, e:
        s= "%s : Could not open serial port %s: %s\n" % (localtime, serport.portstr, e)
        sys.stderr.write(s)
        problem += 1
        #mail(you, "Heatmiser TimeSet Error ", "Could not open serial port", "errorlog.txt")
        sys.exit(1)

print "%s port configuration is %s" % (serport.name, serport.isOpen())
print "%s baud, %s bit, %s parity, with %s stopbits, timeout %s seconds" % (serport.baudrate, serport.bytesize, serport.parity, serport.stopbits, serport.timeout)

# CYCLE THROUGH ALL CONTROLLERS (Not, just 5)
print 'Switching HOT Water'
# TODO if not V3 controller raise error This should really be detected in API
destination = 5 # hard code to study
#hmKeyLock_Off(destination, serport)
hmHotWater_On(destination, serport)
time.sleep(10) # sleep for 2 seconds before next controller

#END OF CYCLE THROUGH CONTROLLERS
print serport

serport.close() # close port
print "Port is now %s" % serport.isOpen()
#ferr.close()

#if (problem > 0):
    #mail(you, "Heatmiser TimeSet Error ", "A Problem has occurred", "errorlog.txt")
