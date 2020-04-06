# --coding:utf-8--
# File: test.py
# Author: dxj728
# Time: 2019年06月03日06时
# 说明：	命令行执行python -m pydoc -p 端口号 ，可以直接查询官方模块文档。

import  sys
import datetime, time
# reload(sys)
# sys.setdefaultencoding('utf-8')


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

# from time_test import dingshi
# if __name__ == '__main__':
# 	end_time = '23:09:10'
# 	ds = dingshi()
# 	ds.start(end_time)
# 	print('ok')

# import os
# from scapy.all import *
#
# time_list = []
# packets = rdpcap(r"D:\desktop\p1.pcap")
# for data in packets:
# 	if data.haslayer("ICMP"):
# 		str_1 = repr(data)
# 		# print(str_1)
# 		# print(ls(data))
# 		time_list.append(data.time)
# 		# print(data['IP'].payload.original)  # 打印出'IP','IPV6','ARP'或者其他
# 		# print(data.payload.name)#打印出'IP','IPV6','ARP'或者其他
#
# # with PcapReader(r"D:\desktop\p1.pcap") as packets: #Windows这样需要考虑转义字符
# # 	x = packets.read_all()
# # 	for data in packets.read_all():
# # 		str_1 = repr(data)
# # 		print(str_1)
#
# print(time_list)
# t1 = 1583844517.933096
#
# x = time_list[1] - time_list[0]
# print(str(x*1000) + 'ms')


def adder(x):
	def wrapper(y):
		return x + y
	return wrapper
adder5 = adder(5)
print(adder5(adder5(6)))

def func(s, i, j):
	if i < j:
		func(s, i + 1, j - 1)
	s[i],s[j] = s[j], s[i]

def main():
	a = [10, 6, 23, -90, 0, 3]
	func(a, 0, len(a)-1)
	for i in range(6):
		print a[i]
		print "\n"
main()










