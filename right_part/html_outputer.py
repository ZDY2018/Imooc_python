# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('python_org_crawled_data.html', 'w')

        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write("<table border='1'>")

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')