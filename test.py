# --coding:utf-8--
# File: test.py
# Author: dxj728
# Time: 2019年06月03日06时
# 说明：	命令行执行python -m pydoc -p 端口号 ，可以直接查询官方模块文档。

import openpyxl, sys
import datetime, time
reload(sys)
sys.setdefaultencoding('utf-8')


# excel_path = r'D:\desktop\test.xlsx'
#
# ##**********************************读取操作*******************************
# wb = openpyxl.load_workbook(excel_path)
# # ws00 = wb.active
# ws01 = wb['Sheet1']
#
# # 索引从0开始
# x = ws01.cell(4, 2).value
# print(x)
#
# # ********************************写入操作********************************
# ws02 = wb.create_sheet('sheet3_openpyxl')
#
# ws02['A1'] = 42  # 写入数字
# ws02['B1'] = u"你好" + "dxj728"  # 写入文字（UTF-8格式）
# ws02['A2'] = datetime.datetime.now()  # 写入当前时间
# ws02.cell(3, 3).hyperlink = 'https://www.dxj728.com'  # 插入超链接（明文）
# ws02.cell(4, 4, value=('=HYPERLINK("{}","{}")'.format('https://www.dxj728.com', 'dxj728')))  # 插入超链接字符
!

# wb.save(excel_path)
# 获取所有行
# rows = []
# row1_values = []
# print(ws[0])
# for row in ws.iter_rows():
# 	rows.append(row)
# print(len(rows[0]))
# for i in range(len(rows)):
# 	row1_values.append(rows[0][i].value.encode('utf-8'))
# print(row1_values)
# # 获取所有列
# cols = []
# for col in ws.iter_cols():
# 	cols.append(col)
# print("rows：{} cols:{}".format(rows[0],cols[0]))


# 创建5层嵌套字典dict