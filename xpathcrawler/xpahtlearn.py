#-*-encoding=utf8-*-

from lxml import etree
import requests

#初始化页面
startUrl = 'http://www.jikexueyuan.com/course/?pageNum=1'

#xpath初始化
source = requests.get(startUrl).text
selector = etree.HTML(source)

#手动获取xpath
# titleList = selector.xpath('//h2[@class="lesson-info-h2"]/a/text()')
# print(titleList)

#chrome自动获取xpath

#xpath常见方法的使用

#xpath特殊方法的使用
