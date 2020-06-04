# 第一个爬虫示例,爬取百度页面

import requests #导入爬虫的库，不然调用不了爬虫的函数
import os

response = requests.get("http://www.baidu.com")  #生成一个response对象

response.encoding = response.apparent_encoding #设置编码格式

print("状态码:"+ str( response.status_code ) ) #打印状态码

with open(file="baidu.txt",mode="w",encoding="utf-8")as fo:
    fo.write(response.text)
