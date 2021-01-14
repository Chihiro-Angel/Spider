#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 20:25
# @Author  : Aquarius
# @File    : request_demo.py
# @Software: PyCharm
import scrapy
from scrapy.http import FormRequest
from ..items import BookInfoItem

class BossSpider(scrapy.Spider):
    name = 'req_demo'

    def start_requests(self):
        start_url = 'http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html'
        yield scrapy.Request(start_url, meta={'name': 'Tom'}, callback=self.parse)
        # print(req.url, req.method, req.body)  # 可以看
        # print(req.headers)
        # print(req.cookies)
        # print(req.url)
        # req.url = "https://www.baidu.com"  # 不可以改
        # req = req.replace(url="https://www.baidu.com")  # 可以更改请求内容,返回值
        # req1 = req.copy()  # 请求的复制
        # yield req

    def parse(self, response):
        item = BookInfoItem()
        urls = response.xpath('//div[@class="bookname"]/a/@href').extract()
        item['book_name'] = response.xpath('//div[@class="bookname"]/a/text()').extract()[0]
        yield scrapy.Request(urls[0], meta={'list_item':item},callback=self.book)

    def book(self,response):
        item = response.meta['list_item']
        item['book_sorted'] = response.xpath('//div[@class="nums"]/span[1]/i/text()').extract()
        yield item








