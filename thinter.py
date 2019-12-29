# --coding=utf-8--
# File: thinter.py
# Author: dxj728
# Time: 2019年07月04日23时
# 说明：python图形化编程库thinter的使用

# python2 导入 from Tkinter import *

# python3 导入
from tkinter import *
# 创建TK对象，TK代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
# 创建lable对象，第一个参数指定将该Lable放入root内
w = Label(root, text='hello, world!')
# 调用pack进行布局
# 启动主窗口
root.mainloop()



