# --coding:utf-8--
# File: threading_test.py
# Author: dxj728
# Time: 2019年03月06日23时
# 说明：多线程模块练习
# 参考来源： 廖雪峰的官方网站（进程与线程章节）：https://www.liaoxuefeng.com
import os


"""线程：
    特点：
    1.是进程的执行单元，一个线程必须拥有一个父进程
    2.线程不拥有系统资源，通过与父进程的其他线程共享进程所拥有的全部资源
    3.线程是独立运行的，其本身并不知道进程中是否还有其他线程存在
    4.线程的运行是抢占式的，即当前运行的线程在任何时候都有可能被挂起，以便于其他线程运行
"""

"""运行与阻塞：
    线程进入阻塞状态时条件：
        1.线程调用sleep()方法主动放弃其所占用的处理器资源
        2.线程调用了一个阻塞式IO方法，在IO返回之前，该线程阻塞
        3.线程试图获得一个锁对象，但该锁对象正被其他线程持有。
        4.线程在等待某个通知(Notify)
    线程解除阻塞重新进入就绪状态条件
        1.调用sleep()方法的线程经过了指定的时间
        2.线程调用的阻塞式IO方法已经返回
        3.线程成功的获得了锁对象
        4.线程正在等待某个通知时，其他线程发出了一个通知
"""

"""并发&并行
    并行(Parallel)：指同一时刻有多条指令在多个处理器上同时执行，适用于多进程
    并发(Concurrency)：指同一时刻只能有一条指令执行，但多个进程指令被快速轮换执行，适用于多线程
"""

"""线程控制:
    线程等待：join()方法
        jt.join(timeout=None)
        当程序执行流中调用其他线程的join()方法时，当前程序会被阻塞，知道被join()方法加入的join线程执行完成后继续执行
        timeout参数：该参数指定当前程序阻塞等待的时间最长为timeout秒，如果在timeout时间内join线程还未被执行结束，则不再等待
    后台线程:
        Daemon Thread，也被称为守护线程/精灵线程，如python解释器的垃圾回收线程
        特点：如果所有的前台线程都死亡了，则后台线程自动死亡
        创建后台线程的两种方式：
            1.创建线程时主动将线程的daemon属性设置为True(在start()方法调用前设置)
            2.后台线程启动的线程默认为后台线程
    线程睡眠：time.sleep(secs)
        用于指定线程阻塞多少秒
"""


##-----------------linux下创建线程及使用：fork()------------------
# print("当前进程是： %s" %os.getpid())
# pid = os.fork()
# if pid == 0:
#   print('生成的子线程：%s 当前父线程: %s '%(os.getpid(),os.getppid()))
# else:
#   print('主线程：%s 子线程：%s'% (os.getpid(),pid))


## -----------------windows下创建线程及使用1：直接创建（推荐）------------------

import threading, time
''' 线程构造器创建线程(推荐)----------------'''
# def action(max):
#     """线程调度方法"""
#     for i in range(max):
#         td_name = threading.current_thread().name	# 获取当前线程的线程名称
#         print( td_name + ':' + str(i))
#         time.sleep(1)		# 线程睡眠，当前线程处于阻塞状态
#
#
# """创建及使用示例"""
# threading.Thread(target=action, args=(100,), name="新线程").start()
# for i in range(40):
#     if i == 20:
#         """创建线程:
#                 __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
#                 group: 指定该线程所属的线程组
#                 target: 指定该线程要调度的目标方法
#                 args: 指定一个元组，以位置参数的形式依序为target目标函数传参
#                 kwargs: 指定一个字典，以关键字参数形式为target目标函数传参
#                 daemon: 指定创建的线程是否为后台线程
#         """
#         jt = threading.Thread(target=action, args=(100,), name ="被join的线程")		# 创建线程（默认为前台线程）
#
#         jt.daemon = True		# 设置为守护线程（后台线程，在start方法前设置，后台线程创建的也为后台线程），将在前台线程死亡后自动死亡
#
#         """线程启动: 线程已就绪，等待系统线程调度，可随时执行(实际运行取决于python解释器中线程调度器的调度)"""
#         jt.start()
#
#         jt.join(timeout=10)		# 线程等待，主线程必须在子线程执行完成后才可再次执行, timeout设置最长等待时间（单位为秒），过时不再等待
#
#     if i > 20:
#         x = jt.is_alive()		# 判断线程是否已死亡，就绪，运行，阻塞时返回True, 新建，死亡时返回False, 已死亡的线程无法再次启动start(引发RuntimeRror异常)
#         print(jt.is_alive())
#     print(threading.current_thread().name + ' ' + str(i))       # 返回当前正在执行的线程对象


##-----------------windows下创建线程及使用2：继承重写Thread类创建------------------

# import threading
# '''继承Thread类来创建线程类------------'''
# class FkThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.i = 0
#
#     def run(self):
#         """重写run方法作为线程执行体，但不可直接调用run方法"""
#         while self.i < 100:
#             print(threading.current_thread().getName() + ': ' + str(self.i))
#             self.i += 1
#
# """创建及使用示例"""
# for i in range(100):
#     print(threading.current_thread().getName() + ': ' + str(i))
#     if i == 20:
#         ft1 = FkThread()
#         ft1.start()
#         ft2 = FkThread()
#         ft2.start()
# print("执行完成")


##-----------------线程锁------------------
"""线程锁
    分类：
        threading.Lock(): 基本锁对象，每次只能锁定一次，其余的锁清秋，需等待锁释放后才能获取
        threading.RLock(): 可重入锁(常用)，可以在同一个线程中进行多次锁定，也可以多次释放，其acquire()和release()方法必须成对出现
    方法：
        acquire(blocking=True, timeout=-1): 请求对Lock或RLock加锁，
            block参数：默认为线程阻塞等待其他线程释放锁，False时该调用不会阻塞，并将立即返回当前线程是否实际获得了锁
            timeout参数：指定加锁多少秒
        release():释放锁
"""
import threading

class X:
    """使用锁的代码格式demo"""
    def __init__(self):
        self.lock = threading.Lock()
        self.Rlock = threading.RLock()
        
    def m(self):
        """定义需要保证线程安全的方法"""
        self.lock.acquire()     # 加锁
        try:
            print('需要保证线程安全的代码体')
        finally:        # 使用finally来保证释放锁
            self.lock.release()     # 修改完成释放锁


##-----------------线程通信------------------


















# ***************线程池**********************
#
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
#
# # 定义一个准备作为线程任务的函数
# def action(max):
# 	try:
# 		my_sum = 0
# 		for i in range(max):
# 			print(threading.current_thread().name + ' ' + str(i))
# 			my_sum += 1
# 		time.sleep(20)
# 		return my_sum
# 	except Exception as e:
# 		print('1'+ str(e))
#
# try:
# 	# 创建一个包含两个线程的线程池
# 	with ThreadPoolExecutor(max_workers=3) as pool:
#
# 		# 使用线程执行map计算
# 		# 后面的元组有3个元素，
# 		results = pool.map(action, [50, 100, 150, 200], timeout=10)
# 		print('----------')
# 		for r in results:
# 			print(r)
# except Exception as e:
# 	print('2'+ str(e))


# ————————————————————Condition通信———————————————————————————
#
# '''间隔存钱取钱练习'''
# import threading
#
# class Account:
# 	# 定义构造器
# 	def __init__(self, account_no, balance):
# 		# 封装账户编号和账户余额两个成员变量
# 		self.account_no = account_no
# 		self._balance = balance
# 		self.cond = threading.Condition()
# 		# 定义是否已经存钱的标志
# 		self._flag = False
#
# 	# 因为账户余额不允许随便修改，所以只为self._balance提供get方法
# 	def getBalance(self):
# 		return self._balance
#
# 	# 提供一个线程安全的draw()方法来完成取钱操作
# 	def draw(self, draw_amount):
# 		# 加锁，相当于调用condition绑定的lock的acquire()
# 		self.cond.acquire()		# timeout参数可指定超时时间
# 		try:
# 			# 如果self._flag为False, 则表明账户中还没有人存钱进去。取钱方式被阻塞
# 			if not self._flag:
# 				self.cond.wait()		# timeout参数可指定超时时间
# 			else:
# 				# 执行取钱操作
# 				print(threading.current_thread().name + "取钱：" + str(draw_amount))
# 				self._balance -= draw_amount
# 				print('账户余额为：' + str(self._balance))
# 				# 将表明账户中是否已有存款的标志设置为False
# 				self._flag = False
# 				# 唤醒其他线程
# 				self.cond.notify_all()
# 		finally:
# 			# 释放锁
# 			self.cond.release()
#
# 	def deposit(self, deposit_amount):
# 		# 加锁
# 		self.cond.acquire()
# 		try:
# 			# 如果self._flag为True, 表明账户中已有人存钱进去，存款方法被阻塞
# 			if self._flag:
# 				self.cond.wait()
# 			else:
# 				# 执行存款操作
# 				print(threading.current_thread().name + '存款：' + str(deposit_amount))
# 				self._balance += deposit_amount
# 				print('账户余额为：' + str(self._balance))
# 				# 将表明账户中是否已有存钱的标志设置为True
# 				self._flag = True
# 				# 唤醒其他线程
# 				self.cond.notify_all()
# 		finally:
# 			# 释放锁
# 			self.cond.release()
#
# def draw_many(account, draw_amount, max):
# 	for i in range(max):
# 		account.draw(draw_amount)
#
# def deposit_many(account, deposit_amount, max):
# 	for i in range(max):
# 		account.deposit(deposit_amount)
#
# # 创建一个账户
# acct = Account("123456", 0)
# threading.Thread(name='取钱者甲', target=draw_many, args=(acct, 800, 100)).start()
# threading.Thread(name='存钱者A', target=deposit_many, args=(acct, 800, 100)).start()
# threading.Thread(name='存钱者B', target=deposit_many, args=(acct, 800, 100)).start()

# ————————————————————使用队列（Queue）控制线程通信———————————————————————————

# '''简单用法示例'''
# import queue
#
# # 定义一个长度为2的阻塞队列
# bq = queue.Queue(2)
# bq.put('python')
# bq.put('c++')
# print('11111111')
# bq.put('java')		# 队列已满，此处会阻塞线程
# print('22222222')

# import threading
# import time
# import queue
#
# def product(bq):
# 	str_tuple = ("python", 'c++', 'java')
# 	for i in range(99999):
# 		print(threading.current_thread().name + '生产值准备生产元组元素！')
# 		time.sleep(0.2)
# 		# 尝试放入元素，如果队列已满，则线程会被阻塞
# 		bq.put(str_tuple[i % 3])
# 		print(threading.current_thread().name + '生产者生产完成')
#
# def consume(bq):
# 	while True:
# 		print(threading.current_thread().name + '消费者准备消费元组元素')
# 		time.sleep(0.2)
# 		# 尝试取出元素，如果队列已空，则线程被阻塞
# 		t = bq.get()
# 		print(threading.current_thread().name + '消费者消费[%s]元素完成' % t)
#
# # 创建一个容量为1的队列
# bq = queue.Queue(maxsize=1)
# # 启动3个生产者线程
# threading.Thread(name='A', target=product, args=(bq,)).start()
# threading.Thread(name='B', target=product, args=(bq,)).start()
# threading.Thread(name='C', target=product, args=(bq,)).start()
# # 启动1个消费者线程
# threading.Thread(name='甲', target=consume, args=(bq,)).start()
# '''
# 结果：本队列大小为1，3个生产者无法连续放入元素，必须等待消费者取出一个元素后，其中的一个生产者线程才能放入一个元素
# '''

# ————————————————————使用事件（Event）控制线程通信———————————————————————————

# '''简单使用示例'''
# import threading
# import time
#
# event = threading.Event()
# def cal(name):
#     # 等待事件，进入等待阻塞状态
#     print('%s启动，'% threading.currentThread().getName())
#     print('%s 准备开始计算状态' % name)
#     event.wait()		# 阻塞当前进程，timeout参数可设置阻塞事件
#     # 收到事件后进入运行状态
#     print('%s 收到通知了' % threading.currentThread().getName())
#     print('%s 正式开始计算' % name)
#
# # 创建并启动两个线程, 它们都会在wait处等待
# threading.Thread(target=cal, args=('甲')).start()
# threading.Thread(target=cal, args=('乙')).start()
# time.sleep(2)
# print('---------')
# # 发出事件
# print('主程序发出事件')
#
# '''
# set()		# 将Event的内部标志设置为True, 并唤醒所有处于等待状态的线程
# clear()		# 将Event的内部标志设置为False，一般接下来会调用wait()方法来阻塞当前线程
# wait()		# 该方法会阻塞当前线程，timeout可设置超时时间
# is_set()	# 该方法返回Event的内部旗标是否设置为True
# '''
