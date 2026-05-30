from xml.dom import minidom

xmldoc = minidom.parse("trial.xml")

document = xmldoc.getElementsByTagName("monier")[0]

H1 = document.getElementsByTagName("H1")
H1A = document.getElementsByTagName("H1A")
H1B = document.getElementsByTagName("H1B")
H2 = document.getElementsByTagName("H2")
H2A = document.getElementsByTagName("H2A")
H2B = document.getElementsByTagName("H2B")
H3 = document.getElementsByTagName("H3")
H3A = document.getElementsByTagName("H3A")
H3B = document.getElementsByTagName("H3B")
H4 = document.getElementsByTagName("H4")
H4A = document.getElementsByTagName("H4A")
H4B = document.getElementsByTagName("H4B")
HPW = document.getElementsByTagName("HPW")

f =open("test.txt", 'w')

for root in H1:
	head = root.getElementsByTagName("h")
	word = head.getElementsByTagName("key1")[0].firstChild.data
	body = root.getElementsByTagName("body")
	if(body.getElementsByTagName("lex")[0].firstChild.data==null):
		gender = ind
	else:
		gender = body.getElementsByTagName("lex")[0].firstChild.data

	write = "Word: "+ word +", Gender: "+gender+"\n"
	f.write(write)

f.close()


