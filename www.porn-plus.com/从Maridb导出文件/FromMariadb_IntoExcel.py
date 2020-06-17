

# 读取数据库数据
# 保存成excel文件
import csv
import pandas as pd
import numpy as np

from sqlalchemy import create_engine
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/Y_yin1')
    sql = ''' select * from pp1; '''
    df = pd.read_sql_query(sql, engine)
    # 　保存成csv文件必须是列表
    # 1. pandas ---->list
    # 2. 直接用pandas保存为excel文件
    train_data = np.array(df)  # np.ndarray()
    train_x_list = train_data.tolist()  # list
    df.to_excel("l.xlsx")

    # 首先使用np.array()    函数把DataFrame转化为np.ndarray()，再利用tolist()    函数把np.ndarray()    转为list
    with open('dog.csv', 'w', encoding='utf-8', newline='' "") as myFile:
        myWriter = csv.writer(myFile)

        myWriter.writerows(train_x_list)


#  Pandas将列表（List）转换为数据框（Dataframe）

# Python中将列表转换成为数据框有两种情况：第一种是两个不同列表转换成一个数据框，第二种是一个包含不同子列表的列表转换成为数据框。
#
# 第一种：两个不同列表转换成为数据框
# 第二种：将包含不同子列表的列表转换为数据框


# from pandas.core.frame import DataFrame
#
# a = [1, 2, 3, 4]  # 列表a
# b = [5, 6, 7, 8]  # 列表b
#
# c = {"a": a,
#      'b': b}  # 将列表a，b装换成字典
#
# data = DataFrame(c)
# print(data)

