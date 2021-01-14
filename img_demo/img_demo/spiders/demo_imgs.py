# -*- coding: utf-8 -*-
import json

import scrapy

from ..items import ImgDemoItem


class DemoImgsSpider(scrapy.Spider):
    name = 'demo_imgs'
    start_urls = 'http://www.tianjiang903.xyz/api.php?cid=360tags'
    headers = {
        "Referer": "http://www.tianjiang903.xyz/",
    }
    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls,
            headers=self.headers,
            callback=self.parse)

    def parse(self, response):
        print(response.headers)
        print(response.text)
        for sku in json.loads(response.text)['data']:
            type_id = sku['id']
            type_name = sku['name']
            pages = sku['order_num']
            # print('\n\n\n**************************',type(pages),'*******************************************\n\n\n')
            # 拼接子分类的URL,,可修改
            for page in range(int(pages)):
                url = "http://www.tianjiang903.xyz/api.php?cid="+str(type_id)+"&start="+str(page*30)+"&count=30"
                yield scrapy.Request(
                    url=url,
                    headers=self.headers,
                    callback=self.parse_img_url,
                    meta={
                        'type_name': type_name
                    }
                )

    def parse_img_url(self,response):
        item = ImgDemoItem()
        item['type_name'] = response.meta['type_name']
        for sku in json.loads(response.text)['data']:
            item['image_urls'] = [sku['img_1280_1024']]
            item['tag_name'] = sku['utag']
            yield item

            # yield scrapy.Request(
            #     url=img_url,
            #     callback=self.parse_img_item,
            #     meta={
            #         'type_name': type_name,
            #         'tag_name': tag_name
            #     }
            # )

    # def parse_img_item(self,response):
    #     type_name = response.meta['type_name']
    #     tag_name = response.meta['tag_name']
    #     content = response.body
    #
    #     if type_name:
    #         type_name = type_name.strip()
    #     else:
    #         type_name = '其他'
    #
    #     if tag_name:
    #         tag_name = tag_name.strip()
    #     else:
    #         tag_name = '其他'
    #
    #     item = ImgDemoItem()
    #     item['type_name'] = type_name
    #     item['tag_name'] = tag_name
    #     item['content'] = content
    #     yield item



# 新闻


# 情感分析：自然语言处理（NLP）。
    # 今天的新闻的情感倾向，0-10
    # 今天 天气 真好，我 很 开心 （jieba） 7

# NLP + 机器学习 + 数据分析（numpy pandas matplotlib{matlib}）
# web -> 展示，NLP

# 微博热搜：xxx恋情公布 + NLP -> 同意/不同意












