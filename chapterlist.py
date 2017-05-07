import html_downloader
from bs4 import BeautifulSoup
import re

# uri = 'http://www.qu.la/book/24868/'
# main = html_downloader.HtmlDownloader()
# content = main.download(uri)
#
# soup = BeautifulSoup(content, 'html.parser', from_encoding='utf')
#
# chapterlist = soup.find('div',id='list').find_all('a')

# print(chapterlist)

with open('text.html') as f:
    cont = f.readlines()

    print(cont[0].encode('utf-8').decode('utf-8'))