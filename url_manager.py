# coding = utf-8
class UrlManger(object):
    '''
    初始化URL管理器，包括一个未下载列表和一个已下载列表
    '''

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    '''
    添加URL到未下载列表
    '''
    def add_new_url(self, url):
        '''判断URL是否存在，如果存在则添加，如果出错则返回'''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  ###调用set的add方法，添加一条内容
    '''
    添加一列URL集合到未下载列表
    '''
    def add_new_urls(self,urls):
        '''判断URL集合是否存在，如果存在则添加，如果出错则返回'''
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)  ###调用单个URL添加方法，两种函数方便了调用
    '''
    队列方法操作URL，使用过的URL在未下载列表中删除，并添加到已下载列表中
    '''
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    '''
    判断是否URL是否合法，判断比较简单，只判断URL长度
    '''
    def has_new_url(self):
        return len(self.new_urls)!=0