# --coding:utf-8--
# File: pyinstaller_test.py
# Author: dxj728
# Time: 2020年01月05日11时
# 说明：打包exe文件练习
# 库安装： pip install pyinstaller
'''pyinstaller -F -w game.py  （-F表示打包单个文件，-w是为了打开exe时候不弹出黑框）'''
'''pyinstaller -F -w -i bitbug_favicon.ico game.py  （-i用来设置编译成exe文件的图标，后面跟.ico格式的图片文件）'''

import os

cur_path = os.path.abspath(__file__)
print(cur_path)
cur_dir = os.path.dirname(cur_path)
print(cur_dir)
new_dir = os.path.join(cur_dir, 'test')
if not os.path.exists(new_dir):
	os.mkdir(new_dir)
## todo:上述未完成独立打包



