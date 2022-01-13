# --coding:utf-8--
# File: with_test.py
# Author: dxj728
# Time: 2021年01月16日20时
# 说明：with语句学习


"""with语句管理资源:
    with context_express [as target(s)]:
        处理代码块
    管理资源要求：实现上下文管理协议(context manager protocol)的类，返回对象可以称为上下文管理器，实现上下文管理协议必须实现以下两个方法。
    context_express.__enter__(): 进入上下文管理器必须调用的方法，在处理代码块之前执行，如果with有as子句，则__enter__方法的返回值将赋予给as子句后的变量/元组
    context_express.__exit__(exc_type, exc_value, exc_tb): 退出上下文管理器必须调用的方法，在处理代码块之后执行。可通过该方法判断处理代码块是否存在异常
"""

class FkResource:
    def __init__(self, tag):
        self.tag = tag
        print("__init__：{}".format(tag))
        
    def __enter__(self):
        """定义__enter__方法，它是在处理代码块执行之前执行的方法"""
        print('__enter__(): {}'.format(self.tag))
        return "enter ok"   # 可返回任意类型的值，该返回值将作为as语句后变量的值
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """定义__exit__方法，它是在执行代码块执行之后执行的方法"""
        print('__exit__(): {}'.format(self.tag))
        if exc_tb is None:      # exc_tb为None，代表没有异常
            print('无异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False        # 可省略，默认返回None


print('示例1...')
with FkResource('孙悟空') as dr:
    print(dr)                   # enter ok
    print('1无异常')            #
'''示例1执行结果'''
# __init__：孙悟空
# __enter__(): 孙悟空
# enter ok
# 无异常
# __exit__(): 孙悟空
# 无异常时关闭资源


print('示例2...')
with FkResource("猪八戒") as ds:
    print(ds)                   # enter ok
    print('2异常前')
    raise Exception
    print('2异常后')           # 此处不会被执行到
'''示例2执行结果'''
# __init__：猪八戒
# __enter__(): 猪八戒
# enter ok
# 异常前
# __exit__(): 猪八戒
# 遇到异常时关闭资源
# Traceback (most recent call last):
#     File "D:/git/python_test/with_test.py", line 45, in <module>
#         raise Exception
# Exception