# --coding:utf-8--
# File: list_test.py
# Author: dxj728
# Time: 2020年11月12日22时
# 说明：列表方法学习
# 参考来源：https://www.runoob.com/python3/python3-list.html


print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

'''列表的创建：
	1.直接[]定义创建
	2.使用list()函数将元组、区间(range)等对象转换为列表
'''

list_demo = ['hello', 20, 'world', -5.6, 'a']
list_demo2 = [7.2, 'ok', False]
print(type(list_demo))  # <class 'list'>


'''切片：
	list[start:end:step]: 切片，返回值后生效
	start：开始索引值（包含），可正可负。
	end：结束索引值（不包含），可正可负。
	step: 步长，复数为逆序（元素值本身不变）
'''
list1 = list_demo[1:3]
# print(list1)    # [20, 'world']


'''加法、乘法
	list加法：和就是列表包含的元素总和
	ret值：返回值生效
	注意：列表只能与列表相加，不能与元组直接相加
	
	list乘法：只能和整数进行乘法运算，意义就是将包含元素重复整数倍
	ret值：返回值生效
	注意：只能和整数进行乘法运算
'''
list2 = list_demo + list_demo2
# print(list2)    # ['hello', 20, 'world', -5.6, 'a', 7.2, 'ok', False]
list3 = list_demo2 * 3
# print(list3)    # [7.2, 'ok', False, 7.2, 'ok', False, 7.2, 'ok', False]


'''
	in运算: 用于判断列表或元组是否包含某个元素
	ret值：返回True/False
'''
# print(2 in list_demo)   # False


'''
	len(): 获取列表的长度, 返回值生效
	max(): 获取列表的最大值(必须为相同类型，并且可以比较大小)，返回值生效
	min(): 获取列表的最小值(必须为相同类型，并且可以比较大小)，返回值生效
'''
# print(max(list_demo))   # TypeError异常报错，非相同类型
int_list_demo = [20, 10, -2, 15.2, 102]     # 比较实际数值
# print(max(int_list_demo))   # 102
# print(min(int_list_demo))   # -2
# print(len(int_list_demo))   # 5
str_list_demo = ['abc', 'crazyit', 'Python', 'Kotlin']  # 顺序比较ASCII码值，小写字母97~122，大写字母65~90
# print(max(str_list_demo))   # crazyit
# print(min(str_list_demo))   # Kotlin

'''增删查改:
	增加元素
	list.append(): 入栈(代替push),参数值作为单个整体追加至原列表结尾，直接生效
	list.extend(): 参数值中的元素全部追加至原列表结尾，直接生效
	list.insert(): 在原列表中间增加元素，直接生效
	
	删除元素
	del语句：专用于删除操作,直接生效
	list.remove(): 删除第一个找到的元素，如未找到，引发ValueError错误,直接生效
	list.pop([index=-1]): 出栈，移除列表中的一个元素（默认最后一个元素），并且返回该元素的值, 直接生效
	list.clear(): 清空列表中的所有元素,直接生效
'''
# list_demo.append([1, 2])
# print(list_demo)    # ['hello', 20, 'world', -5.6, 'a', [1, 2]]
# list_demo.extend([1, 2])
# print(list_demo)    # ['hello', 20, 'world', -5.6, 'a', [1, 2], 1, 2]
# list_demo.insert(3, 'ok')
# print(list_demo)    # ['hello', 20, 'world', 'ok', -5.6, 'a', [1, 2], 1, 2]

# del list_demo[1:3]  # 删除第2个到第4个(不包含)元素
# print(list_demo)    # ['hello', -5.6, 'a']
# list_demo.remove('a')   # 删除第一个找到的'a'
# print(list_demo)    # ['hello', -5.6]
# x = list_demo.pop()
# print(list_demo)    # ['hello']
# print(x)            # -5.6
# list_demo.clear()
# print(list_demo)    # []


'''其他方法
	list.count(): 统计列表中某个元素出现的次数，返回值生效
	list.index(x, start, end): 用于判断某个元素在列表中出现的位置，如果该元素未出现，则报ValueError异常，start和end参数指定范围，返回值生效
	list.reverse(): 反向列表中元素，直接生效
	list.sort(x, cmp, key, reverse): 对列表元素进行排序，默认升序，需为同一比较类型，字符串按照编码比较大小，直接生效
		cmp: 指定的比较函数，python2可使用，python3取消该参数
		key: 用于生成比较的键的方法，
		reverse: 排序规则，True(降序)，False(默认升序)
	list.copy(): 用于复制列表，返回复制后的新列表，返回值生效
'''
# print(list_demo.count(20))      # 1     \\出现1次
# print(list_demo.index(20))      # 1     \\出现索引为1
# list_demo.reverse()
# print(list_demo)        # ['a', -5.6, 'world', 20, 'hello']
# int_list_demo.sort()
# print(int_list_demo)    # [-2, 10, 15.2, 20, 102]
# copy_list = list_demo.copy()
# print(copy_list)       # ['hello', 20, 'world', -5.6, 'a']
