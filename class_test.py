# --coding:utf-8--
# File: class_test.py
# Author: dxj728
# Time: 2021年01月09日16时
# 说明：类和对象的学习

"""
	面向对象的三大特征：封装、多态、封装
"""
class Person:
	"""类的文档：当前仅为示例使用"""
	cls_var = 'cls_var'      # 类变量，使用类调用变量(实例化调用亦可,但此时可读不可改)，定义该类本身所包含的状态数据
	
	def __init__(self, name='dxj', age=18):
		"""类的构造方法"""
		self.name = name        # 类的实例变量，用于定义示例对象所包含的状态数据
		self.age = age
		'''类的封装特性体现'''
		self.__weight = 100      # 双下划线隐藏变量，实际使用 对象._类名+隐藏方法/变量即可实现访问修改(不建议)
	
	def __del__(self):
		"""类的析构方法(很少使用):python作为高级语言，使用引用计数动态回收，很少使用该方法"""
		pass
	
	def say(self):
		"""类的实例方法：常见使用
			用于定义该类的对象的行为或功能实现，使用实例化对象调用(类直接调用需要给self传参)
		"""
		print('say():')

	@classmethod
	def walk(cls):
		"""类方法：使用@classmethod修饰
			可以使用类直接调用方法，无需实例化(实例化调用亦可)，python会默认绑定类方法的第一个参数(通常建议参数名为cls)
		"""
		print('类方法walk:')
		
	@staticmethod
	def run():
		"""静态方法：使用@staticmethod修饰
			可以直接使用类调用方法，无需实例化(实例化调用亦可)，但是需要手动绑定方法的第一个参数(亦可不传or不使用)
		"""
		print('静态方法run:')
	
	def __hide(self):
		'''类的封装特性体现'''
		print("类的隐藏方法")     # 无法显式调用出来，但可通过 对象._类名+隐藏方法 实现调用(不建议)

	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
	def del_name(self):
		self.name = "j"
		
	"""使用property方法定义属性1：
		相当于实例变量
		4个传参分别代表：getter, setter, del方法，doc文档
		依序传参个数代表当前属性能力：0个(不能读也不能写)，1个(只读)，2个(可读可写)，3个(可读可写可删除)，4个(3个+文档说明)
	"""
	name_info = property(get_name, set_name, del_name, "用于描述实例的属性")      # 当前定义了info属性及其访问器方法
	
	"""使用property方法定义属性2
		相当于实例变量
		装饰器名称代表其修饰方法，调用装饰器即代表赋予该属性相关能力，未调用该装饰器则代表属性无此能力
	"""
	@property       # 使用@property修饰器定义age_info属性
	def age_info(self):
		"""doc:定义age相关属性"""     # 此函数说明即代表属性doc文档
		return self.age
	
	@age_info.setter     # 修饰age属性的setter方法
	def age_info(self, age):
		self.age = age
	
	@age_info.deleter    # 修饰age属性的delter方法
	def age_info(self):
		self.age = 0


p = Person()    # 类的实例化

p.say()     # say():    \\ 类的实例方法调用，使用对象调用方法，常见用法
print(p.name)   # dxj   \\ 类的实例变量调用，使用对象调用，常见用法

print(Person.cls_var)   # cls_var    \\ 类的变量调用，使用类调用
Person.say('hi')        # say():    \\ 类的调用方法，显式传参，此调用称“未绑定方法”
Person.walk()           # 类方法walk:
Person.run()            # 静态方法run:

print(p.cls_var)    # cls_var   \\ 类的变量调用，使用对象调用
p.cls_var = "A"     # 此时是新建一个实例变量，而非修改类变量(可读不可改特性)
print(p.cls_var)    # A     \\ 此时打印实例变量
print(Person.cls_var)   # Hi    \\ 类变量不变

t = Person("d", 6)
print(Person.name_info.__doc__)     # '用于描述实例的属性'   \\ doc文档仅可使用类调用
help(Person)        # 另一种查看类属性方法的方式
print(t.name_info)  # d     \\ 访问t的name_info属性
t.name_info = 'x'   # 对t的name_info属性赋值
print(t.name_info)  # x
del t.name_info     # 删除t的name_info属性
print(t.name_info)  # j
print(t.age_info)   # 6
t.age_info = 12
print(t.age_info)   # 12
del t.age_info
print(t.age_info)   # 0
print(Person.age_info.__doc__)      # 'doc:定义age相关属性'   \\ doc文档仅可使用类调用

# def func_add(self):
# 	print('func_add:', self)
#
#
# p.foo = func_add        # 动态为类添加方法，但需要手动为第一个参数值传参
# p.foo(p)



