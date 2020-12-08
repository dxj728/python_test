# --coding:utf-8--
# File: set_test.py
# Author: dxj728
# Time: 2020年12月08日22时
# 说明：set(集合)类型学习
# 参考来源：https://www.runoob.com/python/python-func-set.html
#           https://blog.csdn.net/qq_40942329/article/details/78554218


set_demo = {1, 2, 2, 3, 'ok'}
set_demo2 = {1, 2, 4}
# print(type(set_demo))   # <class 'set'>
# print(set_demo)     # {1, 2, 3, 'ok'}
# print(dir(set))
# 'add', 'clear', 'copy', 'pop', 'update', 'remove', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update','isdisjoint','issubset','issuperset','symmetric_difference','symmetric_difference_update','union'

'''
	集合定义：一个无序、 不重复元素集
	集合创建：
		1.使用{value}创建，注：成功创建后自动去除重复元素
		2.使用set(set)函数创建，seq:可迭代对象
'''
# set1 = set('hello')
# print(set1)     # {'h', 'o', 'l', 'e'}

'''支持的常规运算操作：
	1.in 运算：是否为成员之一，返回True/False
	2.for x in set 运算: 逐一无序取出
	3.len(): 返回元素的个数
	4.max(): 同一类型返回最大值
	5.min(): 同一类型返回最小值
	6.del语句: 删除set对象，
'''
# print(2 in set_demo)    # True
# for x in set_demo:
# 	print(x)    # 无序打印
# print(len(set_demo))    # 4
# print(max({1, 2, 2, 3}))    # 3
# print(min({1, 2, 2, 3}))    # 1
# del set_demo
# print(set_demo)     # NameError异常: set_demo 名称未定义

'''增删查改：
	1.set.add(x): 增加一项(单个元素)，直接生效
	2.set.pop(): 随机弹出一项，直接生效
	3.set.remove(): 删除指定值，直接生效
	4.set.update(seq): 在set中添加多项(可迭代对象)，直接生效
	5.set.clear()；清空set至空集合，直接生效
'''
# set_demo.add(4)
# print(set_demo)     # {1, 2, 3, 4, 'ok'}
# set_demo.pop()
# print(set_demo)     # 随机(有规律)：{2, 3, 4, 'ok'}
# set_demo.remove(2)
# print(set_demo)     # {3, 4, 'ok'}
# set_demo.update({1:'a', 6: 7})
# print(set_demo)     # {1, 3, 4, 6, 'ok'}
# set_demo.clear()
# print(set_demo)     # set()

'''独有操作(运算符版本)：set之间计算交集，并集，差集, 运算符计算参数必须均为set集合
	set1 & set2 : 计算交集(重叠部分)，返回值生效
	set1 | set2 : 计算并集(混合全部)，返回值生效
	set1 - set2 : 计算差集(存在set1，但不存在于set2中)，返回值生效
	set1 ^ set2 : 计算对称差集(均不存在)，返回值生效
	set1 <= set2: 测试set1是否是set2的子集(set2包含set1中任一元素)，返回值生效
	set1 >= set2: 测试set1是否是set2的父集(set1包含set2中任一元素)，返回值生效
	
'''
# set_demo = {1, 2, 2, 3, 'ok'}
# set_demo2 = {1, 2, 4}

# x1 = set_demo & set_demo2
# print(x1)       # {1, 2}
# x2 = set_demo | set_demo2
# print(x2)       # {1, 2, 3, 'ok'}
# x3 = set_demo -set_demo2
# print(x3)       # {3, 'ok'}
# x4 = set_demo ^ set_demo2
# print(x4)       # {3, 4, 'ok'}
# x5 = set_demo <= set_demo2
# print(x5)       # False
# x6 = set_demo >= set_demo2
# print(x6)       # False

'''独有方法(非运算符版本)：非运算符计算参数需为可迭代对象即可
	set.issubset(seq):
'''


