# --coding:utf-8--
# File: SQLite.py
# Author: dxj728
# Time: 2021年08月01日11时
# 说明：python默认自带sqlite数据库学习
#   sqlite3.apilevel >> '2.0'  代表该数据库模块遵守DB2.0规范
#   sqlite3.paramstle >> 'qmark'    代表该数据库SQL语句使用?代表参数


'''SQLite内部支持数据类型：
    NULL、INTEGER、REAL(浮点数)、TEXT(文本)、BLOB(大二进制对象)
    实际上，SQLite也兼容varchar(n), char(n), decimal(p,s)等数据类型，只不过会在运算或保存时将其转为上述5种类型之一
    除integer primary key定义的字段只能存储64位整数以外，允许各种类型的数据保存到任何类型的字段中，即存入数据时忽略底层数据列实际的类型，亦可以建表时省略字段后的类型声明
'''


import sqlite3


'''1.打开或创建一个sqlite数据库，存在即打开，不存在即在当前目录下创建'''
conn = sqlite3.connect('sqlite_test.db')  # 如果创建数据库名为":memory:",即代表该数据库创建在内存中

'''2.获取游标'''
cursor = conn.cursor()

'''3.执行DDL语句创建数据表'''
sql1 = '''create table user_tb(_id integer primary key autoincrement,
                                name text,
                                pass text,
                                gender text)'''
cursor.execute(sql1)
sql2 = '''create table order_tb(_id integer primary key autoincrement,
                                item_name text,
                                item_price real,
                                item_number real,
                                user_id inteter,
                                foreign key(user_id) references user_tb(_id))'''
cursor.execute(sql2)

'''4.执行DML语句进行增删查改'''
cursor.execute('insert into user_tb values(null, ?, ?, ?)',
               ('孙悟空', '123456', 'male'))
cursor.execute('insert into order_tb values(null, ?, ?, ?, ?)',
               ('鼠标', '34', '3', 1))
conn.commit()   # 提交事务


cursor.close()  # 关闭游标
conn.close()    # 关闭连接