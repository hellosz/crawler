#-*-encoding:utf-8-*-

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanItem


class DouBan(CrawlSpider):
    name = 'douban'
    start_urls = ['http://movie.douban.com/top250']
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        movieList = selector.xpath('//ol[@class="grid_view"]/li')
        print(movieList)
        for movie in movieList:
            #读取数据
            item = DoubanItem()
            title = movie.xpath('div/div[@class="info"]/div[1]/a/span/text()').extract()
            item['movieInfo']= movie.xpath('div/div[@class="info"]/div[2]/p[1]/text()').extract()[0]
            item['star'] = movie.xpath('div/div[@class="info"]/div[2]/div/span[@class="rating_num"]/text()').extract()[0]
            quote = movie.xpath('div/div[@class="info"]/div[2]/p[2]/span/text()').extract()
            #特殊数据处理
            if quote:
                item['quote'] = quote[0]
            else:
                item['quote'] = ''
            item['title'] = ''.join(title)

            #数据保存
            yield item
        #下一页处理
        nextPage = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            nextPage = nextPage[0]
            print(self.url + nextPage)
            yield Request(self.url + nextPage, callback=self.parse)
