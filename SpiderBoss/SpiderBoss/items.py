# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderbossItem(scrapy.Item):
    name = scrapy.Field()
    auth = scrapy.Field()
    title = scrapy.Field()
    novel_title = scrapy.Field()
    text = scrapy.Field()


class BookInfoItem(scrapy.Item):
    book_name = scrapy.Field()
    book_sorted = scrapy.Field()


class BookListItem(scrapy.Item):
    book_name = scrapy.Field()
    book_auth = scrapy.Field()
    book_type = scrapy.Field()


class BookListNovelItem(scrapy.Item):
    book_name = scrapy.Field()
    book_auth = scrapy.Field()
    book_type = scrapy.Field()