# --coding:utf-8--
# File: variables&types_test.py
# Author: dxj728
# Time: 2020年12月14日22时
# 说明：变量和数据类型学习


print('hello world')

'''变量
    python中变量创建无需声明，并且数据类型可以被动态改变(弱类型语言特性)
'''
# a = 5
# print(a)    # 5         \\无需声明，变量赋值同时即是创建变量
# a = 'hello'
# print(a)    # hello     \\动态改变
#
# # 多变量赋值
# a = b = c = 1
# x, y, z = 1, 2, 3


'''常量：设定后不能再进行变动
    python中没有常量，一般通过约定俗成的变量名全大写的形式表示这是一个常量，并未真正实现，其对应值已然可以被改变
'''
# PI = 3.14


'''标准数据类型
    数值：下分为整型(int)、浮点型(float)、复数(complex)、长整型(long，python2)、
    字符串：str
    列表：list
    元组：tuple
    字典：dict
    集合: set
'''
int_10 = 4
int_2 = 0b111
int_8 = 0o54
int_16 = 0x2f
# print(type(4))      # int整型，十进制
# print(type(0b111))      # int整型，二进制(0b或0B开头)
# print(type(0o54))       # int整型，八进制(0o或0O开头)
# print(type(0x2f))      # int整型，十六进制(0x或0X开头)
#
# print(type(2.1))    # float浮点型
# print(type(5.12e2))     # float浮点型，科学计数形式(e或E)
#
# print(type(3+0.2j))     # complex复数
#
# print(type('e'))        # str字符串
#
# print(type([1, 2]))    # list列表
#
# print(type((1,)))       # tuple元组
#
# print(type({1: 'a', 2: 'b'}))   # dict字典
#
# print(type({1,2}))      # set集合

'''整型进制转换'''
# int2 = int('0b111', base=2)     # 二进制转十进制
# int8 = int('0o54', base=8)      # 八进制转十进制
# int16 = int('0x2f', base=16)    # 十六进制转十进制
# print(int2, int8, int_16)       # 7 44 47


'''变量作用域:
    局部变量：函数中定义的变量，包括传参，都称为局部变量
    全局变量：在函数外面，全局范围内定义的变量，被称为全局变量
'''
print(globals())    # 打印全局变量，总是返回全局变量字典
print(locals())     # 打印当前作用域中变量，全局范围内返回全局变量字典，函数内返回当前局部变量字典
print(vars())       # 打印指定对象范围内的所有变量字典，不传入参数的话，默认返回与locals()相同
# 备注: locals()和globals()获取到的全局变量可以被修改应用原值，但locals()获取的局部变量修改不影响原值

str1 = 'hello'      # 全局变量str1
str2 = 'world'      # 全局变量str2
def fun(str1='hi'):
    print(str1)     # 局部变量str1
    print(globals()['str2'])    # 访问全局变量str2
    global str2
    print(str2)     # 声明全局变量str2
    # global str1
    # print(str1)
    

# fun()
