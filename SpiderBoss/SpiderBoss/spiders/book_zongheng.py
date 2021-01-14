# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import BookInfoItem
from ..items import BookListItem
"""
LinkExtractor:解析链接
rules：规则

"""

class BookZonghengSpider(CrawlSpider):
    name = 'book.zongheng'
    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html']
    rules = (
        # 书的详情页面 url      name  sort
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/book/\d+.html'),
             callback='parse_item', follow=True),

        # 书籍的列表页         book_name book_auth book_type
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/store/c0/c0/b0/u0/p\d/v9/s9/t0/u0/i1/ALL.html'),
             callback='parse_list_item', follow=True),
    )

    def parse_item(self, response):
        # 详情页解析
        item = BookInfoItem()
        item['book_name'] = response.xpath('//div[@class="book-name"]//text()').extract_first().replace('\r\n','').strip()

        item['book_sorted'] = ''.join(response.xpath('//i[@class="a1"]//text()').extract())
        yield item

    def parse_list_item(self,response):
        # 列表页解析
        item = BookListItem()
        item['book_name'] = response.xpath('//div[@class="bookname"]/a//text()').extract()
        item['book_auth'] = response.xpath('//div[@class="bookilnk"]/a[1]/text()').extract()
        item['book_type'] = response.xpath('//div[@class="bookilnk"]/a[2]/text()').extract()

        yield item
        # 总页数
        page = int(response.xpath('//a[@class="scrollpage"]/text()').extract()[-1])
        # 当前页
        url_list = []
        for i in range(2, page):
            url = "http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html".format(str(i))
            url_list.append(url)
            yield scrapy.Request(url)
        # yield scrapy.Request(url_list)
        