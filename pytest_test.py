# --coding:utf-8--
# File: pytest_test.py
# Author: dxj728
# Time: 2022年03月07日23时
# 说明：pytest模块学习


import pytest

def setup_function():
    print('setup function-----------')

def teardown_function():
    print('teardown function----------')

    def setup_method(self):
        print('setup_method-------')

    def teardown_method(self):
        print('teardonw_method-------')

    def setup(self):
        print('setup-----------------')

    def teardown(self):
        print('teardonw--------------')

    def test_1(self):
        print('第一个类的测试方法1')

    def test_2(self):
        print('第一个类的测试方法2')

    # 类中的静态方法也是函数，
    @staticmethod
    def test_static():
        print('这个是一个类的静态方法-------')
    # 类方法不会作为测试方法执行
    @classmethod
    def test_cls(cls):
        print('这个是一个类方法-----')

def test_function():
    print('这个是函数1')


def test_function2():
    print('这个是函数2')

if __name__ == '__main__':
    pytest.main(['-vs','./pytest_test.py'])


