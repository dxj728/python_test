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


# def action(max):
#     for i in range(max):
#         print("{}子进程 (父进程：{} ): {}".format(os.getpid(), os.getppid(), i))
#
#
# if __name__ == '__main__':
#     for i in range(100):
#         print("{}主进程： {}".format(os.getpid(), i))
#         if i == 20:
#             mp1 = multiprocessing.Process(target=action, args=(100,))       # 创建第一个进程
#             mp1.start()     # 启动第一个进程
#
#             mp2 = multiprocessing.Process(target=action, args=(100,))       # 创建第二个进程
#             mp2.start()     # 启动第二个进程
#             mp2.join()      # 主进程必须等待mp2进程完成后才能向下执行
#     print("主进程执行完成")


# windows下创建线程及使用2：继承Process创建

import multiprocessing
import os

# class MyProcess(multiprocessing.Process):
#     def __init__(self, max):
#         self.max = max
#         super().__init__()
#
#     def run(self):
#         """重写run()方法作为进程执行体"""
#         for i in range(self.max):
#             print("{}子进程 (父进程: {}): {}".format(os.getpid(), os.getppid(), i))
#
#
# if __name__ == '__main__':
#     for i in range(100):
#         print("{}主进程： {}".format(os.getpid(), i))
#         if i == 20:
#             mp1 = MyProcess(100)        # 创建第一个进程
#             mp1.start()     # 启动第一个进程
#             mp2 = MyProcess(100)        # 创建第二个进程
#             mp2.start()     # 启动第二个进程
#             mp2.join()
#     print("主进程执行完成！")


## -----------------进程池(multprocessing.Pool)------------------
"""进程池：
    pool = multiprocessing.Pool(processes=4)
    实际上该Pool()函数是multprocessing.pool.Pool类
    进程池相关方法：
        1. apply(func, args, kwds): 提交func函数至进程池处理，该方法会被阻塞直到func函数执行完成
            参数func: 需要提交给进程池处理的函数func
            参数args: 代表传给func函数的位置参数
            参数kwds: 代表传给func的关键字参数
        2. apply_async(func, args, kwds, callback, error_callback): 相当于apply()方法的异步版本，不会被阻塞
            参数func: 需要提交给线程池执行的函数func
            参数args: 传给func的位置参数
            参数kwds: 传给func的关键字参数
            参数callback: 指定func函数完成后的回调函数
            参数error_callback: 指定func函数出错后的回调函数
        3. map(func, iterable, chunksize): 类似于map()全局函数，此处使用进程对iterable中的每一个元素执行func函数
        4. map_async(func, iterable, chunksize, callback, error_callback): 上述map()函数的异步版本，即不会被阻塞
            参数callback: 指定func函数完成后的回调函数
            参数error_callback: 指定func函数出错后的回调函数
        5. imap(func, iterable chunksize): map方法的延迟版本
        6. imap_unordered(func, iterable, chunksize): 功能类似于imap()方法，该方法不能保证所生成的结果(多结果时)与原iterable中元素顺序一致
        7. starmap(func, iterable, chunksize): 功能类似于map()方法，但该方法要求iterable的元素也是iterable对象，程序会将每一个元素解包后作为func的参数
        8. close(): 关闭进程池，调用该方法后，进程池将不再接收新任务，会将当前进程池中的所有任务执行完成后再关闭
        9. terminate(): 立即中止进程池
        10. join(): 等待所有进程完成
"""
import multiprocessing
import time
import os


# def action(name='default'):
#     '''作为进程任务的函数func'''
#     print('{}进程正在执行，参数为{}'.format(os.getpid(), name))
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     """---使用代码示例1---"""
#     pool = multiprocessing.Pool(processes=4)        # 创建包含4个进程的进程池
#     # 将action分3次提交给进程池
#     pool.apply_async(action)
#     pool.apply_async(action, args=('位置参数',))
#     pool.apply_async(action, kwds={'name': '关键字参数'})
#     pool.close()
#     pool.join()
#
#     """---使用代码示例2---"""
#     with multiprocessing.Pool(processes=4) as pool:
#         results = pool.map(action, (50, 100, 150))
#         for r in results:
#             print(r)


# -----------------进程间通信------------------








