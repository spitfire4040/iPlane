import sys
import os
import urllib

url = "http://iplane.cs.washington.edu/data/iplane_logs/2016/04/01/trace.out.lim-planetlab-2.univ-reunion.fr.gz"

urllib.urlretrieve(url, "/home/jay/iPlane/temp/temp.txt")