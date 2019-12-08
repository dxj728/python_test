# --coding:utf-8--
# File: multiprocessing_test.py
# Author: dxj728
# Time: 2019年03月26日00时
# 说明：多进程练习（廖雪峰的python教程：多进程）

# 进程池(Pool)
from multiprocessing import Pool
import os, time, random

# def long_time_task(name,j):
# 	print('Run task %s (%s)...' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print(j)
# 	print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
# 	print('Parent process %s.' % os.getpid())
# 	j=0
# 	p = Pool(4)				# 同时运行的最多进程数，实际效果与CPU核心数有关，
# 	for i in range(5):
# 		p.apply_async(long_time_task, args=(i, j))
# 	print('Waiting for all subprocesses done...')
# 	p.close()		# 关闭进程池，不再接受新任务，将当前进程池中的所有任务执行完成后再关闭自己
# 	p.join()		# 等待所有进程完成
# 	print('All subprocesses done.')


import multiprocessing
import os

def action(max):
	for i in range(max):
		print("{}子进程（父进程：{})：{}".format(os.getpid(), '0', i))

if __name__ == '__main__':
	for i in range(100):
		print("{}主进程： {}".format(os.getpid(), i))
		if i == 20:
			mp1 = multiprocessing.Process(target=action, args=(100, ))
			mp1.start()
			mp2 = multiprocessing.Process(target=action, args=(100, ))
			mp2.start()
			mp2.join()
	print('主进程完成！')