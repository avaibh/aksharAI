import sys
import re
file = open("output.txt", 'w')
sys.stdout = file
#letters = set("[}[{")
with open('test_out1.txt') as f:
    lines = f.readlines()
for line in lines:
	if "[" in line:
		ICW = line.partition('[-')[-1].rpartition('-]')[0]
		icw = ICW.split()
		for icw_l in icw:
			print icw_l + "	" + "-1"
	if "($" in line:
		CW = line.partition('($')[-1].rpartition('$)')[0]
		w = CW.split()
		for w_l in w:
			print w_l + "	" + "+1"
