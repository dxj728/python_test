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

# # python2导入 from Tkinter import *
# # python3导入
# from tkinter import *
#
# # 定义继承Frame的Application类
# class Application(Frame):
# 	def __init__(self, master=None):
# 		Frame.__init__(self, master)
# 		self.pack()
# 		# 调用initWidgets()方法初始化界面
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		# 创Labled对象， 第一个参数指定将该LABLE放入root内
# 		w = Label(self)
# 		# 创建一个位图
# 		bm = PhotoImage(file="image.png")
# 		# 使用一个不会被释放的变量引用该图片，否则该图片会被回收
# 		w.x = bm
# 		# 设置显示的图片是bm
# 		w['image'] = bm
# 		w.pack()
# 		# 创建button对象，第一个参数指定将该button放入root内
# 		okButton = Button(self, text="确定")
# 		okButton['background'] = 'yellow'		# or: okButton.configure(background='yellow')
# 		okButton.pack()
#
# # 创建Application对象
# app = Application()
# # Frame有一个默认的mater属性，该属性为TK对象（窗口）
# print(type(app.master))
# # 通过master属性来设置窗口标题
# app.master.title('你猜猜看')
# # 启动
# app.mainloop()

# ## ************************布局管理1.pack布局管理器（相对布局）**********************
#
# # python2导入 from Tkinter import *
# # python3导入
# from tkinter import *
#
# class APP:
# 	def __init__(self, master):
# 		self.master = master
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		# 创建的第一个容器, 容器是看不到的
# 		fm1 = Frame(self.master)
# 		# 该容器放在左边排列
# 		fm1.pack(side=LEFT, fill=BOTH, expand=YES)
# 		# 像容器1中添加三个按钮
# 		Button(fm1, text='1.first').pack(side=TOP, fill=X, expand=YES)
# 		Button(fm1, text='1.second').pack(side=TOP, fill=X, expand=YES)
# 		Button(fm1, text='1.third').pack(side=TOP, fill=X, expand=YES)
# 		# 创建的第二个容器
# 		fm2 = Frame(self.master)
# 		# 该容器放在左边排列，紧挨着容器1
# 		fm2.pack(side=LEFT, padx=20, expand=YES)
# 		# 像容器2中添加三个按钮
# 		Button(fm2, text='2.first').pack(side=RIGHT, fill=Y, expand=YES)
# 		Button(fm2, text='2.second').pack(side=RIGHT, fill=Y, expand=YES)
# 		Button(fm2, text='2.third').pack(side=RIGHT, fill=Y, expand=YES)
# 		# 创建的第三个容器
# 		fm3 = Frame(self.master)
# 		# 该容器放在右边排列
# 		fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
# 		# 像容器2中添加三个按钮
# 		Button(fm3, text='3.first').pack(side=BOTTOM, fill=Y, expand=YES)
# 		Button(fm3, text='3.second').pack(side=BOTTOM, fill=Y, expand=YES)
# 		Button(fm3, text='3.third').pack(side=BOTTOM, fill=Y, expand=YES)
#
# root = Tk()
# root.title("pack布局")
# display = APP(root)
# root.mainloop()


## ************************布局管理2.Grid布局管理器（表格布局）**********************

# python 2.x 使用： from Tkinter import *
# python 3.x 使用
from tkinter import *

class APP:
	def __init__(self, master):
		self.master = master
		self.initWidgets()
		self.expr=None

	def initWidgets(self):
		# 创建一个输入组件
		self.e = Label(relief=SUNKEN, font=('Courier New', 24),\
				  	width=25, bg='white', anchor=E)
		# 对该输入组件使用pack布局， 放在容器顶部
		self.e.pack(side=TOP, pady=10)
		p = Frame(self.master)
		p.pack(side=TOP)
		# 定义字符串元组
		names = ('0', '1', '2', '3', '4', '5', '6',
				 '7', '8', '9', '+', '-', '*', '/',
				 '.', '=')
		# 遍历字符串元组
		for i in range(len(names)):
			# 创建Button, 将Button放入P组件中
			b = Button(p, text=names[i], font=('Verdana', 20), width=6)
			b.grid(row = i // 4, column=i % 4)
			# 为鼠标左键的单击事件绑定事件处理办法
			b.bind('<Button-1>', self.click)
			# 为鼠标左键的双击事件绑定事件处理方法
			if b['text'] == '=':
				b.bind('<Double-1>', self.clean)

	def click(self, event):
		# 如果用户单击的是数字键或者点号
		if (event.widget['text'] in ('0', '1', '2', '3',
									 '4', '5', '6',
									 '7', '8', '9', '.')):
			self.e['text'] = self.e['text'] + event.widget['text']
		# 如果用户单击了运算符
		elif(event.widget['text'] in ('+', '-', '*', '/')):
			# 如果当前表达式为NONE，则直接用show组件的内容和运算符进行连接
			if self.expr is None:
				self.expr = self.e['text'] + event.widget['text']
			# 如果当前表达式不为None，则用表达式、show组件的内容和运算符进行连接
			else:
				self.expr = self.expr + self.e['text'] + event.widget['text']
			self.e['text'] = ''
		elif(event.widget['text'] == '=' and self.expr is not None):
			self.expr = self.expr + self.e['text']
			print(self.expr)
			# 使用eval函数计算表达式的值
			self.e['text'] = str(eval(self.expr))
			self.expr = None

	# 当双击‘=’时，程序清空计算结果，将表达式设为None
	def clean(self, event):
		self.expr = None
		self.e['text'] = ''

root = Tk()
root.title('Grid布局-计算器')
APP(root)
root.mainloop()

# ## ************************布局管理3.Place布局管理器（绝对布局）**********************
#
# # python2 使用这行 from Tkinter import *
# # python3 使用这行
# from tkinter import *
# import random
#
# class App:
# 	def __init__(self, master):
# 		self.master = master
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		# 定义字符串元组
# 		books = ('蜡笔小新第一季', '蜡笔小新第二季', '蜡笔小新第三季', '蜡笔小新第四季')
# 		for i in range(len(books)):
# 			# 生成3个随机数
# 			ct = [random.randrange(256) for x in range(3)]
# 			grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
# 			# 将元组中的3个随机数格式化成十六进制数，转换成颜色格式
# 			bg_color = "#%02x%02x%02x" % tuple(ct)
# 			# 创建lable，设置背景色和前景色
# 			lb = Label(root, text=books[i], fg='white' if grayness < 125 else 'Black', bg=bg_color)
# 			# 使用place()设置该lable的大小和位置
# 			lb.place(x=20, y=30+i*36, width=180, height=30)
#
# root = Tk()
# root.title('place布局学习')
# # 设置窗口大小和位置
# root.geometry('250x250+10+300')  # 主框的初始显示大小及位置  长*高+X轴偏移+Y轴偏移
# App(root)
# root.mainloop()

# ## ************************简单事件的处理**********************
# # python2 使用这行 from Tkinter import *
# # python3 使用这行
# from tkinter import *
# import random
#
# class App:
# 	def __init__(self, master):
# 		self.master = master
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		self.label = Label(self.master, width=10)
# 		self.label['font'] = ('Courier', 20)
# 		self.label['bg'] = 'white'
# 		self.label.pack()
# 		bn = Button(self.master, text='单击我', command=self.change)		# 简单的事件处理
# 		bn.pack()
#
# 	# 定义事件处理方法
# 	def change(self):
# 		self.label['text'] = '欢迎学习python'
# 		# 生成3个随机数
# 		ct = [random.randrange(256) for x in range(3)]
# 		grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
# 		# 将元组中的三个随机数格式化成十六进制数，抓换成颜色格式
# 		bg_color = "#%02x%02x%02x" %tuple(ct)
# 		self.label['bg'] = bg_color
# 		self.label['fg'] = 'black' if grayness > 125 else 'white'
#
# root = Tk()
# root.title('简单事件处理')
# App(root)
# root.mainloop()

# ## ************************绑定简单事件**********************

# python3 使用这行
# from tkinter import *
# import random
#
# class App:
# 	def __init__(self, master):
# 		self.master = master
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		self.show = Label(self.master, width=30, bg='white', font=('times', 20))
# 		self.show.pack()
# 		bn = Button(self.master, text='单击我或双击我')
# 		bn.pack(fill=BOTH, expand=YES)
# 		# 为左键单击事件绑定处理方法
# 		bn.bind('<Button-1>', self.one)
# 		# 为左键双击事件绑定处理方法
# 		bn.bind('<Double-1>', self.double)
#
# 	def one(self, event):
# 		self.show['text'] = '左键单击：{}'.format(event.widget['text'])
#
# 	def double(self, event):
# 		self.show['text'] = "左键双击，退出程序:" + event.widget['text']
# 		print("左键双击，退出程序:" + event.widget['text'])
#
# 		import sys, time;
# 		time.sleep(3)
#
# root = Tk()
# root.title('简单绑定')
# App(root)
# root.mainloop()

# # *********************************鼠标移动事件绑定练习********************
# # python3 使用这行
# from tkinter import *
#
# class App:
# 	def __init__(self, master):
# 		self.master = master
# 		self.initWidgets()
#
# 	def initWidgets(self):
# 		lb = Label(self.master, width=40, height=3)
# 		lb.config(bg='lightgreen', font=('Times', 20))
# 		# 为鼠标移动事件绑定事件处理办法
# 		lb.bind('<Motion>', self.motion)
# 		# 为按住左键时的鼠标移动事件绑定事件处理办法
# 		lb.bind('<B1-Motion>', self.press_motion)
# 		lb.pack()
# 		self.show = Label(self.master, width=38, height=1)
# 		self.show.config(bg='white', font=('Courier New', 20))
# 		self.show.pack()
#
# 	def motion(self, event):
# 		self.show['text'] = '鼠标移动到：(%s, %s)'% (event.x, event.y)
# 		return
#
# 	def press_motion(self, event):
# 		self.show['text'] = '按住鼠标的位置为：（%s, %s）'% (event.x, event.y)
# 		return
#
# root = Tk()
# root.title('鼠标事件')
# App(root)
# root.mainloop()















