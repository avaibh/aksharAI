import os
import xml.etree.ElementTree as et
from xml.dom import minidom

# xmldoc = minidom.parse("monier.xml")

tree = et.parse("monier.xml")
roots = tree.getroot()
f =open("newdata.txt", 'w')

# for child in roots:
# 	for element in child :
# 		if (element.tag =="h"):
# 			for wordC in element:
# 				if (wordC.tag =="key1"):
# 					word = wordC.text
# 		if (element.tag =="body"):
# 			for lex in element:
# 				if (lex.tag == "lex"):
# 					gender = lex.text
for child in roots:
	for element in child.iter(tag = 'h'):
		word = element.find('key1')
		wordText = word.text
	for element in child.iter(tag = 'body'):
		lextag = element.find('lex')
		if lextag is None:
			gender = "flag"
		else:
			gender = lextag.text
		if(gender != "flag"):	
			f.write(wordText+" "+ gender+ "\n")

# write = "Word: "+ word +", Gender: "+"\n"
# f.write(write)

f.close()