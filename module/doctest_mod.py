# --coding:utf-8--
# File: doctest_mod.py
# Author: dxj728
# Time: 2020年04月06日22时
# 说明：python文档测试(doctest模块练习)

'''
    用法：程序只要导入doctest模块，并调用testmod()函数即可
    直接执行此代码，testmod()函数会自动提取该模块的说明文档中的测试用例，并执行生成测试报告
        a. 测例不通过将输出异常打印
        b. 通过则不生成任何输出

'''

## ----------------------文档测试示例代码----------------------

def square (x):
    '''
    一个用于计算平方的函数

    例如
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-3)
    9
    >>> square(0)
    0
    '''
    # return x * 2  # ①、故意写错的
    return x ** 2 # 修改正确

class User:

    '''
    定义一个代表用户的类，该类包含如下两个属性：
    name - 代表用户的名字
    age - 代表用户的年龄

    例如
    >>> u = User('fkjava', 9)
    >>> u.name
    'fkjava'
    >>> u.age
    9
    >>> u.say('i love python')
    'fkjava说: i love python'
    '''
    def __init__(self, name, age):
        self.name = 'fkit'  # ②、故意写错的
        # self.name = name  # 修改正确
        self.age = age
    def say(self, content):
        return self.name + '说: ' + content


if __name__=='__main__':
    import doctest
    doctest.testmod()






