# --coding:utf-8--
# File: os_test.py
# Author: dxj728
# Time: 2019年08月19日23时
# 说明：python3.6下 os模块，os.path模块学习笔记

import os

dir_path = r'D:\test'
dir_paths = r'D:\test\haha\so\e'
file_path = r'D:\test\test.txt'
## *********************** os 模块 ***********************************

# x = os.getcwd()                # 获取当前所在路径，返回值: 字符串
#
# x = os.listdir(dir_path)        # 获取指定路径下文件和目录名称的列表list，返回值: list[string,]
#
# os.chdir(dir_path)            # 将当前工作目录改为指定目录，无返回值（在任何情况下都返回None）
#
# dir_path = r'D:\test\xixi'
# os.mkdir(dir_path)        # 创建一个目录，并指定访问权限（8进制，默认权限511，linux下777权限，windows下无mode参数可忽略），无返回值，目录存在是报WindowsError错误
#
#
# os.makedirs(dir_paths)        # 递归创建目录，并指定访问权限（windows下mode参数无用），无返回值，目录存在是报错
#
# os.rmdir(dir_paths)        # 删除指定的空目录，无返回值，目录非空时报OSError异常，目录不存在报WindowsNotFound异常
#
# os.removedirs(dir_paths)        # 递归删除指定的目录，无返回值，路径为文件、非空目录、路径不存在时均报异常错误
#
# os.remove(file_path)        # 删除指定文件，无返回值，路径为目录时报异常错误

cmd = 'ping 127.0.0.1'
# os.system(cmd)

# https://blog.csdn.net/chengxuyuanyonghu/article/details/79317772
import subprocess
subprocess.run(cmd, shell=True)