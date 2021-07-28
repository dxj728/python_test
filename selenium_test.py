# --coding:utf-8--
# File: selenium_test.py
# Author: dxj728
# Time: 2019年03月20日21时
# 说明：selenium驱动浏览器动作
# 环境配置：
#     安装requests库: pip3 install requests
#     安装selenium库: pip3 install selenium
#     安装chromedriver驱动: 下载网址：http://chromedriver.storage.googleapis.com/index.html
#         windows下配置环境变量： 将chromedriver.exe放置于python的script目录下
#         linux/mac下配置环境变量： sudo mv chromedriver /usr/bin
#         验证执行：控制台直接执行: chromedriver 查看输出
#     firefox驱动：GeckoDriver
# 参考教程：https://zhuanlan.zhihu.com/p/111859925

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 打开百度进行搜索
browser = webdriver.Chrome()    # 创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser.set_window_size(1600, 900)    # 浏览器窗口调整
try:
    browser.get('https://www.baidu.com')    # 通过浏览器向服务器发送URL请求
    input = browser.find_element_by_id('kw')    # 通过id定位元素，并实例化为Webelement类
    input.send_keys('python')   # 键盘事件
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 5)    # 设置显式等待
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))    # 通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在
    time.sleep(3)
    input = browser.find_element_by_id('kw')    # 通过id定位元素，并实例化为Webelement类
    input.clear()   # 清除文本
    time.sleep(1)
    input.send_keys('hello world!')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    browser.back()
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])     # 浏览器切换至第2个窗口
    browser.get('https://www.csdn.net')
    wait = WebDriverWait(browser, 5)
    browser.switch_to.window(browser.window_handles[0])     # 浏览器切换回第1个窗口
    time.sleep(1)
    browser.back()
    time.sleep(3)
    browser.forward()
    print('over')
finally:
    # browser.close()     # 关闭单个窗口
    browser.quit()		# 关闭所有窗口

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
