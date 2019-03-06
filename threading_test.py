# --coding:utf-8--
# File: threading_test.py
# Author: dxj728
# Time: 2019年03月06日23时
# 说明：多线程模块练习
# 参考来源： 廖雪峰的官方网站（进程与线程章节）：https://www.liaoxuefeng.com
import os

##-----------------fork()仅在linux/mac下使用------------------
print("当前进程是： %s" %os.getpid())
pid = os.fork()
if pid == 0:
	print('生成的子线程：%s 当前父线程: %s '%(os.getpid(),os.getppid()))
else:
	print('主线程：%s 子线程：%s'% (os.getpid(),pid))


