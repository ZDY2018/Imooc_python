# -*- coding:utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()


    #向管理器中添加新的url（单个添加）
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加新的url（批量添加）
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url) #调用添加单个url函数进行添加


    #是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls)!=0

    #向管理器获取一个新的url
    def get_new_url(self):
        new_url=self.new_urls.pop() #从列表中获取一个url 并移除这个url
        self.old_urls.add(new_url)
        return new_url

