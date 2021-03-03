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

# import os
#
# print("当前进程是： %s (父进程)" % os.getpid())
# ret = os.fork()     # 开始fork一个子进程
# # 从此处开始，下面的代码都会被两个进程执行
# print('start...')
# if ret == 0:
#     print('生成的子线程：%s 当前父线程: %s ' % (os.getpid(), os.getppid()))     # 通过返回值来确定程序是否在执行子进程(此处仅有子进程执行)
# else:
#     print('主线程：%s 子线程：%s' % (os.getpid(), ret))     # 此处仅有父线程执行
# print('end...')


# ----------------------multiprocessing模块-----------------------
"""multiprocessing模块提供了Process来创建新进程，共有两种方式：
    1.以指定函数作为target，创建Process对象即可创建新进程
    2.继承Process类，并重写其run()方法来创建进程类，程序创建Process子类的实例作为进程
    Process类的相关方法和属性：
        1. run(): 重写该方法可实现进程的执行体
        2. start(): 该方法用于启动进程
        3. join([timeout]): 当前进程必须等待被join的进程执行完成后才能向下执行
        4. name: 该属性用于设置或访问进程名字
        5. is_alive(): 判断进程是否还活着
        6. daemon: 该属性用于判断或设置进程的后台状态
        7. pid: 返回进程的ID
        8. authkey: 返回进程的授权key
        9. terminate(): 中断该进程
"""
# windows下创建线程及使用1：直接创建（推荐）

import multiprocessing
import os


def action(max):
    for i in range(max):
        print("{}子进程 (父进程：{} ): {}".format(os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    for i in range(100):
        print("{}主进程： {}".format(os.getpid(), i))
        if i == 20:
            mp1 = multiprocessing.Process(target=action, args=(100,))       # 创建第一个进程
            mp1.start()     # 启动第一个进程
            
            mp2 = multiprocessing.Process(target=action, args=(100,))       # 创建第二个进程
            mp2.start()     # 启动第二个进程
            mp2.join()      # 主进程必须等待mp2进程完成后才能向下执行
    print("主进程执行完成")


# windows下创建线程及使用2：继承Process创建

import multiprocessing
import os

class MyProcess(multiprocessing.Process):
    def __init__(self, max):
        self.max = max
        super().__init__()
        
    def run(self):
        """重写run()方法作为进程执行体"""
        for i in range(self.max):
            print("{}子进程 (父进程: {}): {}".format(os.getpid(), os.getppid(), i))

        
if __name__ == '__main__':
    for i in range(100):
        print("{}主进程： {}".format(os.getpid(), i))
        if i == 20:
            mp1 = MyProcess(100)        # 创建第一个进程
            mp1.start()     # 启动第一个进程
            mp2 = MyProcess(100)        # 创建第二个进程
            mp2.start()     # 启动第二个进程
            mp2.join()
    print("主进程执行完成！")


