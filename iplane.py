# import headers
import sys
import os

# initialize variables
trace = []
traces = []
hop = 1
flag = False
src = ''
dst = ''

# open input file
f = open("temp.txt", "r")

# open number file
numfile = open("num.txt", "r")

# read number file and close
num = numfile.read()
numfile.close()

# iterate through lines of f
for line in f:
	line = line.split()

	# if 'destination', write and reset
	if (line[0] == "destination:"):
		dst = line[1]

		# get rid of empty line
		if trace != None:
			traces.append(trace)

		# reset lists and flag
		trace = []
		hop = 1
		flag = False
	else:
		if line[1] == "0.0.0.0":
			addr = '0'
		else:
			addr = line[1]

		# print src:dst on first pass
		if (flag == False):
			trace.append(addr + ':' + dst + ' ')
			trace.append(addr + '-' + str(hop) + ' ')
			flag = True
			hop += 1		
		else:
			trace.append(addr + '-' + str(hop) + ' ')
			hop += 1
f.close()

# open output file
out = open("all_trace_" + num + ".txt", "w")

# write list to file
for item in traces:
	if not item:
		pass
	else:
		out.write(''.join(item) + '\n')
out.close()

# reset number file for next time
filenum = int(num)
filenum += 1
numfile = open("num.txt", "w")
numfile.write(str(filenum))
numfile.close()