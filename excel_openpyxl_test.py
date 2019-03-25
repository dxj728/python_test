# coding=utf-8
# File: excel_openpyxl_test.py
# Author: dxj728
# Time: 2019年03月21日23时
# 说明：openpyxl操作excel的练习
# 参考来源：https://www.cnblogs.com/zeke-python-road/p/8986318.html
# openpyxl模块安装：pip install openpyxl

import openpyxl
import datetime, time


# 创建excel操作类
class Excel(object):
	# 初始化表格路径
	def __init__(self, excel_path=None):
		if excel_path:
			self.excel_path = excel_path
		else:
			print('未提供表格路径，可能会出现错误')
			exit(-1)

	# 新创建一个excel工作簿并写入表格
	def create_write(self, sheet=None, data=None):
		wb = openpyxl.Workbook()  # 创建文件对象
		if sheet is None:		# 判断是否提供新建表格名
			ws = wb.active		# 创建默认表格（Sheet）
		else:
			ws = wb.create_sheet(sheet)
		# TODO:根据数据类型写入数据（string,list(dict)）

		wb.save(self.excel_path)  # 存储内容至excel工作簿
		return

	# 新创建一个excel工作簿并写入表格
	# 输入：sheet(字符串，表格名)
	def load_write(self, sheet=None, data=None):
		wb = openpyxl.load_workbook(self.excel_path)  # 创建文件对象
		if sheet is None:		# 判断是否提供新建表格名
			ws = wb.active		# 获取默认的已存在活动表格
		else:
			ws = wb[sheet]
		# TODO:根据数据类型写入数据（string,list(dict)）

		wb.save(self.excel_path)  # 存储内容至excel工作簿
		return
		pass

	# 表格的各种奇怪方法尝试练习
	def test(self, data = None):
		wb = openpyxl.Workbook()	# 创建文件对象
		ws = wb.active		# 获取默认的第一个sheet

		ws['A1'] = 42		# 写入数字
		ws['B1'] = "你好" + "dxj728"		#写入文字（UTF-8格式）
		ws['A2'] = datetime.datetime.now()		# 写入当前时间
		ws['A3'] = time.strftime("%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}").format(y='年', m='月', d='日', h='时', f='分', s='秒')		# 写入当前可读时间（字符串）
		ws.cell(3, 3).hyperlink = 'https://www.dxj728.com'		# 插入超链接（明文）
		ws.cell(4, 4, value=('=HYPERLINK("%s"，"%s")' % ('https://www.dxj728.com', 'dxj728')))		# 插入超链接字符

		wb.save(self.excel_path)		# 存储内容至excel工作簿


if __name__ == '__main__':

	excel_path = r'D:\desktop\test.xlsx'

	excel_test = Excel(excel_path)
	excel_test.test()
