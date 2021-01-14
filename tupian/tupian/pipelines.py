# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

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
        img_type1 = item['image_type1']
        img_type2 = item.get('image_type2',None)
        img_name = item['image_name']
        if img_type2:
            return '%s/%s/%s.jpg'%(img_type1,img_type2,img_name)
        else:
            return '%s/%s.jpg'%(img_type1,img_name)
