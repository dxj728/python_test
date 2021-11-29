# --coding:utf-8--
# File: MySQL.py
# Author: dxj728
# Time: 2021年11月29日23时
# 说明：python相关mysql连接操作学习
# 依赖库： pip install mysql-connector-python


import mysql.connector

#   mysql.connector.apilevel >> '2.0'  代表该数据库模块遵守DB2.0规范
#   mysql.connector.paramstle >> 'pyformat'    代表该数据库SQL语句中使用扩展格式代码代表参数，mysql为%s

# 连接数据库
conn = mysql.connector.connect(user='dxj728', password="HJKLiop123", host='localhost', port="3306", database="test", use_unicode=True)
# 获取游标
c = conn.cursor()
