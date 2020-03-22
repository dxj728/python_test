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


##-----------------windows下使用线程：直接创建（常用推荐）------------------

# import threading, time
# ''' 线程构造器创建线程(推荐)----------------'''
# def action(max):
# 	for i in range(max):
# 		td_name = threading.current_thread().name	# 获取当前线程的线程名称
# 		print( td_name + ':' + str(i))
# 		time.sleep(1)		# 线程睡眠，当前线程处于阻塞状态
#
# threading.Thread(target=action, args=(100,), name="新线程").start()
# for i in range(40):
# 	if i == 20:
# 		jt = threading.Thread(target=action, args=(100,), name ="被join的线程")		# 创建线程（默认为前台线程）
#
# 		jt.daemon = True		# 设置为守护线程（后台线程，在start方法前设置，后台线程创建的也为后台线程），将在前台线程死亡后自动死亡
#
# 		jt.start()		# 线程已就绪，等待系统线程调度，可随时执行
#
# 		jt.join(timeout=10)		# 线程等待，主线程必须在子线程执行完成后才可再次执行, timeout设置最长等待时间（单位为秒），过时不再等待
#
# 	if i > 20:
# 		x = jt.is_alive()		# 判断线程是否已死亡，就绪，运行，阻塞时返回True, 新建，死亡时返回False, 已死亡的线程无法再次启动start(引发RuntimeRror异常)
# 		print(jt.is_alive())
# 	print(threading.current_thread().name + ' ' + str(i))

##-----------------windows下使用线程：继承创建------------------
# import threading
# '''继承Thread类来创建线程类------------'''
# class FkThread(threading.Thread):
# 	def __init__(self):
# 		threading.Thread.__init__(self)
# 		self.i = 0
#
# 	## 重写run方法作为线程执行体
# 	def run(self):
# 		while self.i < 100:
# 			print(threading.current_thread().getName() + ': ' + str(self.i))
# 			self.i += 1
#
# for i in range(100):
# 	print(threading.current_thread().getName() + ': ' + str(i))
# 	if i == 20:
# 		ft1 = FkThread()
# 		ft1.start()
# 		ft2 = FkThread()
# 		ft2.start()
# print("执行完成")

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


# ————————————————————线程锁————————————————————————————

# '''使用方法demo'''
# import threading
#
# class X:
# 	# 定义保证线程安全的方法
# 	def m(self):
# 		# 加锁
# 		self.lock.acquire()
# 		try:
# 			# 需要保证线程安全的代码
# 			# 方法体
# 		finally:		# 使用finally来保证释放锁
# 			# 修改完成释放锁
# 			self.lock.release()

# '''代码示例'''
# import threading
# import time
#
# class Account:
# 	# 定义构造器
# 	def __init__(self, account_no, balance):
# 		# 封装账户编号和账户余额两个成员变量
# 		self.account_no = account_no
# 		self._balance = balance
# 		self.lock = threading.RLock()		# 设置可重入锁（使用较广泛），acquire()必须与release()成对出现
#
# 	# 因为账户余额不允许随便修改，所以只为self._balance提供get方法
# 	def getBalance(self):
# 		return self._balance
#
# 	# 提供一个线程安全的draw()方法来完成取钱操作
# 	def draw(self, draw_amount):
# 		# 加锁
# 		self.lock.acquire()		# 加锁, timeout=参数可指定加锁时间，超时后会自动释放对lock的锁定
# 		try:
# 			# 账户余额大于取钱数目
# 			if self._balance >= draw_amount:
# 				# 吐出钞票
# 				print(threading.current_thread().name + '取钱成功，吐出钞票：' + str(draw_amount))
# 				time.sleep(1)
# 				# 修改余额
# 				self._balance -= draw_amount
# 				print("余额为：" + str(self._balance))
# 			else:
# 				print(threading.current_thread().name + '取钱失败，余额不足')
# 		finally:
# 			# 修改完成，释放锁
# 			self.lock.release()		# 释放锁
#
# # 定义一个函数来模拟取钱操作
# def draw(account, draw_amount):
# 	account.draw(draw_amount)
#
# # 创建一个账户
# acct = Account("123456", 1000)
# # 使用两个线程模拟从同一个账户中取钱
# threading.Thread(name='A', target=draw, args=(acct, 800)).start()
# threading.Thread(name='B', target=draw, args=(acct, 800)).start()


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
# 		self.cond.acquire()
# 		try:
# 			# 如果self._flag为False, 则表明账户中还没有人存钱进去。取钱方式被阻塞
# 			if not self._flag:
# 				self.cond.wait()
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







