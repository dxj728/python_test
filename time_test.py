# --coding:utf-8--
# File: time_test.py
# Author: dxj728
# Time: 2019年03月31日16时
# 说明：time模块及时间类的学习

import datetime
import time

## **********************************datetime类学习**************************************************

#
# # 返回世界标准时间（格林尼治时间），返回值类型：datetime类型，精确至微秒
# utc_now = datetime.datetime.utcnow()
#
# # 返回当前的时间，返回值类型：datetime类型，精确至微秒 例：2019-03-31 16:56:02.049465
# dt_today = datetime.datetime.now()
# # 将当前的datetime类型时间转换为可读字符串，返回值类型：string字符串
# str_now1 = dt_today.strftime('%Y/%m/%d %H:%M:%S %p')		# 例：2019/03/31 17:49:00 PM
# str_now2 = dt_today.strftime('%y/%m/%d %b %a')		# 例：19/03/31 Mar Sun
# str_now3 = dt_today.strftime('%B %A %Z')		# 例：19/03/31 Mar Sun
# '''strftime其他参数
# 	%I：12小时制小时数（01-12）
# 	%w: 今天是本周的第（0-6）天(周日为星期开始)
# 	%j：今天是本年的第（001-366）天
# 	%W：这周是本年的第（00-53）周（周一为星期的开始）
# 	%U：这周是本年的第（00-53）周（周日为星期的开始）
# 	%%：%号本身
# '''
# days = dt_today.day		# 返回这个月当天的天数，int类型，例如：31
# day = dt_today.isoweekday()		# 返回int类型1~7 代表周一~周日
#
# # 将指定日期时间转换为datetime类型，返回值类型：datetime类型，例：1995-01-29 06:06:06
# dt1 = datetime.datetime(year=1994, month=7, day=28, hour=12, minute=12, second=12, microsecond=0)
# dt2 = datetime.datetime(1995, 1, 29, 6, 6, 6)
#
# # 将一个时间区间转换为特定的时间格式，返回值类型：timedelta类型，例：1 day, 0:00:00
# delta = datetime.timedelta(days=1)
#
#
# class OldDay(object):
# 	# 初始化方法：确定当前时刻
# 	def __init__(self):
# 		self.today = datetime.datetime.now()
#
# 	# 返回前一天的时刻，返回值类型：datetime（默认为00时刻）
# 	def get_one_day_ago(self):
# 		oneday = datetime.timedelta(days=1)
# 		day = self.today - oneday
# 		date_one_day_ago = datetime.datetime(day.year, day.month, day.day)
# 		print(date_one_day_ago.strftime('%Y/%m/%d'))
# 		return date_one_day_ago
#
# 	# 返回前一周的时刻,返回值类型：datetime（默认为00时刻）
# 	def get_one_week_ago(self):
# 		one_week = datetime.timedelta(days=7)
# 		day = self.today - one_week
# 		date_one_week_ago = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
# 		print(date_one_week_ago.strftime('%Y/%m/%d'))
# 		return date_one_week_ago
#
# 	# 返回前一月（30天）的时刻,返回值类型：datetime（默认为00时刻）
# 	def get_one_month_ago(self):
# 		one_month = datetime.timedelta(days=30)
# 		day = self.today - one_month
# 		date_one_month_ago = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
# 		print(date_one_month_ago.strftime('%Y/%m/%d'))
# 		return date_one_month_ago
#
# 	# 返回前一天的开始时刻（datetime类型）、结束时刻（datetime类型）
# 	def get_last_day(self):
# 		oneday = datetime.timedelta(days=1)
# 		day = self.today - oneday
# 		last_day_start = datetime.datetime(day.year, day.month, day.day)
# 		last_day_end = datetime.datetime(day.year, day.month, day.day)
# 		str_last_day_start = str(last_day_start)
# 		str_last_day_end = str(last_day_end)
# 		print('--'.join([str_last_day_start, str_last_day_end]))
# 		return last_day_start, last_day_end
#
# 	# 返回前一周的开始时刻（datetime类型）、结束时刻（datetime类型）
# 	def get_last_week(self):
# 		dayscount = datetime.timedelta(days=self.today.isoweekday())
# 		last_week_end = self.today - dayscount		# 计算出上周的截止时间
# 		sixdays = datetime.timedelta(days=6)
# 		last_week_start = last_week_end - sixdays		# 计算出上周的开始时间
# 		date_from = datetime.datetime(last_week_start.year, last_week_start.month, last_week_start.day, 0, 0, 0)
# 		date_to = datetime.datetime(last_week_end.year, last_week_end.month, last_week_end.day, 23, 59, 59)
# 		print('---'.join([str(date_from), str(date_to)]))
# 		return last_week_start, last_week_end
#
# 	# 返回前一个月第一天和最后一天的日期时间（均为datetime类型）
# 	def get_last_month(self):
# 		dayscount = datetime.timedelta(days=self.today.day)		# 获取今天在本月的天数
# 		last_month_end = self.today - dayscount		# 获取上个月的截止时间
# 		last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1, 0, 0, 0)
# 		last_month_end = datetime.datetime(last_month_end.year, last_month_end.month, last_month_end.day, 23, 59, 59)
# 		print('---'.join([str(last_month_start), str(last_month_end)]))
# 		return last_month_start, last_month_end
#
#
# old_day = OldDay()
# old_day.get_one_day_ago()
# old_day.get_one_week_ago()
# old_day.get_one_month_ago()
# old_day.get_last_day()
# old_day.get_last_week()
# old_day.get_last_month()

## **********************************time类学习**************************************************

# 获取当前的时间戳，返回值类型：float 单位：秒 表示范围：1970年至2038年
# ticks = time.time()
#
# # 将时间戳转换为时间元祖类型，返回值类型：struct_time
# float_time = 1567702282000
# local_time = time.localtime(float_time/1000)
# str_time = time.strftime('%Y%m%d %H%M%S', local_time)
# print(str_time)
#
# float_time = 1567698380000
# local_time = time.localtime(float_time/1000)
# str_time = time.strftime('%Y%m%d %H%M%S', local_time)
# print(str_time)
# hour = local_time.tm_hour		# 获取当前的小时时刻,返回值类型：int
# print(local_time)



## **********************************calendar类学习**************************************************

# class dingshi():
# 	def __init__(self):
# 		pass
#
# 	def start(self, end_time):
# 		while True:
# 			str_now = datetime.datetime.now().strftime('%H:%M:%S')
# 			if str_now == end_time:
# 				print('time:{}'.format(str_now))
# 				exit(-1)
# 				break
# 		return

## ********************************判定时间区间*************************************

now = datetime.datetime.now()
b = datetime.datetime(2019,12,26,23,10)
print(now < b)
