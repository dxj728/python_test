# --coding:utf-8--
# File: IO_test.py
# Author: dxj728
# Time: 2019年10月11日22时
# 说明：https://blog.csdn.net/qq_39928840/article/details/81132230

import os

"""获取用户输入"""
msg = input("请输入你的值：")      # python3中使用该方法获取用户输入，等同于python2中raw_input()，返回字符串
print(msg)          # hi
print(type(msg))    # <class 'str'>



# if __name__ == '__main__':
# 	file_path = r'D:\git\python_test\work.txt'
#
# 	f = open(file_path, 'rb', True)
# 	str_mysql = f.read().decode('utf-8').strip()
# 	print(str_mysql)
# 	str_mysql = str_mysql.lower()
# 	x = str_mysql.split('select')[1]
# 	print(x)
# 	y = x.split('from')[0]
# 	print(y)
# 	z = y.split(',')
# 	print(z)
# 	new_list = []
# 	for col in z:
# 		if 'as' in col:
# 			col = col.split('as')[1]
# 		col = col.strip()
# 		new_list.append(col)
# 	print(new_list)
