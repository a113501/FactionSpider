# coding = utf-8
import urllib.request

class HtmlDownloader(object):
    '''
    下载器模块
    '''
    def download(self,url):
        '''
        判断URL是否合法，合法则进行下一语句，不合法则返回None
        '''
        if url is None:
            return None
        response = urllib.request.urlopen(url) ###调用urllib.request中的urlopen方法，此处处理较为简单，可加入cookie，UA等

        if response.getcode() != 200:###判断页面响应，如果HTTP状态不是200，即错误，返回Noone
            return None

        return response.read() ###返回响应内容