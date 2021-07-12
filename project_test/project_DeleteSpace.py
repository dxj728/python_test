# --coding:utf-8--
# File: project_DeleteSpace.py
# Author: dxj728
# Time: 2021年07月11日22时
# 说明：利用GUI文件对话框实现的一个删除代码文件行尾空格的小工具

import os, time
import logging
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
# 导入文件对话框
from tkinter import filedialog


current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
log_path = os.path.join(current_work_dir, 'DeleteSpaceToolsV1_0.log')
logging.basicConfig(level=logging.DEBUG,
                    filename=log_path,
                    format="%(asctime)s%(name)s %(levelname)s %(pathname)s %(lineno)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S %a')


class App:
    def __init__(self, master):
        self.master = master
        self.file_list = []
        self.max = 100
        self.cur = 0
        self.progressbar = None
        self.init_widgets()

    def init_widgets(self):
        fm1 = LabelFrame(self.master, text='文件选取')  # 创建第一个容器
        fm1.pack(side=TOP, fill=X, pady=5, expand=True)
        fm1_1 = Frame(fm1)  # 嵌套容器1
        fm1_1.pack(side=TOP)
        ttk.Button(fm1_1, text='文件', command=self.open_filename).pack(side=LEFT, fill=X, ipadx=10, padx=30, expand=True)
        ttk.Button(fm1_1, text='文件夹', command=self.open_dir).pack(side=LEFT, fill=X, ipadx=10, padx=30, expand=True)
        fm1_2 = Frame(fm1)  # 嵌套容器2
        fm1_2.pack(side=TOP)
        Label(fm1_2, text='当前状态: ').pack(side=LEFT, padx=10)
        Label(fm1_2, textvariable=str_select_status).pack(side=LEFT, padx=10)

        self.fm2 = LabelFrame(self.master, text='执行进度')  # 创建第二个容器
        self.fm2.pack(side=TOP, fill=X, expand=True)
        Label(self.fm2, textvariable=str_progress_statue).pack(side=LEFT, padx=5, pady=5, anchor=W)
        self.progressbar = ttk.Progressbar(self.fm2, maximum=100, value=0)
        self.progressbar.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        ttk.Button(self.fm2, text='开始执行', command=self.start).pack(side=RIGHT, expand=True)

        fm3 = LabelFrame(self.master, text='Notes by dxj')  # 创建第三个容器
        fm3.pack(side=TOP, fill=X, expand=True)
        Label(fm3, text='    1.仅对.py和.txt文件生效(utf-8编码)').pack(side=TOP, ipady=0, pady=0, expand=True, anchor=W)
        Label(fm3, text='    2.会在原文件路径下产生新文件目录(new_file)，需手动替换原文件').pack(side=TOP, ipady=0, pady=1, expand=True, anchor=W)

    def open_filename(self):
        # 调用askopenfilenames()方法获取多个文件的文件名
        self.file_list = []
        filenames_tuple = filedialog.askopenfilenames(title='选取一个或多个文件', filetypes=[('所有文件', '*')], initialdir='d:/')
        logging.info(filenames_tuple)
        for filename in filenames_tuple:
            file_type = os.path.splitext(filename)[1]
            if file_type in ('.py', '.txt'):
                self.file_list.append(filename)
        self.max = len(self.file_list)

        str_select_status.set('已选取相关文件 {}个'.format(self.max))
        self.progressbar['maximum'] = self.max
        self.progressbar['value'] = 0
        str_progress_statue.set('0/{}'.format(self.max))

    def open_dir(self):
        # 调用askdirectory()方法打开目录
        self.file_list = []
        dirs = filedialog.askdirectory(title='选取一个文件夹', initialdir='d:/')
        logging.info(dirs)
        self.listdir(dirs)
        self.max = len(self.file_list)

        str_select_status.set('文件夹中相关文件 {}个'.format(self.max))
        self.progressbar['maximum'] = self.max
        self.progressbar['value'] = 0
        str_progress_statue.set('0/{}'.format(self.max))

    def listdir(self, path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                self.listdir(file_path)
            else:
                file_type = os.path.splitext(file)[1]
                if file_type in ('.py', '.txt'):
                    self.file_list.append(file_path)

    def start(self):
        str_select_status.set('进行中...'.format(self.max))
        logging.info('***start************')
        for i in range(self.max):
            cur_file_path = self.file_list[i]
            logging.info(cur_file_path)
            cur_file_dir = os.path.dirname(cur_file_path)
            new_file_dir = os.path.join(cur_file_dir, 'new_file')
            if not os.path.exists(new_file_dir):
                os.makedirs(new_file_dir)
            file_name = os.path.basename(cur_file_path)
            new_file_path = os.path.join(new_file_dir, file_name)
            if os.path.exists(new_file_path):
                os.remove(new_file_path)
                logging.info('delete exists file!')
            logging.info(new_file_path)
            with open(cur_file_path, 'r', encoding='utf-8') as file_line:
                with open(new_file_path, 'a', encoding='utf-8') as new_line:
                    content = file_line.readlines()
                    for j in range(len(content)):
                        new_line.write(content[j].rstrip())
                        new_line.write('\n')
            self.progressbar['value'] = i+1
            str_progress_statue.set('{}/{}'.format(i+1, self.max))
            self.fm2.update()
            time.sleep(1)
        str_select_status.set('已完成'.format(self.max))


try:
    root = Tk()
    
    str_select_status = StringVar()
    str_select_status.set('无')

    str_progress_statue = StringVar()
    str_progress_statue.set('0/0')

    root.title("代码空格删除工具V1.0")
    root.geometry('400x200')  # 设置主窗口大小
    root.resizable(0, 0)    # 固定窗口，防止用户调整尺寸
    App(root)

    root.mainloop()
except Exception as e:
    logging.error(e)
