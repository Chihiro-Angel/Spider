# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price_now = scrapy.Field()
    price_old = scrapy.Field()
    course_nama = scrapy.Field()
    people_num = scrapy.Field()
