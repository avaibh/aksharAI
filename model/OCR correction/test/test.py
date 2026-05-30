import sys
import re
file = open("test_out.txt", 'w')
sys.stdout = file
#letters = set("[}[{")
# with open('wdiffout') as f:
#     lines = f.readlines()
# for line in lines:
# 	# b = letters & set(line)
# 	# if not b:
# 	# 	print line +"	"+ "+1"
# 	if '{' in line:
# 		# ICW = line.partition('{+')[-1]
# 		# if '}' in line:
# 		# 	ICW = line.partition('{+')[-1].rpartition('+}')[0]
# 		# 	print ICW + "	" + "-1"
with open('wdiffout', 'r') as myfile:
    data = myfile.read().replace('\n',' ')

data = data.replace("}","}@($")       
data = data.replace("[","$)@[")
data = data.replace("{","$){")
data = data.replace("@","\n") 
print data

