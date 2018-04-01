# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    #用于收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    #展示页面
    def output_html(self):
        fout=open('output.html','w')#写模式

        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table>')
        fout.write("<table border='1'>")
        if len(self.datas)==0:
            print "空数据"
        #python默认ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))#防止乱码
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()