


# from selenium import webdriver
# browser =webdriver.Chrome()

# import urllib.request
# target_url="http://www.baidu.com"
# response = urllib.request.urlopen(target_url)
# realurl = response.geturl()
# print(realurl)

# import urllib.parse
# import urllib.request
# word = '周杰伦'
# url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=20' # word为关键词，pn是百度用来分页的..
# response = urllib.request.urlopen(url)
# page = response.read()
# print(page)

# import os
#
# filepath=r'D:\desktop\hahaha'
#
# if os.path.exists(filepath):
#     os.removedirs(filepath)
# else:
#     os.mkdir(filepath)


from lxml import etree
import requests

class Login():
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selecor = etree
        token = selecor
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)
