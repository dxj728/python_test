# --coding:utf-8--
# File: class_test.py
# Author: dxj728
# Time: 2021年01月09日16时
# 说明：类和对象的学习

"""
	面向对象的三大特征：封装、继承、多态
"""
class Person:
	"""类的文档：定义了一个Person类作为示例"""
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
	
	def __hide(self):
		'''类的封装特性体现'''
		print("类的隐藏方法")  # 无法显式调用出来，但可通过 对象._类名+隐藏方法 实现调用(不建议)

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
# help(Person)        # 另一种查看类属性方法的方式
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

# ----------------------------使用type()函数创建类----------------------------
def fn(self):
	print('fn函数')
	
Dog = type('Dog', (object,), {'walk':fn, 'age':6})
d = Dog()
print(type(d))      # <class '__main__.Dog'>
print(type(Dog))    # <class 'type'>    \\ 所有的类均可视为type类的实例
d.walk()            # 'fn函数'
print(d.age)        # 6

# ----------------------------枚举类----------------------------
import enum

"""创建枚举类1：直接使用Enum列出多个枚举值来创建枚举类"""
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))    # 参数1为类名，参数2为枚举值元组(每个枚举成员都有name，value两个属性，value默认从1开始)
print(Season.SPRING)        # Season.SPRING     \\ 直接访问指定枚举
print(Season.SPRING.name)   # SPRING            \\ 访问枚举成员的变量名
print(Season.SPRING.value)  # 1                 \\ 访问枚举成员的值，默认从1开始递增
print(Season['SUMMER'])     # Season.SUMMER     \\ 根据枚举变量名访问枚举对象
print(Season(3))            # Season.SUMMER     \\ 根据枚举值访问枚举对象
for name, m in Season.__members__.items():  # 通过__members__属性遍历枚举
	print(name, m, m.value)
	# SPRING Season.SPRING 1
	# ... ...
	# WINTER Season.WINTER 4
	
"""创建枚举类2：通过继承Enum来派生枚举类，可定义更复杂的枚举"""
class E(enum.Enum):
	"""派生枚举类可自定义枚举值，以封装元组形式自动传给对应的value属性"""
	EAST = '东', '右东'
	SOUTH = '南', '下南'
	WEST = '西', '左西'
	NORTH = '北', '上北'
	def __init__(self, c_name, desc):
		"""枚举值构造器(可选)，传入参数必须按序对应枚举的value值"""
		self.c_name = c_name
		self._desc = desc
	
	@property
	def desc(self):
		return self._desc
	
	def info(self):
		"""枚举类可自定义的方法"""
		print('info:{}'.format(self.value))


print(E.SOUTH)          # E.SOUTH
print(E.SOUTH.value)    # ('南', '下南')
print(E['WEST'])        # E.WEST
print(E(('南', '下南')))          # E.SOUTH
E.SOUTH.info()   # info:('南', '下南')     \\ 调用枚举值的info方法
print(E.SOUTH.desc)     # '下南'        \\ 访问自定义的desc属性

# ----------------------------类的继承----------------------------
from types import MethodType

def fun_walk(self):
	print('walk...')

def say(self):
	print(self.S)

class meta_class(type):
	"""
	使用metaclass来使创建的某一批类全部均带有某种特征
	"""
	def __new__(cls, name, bases, attr):
		"""
		:param cls: 代表被动态修改的类
		:param name: 代表被动态修改的类名
		:param bases: 代表被动态修改类的所有父类
		:param attr: 代表被动态修改的类的所有属性、方法等组成的字典
		"""
		attr['say'] = say
		return type.__new__(cls, name, bases, attr)

class BaseA(metaclass=meta_class):
	def __init__(self, a, s):
		self.A = a
		self.S = s
	def info(self):
		print("BaseA中的info方法")
	def foo(self):
		print('BaseA中的foo方法')
	def funA(self):
		print('BaseA的funA: {}'.format(self.A))
		
class BaseB(metaclass=meta_class):
	def __init__(self, b, s):
		self.B = b
		self.S = s
	def info(self):
		print('BaseB中的info方法')
	def foo(self):
		print('BaseB中的foo方法')
		
class Sub(BaseA, BaseB):     # 多继承，前后顺序确定调用优先级
	__slots__ = ('walk', 'run', 'age', 'name')  # 使用__slots__属性限制当前类的实例允许动态添加的所有属性名和方法名，但不限制使用类动态添加，对于派生子类亦无作用
	def __init__(self, a, b, s):
		super().__init__(a, s)     # 通过super()函数调用父类的构造方法，BaseA继承顺序优先，故等同于super(BaseA, self).__init__(a)
		BaseB.__init__(self, b, s)    # 通过类调用父类的构造方法，需要手动传入self参数，等同于super(BaseB, self).__init__(b, s),
	def foo(self):
		print('Sub中的foo方法')     # 重写父类方法
	def bar(self):
		BaseA.foo(self)     # 调用父类方法，使用类名调用实例方法，需要手动绑定第一个参数
	def funB(self):
		print('BaseB的funB: {}, {}'.format(self.B, self.S))


a = BaseA('A', 'S1')
a.say()     # S1        \\ 使用metaclass使新建类全部默认带有某种特征
b = BaseB('A', 'S2')
b.say()     # S2        \\ 使用metaclass使新建类全部默认带有某种特征

m = Sub('A', 'B', 'S')
m.info()    # 'BaseA中的info方法'    \\ 继承顺序决定了调用优先级
m.foo()     # 'Sub中的foo方法'      \\ 子类方法覆盖了父类方法
m.bar()     # 'BaseA中的foo方法'      \\ 未绑定方法调用父类中被重写的方法
m.funA()    # 'BaseA的funA: A'
m.funB()    # 'BaseB的funB: B, S'
m.name = 'd'    # 实例对象动态添加属性
m.walk = MethodType(fun_walk, m)   # 实例对象动态添加方法,原方法必须至少有一个参数可以接收self
m.walk()    # walk...


ret1 = issubclass(Sub, BaseA)       # 判断类是为 类或元组所包含的多个类中任意类的子类,返回True/False
print(ret1)         # True
ret2 = isinstance(a, BaseA)         # 判断变量是否为 类或元组所包含的多个类中任意类的实例,返回True/False
print(ret2)         # True

'''该属性查看该类的所有直接父类，返回所有直接父类组成的元组'''
print(Sub.__bases__)        # (<class '__main__.BaseA'>, <class '__main__.BaseB'>)
'''该方法查看该类的所有直接子类，返回所有直接子类组成的列表'''
print(BaseA.__subclasses__())   # [<class '__main__.Sub'>]

