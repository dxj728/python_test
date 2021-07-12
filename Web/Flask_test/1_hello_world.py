# --coding:utf-8--
# File: hello_world.py
# Author: dxj728
# Time: 2020年05月25日23时
# 说明：

from flask import Flask

## -----------------最简单的实现--------------------
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'hello'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000)



