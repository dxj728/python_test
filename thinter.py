# --coding=utf-8--
# File: thinter.py
# Author: dxj728
# Time: 2019年07月04日23时
# 说明：python图形化编程库thinter的使用

## *************第一种创建窗口的方式********************
# python2 导入 from Tkinter import *

# # python3 导入
# from tkinter import *
# # 创建TK对象，TK代表窗口
# root = Tk()
# # 设置窗口标题
# root.title('窗口标题')
# # 创建lable对象，第一个参数指定将该Lable放入root内
# w = Label(root, text='hello, world!')
# # 调用pack进行布局
# # 启动主窗口
# root.mainloop()

## ************第二种创建创建窗口的方式*********************

# python2导入 from Tkinter import *
# python3导入
from tkinter import *

# 定义继承Frame的Application类
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		# 调用initWidgets()方法初始化界面
		self.initWidgets()

	def initWidgets(self):
		# 创Labled对象， 第一个参数指定将该LABLE放入root内
		w = Label(self)
		# 创建一个位图
		bm = PhotoImage(file="image.png")
		# 使用一个不会被释放的变量引用该图片，否则该图片会被回收
		w.x = bm
		# 设置显示的图片是bm
		w['image'] = bm
		w.pack()
		# 创建button对象，第一个参数指定将该button放入root内
		okButton = Button(self, text="确定")
		okButton['background'] = 'yellow'		# or: okButton.configure(background='yellow')
		okButton.pack()

# 创建Application对象
app = Application()
# Frame有一个默认的mater属性，该属性为TK对象（窗口）
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('你猜猜看')
# 启动
app.mainloop()

