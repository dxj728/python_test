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

# ***************************************************xlrd读取操作部分************************************
# 打开excel文件
wb = xlrd.open_workbook(excel_path)

# 获取工作簿的所有sheet名
str_sheets = wb.sheet_names()
print('str_sheets值：' + str(str_sheets))

# 根据sheet索引或者名称获取sheet内容(两种方法)
ws01 = wb.sheet_by_index(0)        # sheet索引从0开始
ws02 = wb.sheet_by_name('Sheet1')

# 获取表的名称、行列值
str_sheet_name = ws02.name
rows = ws02.nrows
cols = ws02.ncols
print('sheet表名称:' + str_sheet_name + '  行数：' + str(rows) + '  列数：'+ str(cols))

# 获取表的行列的内容,索引从0开始
first_row = ws02.row_values(0)
second_col = ws02.col_values(1)
print('第一行内容：' + str(first_row) + '\n第二列内容: ' + str(second_col))

# 获取单元格内容（三种方法）
str1 = ws02.cell(3, 1).value.encode('utf-8')
str2 = ws02.cell_value(3, 1).encode('utf-8')
str3 = ws02.row(3)[1].value.encode('utf-8')
print('str1值：{} str2值：{} str3值：{}'.format(str1, str2, str3))

# ***************************************************xlwt写入操作部分************************************


# 设置单元格样式
def set_style(bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = u'黑体'
    font.bold = bold
    font.color_index = 4
    font.height = 220

    style.font = font
    return style


# 写入excel
def write_excel():
    f = xlwt.Workbook()  # 创建工作簿
    # 创建第一个sheet:
    sheet2 = f.add_sheet(u'sheet2_write', cell_overwrite_ok=True)  # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']

    # 生成第一行
    for i in range(0, len(row0)):
        sheet2.write(0, i, row0[i], set_style())

    f.save(r'd:\desktop\test1.xls')  # 保存文件

write_excel()


# all_datas = []
# for i in range(1, rows):
#     row_value = ws02.row_values(i)
#     data = {}
#     for j in range(0, cols):
#         data[first_row[j]] = row_value[j]
#     all_datas.append(data)
#
# # print(first_row)
#
# list_rows = []
#
# for i in first_row:
#     print(i)
#     # print(chardet.detect(i))
#     j = i.encode('utf-8')
#     print(j)
#     list_rows.append(j)
# print(list_rows)
# print(all_datas)
# conn = mysql.connector.connect(host='120.78.218.216', port=3306, user='root', password='123456', database='coralcloud')
# for i in range(len(all_datas)):
#     print('******************************')
#     num = str(int(all_datas[i][u'年龄']))
#     print(num)
#     print(all_datas[i][u'工号'])
#     print(all_datas[i][u'姓名'])
#     cur = conn.cursor()
#     cur.execute("insert into oc_users (uid,displayname,password) values (%s, %s, %s)",[all_datas[i][u'工号'], all_datas[i][u'姓名'], num])
#     conn.commit()
#     cur.close()
# conn.close()
