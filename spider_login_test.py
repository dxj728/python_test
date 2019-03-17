# --coding:utf-8--
# File: spider_login_test.py
# Author: dxj728
# Time: 2019年03月17日22时
# 说明：爬虫模拟网站登录(www.github.com)

import urllib,os
import requests
from lxml import etree

class Spider(object):
	def __init__(self):
		self.__headers = {
			'Referer': 'https://github.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
			'Host': 'github.com'
		}
		self.__login_url = 'https://github.com/login'
		self.session = requests.session()

	def __get_token(self):
		respond = self.session.get(self.__login_url, headers=self.__headers)
		if respond.status_code != 200:
			print('首次get请求失败(获取token)：' + str(respond.status_code))
			exit(-1)
		selector = etree.HTML(respond.text)
		token = selector.xpath('//form/input[2]/@value')
		print(token)
		return token

	def login(self, name, password):
		token = self.__get_token()
		post_data = {
			'commit': 'Sign in',
			'utf8': '✓',
			'authenticity_token': token,
			'login': name,
			'password': password
		}
		self.__login_url = 'https://github.com/session'
		respond = self.session.post(self.__login_url, data=post_data, headers=self.__headers)
		if respond.status_code != 200:
			print('首次get请求失败(获取token)' + str(respond.status_code))
			exit(-1)
		print(respond.text)


if __name__ == '__main__':

	name = 'dxj728'
	password = '******'
	git_spider = Spider()
	git_spider.login(name, password)
