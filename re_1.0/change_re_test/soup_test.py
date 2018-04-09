import urllib2,re
from bs4 import BeautifulSoup
url="https://www.imooc.com/"
res=urllib2.urlopen(url)
html_doc=res.read()
soup=BeautifulSoup(
    html_doc,
    'html.parser',
    from_encoding='utf8'
)
#data-original="//img.mukewang.com/5abc43e500012ec805120512.jpg"
links=soup.find_all('img',src=re.compile(r'//.+\.jpg'))
i=0
try:
    for link in links:
        link="http:"+link['src']
        print i,"    ", link
        # req=urllib2.urlopen(link)
        # file=open("D:/a/"+str(i)+".jpg",'wb+')
        # file.write(req.read())
        i=i+1

except IOError:
    print "Error Url"
# file.close()