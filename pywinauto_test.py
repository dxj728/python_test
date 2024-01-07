# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       :  pywinauto_test.py
# Time       ： 2023/9/10 16:17
# Author     ： dxj728
# version    ： python 3.7
# Description： pywinauto模块学习
                pip install pywinauto
                参考链接：https://blog.csdn.net/Tester_muller/article/details/131154953
                        https://blog.csdn.net/m0_37602827/article/details/108308991
                        https://blog.csdn.net/shawpan/article/details/78170117
"""
import time
import pywinauto


"""定义Application类对象"""
app = pywinauto.Application()     # Application(backend)：backend有两个取值：win32和uia，win32 为默认值，backend取值不同，接口调用差异较大。

app_path = r'D:\Program Files\Notepad++\notepad++.exe'
"""打开应用"""
app.start(app_path)
"""连接应用: 待连接的应用必须是已经打开的应用，连接应用是为了将 app 对象与目标应用绑定，以实现对目标应用的控制。"""
app.connect(path=app_path)
"""关闭应用"""
# time.sleep(5)
# app.kill()

"""定位窗口"""
# dlg = app.window()

app.
