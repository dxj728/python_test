# --coding:utf-8--
# File: pydoc_mod.py
# Author: dxj728
# Time: 2020年04月06日20时
# 说明：pydoc模块练习使用

'''
    使用方法:
        1. DOS中查看模块文档（即已有注释整合）

            python -m pydoc 模块名

              eg: python -m pydoc fkmodule
              效果：在DOC控制台中输出注释及代码结构信息等，使用空格翻页输出

        2. 生成html文档

            python -m pydoc -w 模块名

            eg: python -m pydoc -w fkmodule
            效果：在当前目录下生成fkmodule.html文件，内容与控制台输出内容相同

        3. 为指定目录下所有模块生成html文档(不建议)

            python -m pydoc -w 目录名

            效果：当前目录下生成指定目录的所有html文件
            缺陷：需要展示子目录下文件说明时，会去子目录下找对应的html文件，文件如果不存在，会显示404错误

        4. 启用本地服务器来查看文档信息(推荐)

            python  -m pydoc -p 端口号

            eg: python -m pydoc -p 8899
            效果：开启HTTP服务器以8899端口提供服务，DOS中输入b命令可启动浏览器（用户亦可自行启动浏览器），输入q命令停止服务器

        5. 查找模块

            python -m pydoc -k 被搜索模块的部分内容

            eg: python -m pydoc -k fk
            效果：输出所有包含'fk'字符的模块

'''
