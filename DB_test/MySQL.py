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
c.execute('insert into user_tb values(null, %s, %s, %s)', ('孙悟空', '123456', 'male'))
conn.commit()   # 增删改等修改数据的DML语句需要事务提交commit后生效，查询语句亦不需要commit提交事务

'''3.3调用executemany()方法多次执行同一条语句'''
c.executemany('insert into user_tb values(null, %s, %s, %s)',
                (('sun', '123456', 'male'),
                 ('bai', '123456', 'female'),
                 ('zhu', '123456', 'male'),
                 ('niu', '123456', 'male'),
                 ('tang', '123456', 'male')))
conn.commit()   # 数据修改需要commit()提交事务生效

'''3.4 autocommit：mysql数据库模块自带属性，为True时代表关闭该连接的事务支持，即DML语句执行后会自动提交事务，无需commit()方法显式调用'''
conn.autocommit = True

'''3.5查询数据'''
c.execute('select * from user_tb where id > %s', (2,))
for col in c.description:   # 游标的description属性可获取列信息
    print(col[0], end='\t')     # col[0]为当前列名
for row in c:       # 直接遍历游标中的结果集
    print(row)      # row为本条数据，元组格式

result1 = c.fetchone()   # 获取单条结果，每执行一次，游标会从移动一次数据位置，返回值为元组格式
result2 = c.fetchmany(10)   # 获取多条结果，每执行一次，游标会移动size次数据位置，size为指定条数，当前为10次，返回值为元组格式的列表
result3 = c.fetchone()   # 获取全部结果，返回值为元组格式的列表

'''4.关闭游标'''
c.close()

'''5.关闭连接'''
conn.close()

