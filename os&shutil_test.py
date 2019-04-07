# --coding:utf-8--
# File: os&shutil_test.py
# Author: dxj728
# Time: 2019年04月07日23时
# 说明：os及shutil等系统模块操作练习，用于文件路径操作
# 参考来源：https://www.cnblogs.com/feeland/p/4463682.html

import datetime
import os
import shutil

excel_path = r'D:\desktop\test.xlsx'
time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

excel_dir = os.path.dirname(excel_path)		# 获取当前文件路径的上级目录路径
test_dir = os.path.join(excel_dir, 'test')		# 通用路径拼接方法，返回各系统的正确路径
copy_excel_path = os.path.join(test_dir, '备份'+time+'.xlsx')

# ***********************os模块练习*************************

if not os.path.exists(test_dir):
	os.mkdir(test_dir)		# 创建文件夹，文件已存在时报错（无法创建）

os.rmdir(test_dir)		# 删除空文件夹
os.remove(copy_excel_path)	# 删除单一文件


# ***********************shutil模块练习**********************

shutil.copy(excel_path, copy_excel_path)		# 复制文件/文件夹，复制 old 为 new（new是文件，若不存在，即新建），复制 old 为至 new 文件夹（文件夹已存在）

shutil.move(excel_path, test_dir)		# 移动文件/文件夹至 new 文件夹中

shutil.rmtree(test_dir)		# 强制删除文件夹及其下所有文件，路径下已打开文件无法删除会报错
