# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       :  pyautogui_test.py
# Time       ： 2023/9/7 21:37
# Author     ： dxj728
# version    ： python 3.7
# Description： 
"""
import time
import pyautogui

# """获取屏幕尺寸"""
# size = pyautogui.size()
# print(type(size))   # <class 'pyautogui.Size'>
# print(size)         # Size(width=2880, height=1800)
# print(size.width)   # 2880  int类型
# print(size.height)  # 1800  int类型
#
# """获取鼠标当前位置"""
# pos = pyautogui.position()
# print(type(pos))    # <class 'pyautogui.Point'>
# print(pos)          # Point(x=1397, y=1271)
# print(pos.x)        # 1537 int类型
#
# x, y = pyautogui.size()
# """判断鼠标坐标是否在屏幕范围内"""
# is_onScreen = pyautogui.onScreen(x, y)
# print(is_onScreen)  # False 布尔类型
#
# """鼠标绝对位置移动，移动至当前屏幕正中心，移动时长10s"""
# pyautogui.moveTo(x/2, y/2, duration=10)     # 无返回值
# """鼠标相对位置移动，相对当前位置横坐标+100（向右100），纵坐标-200（向上100），移动时长10s"""
# pyautogui.moveRel(100, -200, duration=1)     # 无返回值
#
# """鼠标点击事件"""
# pyautogui.click(x/2, y/2)   # 无返回值，在屏幕右下角单击，默认左键
# time.sleep(2)
# pyautogui.click(100, 100, clicks=2, interval=0.5, button='right', duration=0.2)  # 无返回值，移动至(100,100)点击2次右键，点击间隔0.5s，移动时长0.2秒
# """鼠标滚轮事件"""
# pyautogui.scroll(500)     # 无返回值，鼠标位置不变，滚轮向上滚500个单位（预计为像素点）
#
#
# """键盘控制（不支持中文）"""
# pyautogui.press('a')    # 无返回值，键名用字符串表示，支持的所有键名，存在pyautogui.KEYBOARD_KEYS变量中，包括26个字母、数字、符号、F1~F20、方向等等所有按键
# pyautogui.press(['p', 'y', 'space'], interval=0.1)
#
# pyautogui.typewrite('hello, PyAutoGUI!\n')  # 无返回值，传入字符串
# pyautogui.typewrite(['s', 'r', 'f', 'space'], interval=0.1)    # 传入键名列表，按键之间间隔0.1s（默认0）
#
# pyautogui.hotkey('ctrl', 'shift', 'esc')     # 无返回值，调出任务管理器
#
# """消息窗口"""
# ale = pyautogui.alert(text='warning!!!', title='alert消息框', button='OK')   # 提示对话框，点击的按键被返回
# print(type(ale))    # <class 'str'>
# print(ale)          # OK
#
# con = pyautogui.confirm(text='请选择', title='PyAutoGUI消息框', buttons=['1', '2...', '3'])     # 选择对话框，点击的按键被返回
# print(type(con))        # <class 'str'>
# print(con)              # 2...
#
# pro = pyautogui.prompt(text='请输入', title='PyAutoGUI消息框', default='请输入')       # 输入对话框，点击ok按钮后返回输入内容
# print(type(pro))        # <class 'str'>
# print(pro)              # exp: 123456
#
# pas = pyautogui.password(text='输入密码', title='PyAutoGUI消息框', default='',mask='*')        # 密码输入框，点击ok按钮后返回输入内容
# print(type(pas))        # <class 'str'>
# print(pas)              # exp: 123456

"""截图相关"""
# 屏幕截图方法；传入文件保存路径及名称；region参数，截图区域，由左上角坐标、宽度、高度4个值确定，如果指定区域超出了屏幕范围，超出部分会被黑色填充，默认`None`,截全屏
scr = pyautogui.screenshot('D:\shot_test.png', region=(630, 212, 600, 400))
print(type(scr))        # <class 'PIL.Image.Image'>, image对象，需要pillow库定义支持
print(scr)              # <PIL.Image.Image image mode=RGB size=600x400 at 0x1E2D71BF8C8>

# 图片匹配功能，是在屏幕按像素匹配，定位图片在屏幕上的坐标位置，locateOnScreen()函数返回region对象,即左上角坐标、宽度、高度4个值组成的元组，可用center()函数计算出中心坐标，
loc = pyautogui.locateOnScreen('D:\shot_test.png', region=(0, 0, 1920, 1080))
print(type(loc))        # <class 'pyscreeze.Box'>
print(loc)              # Box(left=630, top=212, width=600, height=400)
print(loc.left)         # 630,int类型

# 图片匹配功能，直接返回匹配中心坐标。
loc2 = pyautogui.locateCenterOnScreen('D:\shot_test.png', region=(0, 0, 1920, 1080))
print(type(loc2))       # <class 'pyscreeze.Point'>
print(loc2)             # Point(x=930, y=412)
print(loc2.x)           # 930,int类型
pyautogui.moveTo(*loc2, duration=0.5)    # 移动鼠标至该位置
pyautogui.rightClick(*loc2)         # 在该位置点击





