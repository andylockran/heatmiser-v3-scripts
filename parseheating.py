# Parses the csv file to produce XML file for reading my Simile Timeline
from struct import pack
import time
import csv
import shutil

from stats_defn import StatList

number_of_controllers = len(StatList)
print "No of controllers is %d" % (number_of_controllers)

status = [0,0,0,0,0,0,0,0,0,0,0,0,0] #one bigger than size required
start = range(number_of_controllers+1)
stop = range(number_of_controllers+1)

# Make a temporary copy of the csv file
shutil.copy2('heatmiser_status.csv','heatmiser_status.csv.tmp')
# @todo trap file exception
fout = open('heattimeline.xml', 'w')

agregated = 0

s = '<data>\n'
fout.write(s)
# @todo trap file exception
fin = csv.reader(open('heatmiser_status.csv.tmp', 'r'))

# Read the first line to get the initial status
first = fin.next()
print first
for i in range(0,number_of_controllers):
	state=first[6+ (i*6)]
	#print state
	if (state == '1'):
		# This unit is on
		status[i+1] = 1
		start[i+1]=first[0]
		agregated = 1
		agregated_start = first[0]
	else:
		status[i+1] = 0
		start[i+1] = 0
print status
print start
# Weve got the initial status

# Now read the rest of the file
something_is_on = 0
something_was_on = agregated
for row in fin:
	#print row
	something_is_on = 0
	print "."
	for i in range(0,number_of_controllers):
		state=row[6+(i*6)]
		st = int(state)
		#print st
		if (st == 0):
			#print "state0"
			if (st == status[i+1]):
				# No change
				#print "no change"
				print "."
			else:
				#Change to off
				stop[i+1] = row[0]
				status[i+1] = 0
				s = '<event start ="' + start[i+1] + '"\n'
				fout.write(s)
				s = 'end ="' + stop[i+1] + '"\n'
				fout.write(s)
				s = 'isDuration="true"\n'
				fout.write(s)
				s = 'title="' + StatList[i][1] + '"\n'
				fout.write(s)
				s = 'color="blue"\n'
				fout.write(s)
				s = 'textColor="black"\n'
				fout.write(s)
				s = 'trackNum="' + repr(i+1) + '">\n'
				fout.write(s)
				s = 'Some other text\n'
				fout.write(s)
				s = '</event>\n'
				fout.write(s)
		else:
			# This controller is on
			#print "state1"
			something_is_on = 1
			if (status[i+1] == 0):
				# It was off last poll so has turned on
				status[i+1] = 1
				start[i+1] = row[0]
	if (agregated == 0 and something_is_on ==1):
		agregated = 1
		agregated_start = row[0]
	if (something_is_on == 0 and agregated == 1):
		# Agregated demand has turned off
		agregated = 0
		s = '<event start ="' + agregated_start + '"\n'
		fout.write(s)
		s = 'end ="' + row[0] + '"\n'
		fout.write(s)
		s = 'isDuration="true"\n'
		fout.write(s)
		s = 'title="' + 'total' + '"\n'
		fout.write(s)
		s = 'color="red"\n'
		fout.write(s)
		s = 'textColor="red"\n'
		fout.write(s)
		s = 'trackNum="' + repr(13) + '">\n'
		fout.write(s)
		s = 'Agregatede Some other text\n'
		fout.write(s)
		s = '</event>\n'
		fout.write(s)
		
	something_was_on = something_is_on

	#print ', '.join(row)

#line = fin.readline()
#print line

# So thats the end of the csv file
# Dump the ones that are still on
# Generate a RFC2822 format date
# This works with both Excel and Timeline
localtime = time.asctime( time.localtime(time.time()))
localtime = time.strftime("%d %b %Y %H:%M:%S +0000", time.localtime(time.time()))
for i in range(0,number_of_controllers):
    if (status[i+1] == 1):
        # This one is currently on
        s = '<event start ="' + start[i+1] + '"\n'
        fout.write(s)
        s = 'end ="' + localtime + '"\n'
        fout.write(s)
        s = 'isDuration="true"\n'
        fout.write(s)
        s = 'title="' + StatList[i][1] + '"\n'
        fout.write(s)
        s = 'color="lightblue"\n'
        fout.write(s)
        s = 'textColor="black"\n'
        fout.write(s)
        s = 'trackNum="' + repr(i+1) + '">\n'
        fout.write(s)
        s = 'Some other text\n'
        fout.write(s)
        s = '</event>\n'
        fout.write(s)
        
if (agregated == 1):
	s = '<event start ="' + agregated_start + '"\n'
	fout.write(s)
	s = 'end ="' + localtime + '"\n'
	fout.write(s)
	s = 'isDuration="true"\n'
	fout.write(s)
	s = 'title="' + 'total' + '"\n'
	fout.write(s)
	s = 'color="pink"\n'
	fout.write(s)
	s = 'textColor="black"\n'
	fout.write(s)
	s = 'trackNum="' + repr(13) + '">\n'
	fout.write(s)
	s = 'Agregatede Some other text\n'
	fout.write(s)
	s = '</event>\n'
	fout.write(s)

s = '</data>\n'
fout.write(s)

#fin.close()
fout.close()

# @todo Delete the temporary csv file


#

