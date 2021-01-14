#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 21:10
# @Author  : Aquarius
# @File    : boss.py
# @Software: PyCharm

# 解析爬虫

import scrapy
from ..items import SpiderbossItem, BookListItem

class BossSpider(scrapy.Spider):
    # 爬虫名 唯一 启动时候去使用
    name = 'novel'

    # url 请求
    # def start_requests(self):

    #     start_url = 'http://book.zongheng.com/chapter/890534/58629142.html'
    #     headers = {}
    #     cookie ={}

    #     yield scrapy.Request(start_url,headers=headers,cookies=cookie,callback=self.parse)   # callback 回调

    # # 页面解析函数
    # def parse(self, response):
    #     """
    #     1、响应。items。2、提取下一页url，并且访问他
    #     :param response:
    #     :return:
    #     """

    #     item = SpiderbossItem()
    #     item['name'] = response.xpath('//div[@class="reader_crumb"]/a[3]//text()').extract_first()
    #     item['auth'] = response.xpath('//div[@class="bookinfo"]/a[1]/text()').extract_first()
    #     item['novel_title'] = response.xpath('//div[@class="title_txtbox"]/text()').extract_first()
    #     novel_doc = response.xpath('//div[@class="content"]//p//text()').extract()
    #     item['text'] = '\n'.join(novel_doc)
    #     yield item

    #     # with open('%s.txt'%name, 'a+', encoding='utf-8') as f:
    #     #     f.write(name + '\r\n' + auth + '\r\n' + novel_title + '\r\n' + text)

    #     # yeild 多次请求  下一页
    #     return scrapy.Request('http://book.zongheng.com/chapter/886905/58211812.html')  # 每次都进行的下一页请求

    def start_requests(self):

        start_url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html'
        headers = {}
        cookie ={}

        yield scrapy.Request(start_url,headers=headers,cookies=cookie,callback=self.parse)
    def parse(self, response):
        item = BookListNovelItem()
        book_names = response.xpath('//div[@class="bookname"]/a//text()').extract()
        book_auths = response.xpath('//div[@class="bookilnk"]/a[1]/text()').extract()
        book_types = response.xpath('//div[@class="bookilnk"]/a[2]/text()').extract()
        for index, data in enumerate(book_names):
            item['book_name'] = data
            item['book_auth'] = book_auths[index]
            item['book_type'] = book_types[index]
            yield item
        # 总页数
        page = response.xpath('//a[@class="scrollpage"]/text()').extract()[-1]
        # 当前页
        for i in range(2, int(page) + 1):
            url = "http://book.zongheng.com/store/c0/c0/b0/u0/p" + str(i)+ "/v9/s9/t0/u0/i1/ALL.html"
            yield scrapy.Request(url)