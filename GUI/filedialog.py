# --coding:utf-8--
# File: filedialog.py
# Author: dxj728
# Time: 2021年05月13日22时
# 说明：文件对话框

from tkinter import *
from tkinter import ttk
# 导入文件对话框
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        ttk.Button(self.master, text='获取多个打开文件的文件名', command=self.open_filenames).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='打开目录', command=self.open_dir).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def open_filenames(self):
        # 调用askopenfilenames()方法获取多个文件的文件名
        filenames_tuple = filedialog.askopenfilenames(title='获取多个文件路径', filetypes=[('所有文件', '*'), ('')], initialdir='d:/')
        print(filenames_tuple)

    def open_dir(self):
        # 调用askdirectory()方法打开目录
        dirs = filedialog.askdirectory(title='打开目录', initialdir='d:/')
        print(dirs)


root = Tk()
root.title("文件对话框test")
App(root)
root.mainloop()

