# --coding:utf-8--
# File: matplotlib.py
# Author: dxj728
# Time: 2020年10月14日22时
# 说明：2D数据绘图库包学习


import matplotlib.pyplot as plt
## ------简单折线图-----
# x_list = ['2010', '2012', '2013', '2014', '2015', '2016', '2017']
# y_list = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# plt.plot(x_list, y_list)
# plt.show()

## ------复式折线图------
x_list = ['2010', '2012', '2013', '2014', '2015', '2016', '2017']
y_list = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y2_list = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
plt.plot(x_list, y_list, x_list, y2_list)       # or plt.plot(x_list, y2_list)
plt.show()

