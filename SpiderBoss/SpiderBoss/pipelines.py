# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import BookInfoItem, BookListItem, SpiderbossItem, BookListNovelItem

# class SpiderbossPipeline(object):
    
#     def process_item(self, item, spider):
#         # 处理item
#         if isinstance(item, SpiderbossItem):
#             self.f.write(item['name'] + '\r\n' +
#                         item['auth'] + '\r\n' +
#                         item['novel_title'] + '\r\n' +
#                         item['text'])
#             self.f.write('\n')
#         # item MySQL、MongoDB 抽象出来
#         return item

#     def open_spider(self,spider):
#         # 爬虫被打开的时候运行
#         # print('**'*30)
#         # 打开文件句柄
#         self.f = open('test.json','w',encoding='utf-8')

#     def close_spider(self,spider):
#         # 爬虫关闭的时候运行
#         # print('++'*30)
#         self.f.close()

class SpiderbookPipeline(object):
    
    def process_item(self, item, spider):
        if isinstance(item, BookListItem):
            content = json.dumps(dict(item),ensure_ascii=False)
            self.f1.write(content)
            self.f1.write('\n')
        elif isinstance(item, BookInfoItem):
            content = json.dumps(dict(item), ensure_ascii=False)
            self.f2.write(content)
            self.f2.write('\n')
        elif isinstance(item, BookListNovelItem):
            content = json.dumps(dict(item), ensure_ascii=False)
            self.f3.write(content)
            self.f3.write('\n')
        return item

    def open_spider(self,spider):
        # 爬虫被打开的时候运行
        # print('**'*30)
        # 打开文件句柄
        self.f1 = open('book.json', 'w', encoding='utf-8')
        self.f2 = open('book_sort.json', 'w', encoding='utf-8')
        self.f3 = open('book_test.json', 'w', encoding='utf-8')

    def close_spider(self,spider):
        # 爬虫关闭的时候运行
        # print('++'*30)
        self.f1.close()
        self.f2.close()
        self.f3.close()
