# --coding:utf-8--
# File: big_zip.py
# Author: dxj728
# Time: 2019年03月27日23时
# 说明：文件解压练习(zipfile模块学习)

import os
import zipfile

# extract()逐个解压文件至指定目录
def unzip(zip_path, out_path):
    if not os.path.exists(zip_path):
        print('待解压文件不存在')
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    myzip = zipfile.ZipFile(zip_path, 'r')
    for file in myzip.namelist():
        myzip.extract(file, out_path)
    myzip.close()

# extractall()一次全部解压，输出路径不存在会自动递归创建
def unzip2(zip_path, out_path):
    if not os.path.exists(zip_path):
        print('待解压文件不存在')
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    myzip = zipfile.ZipFile(zip_path, 'r')
    # out_path = r'D:\desktop\test\hahaha\ooo'
    myzip.extractall(out_path)
    myzip.close()

if __name__ == '__main__':
    out_path = r'D:\desktop\test'
    zip_path = r'D:\desktop\test\test.zip'
    unzip(zip_path, out_path)
    manual_path = os.path.join(out_path, 'Manual.zip')
    unzip(manual_path, out_path)
    unzip2(zip_path, out_path)