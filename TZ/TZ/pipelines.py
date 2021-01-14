# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TzPipeline(object):
    def process_item(self, item, spider):
        self.f.write(
            item['course_nama'] + "--" +
            item['price_now'] + "--" +
            item['price_old'] + "--" +
            item['people_num'])
        self.f.write('\n')
        return item

    def open_spider(self, spider):
        self.f = open('data.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()
