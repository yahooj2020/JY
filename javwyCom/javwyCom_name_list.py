# ! -*- coding:utf-8 -*-
import datetime
import urllib.request

import os


#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver



def get_one_page(url):
    #
    # driver.get(url)
    # html = driver.page_source
    # return html

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except :
        return None

def parse_page(html):
    big_list = []
    selector = etree.HTML(html)
    name = selector.xpath('/html/body/div[2]/div/div[1]/div/div[2]/ul/li/a/text()')
    links = selector.xpath('/html/body/div[2]/div/div[1]/div/div[2]/ul/li/a/@href')

    for i1,i2 in zip(name,links):
        big_list.append((i1,'http://javwy.com'+i2))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='javwyCom',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into javwyCom_name_list (name,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":

    for item in range(1,10):
        url = 'http://javwy.com/jav-actress-list/page/{0}'.format(item)
        html = get_one_page(url)
        content = parse_page(html)
        insertDB(content)
        time.sleep(1)



#
# create table javwyCom_name_list(
# id int not null primary key auto_increment,
# name text,
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table R_links;



