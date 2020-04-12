# --coding:utf-8--
# File: re_mod.py
# Author: dxj728
# Time: 2020年04月12日21时
# 说明：正则表达式及re模块学习
# 参考：python核心编程
# 不足：缺乏正向前视断言、负向前视断言、正向后视断言、后向后视断言的理解学习

import re

# '''
# 基础概念：
# 	abc: 直接匹配文本字符串字面值，全匹配模式
# 	. : 匹配任何1个字符，但不包含\n
# 	| : 匹配正则表达式或(or)
# 	^ : 匹配字符串开始部分
# 	$ : 匹配字符串结束部分
# 	* : 匹配0次或多次前面的正则表达式
# 	+ : 匹配1次或多次前面的正则表达式
# 	? : 匹配0次或1次前面的正则表达式
# 	{N} : 匹配N次前面出现的正则表达式
# 	{M,N} : 匹配M~N次前面出现的表达式
# 	[abc] : 匹配来自字符集的任一字符
# 	[a-b] : 匹配a-b范围内中的任一字符
# 	[^abc] : 不匹配此字符集中出现的任一字符
# 	(abc) : 匹配内部的正则表达式，并另存为子组
#
# 	\d : 匹配任何十进制数字
# 	\w : 匹配任何字母数字字符
# 	\W : 不匹配任何字母数字字符
# 	\s : 匹配任何空格字符，等同于 [\n\t\r\v\f]
# 	\b : 匹配任何单词边界
# 	\B : 不匹配任何单词边界
# 	\c : 逐个匹配任何特殊字符，如\n等，不匹配其特殊含义
# 	\N : 匹配已保存的子组N
# 	\A : 匹配字符串的开始，等同于^
# 	\Z : 匹配字符串的结束，等同于$
#
# 	贪婪模式： 正则表达式本质上实现贪婪匹配，即匹配尽可能多的字符
# 	非贪婪模式: 使用非贪婪操作符'?', 在'*'、'+'、'?' 后均可以使用该操作符
#
# '''

'''
返回的匹配对象方法
	group()：以普通方式显示所有的匹配部分,但也能通过参数获取各个匹配的子组
	groups(): 返回一个包含所有匹配子字符串的元组
'''

pattern = 'abc'

'''
	预编译方法（非必须），可以显著提高执行速度
	入参：正则表达式
	返回：一个正则表达式对象；对象可直接调用匹配方法，
'''
ret = re.compile(pattern) 	# 编译一个正则表达式，返回
# ret.match()
# ret.search()

'''
	match()方法：从字符串起始部分进行匹配，
	返回：匹配成功返回匹配对象，匹配失败返回None
'''
x = 'abc'
m = re.match(x, 'abcd')		# m为返回的匹配对象或None
if m is not None:
	ret = m.group()		# 匹配对象的group方法可显示成功的匹配，None值调用group会报属性异常
	print('match():' + ret)
	# match():abc


'''
	search()方法：从字符串任意位置进行匹配
	返回：搜索成功返回匹配对象，搜索失败返回None
'''
x = 'abc'
m = re.search(x, '0abcd')		# m为返回的匹配对象或None
if m is not None:
	ret = m.group()		# 匹配对象的group方法可显示成功的匹配，None值调用group会报属性异常
	print('search():' + ret)
	# search():abc


'''
	findall()方法： 查询字符串中正则表达式全部的非重复出现的情况
	返回：查询成功返回所有匹配部分的列表，查询失败返回空列表
'''
x = 'car'
m = re.findall(x, 'carry the barcardi to the car')
print('findall():' + str(m))
# findall():['car', 'car', 'car']


'''
	finditer()方法： 与findall类似，但更加节省内存，查询字符串中正则表达式全部的非重复出现的情况
	返回：一个迭代器
'''
x = 'car'
m = re.finditer(x, 'carry the barcardi to the car')
for g in m:
	print('finditer():' + g.group())
# finditer():car
# finditer():car
# finditer():car


'''
	sub()方法：搜索与替换，将正则表达式匹配的部分进行某种形式的替换，通常为字符串或者函数
	返回：替换后的字符串
'''
x = 'X'
m = re.sub(x, 'Mr.D', 'hello, X \nOK, X')
print('sub():\n' + m)
# sub():
# hello, Mr.D
# OK, Mr.D


'''
	subn()方法：搜索与替换，同sub()类似, 单返回参数多一个数量
	返回：替换后的字符串和表示替换总数的数字的元组
'''
x = 'X'
m = re.subn(x, 'Mr.D', 'hello, X \nOK, X')
print('subn():' + str(m))
# subn():('hello, Mr.D \nOK, Mr.D', 2)


'''
	split()方法： 基于正则表达式的模式分割字符串
	返回：分割后的元素列表（不含分割字符）
'''
m = re.split(':', 'str1:str2"str3')
print('split():' + str(m))
# split():['str1', 'str2"str3']

