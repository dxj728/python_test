# --coding:utf-8--
# File: unittest_mod.py
# Author: dxj728
# Time: 2020年04月06日23时
# 说明：单元测试学习(unittest模块)

import unittest

# -----------------------单测例测试-------------------------------
from unittest_test import *


class TestCrazyitModule(unittest.TestCase):
	# 测试一元一次方程的求解
	def test_one_equation(self):
		''' 对结果进行断言判断 '''
		# 断言该方程的解应该为-1.8
		self.assertEqual(one_equation(5, 9), 1.8)
		# 断言该方程的解应该为-2.5
		self.assertTrue(one_equation(4, 10) != -2.5, .00001)
		# 断言方程的解应该为-27/4
		self.assertTrue(one_equation(4, -27) == -27 / 4)
		''' 对异常进行断言判断 '''
		# 断言当a == 0 时的情况，断言引发ValueError
		with self.assertRaises(ValueError):
			one_equation(0, 9)

	# 测试一元二次方程的求解
	def test_two_equation(self):
		''' 对结果进行断言判断 '''
		r1, r2 = two_equation(1, -3, 2)
		self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
		r1, r2 = two_equation(2, -7, 6)
		self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
		# 断言只有一个解的情况
		r = two_equation(1, -4, 4)
		self.assertEqual(r, 2.0, '求解出错')
		''' 对异常进行断言判断 '''
		# 断言当a==0时的情况， 断言引发ValueError
		with self.assertRaises(ValueError):
			two_equation(0, 9, 3)
		# 断言引发ValueError
		with self.assertRaises(ValueError):
			two_equation(4, 2, 3)

	#（可选） 每个测试用例执行前(test开头方法)执行该方法进行初始化
	def setUp(self):
		print('\n====执行setUp模拟初始化固件====')

	#（可选） 每个测试用例执行后(test开头方法)执行该方法进行销毁
	def tearDown(self):
		print('\n====调用tearDown模拟销毁固件====')


''' 
	第一种执行运行方式：main语句执行
	第二种执行运行方式：DOS： python -m unittest 测试文件(unittest_mod.py)
		注： python -m unittest 不指定文件则自动查找并运行当前目录下的所有测试用例
'''
if __name__ == '__main__':
	unittest.main()

# -----------------------测试包批量测试(TestSuite&&TestRunner)-------------------------------

import unittest
from test_fk_math import TestFkMath		# 测例文件类
from test_hello import TestHello


test_cases = (TestHello, TestFkMath)
def whole_suite():
	# 创建测试加载器
	loader = unittest.TestLoader()
	# 创建测试包
	suite = unittest.TestSuite()
	# 遍历所有测试类
	for test_class in test_cases:
		# 从测试类中加载测试用例
		tests = loader.loadTestsFromTestCase(test_class)
		# 将测试用例添加到测试包中
		suite.addTests(tests)
	return suite


'''
	测试报告输出至文件
'''
if __name__ == '__main__':
	# 创建测试运行器（TestRunner）
	# runner = unittest.TextTestRunner(verbosity=2)
	# runner.run(whole_suite())
	with open('fk_test_report.txt', 'a') as f:
		# 创建测试运行器（TestRunner），将测试报告输出到文件中
		runner = unittest.TextTestRunner(verbosity=2, stream=f)
		runner.run(whole_suite())


