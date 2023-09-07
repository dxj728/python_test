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

# """鼠标绝对位置移动，移动至当前屏幕正中心，移动时长10s"""
# pyautogui.moveTo(x/2, y/2, duration=10)     # 无返回值
# """鼠标相对位置移动，相对当前位置横坐标+100（向右100），纵坐标-200（向上100），移动时长10s"""
# pyautogui.moveRel(100, -200, duration=1)     # 无返回值

# """鼠标点击事件"""
# pyautogui.click(x/2, y/2)   # 无返回值，在屏幕右下角单击，默认左键
# time.sleep(2)
# pyautogui.click(100, 100, clicks=2, interval=0.5, button='right', duration=0.2)  # 移动至(100,100)点击2次右键，点击间隔0.5s，移动时长0.2秒
# """鼠标滚轮事件"""
# pyautogui.scroll(500)     # 鼠标位置不变，滚轮向上滚500个单位（预计为像素点）


"""键盘控制"""
pyautogui.press('a')
pyautogui.press(['p','y','space'], interval=0.1)
pyautogui.typewrite('hello, PyAutoGUI!\n')
