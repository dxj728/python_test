# --coding:utf-8--
# File: request_SSL.py
# Author: dxj728
# Time: 2019年11月27日22时
# 说明：

# pip install cryptography
#
# pip install pyOpenSSL
#
# pip install certifi

import requests

r = requests.get("https://www.12306.cn")
print(r.status_code)

