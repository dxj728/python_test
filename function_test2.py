# --coding:utf-8--
# File: function_test2.py
# Author: dxj728
# Time: 2021年01月11日23时
# 说明：python内置函数的简单学习


"""map(func, iter): 根据提供的函数对指定序列做映射
		func: 指定函数
		iter: 元素列表
	:return 包含每次func函数返回值的新列表， python3中，需要使用list()函数手动转换
"""
def square(x):
	"""计算平方数"""
	return x ** 2

ret = map(square, [1, 2, 3, 4, 5])
print(list(ret))        # [1, 4, 9, 16, 25]
