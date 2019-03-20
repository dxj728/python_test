# --coding:utf-8--
# File: selenium_test.py
# Author: dxj728
# Time: 2019年03月20日21时
# 说明：selenium驱动浏览器动作
# 环境配置：
# 	安装requests库: pip3 install requests
#	安装selenium库: pip3 install selenium
#	安装chromedriver驱动: 下载网址：http://chromedriver.storage.googleapis.com/index.html
#		windows下配置环境变量： 将chromedriver.exe放置于python的script目录下
#		linux/mac下配置环境变量： sudo mv chromedriver /usr/bin
#		验证执行：控制台直接执行: chromedriver 查看输出
#	firefox驱动：GeckoDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 打开百度进行搜索
browser = webdriver.Chrome()
try:
	browser.get('http://www.baidu.com')
	input = browser.find_element_by_id('kw')
	input.send_keys('python')
	input.send_keys(Keys.ENTER)
	wait = WebDriverWait(browser, 10)
	wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
	print(browser.current_url)			# 当前页面的url
	print(browser.get_cookies())		# 当前的cookies
	print(browser.page_source)			# 当前界面的源代码
finally:
	browser.close()



