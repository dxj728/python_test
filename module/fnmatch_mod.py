# --coding:utf-8--
# File: fnmatch_mod.py
# Author: dxj728
# Time: 2021年01月14日23时
# 说明：fnmatch模块学习&文件名匹配


"""
	fnmatch匹配支持如下通配符：
		* : 匹配 任意个 任意字符
		？ : 匹配 一个 任意字符
		[] : 匹配 括号内字符序列 之中 的任意字符，支持[a-z]写法
		[!] : 匹配 括号内字符序列 除外 的任意字符，支持[a-z]写法
"""

import fnmatch

file_list = ['os_test.py', 're_mod.py', 'error.log', 'new1.txt']

for file in file_list:
	ret1 = fnmatch.fnmatch(file, '*_test.py')    # 匹配文件名是否是指定的模式(当前判断文件是否以_test.py结尾)，返回True/False
	ret2 = fnmatch.fnmatchcase(file, "_mod.py")  # 匹配文件名，与上相同，只是该方法区分大小写, 返回True/False
	
ret3 = fnmatch.filter(file_list, '[oe]*')       # 对文件名列表进行过滤，匹配指定模式，返回列表
print(ret3)     # ['os_test.py', 'error.log']

ret4 = fnmatch.translate('?.py')    # 将当前模式表达式转为正则表达式
print(ret4)     # (?s:.\.py)\Z
