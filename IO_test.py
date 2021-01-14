# --coding:utf-8--
# File: IO_test.py
# Author: dxj728
# Time: 2019年10月11日22时
# 说明：https://blog.csdn.net/qq_39928840/article/details/81132230


"""input(): python3中使用该方法获取用户输入,等同于python2中raw_input()"""
# msg = input("请输入你的值：")      # 返回用户输入的内容，均为字符串类型

# 示例：
# msg1 = input().strip()              # 单行输入，返回字符串
# msg_list2 = list(map(int, input().strip().split()))      # 单行间隔输入(空格)，返回列表(当前强转为整型)
# msg_list3 = [int(input().strip()) for _ in range(6)]          # 多行输入，返回列表(元素强转为整型)
# msg_list4 = [list(map(int, input().strip().split())) for _ in range(6)]      # 多行多间隔输入，返回嵌套列表(元素强转为整型)

# print('\n'.join(map(str, msg_list4)))    # 返回结果表达


"""
打开文件：open(file, mode, buffer, encoding)
	file: 文件名称或路径
	mode: 文件打开模式
	buffer: 缓冲大小，0(无缓冲)，1(带缓冲)，>1整数(指定寄存区缓冲大小)，负数(默认缓冲大小)
	encoding: 指定字符集，windows下默认为GBK字符集
文件打开模式mode：r、w、a、+、b、
	r: 只读模式，不能创建文件(要求操作文件必须存在)，指针位于文件开头
	w: 写模式，操作文件存在会清空文件，操作文件不存在则新建文件
	a: 追加写入模式，操作文件存在会清空文件，操作文件不存在则新建文件，指针位于文件结尾
	r+: 读写模式，与r作用相同，但可写入文件
	w+: 读写模式，与w作用相同，但可读取文件
	a+: 追加读写模式，与a作用相同，但可读取文件
	b； 二进制模式，可与其他模式结合使用，比如rb、ab等
"""

f = open('test.py', "r", 10, encoding='utf-8')
print(f.name)       # test.py       \\ 返回文件名称或路径
print(f.mode)       # r             \\ 返回被打开文件的访问模式
print(f.encoding)   # utf-8         \\ 返回被打开文件的当前使用字符集
print(f.closed)     # False         \\ 文件是否被关闭，返回True(已被关闭)/False(未被关闭)




















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
