# coding = utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class HtmlParser(object):

    def get_chapter_url(self,root_url,page_cont):
        if root_url is None or page_cont is None:
            return
        soup = BeautifulSoup(page_cont,'html.parser',from_encoding='utf')
        bookinfo,chapter_lists = self._get_chapter(root_url,soup)
        return bookinfo,chapter_lists

    def get_chapter_content(self,chapter_url,chapter_cont):
        if chapter_url is None or chapter_cont is None:
            return
        soup = BeautifulSoup(chapter_cont, 'html.parser', from_encoding='utf')
        data = self._get_chapter_cont_detail(soup)
        return data

    def _get_chapter(self, root_url, soup):
        chapter_list = set()
        bookinfo={}
        links = soup.find_all('a', href=re.compile(r'/book/[0-9]+/[0-9]+.html'))
        bookinfo['title'] = soup.find('div', id='info').find('h1').get_text()
        bookinfo['author'] = soup.find('div', id='info').find('p').get_text()
        bookinfo['intro'] = soup.find('div', id='intro').get_text()
        for link in links:
            chapter_url = link['href']
            chapter_full_url = urljoin(root_url, chapter_url)
            chapter_list.add(chapter_full_url)

        return bookinfo,chapter_list

    def _get_chapter_cont_detail(self, soup):
        content = {}
        title_node = soup.find('div', class_='bookname').find('h1')
        content_node = soup.find('div', id='content')
        content['title'] = title_node.get_text()
        content['data'] = content_node.get_text()
        return content