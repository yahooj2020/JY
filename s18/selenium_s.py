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

from selenium import webdriver

driver = webdriver.Chrome()

def get_one_page(url):
    driver.get(url)
    html = driver.page_source
    return html







def parse_html(html):

    selector = etree.HTML(html)
    patt = re.compile('<h1 class="txt01">(.*?)</h1>', re.S)
    infos = re.findall(patt, html)
    # 目录剔除空格 linux下的目录不一样

    print(infos)

    s_links = selector.xpath('//*[@id="contents"]/div/section/ul/li/a/@href')
    for  item in s_links:
        f_l.append(item)





# 创建文本文档放在文件夹内，然后用wget去下载
if __name__ == "__main__":

    f_l =[]

    a_l = [
    'https://www.r18.com/videos/vod/movies/list/id=1008965/pagesize=120/price=all/sort=popular/type=actress/page=',
    # 'https://www.r18.com/videos/vod/movies/list/id=28011/pagesize=120/price=all/sort=popular/type=actress/page=',
    # 'https://www.r18.com/videos/vod/movies/list/id=1014614/pagesize=120/price=all/sort=popular/type=actress/page=',
    # 'https://www.r18.com/videos/vod/movies/list/pagesize=120/price=all/sort=popular/type=hd/page=',
    # 'https://www.r18.com/videos/vod/amateur/list/pagesize=120/price=all/sort=new/type=all/page=',
    # 'https://www.r18.com/videos/vod/amateur/list/pagesize=120/price=all/sort=popular/type=all/page='

]
    for num in range(1,4):
        try:


            for url in a_l:
                f_u = url+str(num)+'/'
                print(f_u)
                html =get_one_page(f_u)
                parse_html(html)
        except:
            pass

    for f_ in f_l:


        html1 = get_one_page(f_)
        selector = etree.HTML(html1)
        links = selector.xpath('//*[@id="contents"]/div[10]/div/section/section/section[1]/div[1]/div[2]/p/a/@data-video-high')
        for single_pic in links:
            print(single_pic)
            with open('t.txt', 'a') as file_handle:
                # .txt可以不自己新建,代码会自动新建

                file_handle.write(single_pic)  # 写入
                file_handle.write('\n')


