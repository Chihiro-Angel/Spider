# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

i = 0
class ImgDemoPipeline(object):

    def process_item(self, item, spider):
        global i
        i += 1
        with open("imgs/%s/%s.jpg"%(item['type_name'], item['tag_name']), 'wb+') as f:
            f.write(item['content'])

        return item

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class TupianPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_url = item['image_urls']
        if img_url:
            for url in img_url:
                yield Request(url=url,meta={'img_data': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['img_data']
        global i
        i += 1
        return 'imgs/%s/%s.jpg'%(item['type_name'], item['tag_name'])

