# --coding:utf-8--
# File: spider_nextcloud_test.py
# Author: dxj728
# Time: 2019年03月25日22时
# 说明：爬虫模拟nextcloud网站登录(www.dxj728.com)


import urllib,os
import requests
from lxml import etree

# 模拟实现的爬虫类
class Spider(object):
	# 初始化request请求，及请求头内容、登录界面url等
	def __init__(self):
		self.__headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
			'Host': 'www.dxj728.com'
		}
		self.__login_url = 'https://www.dxj728.com/index.php/login'
		self.session = requests.session()

	# 获取登录界面上的authenticity_token数据信息
	# 返回值：authenticity_token值（字符串）
	def __get_token(self):
		respond = self.session.get(self.__login_url, headers=self.__headers)
		if respond.status_code != 200:
			print('首次get请求失败(获取token)：' + str(respond.status_code))
			exit(-1)
		selector = etree.HTML(respond.text)
		token = selector.xpath('//head/@data-requesttoken')		# 获取页面上的该属性值，用于登录使用，居然是个列表list
		print(token)
		return token[0]

	# 实现模拟登录，并打印获取到的数据
	def login(self, name, password):
		token = self.__get_token()
		post_data = {
			'user': name,
			'password': password,
			'timezone_offset': '8',
			'timezone': 'Asia/Shanghai',
			'requesttoken': token,
		}
		self.__login_url = 'https://www.dxj728.com/index.php/login'
		respond = self.session.post(self.__login_url, data=post_data, headers=self.__headers)
		if respond.status_code != 303:
			print('首次get请求失败(获取token)' + str(respond.status_code))
			exit(-1)
		print(respond.text)
		print(respond.status_code)

	# 实现模拟文件下载
	def download(self, file_url):
		token = self.__get_token()
		post_data = {
			'user': name,
			'password': password,
			'timezone_offset': '8',
			'timezone': 'Asia/Shanghai',
			'requesttoken': token,
		}
		self.__login_url = 'https://www.dxj728.com/index.php/login'
		respond = self.session.post(self.__login_url, data=post_data, headers=self.__headers)
		if respond.status_code != 303:
			print('首次get请求失败(获取token)' + str(respond.status_code))
			exit(-1)
		print(respond.text)
		print(respond.status_code)


# 主函数，配置相应信息后启动运行
if __name__ == '__main__':

	name = 'admin'
	password = '123456'
	nextcloud_spider = Spider()
	nextcloud_spider.login(name, password)

