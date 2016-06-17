import sys
import os
import urllib

for x in range(1, 31):
	f = open("/home/jay/iPlane/iPlane_traces/" + str(x) + "/traces.txt", "r")

	if (x < 10):
		day = "0" + str(x)
	else:
		day = str(x)

	out = open("/home/jay/Desktop/iplane_test/Day-" + day, "w")

	for line in f:

		url = "http://iplane.cs.washington.edu/data/iplane_logs/2016/04/" + day + "/" + line

		urllib.urlretrieve(url, "/home/jay/iPlane/temp/temp.txt")