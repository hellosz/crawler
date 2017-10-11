#-*-encoding=utf8-*-
import requests
import re

class spider(object):
    def __init__(self, startUrl):
        print('初始化爬虫程序')
        self.startUrl = startUrl

    def getAllUrls(self, total):
        #首页地址
        now_page = int(re.search('pageNum=(\d+)', self.startUrl).group(1))
        allUrls = []

        #构造链接地址
        for page in range(now_page, now_page + total):
            currentUrl = re.sub('pageNum=\d+', 'pageNum=%d'%page, self.startUrl, re.S)
            allUrls.append(currentUrl)
        return allUrls

    def getPageSource(self, url):
        pageSource = requests.get(url)
        pageSource.encoding = 'utf-8'
        return pageSource.text

    def getItemDom(self, pageSource):
        itemDocList = re.findall('(<li id="\d+" test="0" deg="0".*?</li>)', pageSource, re.S)
        return itemDocList

    def getCourseInfo(self, courseDom):
        courseInfo = {}
        courseInfo['title'] = re.search('<h2 class="lesson-info-h2"><a.*?>(.*)</a></h2>', courseDom, re.S).group(1)
        courseInfo['desc'] = re.search('<p .*>(.*)</p>', courseDom, re.S).group(1)
        detailInfo = re.findall('<em.*?>(.*?)</em>', courseDom, re.S)
        courseInfo['length'] = detailInfo[0]
        courseInfo['class'] = detailInfo[1]
        courseInfo['learnNum'] = detailInfo[2]
        return courseInfo

    def saveInfo(self, courseInfo):
        file = open('courseinfo.txt', 'a', encoding='utf-8')
        for course in courseInfo:
            file.writelines('title:' + course['title'] + '\n')
            file.writelines('desc:' + course['desc'] + '\n')
            file.writelines('length:' + course['length'] + '\n')
            file.writelines('class:' + course['class'] + '\n')
            file.writelines('learnNum:' + course['learnNum'] + '\n\n')

if __name__ == '__main__':
    #初始化里链接
    startUrl = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jkSpider = spider(startUrl)
    #获取所有的链接
    allUrls = jkSpider.getAllUrls(20)

    #爬取数据
    courseInfo = []
    #遍历链接，先大后小
    for eachUrl in allUrls:
        print('正在爬取' + eachUrl)
        #爬取整个页面
        pageSource = jkSpider.getPageSource(eachUrl)
        #爬取需要的数据
        courseDomList = jkSpider.getItemDom(pageSource)
        for courseDom in courseDomList:
            course = jkSpider.getCourseInfo(courseDom);
            courseInfo.append(course)

    # #数据保存
    jkSpider.saveInfo(courseInfo)


