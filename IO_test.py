# --coding:utf-8--
# File: IO_test.py
# Author: dxj728
# Time: 2019年10月11日22时
# 说明：https://blog.csdn.net/qq_39928840/article/details/81132230

import os

"""input(): python3中使用该方法获取用户输入,等同于python2中raw_input()"""
# msg = input("请输入你的值：")      # 返回用户输入的内容，均为字符串类型
# 示例：
# msg1 = input().strip()              # 单行输入，返回字符串
# msg_list2 = list(map(int, input().strip().split()))      # 单行间隔输入(空格)，返回列表(当前强转为整型)
# msg_list3 = [int(input().strip()) for _ in range(6)]          # 多行输入，返回列表(元素强转为整型)
# msg_list4 = [list(map(int, input().strip().split())) for _ in range(6)]      # 多行多间隔输入，返回嵌套列表(元素强转为整型)

# print('\n'.join(map(str, msg_list4)))    # 返回结果表达
























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
