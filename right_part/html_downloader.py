# -*- coding:utf-8 -*-
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        """
        :param url: The url to be downloaded.
        :return:
        """
        if url is None:
            return None

        resp = urllib2.urlopen(url)

        if resp.getcode() != 200:
            return None

        return resp.read()