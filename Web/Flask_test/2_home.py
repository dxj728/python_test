# --coding:utf-8--
# File: 2_home.py
# Author: dxj728
# Time: 2021年07月12日22时
# 说明：使用flask框架练习一个网页小请求
# 参考：廖雪峰python教程：https://www.liaoxuefeng.com/wiki/1016959663602400/1017806472608512

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
