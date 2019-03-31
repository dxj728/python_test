# --coding:utf-8--
# File: time_test.py
# Author: dxj728
# Time: 2019年03月31日16时
# 说明：time模块及时间类的学习

import datetime
import sys

# 返回世界标准时间（格林尼治时间），返回值类型：datetime类型，精确至微秒
utc_now = datetime.datetime.utcnow()

# 返回当前的时间，返回值类型：datetime类型，精确至微秒 例：2019-03-31 16:56:02.049465
dt_today = datetime.datetime.now()
days = dt_today.day		# 返回这个月当天的天数，int类型，例如：31
day = dt_today.isoweekday()		# 返回现在的月份，int类型，例：3

# 将当前的datetime类型时间转换为可读字符串，返回值类型：string字符串
str_now1 = dt_today.strftime('%Y/%m/%d %H:%M:%S %p')		# 例：2019/03/31 17:49:00 PM
str_now2 = dt_today.strftime('%y/%m/%d %b %a')		# 例：19/03/31 Mar Sun
str_now3 = dt_today.strftime('%B %A %Z')		# 例：19/03/31 Mar Sun
'''strftime其他参数
	%I：12小时制小时数（01-12）
	%w: 今天是本周的第（0-6）天(周日为星期开始)
	%j：今天是本年的第（001-366）天
	%W：这周是本年的第（00-53）周（周一为星期的开始）
	%U：这周是本年的第（00-53）周（周日为星期的开始）
	%%：%号本身
'''

# 将指定日期时间转换为datetime类型，返回值类型：datetime类型，例：1995-01-29 06:06:06
dt1 = datetime.datetime(year=1994, month=7, day=28, hour=12, minute=12, second=12, microsecond=0)
dt2 = datetime.datetime(1995, 1, 29, 6, 6, 6)

# 将一个时间区间转换为特定的时间格式，返回值类型：timedelta类型，例：1 day, 0:00:00
# time或datetime相减后值均为timedelta类型
delta = datetime.timedelta(days=1)


class old_day(object):
	def __init__(self):
		self.today = datetime.datetime.now()

	# 返回前一天的时刻，返回值类型：datetime（默认为00时刻）
	def get_one_day_ago(self):
		oneday = datetime.timedelta(days=1)
		day = self.today - oneday
		date_one_day_age = datetime.datetime(day.year, day.month, day.day)
		print(date_one_day_age.strftime('%Y/%m/%d'))
		return date_one_day_age

	# 返回前一天的开始时刻和结束时刻
	def get_last_day(self):
		oneday = datetime.timedelta(days=1)
		day = self.today - oneday
		last_day_start = datetime.datetime(day.year, day.month, day.day)
		last_day_end = datetime.datetime(day.year, day.month, day.day)
		str_last_day_start = str(last_day_start)
		str_last_day_end = str(last_day_end)
		print('--'.join([str_last_day_start, str_last_day_end]))
		return last_day_start, last_day_end

	def week_get(self):
		dayscount = datetime.timedelta(days=self.today.isoweekday())
		dayto = self.today - dayscount
		sixdays = datetime.timedelta(days=6)
		dayfrom = dayto - sixdays
		date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
		date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
		print('---'.join([str(date_from), str(date_to)]))

	def month_get(self):
		"""
		返回上个月第一个天和最后一天的日期时间
		:return
		date_from: 2016-01-01 00:00:00
		date_to: 2016-01-31 23:59:59
		"""
		dayscount = datetime.timedelta(days=self.today.day)
		dayto = self.today - dayscount
		date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
		date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
		print('---'.join([str(date_from), str(date_to)]))
		return date_from, date_to


if __name__ == '__main__':
	old_day = old_day()
	old_day.get_one_day_ago()
	old_day.week_get()
	old_day.month_get()
