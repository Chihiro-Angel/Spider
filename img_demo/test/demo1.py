#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 20:51
# @Author  : Aquarius
# @File    : demo1.py
# @Software: PyCharm

import requests
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Host": "www.tianjiang903.xyz",
    "Referer": "http://www.tianjiang903.xyz/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

# res = requests.get(
#     url="http://www.tianjiang903.xyz/api.php?cid=360tags",
#     headers=headers
# )
#
# print(res.text)
# print(1052/30)

# from urllib import parse
# print(parse.unquote("\u53c2\u6570\u4e0d\u6b63\u786e"))