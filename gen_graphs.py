#
# Neil Trimboy 2011
#

from struct import pack
import time
import sys

import os

from stats_defn import *

d = os.path.join(os.getcwd(),"graphs")
if not os.path.exists(d):
	os.makedirs(d)
	
problem = 0

rrdfile = 'hmstats.rrd'
rrdrocfile = 'hmoptimstart.rrd'
rrdtimeerrfile = 'hmtimedelta.rrd'
rrdloadfile = 'hmload.rrd'

graphs = [
#["Today"],
#["Yesterday"],
#["ThisWeek"],
#["LastWeek"],
#["ThisMonth"],
#["LastMonth"],
["24Hrs", '-24hour', 'now'],
["7days", '-7day', 'now'],
["4Weeks", '-4week', 'now'],
["8Weeks", '-8week', 'now'],
["12Weeks", '-12week', 'now'],
["52Weeks", '-52week', 'now'],
]

for graph in graphs:
	for controller in StatList:
		start_time = graph[1]  
		output_filename = 'graphs/' + controller[SL_SHRT_NAME] + '_' + graph[0] + '.png'
		end_time = graph[2]
		ds_name = 'Air'
		ds_name2 = 'Floor'
		ds_name3 = 'Set'
		ds_name4 = 'Demand'
		width = '400'
		height = '150'
		cur_date = time.strftime('%m/%d/%Y %H\:%M\:%S', time.localtime())       
		cmd_graph = 'rrdtool graph ' + output_filename + \
			' DEF:' + ds_name + '=' + rrdfile + ':' + controller[SL_SHRT_NAME] + 'air' + ':AVERAGE' + \
			' DEF:' + ds_name2 + '=' + rrdfile + ':' + controller[SL_SHRT_NAME] + 'flr' + ':AVERAGE' + \
			' DEF:' + ds_name3 + '=' + rrdfile + ':' + controller[SL_SHRT_NAME] + 'set' + ':AVERAGE' + \
			' DEF:' + ds_name4 + '=' + rrdfile + ':' + controller[SL_SHRT_NAME] + 'dem' + ':MAX' + \
			' VDEF:' + ds_name  + 'last=' + ds_name  + ',LAST' + \
			' VDEF:' + ds_name2 + 'last=' + ds_name2 + ',LAST' + \
			' VDEF:' + ds_name3 + 'last=' + ds_name3 + ',LAST' + \
			' CDEF:heat=' + ds_name4 + ',.5,+,FLOOR,'+ds_name+',UNKN,IF' + \
			' COMMENT:"Generated ' + cur_date + '\\n"' + \
			' AREA:' + ds_name + '#FFF880' \
			' AREA:heat'  + '#FFD0A0' \
			' LINE1:heat'  + '#EDB200' + ':"Heating"'\
			' LINE1:' + ds_name + '#FFD000' + ':"Air"'\
			' GPRINT:' + ds_name  + 'last:"Current Air   = %6.2lf%S"' + \
			' LINE:' + ds_name2 + '#FF0000' + ':"Floor"'\
			' GPRINT:' + ds_name2 + 'last:"Current Floor = %6.2lf%S"' + \
			' LINE:' + ds_name3 + '#008000' + ':"Set"'\
			' GPRINT:' + ds_name3 + 'last:"Current Set   = %6.2lf%S"' + \
			' LINE:' + ds_name4 + '#FC4242' + \
			' --title="Room ' + controller[2] + ' ' + graph[0] + '"' + \
			' --vertical-label="Celcius"' + \
			' --start=' + start_time + \
			' --end=' + end_time + \
			' --width=1000' + \
			' --height=300' + \
			' --lower-limit="0"' + \
			' --right-axis 1:0' + \
			' --right-axis-label="Celcius"'
			# ' GPRINT:' + ds_name  + 'last:"                         Current Air   = %6.2lf%S"' + \
			# ' GPRINT:' + ds_name2 + 'last:"                         Current Floor = %6.2lf%S"' + \
			# ' GPRINT:' + ds_name3 + 'last:"                         Current Set   = %6.2lf%S"' + \
		#	' VDEF:' + ds_name + 'last=' + ds_name + ',LAST' + \
		#	' VDEF:' + ds_name + 'avg=' + ds_name + ',AVERAGE' + \
		#	' COMMENT:"' + cur_date + '"' + \
		#	' GPRINT:' + ds_name + 'avg:"                         average=%6.2lf%S"' + \
		# ' --title=Room "' + rrdfile +'"' + \
			
		print cmd_graph
		cmd = os.popen4(cmd_graph)
		cmd_output = cmd[1].read()
		for fd in cmd: fd.close()
		if len(cmd_output) > 0:
			print cmd_output
			
# Now the optimstart graph
start_time = '-52week'  
output_filename = 'graphs/' + 'optimstart.png'
end_time = 'now'
width = '400'
height = '150'
cur_date = time.strftime('%m/%d/%Y %H\:%M\:%S', time.localtime())       
cmd_graph = 'rrdtool graph ' + output_filename
for controller in StatList:
	cmd_graph += ' DEF:' + controller[1] + 'roc=' + rrdrocfile + ':' + controller[SL_SHRT_NAME] + 'roc' + ':AVERAGE'
	cmd_graph += ' DEF:' + controller[SL_SHRT_NAME] + 'os=' + rrdrocfile + ':' + controller[SL_SHRT_NAME] + 'optimstart' + ':AVERAGE'
	cmd_graph += ' LINE:' + controller[SL_SHRT_NAME] + 'roc#' + controller[SL_GRAPH_COL] + ':' + controller[SL_SHRT_NAME]
	cmd_graph += ' LINE:' + controller[SL_SHRT_NAME] + 'os#' + controller[SL_GRAPH_COL]
	cmd_graph += ' VDEF:' + controller[SL_SHRT_NAME]  + 'last=' + controller[SL_SHRT_NAME] + 'roc' + ',LAST'
	cmd_graph += ' GPRINT:' + controller[SL_SHRT_NAME]  + 'last:"' + controller[SL_SHRT_NAME] + ' ROC   = %6.2lf%S"'
			  
cmd_graph += ' COMMENT:"Generated ' + cur_date + '"' + \
' --title="Optim Start Data"' + \
' --vertical-label="mins per degree"' + \
' --start=' + start_time + \
' --end=' + end_time + \
' --width=1000' + \
' --height=300'
print cmd_graph
cmd = os.popen4(cmd_graph)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
	print cmd_output

# Now the timeerr graph
start_time = '-4week'  
output_filename = 'graphs/' + 'timeerr.png'
end_time = 'now'
width = '400'
height = '150'
cur_date = time.strftime('%m/%d/%Y %H\:%M\:%S', time.localtime())       
cmd_graph = 'rrdtool graph ' + output_filename
for controller in StatList:
	cmd_graph += ' DEF:' + controller[SL_SHRT_NAME] + 'err=' + rrdtimeerrfile + ':' + controller[SL_SHRT_NAME] + 'timedelta' + ':AVERAGE'
	cmd_graph += ' LINE:' + controller[SL_SHRT_NAME] + 'err#' + controller[SL_GRAPH_COL] + ':' + controller[SL_SHRT_NAME]
	cmd_graph += ' VDEF:' + controller[SL_SHRT_NAME]  + 'last=' + controller[SL_SHRT_NAME] + 'err' + ',LAST'
	cmd_graph += ' GPRINT:' + controller[SL_SHRT_NAME]  + 'last:"' + controller[SL_SHRT_NAME] + ' Err   = %6.1lf%S"'
			
cmd_graph += ' COMMENT:"Generated ' + cur_date + '"' + \
' --title="Time Error Data"' + \
' --vertical-label="seconds"' + \
' --start=' + start_time + \
' --end=' + end_time + \
' --width=1000' + \
' --height=300'
print cmd_graph
cmd = os.popen4(cmd_graph)
cmd_output = cmd[1].read()
for fd in cmd: fd.close()
if len(cmd_output) > 0:
	print cmd_output
    
LoadList = [
["zoneload", "A020F0"],
["circuitload", "6B8E23"],
["areaload", "6A5ACD"],
]
    
# Now the load graph
for graph in graphs:
    start_time = graph[1] 
    output_filename = 'graphs/' + 'load'+ '_' + graph[0] + '.png'
    end_time = graph[2]
    width = '400'
    height = '150'
    cur_date = time.strftime('%m/%d/%Y %H\:%M\:%S', time.localtime())       
    cmd_graph = 'rrdtool graph ' + output_filename
    for load in LoadList:
        print load
        cmd_graph += ' DEF:' + load[0] + '=' + rrdloadfile + ':' + load[0] + ':MAX'
        cmd_graph += ' LINE:' + load[0] + '#' + load[1] + ':' + load[0]
        cmd_graph += ' VDEF:' + load[0]  + 'last=' + load[0] + ',LAST'
        cmd_graph += ' GPRINT:' + load[0]  + 'last:"' + load[0] + ' = %6.1lf%S"'
                
    cmd_graph += ' COMMENT:"Generated ' + cur_date + '"' + \
    ' --title="Load Data'+ ' ' + graph[0] + '"' + \
    ' --vertical-label="Load (m^2)"' + \
    ' --start=' + start_time + \
    ' --end=' + end_time + \
    ' --width=1000' + \
    ' --height=300' + \
    ' --lower-limit=0' + \
    ' --rigid'

    # ' --upper-limit=400'

    print cmd_graph
    cmd = os.popen4(cmd_graph)
    cmd_output = cmd[1].read()
    for fd in cmd: fd.close()
    if len(cmd_output) > 0:
        print cmd_output
	
#From heating.py
# Last four weeks: --start end-4w --end 00:00
# January 2001:    --start 20010101 --end start+31d
# January 2001:    --start 20010101 --end 20010201
# Last hour:       --start end-1h
# Last 24 hours:   <nothing at all>
# Yesterday:       --end 00:00
