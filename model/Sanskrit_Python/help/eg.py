from requests import get
from lxml import html, etree
from lxml.html.clean import clean_html
root = get("http://sanskritdocuments.org/")
root.status_code
root.text
tree = html.fromstring(clean_html(root.text))
tree
tree.lxml("//a")
tree.xpath("//a")
level2 = tree.xpath("//a")
for (links in level2):
level2 = tree.xpath("//a/@href")
level2
req_link = []
for link in level2:
    if (link.starts_with("./")):
        req_link.append(link)
type level2[0]
type (level2[0])
level2
level2[0]
level2[0].startswith("./")
req_link = []
for link in level2:
    if (link.startswith("./")):
        req_link.append(link)
req_link
lns = []
for new_l in req_link:
    lns.append("http://sanskritdocuments.org/" + new_l[2:])
lns
pwd
cd code/
mkdir python
cd python/
pg = get(req_link[0])
pg = get(lns[0])
pg.text
tree2 = html.fromstring(clean_html(pg))
tree2 = html.fromstring(clean_html(pg.text))
tree2.xpath("//a/@href")
tree2.xpath("///ul//a/@href")
tree2.xpath("//div[@class='index-content']//ul//a/@href")
pg.url
l = tree2.xpath("//div[@class='index-content']//ul//a/@href")
tree.xpath("//p/text()")
arr = tree.xpath("//p/text()")
arr.join("")
"".join(arr)
print "".join(arr)
print "".join(arr).strip()



for link1 in lns:
    pg_new = get(link1)
    tree2 = html.fromstring(clean_html(pg_new.text))
    tree2.xpath("//div[@class='index-content']//ul//a/@href")
    l2 = tree2.xpath("//div[@class='index-content']//ul//a/@href")
    new_link = []
    for link2 in l2:
        if(link2.startswith("./")):
            new_link.append("http://sanskritdocuments.org/" + link2[2:])
    pdf_link = []
    for link3 in new_link:
        if ".pdf" in link3:
            pdf_link.append(link3)
for link in pdf_link:
    book_name = link.split('/')[-1]
    with open(book_name, 'wb') as book:
        a = requests.get(link, stream=True)
        
        for block in a.iter_content(512):
             if not block:
                 break
 
             book.write(block)
