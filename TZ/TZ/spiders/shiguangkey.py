# -*- coding: utf-8 -*-
import scrapy
from ..items import TzItem


class ShiguangkeySpider(scrapy.Spider):
    name = 'shiguangkey'
    base_url = 'https://www.shiguangkey.com'
    start_urls = ['https://www.shiguangkey.com/course/list']

    def parse(self, response):
        course_urls = response.xpath('//div[@class="_1Ifxn"]/div/div/div[2]/a/@href').extract()
        course_name = response.xpath('//div[@class="_1Ifxn"]/div/div/div[2]/a/text()').extract()
        print(course_urls,course_name)
        for index, url in enumerate(course_urls):
            yield scrapy.Request(
                url=self.base_url + url,
                meta={"course_name":course_name},
                callback=self.air_date
            )

    def air_date(self,  response):
        item = TzItem()
        item['price_now'] = response.xpath('//span[@class="_2J4cA"]/text()').extract()
        item['price_old'] = response.xpath('//span[@class="d2BPU"]/text()').extract()
        item['people_num'] = response.xpath('//span[@class ="_1zFwE"]/text()').extract()

        item['course_nama'] = response.meta['course_name']
        yield item