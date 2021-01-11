# --coding:utf-8--
# File: function_test.py
# Author: dxj728
# Time: 2020年12月26日18时
# 说明：函数的学习


'''函数：执行特定任务的一段代码
	组成：
		a.传入参数，即几个关键的需要动态变化的数据
		b.返回值，即需要传出的几个重要数据
		c.内部的实现过程
'''
def add(a, b):      # a,b为声明参数(形参),
	"""
	函数文档：简单加法实现
	param a: 加数1
	param b: 加数2
	return: 和
	"""
	sum = a + b     # 实现过程
	return sum      # 返回值


add(1, 2)       # 函数的使用，当前1,2为传入值(or实参)


'''函数的参数: 位置参数、关键字参数、默认参数、可变参数、参数收集、逆向参数收集
	定义参数顺序(形参从左至右)：位置参数-->默认参数-->可变参数-->参数收集
	调用参数顺序(实参从左至右)：位置参数-->关键字参数
	python传参方式为值传递，普通对象(str,数值)传递为值/实参的副本，可迭代对象传递为地址的引用
'''


def fun_para(str1):  # str即为最常见的传参，即必备参数or位置参数
	"""
	必备参数(位置参数)：最常见参数，即实参必须以正确的顺序传入函数，调用时的数量必须和形参一样
	"""
	print(str1)
	return


fun_para('Hi!')


def fun_keyword(str1, str2):
	"""
	关键字参数(实参): 根据参数名来传入参数值，无需遵守定义时形参的顺序，但规定关键字参数在位置实参之后传入
	"""
	print(str1)
	print(str2)
	return


fun_keyword('hello', str2='ok')     # hello为普通位置参数，红色的str2代表关键字参数(实参传递)，


def fun_default(str1='hello'):      # str为默认参数
	"""
	默认参数(形参): 函数定义时为形参指定默认值，此形参即为默认参数，规定在位置形参之后定义
	"""
	print(str1)
	return


fun_default()       # 函数调用时忽略传入参数(默认参数)


def fun_varargs(str1, *str2):   # *str2为可变参数，表示传入任意个无名参数，类型为tuple
	"""
	可变参数(形参)：该参数可以接收多个参数值(多个参数被当成元如传入)，通过在形参前加*实现，避免影响其他传参，建议放在形参末尾，规定每个函数最多一个可变参数
	"""
	print(str1)
	for s in str2:
		print(s)
	return


fun_varargs('a', 'b', 'c', 'd')


def fun_dictargs(str1, *str2, **str3):
	"""
	关键字参数(形参)： 也有称之为收集关键字参数，此时python会将传入的关键字参数收集成字典，通过在形参前加**实现，建议放在形参最末尾，规定每个函数最多一个收集关键字参数
	"""
	print(str1)     # 1
	print(str2)     # ('a', 'b', 'c')   \\ 打印元组
	print(str3)     # {'x': 'hi', 'y': 'hello'}  \\ 打印字典


fun_dictargs('1', 'a', 'b', 'c', x='hi', y='hello')



def fun_rever(str1, str2):
	"""
	逆向参数收集(实参)：当函数实参为列表/元组/字典时，将其拆分为单个元素后传递给形参，列表/元组通过给实参前加*实现，字典通过给实参前加**实现
	"""
	print(str1)
	print(str2)


list1 = ['a', 'b']
fun_rever(*list1)       # fun_rever('a', 'b')       \\ 按序逐个传入形参, 多传/少传均为报语法错误

dict1 = {'str1': 1, 'str2': 2}
fun_rever(**dict1)      # fun_rever(str1=1, str2=2)     \\ 等同于传入关键字参数，多传/少传均为报语法错误


## ----------------------------函数的高级用法:函数作为传参、函数作为返回值、匿名函数----------------------------

'''使用函数作为函数形参，即可在调用函数时传入不同的其他函数作为参数，动态的改变代码逻辑
'''
def cal(data, fn):
	result = []
	for e in data:
		result.append(fn(e))
	return result

def square(n):
	return n * n

def cube(n):
	return n * n * n

data = [3, 4, 5]

print(cal(data, square))        # 函数作为参数传入


'''使用函数作为返回值：使用函数作为其他函数的返回值
'''
def get_math_func(type):
	def square(n):      # 局部函数
		return n * n
	def cube(n):        # 局部函数
		return n * n * n
	if type == "square":
		return square   # 函数作为返回值
	else:
		return cube


math_func = get_math_func('square')
print(math_func(5))


'''匿名函数：lambda表达式
	1.必须使用lambda关键字定义
	2.长度只能为一行
	3.lambda关键字之后、冒号左边为参数列表，多个参数使用逗号隔开；冒号右边是返回值
'''

print(lambda x, y: x + y)
"""lambda表达式优点：
	1.省略函数定义过程，使代码更简洁
	2.可以在用完之后立即释放，提高了性能
"""


# ----------------------------偏函数----------------------------
"""偏函数：使用functools.partial可以创建一个新的函数，新函数通过固定住原函数的部分参数定义，从而在调用时更简单。
"""
import functools
int2 = functools.partial(int, base=2)       # 等同于：int(x, base=2)，只是固定了原函数的部分参数，不改变功能返回的新函数
print(int2('10'))   # 2


# ----------------------------@函数装饰器----------------------------
"""函数装饰器：本质上就是一个返回函数的高阶函数
	作用：
		1.将被修饰的函数B作为参数传递给@符号引用的函数A
		2.将函数B替换为函数A的返回值
	附：在被修饰函数之前、之后、抛出异常后增加某种处理逻辑的方式，就是其他编程语言中的AOP(面相切片编程)
"""
import functools

"""带参数的装饰器实例"""
def log(text):  # 装饰器带参数（函数C）
	def decorator(func):    # 装饰器（函数B）
		@functools.wraps(func)  # 修改装饰器属性与调用函数一致，可避免签名错误
		def wrapper(*args, **kw):       # 装饰器实际功能
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log('exec:')
def now():
	print('hello world!')


now()
# exec: now():
# hello world!



