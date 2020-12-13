# --coding:utf-8--
# File: set_test.py
# Author: dxj728
# Time: 2020年12月08日22时
# 说明：set(集合)类型学习
# 参考来源：https://www.runoob.com/python/python-func-set.html
#           https://blog.csdn.net/qq_40942329/article/details/78554218


set_demo = {1, 2, 2, 3, 'ok'}       # 重复的2在后续会被自动消除
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
	3.set.remove(val): 删除指定值，指定值不存在时会报错，直接生效
	4.set.discard(val): 移除指定的集合元素，指定值不存在时不会报错，直接生效
	5.set.update(seq): 在set中添加多项(可迭代对象)，直接生效
	6.set.clear()；清空set至空集合，直接生效
'''
# set_demo.add(4)
# print(set_demo)     # {1, 2, 3, 4, 'ok'}
# set_demo.pop()
# print(set_demo)     # 随机(有规律)：{2, 3, 4, 'ok'}
# set_demo.remove(2)
# print(set_demo)     # {3, 4, 'ok'}
# set_demo.discard('haha')
# print(set_demo)     # {1, 2, 3, 'ok'}
# set_demo.update({1:'a', 6: 7})
# print(set_demo)     # {1, 3, 4, 6, 'ok'}
# set_demo.clear()
# print(set_demo)     # set()

'''独有操作(运算符版本，非运算符版本)：set之间计算交集，并集，差集等方法
	set1 & set2 : 计算交集(重叠部分)，计算参数必须均为set集合, 返回值生效
	set.intersection(seq): 计算交集(重叠部分)，非运算符版参数需为可迭代对象即可，返回值生效
	
	set1 | set2 : 计算并集(混合全部)，计算参数必须均为set集合, 返回值生效
	set.union(seq): 计算并集(混合全部)，非运算符版参数需为可迭代对象即可，返回值生效
	
	set1 - set2 : 计算差集(存在set1，但不存在于set2中)，计算参数必须均为set集合, 返回值生效
	set.difference(seq): 计算差集(存在set1，但不存在于set2中)，非运算符版参数需为可迭代对象即可，返回值生效
	
	set1 ^ set2 : 计算对称差集(均不存在,不重叠部分)，计算参数必须均为set集合, 返回值生效
	set.symmetric_difference(seq): 计算对称差集(均不存在,不重叠部分)，非运算符版参数需为可迭代对象即可，返回值生效
	
	set1 <= set2: 测试set1是否是set2的子集(set2包含set1中任一元素)，计算参数必须均为set集合, 返回值生效
	set.issubset(seq): 测试set是否是seq的子集(seq包含set中的任一元素)，非运算符版参数需为可迭代对象即可，返回值生效
	
	set1 >= set2: 测试set1是否是set2的父集(set1包含set2中任一元素)，计算参数必须均为set集合, 返回值生效
	set.issuperset(seq): 测试set是否是seq的父集(set包含seq中的任一元素)，非运算符版参数需为可迭代对象即可，返回值生效
'''

## set_demo = {1, 2, 2, 3, 'ok'}
## set_demo2 = {1, 2, 4}

# x1 = set_demo & set_demo2
# print(x1)       # {1, 2}
# x1a = set_demo.intersection(set_demo2)
# print(x1a)      # {1, 2}

# x2 = set_demo | set_demo2
# print(x2)       # {1, 2, 3, 'ok'}
# x2a = set_demo.union(set_demo2)
# print(x2a)      # {1, 2, 3, 4, 'ok'}

# x3 = set_demo - set_demo2
# print(x3)       # {3, 'ok'}
# x3a = set_demo.difference(set_demo2)
# print(x3a)      # {3, 'ok'}

# x4 = set_demo ^ set_demo2
# print(x4)       # {3, 4, 'ok'}
# x4a = set_demo.symmetric_difference(set_demo2)
# print(x4a)      # {3, 4, 'ok'}

# x5 = set_demo <= set_demo2
# print(x5)       # False
# x5a = set_demo.issubset(set_demo2)
# print(x5a)      # False

# x6 = set_demo >= set_demo2
# print(x6)       # False
# x6a = set_demo.issuperset(set_demo2)
# print(x6a)      # False

'''独有方法(非运算符版本)：非运算符版参数需为可迭代对象即可
	set.difference_update(seq): 移除两个集合中都存在的元素。在原值上直接生效。
	set.intersection_update(seq): 即计算交集，在原值上直接生效
	set.isdisjoint(seq): 判断两个集合是否包含有相同的元素，存在返回False，不存在返回True，返回值有效
	set.symmetric_difference_update(seq): 计算差集(存在set1，但不存在于set2中)，返回值生效
'''
# set_demo.difference_update(set_demo2)
# print(set_demo)     # {3, 'ok'}

# set_demo.intersection_update(set_demo2)
# print(set_demo)     # {1, 2}

# x7 = set_demo.isdisjoint(set_demo2)
# print(x7)       # False

# set_demo.symmetric_difference_update(set_demo2)
# print(set_demo)     # {3, 4, 'ok'}

'''其他方法
	set.copy(): 返回一个原集合的拷贝(深拷贝)，返回值生效
'''
# x8 = set_demo.copy()
# print(x8)   # {1, 2, 3, 'ok'}
# print(id(set_demo), id(x8))     # 3000130850600 3000382442408(内存地址不同，非浅拷贝)
