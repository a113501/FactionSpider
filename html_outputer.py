# coding = utf-8
import os

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def mkfaction(self,info):
        '''
        创建文件夹
        '''
        self._mkdir(info['title'])
        '''
        写入文件
       '''
        for chapter in self.datas:
            self._mkfile(chapter)
        return r'章节储存完成'

    def _mkdir(self,dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        os.chdir(dirname)

    def _mkfile(self,data):
        f = open(data['title']+r'.txt', 'w')
        #
        # f.write('<html>')
        # f.write('<head><meta charset="utf-8"/></head>')
        # f.write('<body>')
        # f.write('<table>')
        # f.write('<tr>')
        f.write('<td>%s</td>' % data['title'].encode('utf-8','ignore'))
        f.write('<td>%s</td>' % data['data'].encode('utf-8','ignore'))
        # f.write('</tr>')
        # f.write('</table>')
        # f.write('</body>')
        # f.write('</html>')
        f.close()