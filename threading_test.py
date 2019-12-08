# --coding:utf-8--
# File: threading_test.py
# Author: dxj728
# Time: 2019年03月06日23时
# 说明：多线程模块练习
# 参考来源： 廖雪峰的官方网站（进程与线程章节）：https://www.liaoxuefeng.com
import os

##-----------------fork()仅在linux/mac下使用------------------
# print("当前进程是： %s" %os.getpid())
# pid = os.fork()
# if pid == 0:
# 	print('生成的子线程：%s 当前父线程: %s '%(os.getpid(),os.getppid()))
# else:
# 	print('主线程：%s 子线程：%s'% (os.getpid(),pid))


import threading

def action(max):
	for i in range(max):
		print(threading.current_thread().name + ':' + str(i))

threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
	if i == 20:
		jt = threading.Thread(target=action, args=(100,), name ="被join的线程")
		jt.start()
		jt.join()
	print(threading.current_thread().name + ' ' + str(i))

