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
    patt = re.compile('<h1 class="txt01">(.*?)</h1>', re.S)
    infos = re.findall(patt, html)
    # 目录剔除空格 linux下的目录不一样
    f_path = "/root/JY/s18" + "/"+"".join(infos[0].split())
    fpic_path = "".join(f_path.split())
    print(infos)

    mkdir(fpic_path)
    v_name = selector.xpath('//*[@id="contents"]/div/section/ul/li/a/dl/dt/text()')
    links = selector.xpath('//*[@id="contents"]/div/section/ul/li/div/p/a/@data-video-low')
    print(infos)
    print(fpic_path)
    print(links)
    for i1,i2 in zip(v_name,links):
        f_name = "".join(i1.split())
        urllib.request.urlretrieve(i2, '{0}/{1}.mp4'.format(fpic_path,f_name[:20]))
        # Fname = fpic_path+"/"+"".join(i1.split())

        # cmd = 'wget -P {0} {1}.mp4'.format(Fname, i2)
        # subprocess.call(cmd, shell=True)

        # print(cmd)


if __name__ == "__main__":
    a_l = [
        'https://www.r18.com/videos/vod/movies/list/id=1057330/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1037293/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=27230/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1004672/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1030550/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1048468/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1037168/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=21549/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1040946/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1014614/pagesize=120/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1008965/pagesize=30/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=28011/pagesize=30/price=all/sort=popular/type=actress/page=1/',
        'https://www.r18.com/videos/vod/movies/list/id=1032833/pagesize=30/price=all/sort=popular/type=actress/page=1/'


    ]
    for url in a_l:

        html =get_one_page(url)
        parse_html(html)



