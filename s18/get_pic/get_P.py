#! -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import wget
import os
import urllib.request
import subprocess


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def mkdir(path):
    # 引入模块
    import os

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

        return False




def parse_html(html):
    selector = etree.HTML(html)
    # 目录剔除空格 linux下的目录不一样
    v_name = selector.xpath('//*[@id="contents"]/div/section/div/ul/li/a/@href')
    links = selector.xpath('//*[@id="contents"]/div/section/div/ul/li/a/p/img/@src')
    print(v_name,links)

    for i1,i2 in zip(v_name,links):
        patt =re.compile(r"(id=\d+)",re.S)
        get_id= re.findall(patt,i1)

        urllib.request.urlretrieve(i2, '{0}/{1}.jpg'.format(lpath,get_id[0]))
 







if __name__ == "__main__":
    for num in range(1,341):

        url = 'https://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page={0}/'.format(num)
        lpath  ="/root/JY/s18/get_pic"
        html =get_one_page(url)
        parse_html(html)
        print(url)


    # for num in range(1, 10000):

    #     url = 'https://xslist.org/zh/model/{0}.html'.format(num)
    #     print(url)

