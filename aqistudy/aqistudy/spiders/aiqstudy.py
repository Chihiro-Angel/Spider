# -*- coding: utf-8 -*-
import scrapy
from ..items import AqistudyItem


class AiqstudySpider(scrapy.Spider):
    name = 'aiqstudy'
    # allowed_domains = ['www.aqistudy.cn/historydata/']
    base_url = 'https://www.aqistudy.cn/historydata/'
    start_urls = [base_url]

    def parse(self, response):
        city_name = response.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]//li/a/text()').extract()
        city_urls = response.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]//li/a/@href').extract()
        for index, url in enumerate(city_urls):
            yield scrapy.Request(
                url=self.base_url + url,
                meta={'city_name':city_name, 'selenium':True},
                callback=self.air_data
            )

    def air_data(self, response):
        item = AqistudyItem()


