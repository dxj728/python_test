# --coding:utf-8--
# File: app.py
# Author: dxj728
# Time: 2020年03月16日21时
# 说明：zipapp模块练习

from say_hello import *
import time

def main():
    print('程序开始执行！')
    print(say_hello('孙悟空'))
    time.sleep(3)

# 增加main函数
if __name__ == '__main__':
    main()
