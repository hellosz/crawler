#-*-encoding=utf8-*-
import requests
import json
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool


#写文件方法
def wirteFile(item):
    file = open('./tieba.txt', 'a', encoding='utf-8')
    if item is not None:
        file.writelines('[title]:' + str(item['title']) + '\n')
        file.writelines('[author]:' + item['author'] + '\n')
        file.writelines('[desc]:' + item['desc'] + '\n')
        file.writelines('[reply]:' + str(item['reply']) + '\n')
    else:
        print('没有数据！')
    file.close()


#定义爬取方法
def getSource(url):
    print(url)
    html = requests.get(url)
    selector = etree.HTML(html.text)
    commentList = selector.xpath('//li[@class=" j_thread_list clearfix"]')
    for comment in commentList:
        item = {};
        replyInfo = json.loads(comment.xpath('@data-field')[0].replace('&quot', ''))
        item['title'] = comment.xpath('div/div[2]/div/div/a/text()')[0]
        if replyInfo['author_name'] is None:
            item['author'] = ''
        else:
            item['author'] = replyInfo['author_name']
        item['desc'] = comment.xpath('div/div[2]/div[2]/div[1]/div[1]/text()')[0]
        item['reply'] = replyInfo['reply_num']
        print(item)
        wirteFile(item)


#多线程爬取数据
if __name__ == '__main__':
    start_url = 'https://tieba.baidu.com/f?kw=%E6%B5%B7%E5%90%A7%E5%88%86%E6%9E%90&ie=utf-8'
    # 生成前10页面链接
    urls = [start_url + '&pn=' + str(page * 50) for page in range(0, 10)]
    #多线程爬取数据
    threadPool = ThreadPool(4)
    threadPool.map(getSource, urls)
    threadPool.close()
    threadPool.join()
