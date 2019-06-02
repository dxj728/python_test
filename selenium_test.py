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
import time

# 打开百度进行搜索
browser = webdriver.Chrome()
try:
	browser.get('https://www.baidu.com')
	input = browser.find_element_by_id('kw')
	input.send_keys('python')
	input.send_keys(Keys.ENTER)
	wait = WebDriverWait(browser, 5)
	wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
	time.sleep(3)
	input.clear()
	time.sleep(1)
	input.send_keys('hello world!')
	input.send_keys(Keys.ENTER)
	wait = WebDriverWait(browser, 5)
	wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
	browser.back()
	browser.execute_script('window.open()')
	print(browser.window_handles)
	browser.switch_to.window(browser.window_handles[1])
	browser.get('https://www.github.com')
	wait = WebDriverWait(browser, 5)
	browser.switch_to.window(browser.window_handles[0])
	time.sleep(1)
	browser.back()
	time.sleep(3)
	browser.forward()
	print('over')
finally:
	browser.close()		#todo: 此处未能全部关闭，有待解决

#
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# input_first = browser. find_element_by_id('kw')
# print(input_first)
# browser.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium .webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# wait = WebDriverWait(browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'kw')))
# print(input)
# print("over")
# browser.close()
