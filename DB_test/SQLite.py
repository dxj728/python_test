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

'''4.执行DML语句进行增删改（需要commit步骤）'''
cursor.execute('insert into user_tb values(null, ?, ?, ?)',
               ('孙悟空', '123456', 'male'))
cursor.execute('insert into order_tb values(null, ?, ?, ?, ?)',
               ('鼠标', '34', '3', 1))

conn.commit()   # （重要步骤）提交事务后生效

'''5.执行DML语句进行查询（无需commit步骤）'''
cursor.execute('select * from user_tb where _id > ?;', (2,))

count = cursor.rowcount     # 获取返回的记录数, 实际上一直返回-1，无法使用
print(cursor.rowcount)
col_tuple = cursor.description  # 获取返回数据的列信息，为元组嵌套元组结构
print(col_tuple)

result_one = cursor.fetchone()     # 获取返回的1条记录，游标移动至返回结果末尾（即下次查询不会重复返回），无数据返回None
print(result_one)
result_many = cursor.fetchmany(100)     # 获取返回的多条记录(传参为数量n)，游标移动至返回结果末尾（即下次查询不会重复返回），无数据返回None
print(result_many)
result_all = cursor.fetchall()     # 获取返回的全部记录，游标移动至返回结果末尾，无数据返回None
print(result_all)

'''6.关闭游标，关闭连接'''
cursor.close()  # 关闭游标
conn.close()    # 关闭连接


# Other:其他方法
'''cursor.executemany(): 多次执行同一条SQL语句, 不同的参数以序列形式依次传参
        注：select语句可能会返回多个查询结果，因此不能使用该方法执行查询语句，无意义
'''
cursor.executemany('insert into user_tb values(null, ?, ?, ?)',
                   (('sun', '123456', 'male'),
                    ('bai', '123456', 'female'),
                    ('zhu', '123456', 'male'),
                    ('sha', '123456', 'male'),
                    ('tang', '123456', 'male'),))
cursor.executemany('update user_tb set name=? where _id=?',
                   (('小孙', '2'),
                    ('小白', '3'),
                    ('小猪', '4'),
                    ('小沙', '5'),
                    ('小唐', '6'),))

'''cursor.executescript(): 非标准API方法，用于执行一段SQL脚本'''
cursor.executescript('''insert into user_tb values(null, '武松', '3444', 'male');
                        insert into user_tb values(null, '林冲', '4444', 'male');
                        create table item_tb(_id integer primary key autoincrement,
                                              name,
                                              price);
                    ''')
# 上述修改均需要conn.commit()提交事务生效

'''其他函数：conn对象方法
    自定义函数： conn.create_function(name, num_params, func)：注册一个自定义函数，后面程序可以直接在SQL语句中使用该自定义函数
    自定义聚集函数： conn.create_aggregate(name, num_params, aggregate_class): 注册一个自定义的聚集函数
    自定义比较函数： conn.create_collation(name, callable): 注册一个自定义的比较函数
'''