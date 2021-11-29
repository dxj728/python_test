# --coding:utf-8--
# File: MySQL.py
# Author: dxj728
# Time: 2021年11月29日23时
# 说明：python相关mysql连接操作学习
# 依赖库： pip install mysql-connector-python


import mysql.connector

#   mysql.connector.apilevel >> '2.0'  代表该数据库模块遵守DB2.0规范
#   mysql.connector.paramstle >> 'pyformat'    代表该数据库SQL语句中使用扩展格式代码代表参数，mysql为%s

'''1.连接数据库'''
conn = mysql.connector.connect(user='root', password="HJKLiop123", host='localhost', port="3306", database="test", use_unicode=True)

'''2.获取游标'''
c = conn.cursor()

'''3.1调用execute()执行DDL创建表语句'''
sql1 = '''create table user_tb(id INT UNSIGNED AUTO_INCREMENT,
                              name VARCHAR(100),
                              pass VARCHAR(100),
                              gender VARCHAR(100),
                              PRIMARY KEY(id, name)
                              )ENGINE=INNODB DEFAULT CHARSET=utf8;'''
c.execute(sql1)     #DDL语句不需要事务提交(commit)，可直接生效

'''3.2调用execute()执行DML插入数据语句'''
sql2 = ''''''
c.execute('insert into user_tb values(null, %s, %s, %s)', ('孙悟空', '123456', 'male'))
conn.commit()   # 增删改等修改数据的DML语句需要事务提交commit后生效，查询语句亦不需要commit提交事务

'''4.关闭游标'''
c.close()

'''5.关闭连接'''
conn.close()

