# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re
import copy
import pymysql

import time
from selenium import webdriver
from lxml import etree
import datetime
from all_link import f_l


#请求

def get_first_page(url):


# 把首页和翻页处理？

# def removeStall(i_list):
#     f_list = []
#
#     for item in i_list:
#         f_i = "".join(item.split(","))
#         f_list.append(f_i[:-1])
#     return f_list

def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！


    selector = etree.HTML(html)

    l = []
    link = selector.xpath('//*[@id="vidsource"]/@src')
    for item in link:
        l.append(item[:-8])
    return l





def next_page():

    for i in range(1, 88):  # selenium 循环翻页成功！
        try:

            driver.find_element_by_xpath('//*[@id="page"]/a[last()]').click()
            html = driver.page_source
            return html
        except:
            print("先略过～")

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Y_yin1',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into pp1 (f_link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration :
        pass







if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    for one_url in f_l:
        driver.get(one_url)
        html = driver.page_source
        content = parse_html(html)
        insertDB(content)
        driver.quit()
    # while True:
    #     time.sleep(3)
    #     html = next_page()
    #     content = parse_html(html)
    #     insertDB(content)
    #     print(datetime.datetime.now())





# 字段设置了唯一性 unique
# LINK
# create table pp1(
# id int not null primary key auto_increment,
# f_link text
# ) engine=InnoDB  charset=utf8;


# drop table pp1;