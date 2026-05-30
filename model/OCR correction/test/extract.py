import sys
import re
file = open("output.txt", 'w')
sys.stdout = file
#letters = set("[}[{")
with open('test_out.txt') as f:
    lines = f.readlines()
for line in lines:
	if "[" in line:
		ICW = line.partition('[-')[-1].rpartition('-]')[0]
		print ICW + "	" + "-1"
	if "($" in line:
		CW = line.partition('($')[-1].rpartition('$)')[0]
		print CW + "	" + "+1"
