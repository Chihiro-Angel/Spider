# -*- coding: utf-8 -*-
import scrapy


class BosstestSpider(scrapy.Spider):
    name = 'bosstest'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=']

    def parse(self, response):
        print(response.text)
