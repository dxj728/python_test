# --coding:utf-8--
# File: excel_xlrd$elwt_test.py
# Author: dxj728
# Time: 2019年04月16日23时
# 说明：
# xlrd 与 xlwt支持excel2007及之前版本(.xls)，效率更高
# xlrd 与 xlwt 模块安装：pip install xlrd ; pip install xlwt

import os, time
import xlrd, xlwt
import sys
import chardet
import mysql.connector

reload(sys)
sys.setdefaultencoding('utf-8')

excel_path = r'D:\desktop\test.xlsx'

wb = xlrd.open_workbook(excel_path)
ws = wb.sheet_by_name('Sheet1')

rows = ws.nrows
cols = ws.ncols
print(rows, cols)
first_row = ws.row_values(0)
all_datas = []
for i in range(1, rows):
	row_value = ws.row_values(i)
	data = {}
	for j in range(0, cols):
		data[first_row[j]] = row_value[j]
	all_datas.append(data)

# print(first_row)

list_rows = []

for i in first_row:
	print(i)
	# print(chardet.detect(i))
	j = i.encode('utf-8')
	print(j)
	list_rows.append(j)
print(list_rows)
print(all_datas)
conn = mysql.connector.connect(host='120.78.218.216', port=3306, user='root', password='123456', database='coralcloud')
for i in range(len(all_datas)):
	print('******************************')
	num = str(int(all_datas[i][u'年龄']))
	print(num)
	print(all_datas[i][u'工号'])
	print(all_datas[i][u'姓名'])
	cur = conn.cursor()
	cur.execute("insert into oc_users (uid,displayname,password) values (%s, %s, %s)",[all_datas[i][u'工号'], all_datas[i][u'姓名'], num])
	conn.commit()
	cur.close()
conn.close()
