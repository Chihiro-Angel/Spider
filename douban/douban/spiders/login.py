# -*- coding: utf-8 -*-
import scrapy
import json
import logging

logger = logging.getLogger('logger_login')


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['accounts.douban.com']
    start_urls = ['https://accounts.douban.com/passport/login_popup?login_source=anony']
    
    def parse(self, response):
        logger.info("Parse function called on %s", response.url)
        login = "https://accounts.douban.com/j/mobile/login/basic"
        formdata = {
            'ck': '',
            'name': 'sed51320@163.com',
            'password': 'Stars51320',
            'remember': 'false',
            'ticket': ''
        }
        headers = {
            'Cookie': 'll="118407"; bid=b1a6pzLEZTE; apiKey=; __utma=30149280.1501572647.1584417734.1584417734.1584417734.1; __utmc=30149280; __utmz=30149280.1584417734.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21374; __utmb=30149280.5.10.1584417734; login_start_time=1584418181258',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'Sec-Fetch-Mode': 'no-cors',
        }
        yield scrapy.FormRequest(url=login ,method="POST", formdata=formdata, callback=self.login_check, headers=headers)

    def login_check(self, response):
        logger.info("登录验证。。。。。")
        res = json.loads(response.text)
        if res["status"] == "success":
            print('*'*100)
            print("登录成功！")
            print('name: \t',res["payload"]["account_info"]["name"])
            print("phone:\t",res["payload"]["account_info"]["phone"])
            print("id:   \t",res["payload"]["account_info"]["id"])
            print('*'*100)
        else:
            logger.warning("登录失败")
            print("登录失败")
        print(res)
