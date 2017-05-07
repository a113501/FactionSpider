# coding = utf-8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.chapter_downloader = html_downloader.HtmlDownloader()
        self.list_chapter = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self,root_url):
        count = 1
        root_cont = self.list_chapter.download(root_url)
        bookinfo,chapters_links = self.parser.get_chapter_url(root_url,root_cont)

        self.urls.add_new_urls(chapters_links)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.chapter_downloader.download(new_url)
                data = self.parser.get_chapter_content(new_url, html_cont)
                print('已获取第%s篇：%s'% (count,data['title']))
                count += 1
                # if count == 5:
                #     break
                self.outputer.collect_data(data)
            except:
                print('Craw Failed')
        print(bookinfo['title']+r'正在进行储存')
        print(self.outputer.mkfaction(bookinfo))



if __name__=='__main__':
    # root_url = input('请输入小说入口:\n')
    root_url = 'http://www.qu.la/book/24868/'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)