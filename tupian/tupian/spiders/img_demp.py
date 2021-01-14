# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TupianItem

class ImgDempSpider(CrawlSpider):
    name = 'img_demo'
    start_urls = ['http://www.2717.com/beautiful/dongmantupian/2013/3953.html']

    rules = (
        Rule(LinkExtractor(allow=r'/\w+/\w+/\d+/\d+\.html'),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'https://www.2717.com/\w+/\w+/\d+/\d+\.html'), callback='parse_item', follow=True, process_request='up_img_req'),
        Rule(LinkExtractor(allow=r'https://www.2717.com/\w+/\w+/\d+/\d+_\d+\.html'), callback='parse_item', follow=True,process_request='up_img_req'),
        Rule(LinkExtractor(allow=r'\d+_\d+\.html'), callback='parse_item', follow=True,process_request='up_img_req'),
        Rule(LinkExtractor(allow=r'https://www.2717.com/tag/\d+\.html'),callback='parse_item', follow=True, process_request='up_img_req'),
        Rule(LinkExtractor(allow=r'https://www.2717.com/\w+/$'), follow=True, process_request='up_img_req'),
    )

    def parse_item(self, response):
        item = TupianItem()
        item['image_urls'] = response.xpath('//div[@id="picBody"]/p/a/img/@src').extract()
        item['image_name'] = response.xpath('//h1[@class="articleV4Tit"]/text()').extract_first()
        item['image_type'] = response.xpath('//div[@class="articleV4Info"]/a/text()').extract_first()
        yield item

    def up_img_req(self,request):
        if not re.match(r'/\w+/\w+/\d+/\d+\.html',request.url):
            if not re.match(r'/\w+/\w+/\d+/\d+_\d+\.html',request.url):
                request.priority = -1  # 降低优先级
        return request