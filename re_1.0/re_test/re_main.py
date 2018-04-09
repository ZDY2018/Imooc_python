# -*- coding:utf-8 -*-
import re,urllib2
url1="https://www.imooc.com/"
res=urllib2.urlopen(url1)
buf=res.read()
listurl=re.findall(r'//[i|c]. +\.jpg',buf)#返回列表
i=0
for url in listurl:
    file = open('D:/b/' + str(i) + ".jpg", 'wb+')
    try:
        url2 ="http:"+url
        print i,"    ",url2
    #     req = urllib2.urlopen(url2)
    #     buf=req.read()
    #     file.write(buf)
    except IOError:
        print "Error Url"
    i+=1
    # file.close()