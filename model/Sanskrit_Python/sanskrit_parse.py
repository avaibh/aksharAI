from requests import get
from lxml import html, etree
from lxml.html.clean import clean_html
root = get("http://sanskritdocuments.org/")
tree = html.fromstring(clean_html(root.text))
tree.xpath("//a")
level2 = tree.xpath("//a/@href")
req_link = []
for link in level2:
    if (link.startswith("./")):
        req_link.append(link)
lns = []
for new_l in req_link:
    lns.append("http://sanskritdocuments.org/" + new_l[2:])
# new_link = []   
# pdf_link = []
# for link1 in lns:
#     pg_new = get(link1)
#     tree2 = html.fromstring(clean_html(pg_new.text))
#     tree2.xpath("//div[@class='index-content']//ul//a/@href")
#     l2 = tree2.xpath("//div[@class='index-content']//ul//a/@href")
#     for link2 in l2:
#         if(link2.startswith("./")):
#             new_link.append("http://sanskritdocuments.org/" + link2[2:])
# for link3 in new_link:
#         pdf_link.append(link3)   
# for link in pdf_link:
#         book_name = link.split('/')[-1]
#         with open(book_name, 'wb') as book:
#             a = requests.get(link, stream=True)
            
#             for block in a.iter_content(512):
#                  if not block:
#                      break
     
#                  book.write(block)

html_link = []
for link1 in lns:
    try:
		pg_new = get(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})
	except:
		print("Connection refused by the server..")
		print("Let me sleep for 5 seconds")
		print("ZZzzzz...")
		time.sleep(5)
		print("Was a nice sleep, now let me continue...")
		continue
	tree4 = html.f
    tree3 = html.fromstring(clean_html(pg_new.text))
    tree3.xpath("//div[@class='index-content']//ul//a/@href")
    l2 = tree3.xpath("//div[@class='index-content']//ul//a/@href")
    for link2 in l2:
        if ".html" in link2:
            if(link2.startswith("./")):
                html_link.append("http://sanskritdocuwments.org/" + link2[2:])
for link in html_link:
	try:
		pg_html = get(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})
	except:
		print("Connection refused by the server..")
		print("Let me sleep for 5 seconds")
		print("ZZzzzz...")
		time.sleep(5)
		print("Was a nice sleep, now let me continue...")
		continue
	tree4 = html.fromstring(clean_html(pg_html.text))
	arr = tree4.xpath("//div[@id='article']/pre[@id='content']/text()")
	arr1 = tree4.xpath("//div[@id='article']/pre[@id='content']/h2/text()")
	arr2 = "".join(arr).encode('utf-8').strip()
	arr3 = "".join(arr1).encode('utf-8').strip()
	arr4 = arr2 + "\n"+ arr3
	filename = tree4.xpath("//h1/text()")
	filename ="".join(filename).encode('utf-8').strip()+ ".txt"
	f =open(filename, 'w')
	f.write(arr4)
	f.close

        