# --coding:utf-8--
# File: process_test.py
# Author: dxj728
# Time: 2021年03月02日23时
# 说明：多进程练习


# -----------------linux下创建线程及使用：fork()------------------
"""使用os.fork()方法创建新进程(UNIX系统专用)
    os.fork(): 程序会启动两个进程(一个父进程，一个fork出来的子进程)来执行代码，该方法有一个返回值用于表明是哪个进程在执行
        1. 如果fork()方法返回0，表明是fork出来的子进程在执行
        2. 如果fork()方法返回非0，表明是父进程在执行，该方法返回fork()出来的子进程的进程ID
"""

import os

print("当前进程是： %s (父进程)" % os.getpid())
ret = os.fork()     # 开始fork一个子进程
# 从此处开始，下面的代码都会被两个进程执行
print('start...')
if ret == 0:
    print('生成的子线程：%s 当前父线程: %s ' % (os.getpid(), os.getppid()))     # 通过返回值来确定程序是否在执行子进程(此处仅有子进程执行)
else:
    print('主线程：%s 子线程：%s' % (os.getpid(), ret))     # 此处仅有父线程执行
print('end...')


# -----------------windows下创建线程及使用：multiprocessing模块------------------
"""
"""


