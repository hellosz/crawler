#-*-encoding=utf8-*-

from lxml import etree
import requests

#初始化页面
# startUrl = 'http://www.jikexueyuan.com/course/?pageNum=1'

#xpath初始化
# source = requests.get(startUrl).text
# selector = etree.HTML(source)
#
# #手动获取xpath
# # titleList = selector.xpath('//h2[@class="lesson-info-h2"]/a/text()')
# # print(titleList)
#
# #chrome自动获取xpath
# title = selector.xpath('//*[@id="4025"]/div[2]/h2/a/text()')
# print(title)

html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>Document</title>
</head>
<body>
<ul class="first-info" data-field='this is data field'>
    <li class="info-1">info-1</li>
    <li class="info-2">info-2</li>
    <li class="info-3">info-3</li>
</ul>
<ul class="second-info">
     一楼
    <li class="info-1">二楼</li>
    <li class="info-2">三楼</li>
    <li class="info-3">四楼</li>
</ul>
</body>
</html>
'''
#xpath常见方法的使用
selector = etree.HTML(html)
#获取属性
# res = selector.xpath('//ul[@class="first-info"]/@data-field')
# print('获取属性' + res)

#获取标签内容
# res2 = selector.xpath('//ul[@class="second-info"]/text()')
# print('获取文本' + str(res2))

#xpath特殊方法的使用

# #以固定字符串开头
# res3 = selector.xpath('//ul[starts-with(@class, "first")]/@class')
# print('获取开头' + str(res3))
#
# #存在字符串片段
# res3 = selector.xpath('//ul[contains(@class, "info")]/@class')
# print('获取开头' + str(res3))

#交叉文本获取
res3 = selector.xpath('//ul[@class= "second-info"]')[0]
res4 = res3.xpath('string(.)')
print('交叉文本获取' + str(res4))
