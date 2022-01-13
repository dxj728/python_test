# --coding:utf-8--
# File: IO_test.py
# Author: dxj728
# Time: 2019年10月11日22时
# 说明：https://blog.csdn.net/qq_39928840/article/details/81132230


"""input(): python3中使用该方法获取用户输入,等同于python2中raw_input()"""
# msg = input("请输入你的值：")      # 返回用户输入的内容，均为字符串类型

# 示例：
# msg1 = input().strip()              # 单行输入，返回字符串
# msg_list2 = list(map(int, input().strip().split()))      # 单行间隔输入(空格)，返回列表(当前强转为整型)
# msg_list3 = [int(input().strip()) for _ in range(6)]          # 多行输入，返回列表(元素强转为整型)
# msg_list4 = [list(map(int, input().strip().split())) for _ in range(6)]      # 多行多间隔输入，返回嵌套列表(元素强转为整型)

# print('\n'.join(map(str, msg_list4)))    # 返回结果表达


"""打开文件：
    open(file, mode, buffer, encoding)，返回一个文件对象(文件描述符)
    file: 文件名称或路径
    mode: 文件打开模式
    buffer: 缓冲大小，0/False(无缓冲)，1/True(带缓冲)，>1整数(指定寄存区缓冲大小，字节)，负数(默认缓冲大小)
    encoding: 指定字符集，windows下默认为GBK字符集
文件打开模式mode：r、w、a、+、b、
    r: 只读模式，不能创建文件(要求操作文件必须存在)，指针位于文件开头
    w: 写模式，操作文件存在会清空文件，操作文件不存在则新建文件
    a: 追加写入模式，操作文件存在会清空文件，操作文件不存在则新建文件，指针位于文件结尾
    r+: 读写模式，与r作用相同，但可写入文件
    w+: 读写模式，与w作用相同，但可读取文件
    a+: 追加读写模式，与a作用相同，但可读取文件
    b； 二进制模式，可与其他模式结合使用，比如rb、ab等
"""
# f = open('test.py', "r", 10, encoding='utf-8')      # 以只读模式打开当前路径下的test.py文件，缓冲为10字节，指定字符集utf-8，返回file对象
# print(f.name)       # test.py       \\ file对象属性，返回文件名称或路径
# print(f.mode)       # r             \\ file对象属性，返回被打开文件的访问模式
# print(f.encoding)   # utf-8         \\ file对象属性，返回被打开文件的当前使用字符集
# print(f.closed)     # False         \\ file对象属性，文件是否被关闭，返回True(已被关闭)/False(未被关闭)
#
"""关闭文件:
    close()：文件描述符方法，刷新缓冲区里任何还没写入的信息，并关闭文件
"""
# f.close()


"""with语句操作文件：
    将打开的文件放在with语句中，with语句会帮助我们自动关闭文件, 该方法返回值将赋值给as子句后的变量/元组，详细使用见相关py
    语法：
        with context_express as f:
            代码块
    通用实现：只要一个类实现了__enter__()和__exit__(exc_type, exc_value, exc_tb)方法，就可以使用with语句进行管理，详细使用见相关py
"""
# with open('test.py', 'r', True, 'utf-8') as f:
#     for line in f:
#         print(line)
#
# import fileinput
#
# with fileinput.input(files=('test.py', 'A_python.py')) as f:
#     for line in f:
#         print(line)

"""读取文件：
    三种方式：
        1.使用文件描述符的read()方法按字节/字符来读取,
            read(size): 从文件读取指定的字节数，size参数代表读取的字节数，默认size=为-1，表示读取全部文件内容
        2.使用文件描述符的readline()/readlines()方法按行读取内容
            readline(size): 读取整行，包括换行符,size非负参数指定返回指定大小的字节数，包括换行符
            readlines(sizeint): 读取所有行(只到EOF结束)，返回内容行列表，sizeint参数指定返回指定大小的字节数
        3.使用fileinput模块读取多个输入流，无需手动打开文件
"""

'''1.使用raad()方法按字符/字节读取'''
# f = open('test.py', 'r', True, 'utf-8')      # 也可以根据需求使用rb模式来读取字节
# try:
#     while True:
#         ch = f.read(1)      # 读取1个字符，不传参则默认读取文件全部内容
#         if not ch:
#             break
#         print(ch)
# finally:
#     f.close()
'''2.使用readline()/readlines()方法按行读取'''
# f = open('test.py', 'r', True, 'utf-8')      # 也可以根据需求使用rb模式来读取字节
# try:
#     while True:
#         '''2.1 使用readline()每次读取一行'''
#         line = f.readline()     # 每次读取一行
#         if not line:
#             break
#         print(line)
#         '''2.2 使用readlines()读取所有行，返回所有行组成的列表，可使用for ... in ...结构处理'''
#         for cur_line in f.readlines():
#             print(cur_line)
#
# finally:
#     f.close()
'''3.(不常用)使用fileinput模块及方法一次读取多个文件，无需手动打开文件
    f_iter = fileinput.input([files[, inplace[, backup[, bufsize[, mode[, openhook]]]]]])， 返回一个FileInput对象(可迭代)
        files:文件的路径列表
        inplace:是否返回输出结果到原文件中，默认为0不返回，设置为1时返回
        backup:备份文件的扩展名
        bufsize:缓冲区大小
        mode：读写模式，只能是读、写、读写、二进制四种模式，默认是读模式
        openhook：该参数必须是带两个参数（文件名和模式）的函数
    缺陷： 创建FileInput对象时无法指定字符集，比如和操作系统默认的字符集保持一致，故fileinput模块仅限于纯英文文本文件读取。
'''
# import fileinput
# for line in fileinput.input(files=['test.py', 'A_python.py']):
#     print(line)
#     print(fileinput.filename())     # 返回当前正在读取的文件的名称
#     print(fileinput.fileno())       # 返回当前文件的整数“文件描述符”
#     print(fileinput.lineno())       # 返回刚刚读取的行的累计行号
#     print(fileinput.filelineno())   # 返回当前文件中的行号
#     print(fileinput.isfirstline())  # 判断读取的行是不是该文件的第一行，是就返回true，否则返回false
#     print(fileinput.isstdin())      # 判断读取的是否是sys.stdin的最后一行，是就返回true，否则返回false
#     print(fileinput.nextfile())     # 关闭当前文件，以便下一次迭代将读取下一个文件的第一行（如果有的话）
# fileinput.close()       # 关闭FileInput对象


"""写入文件：
    两种方式：
        1.使用文件描述符write()方法写入字符串/字节串
        2.使用文件描述符的writelines()方法写入多个字符串/字节串
    说明：w、w+、wb+模式打开文件时，会立即清空文件内容，使用a、a+、ab+模式在原文件内容后追加内容
"""
# import os
# f = open('test.py', 'ab+')       # b模式写入字节串
# f.writable()        # 文件描述符方法，检查文件是否可写，返回True(可写)/False(不可写)
#
# f.write('hello, world'.encode('utf-8'))     # 写入单字符串，使用二进制写入实现以UTF-8字符集保存文件
#
# # 写入多字符串，os.linesep()方法返回当前操作系统上的换行符
# f.writelines((
#     ('hello world!' + os.linesep).encode('utf-8'),
#     ('hi, dxj' + os.linesep).encode('utf-8'),
#     ('bye!' + os.linesep).encode('utf-8'),
# ))


"""文件指针: 用于标明文件读写的位置，普通模式下每个数据就是一个字符，b模式下每个数据为一个字节
    文件描述符提供以下方法操作文件指针
    seek(offset, whence): 改变当前文件指针的位置
        offset: 文件指针偏移量
        whence: 开始移动时的参考位置，默认whence=0，表示文件从头计算；whence=1时，表示从当前所在位置计算；whence=2时，表示从文件结尾计算
    tell(): 返回文件指针的位置
"""
# f = open('test.py', 'rb+')
#
# print(f.tell())     # 打印文件指针当前所处位置
#
# f.seek(3)   # 文件指针移动到第3处(从文件开头计算)
#
# f.seek(5, 1)    # 文件指针继续向后移动5个位置(以当前位置计算)
#
# f.seek(-10, 2)  # 文件指针移动到倒数第10处


"""tempfile模块：生成临时文件和临时路径"""

'''创建临时文件，函数返回一个类文件对象，支持文件IO，支持with语句管理，在close时文件会被自动删除'''
# tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)

'''创建临时文件，该函数的功能与上一个函数的功能大致相同，只是它生成的临时文件在文件系统中有文件名
    增加的delete参数默认为True时，close后文件会被自动删除，delete参数为False时，文件对象在关闭时不会被删除，因此可以再后续代码中通过对象再次打开'''
# tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)

'''创建临时文件，与上述函数相比，当该程序向临时文件中写入数据时，会先写入到内存中，只到超过max_size才会真正的写入到物理磁盘中
    增加的max_size参数默认为0，当内存中需要写入数据大小超过max_size后或文件的fileno()方法被调用时，将内容写入硬盘，此时操作与TemporaryFile一致'''
# tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)

'''生成临时目录'''
# tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)

import tempfile

fp = tempfile.TemporaryFile()
print(fp.name)  # C:\Users\dxj728\AppData\Local\Temp\tmppzl2lqxk    \\ 返回临时文件路径名

print(tempfile.gettempdir())  # C:\Users\dxj728\AppData\Local\Temp                \\ 获取系统的临时目录
print(tempfile.gettempdirb())  # b'C:\\Users\\dxj728\\AppData\\Local\\Temp'        \\ 与上相同，只是返回字节串
print(tempfile.gettempprefix())  # tmp                                               \\ 返回用于生成临时文件的前缀名
print(tempfile.gettempprefixb())  # b'tmp'                                            \\ 与上相同，只是返回字节串

fp.write('hello'.encode('utf-8'))
fp.write('world'.encode('utf-8'))

fp.seek(0)  # 文件指针移到开始处，准备读取文件
print(fp.read().decode('utf-8'))

fp.close()  # 关闭临时文件，该文件会被自动删除

with tempfile.TemporaryDirectory() as fd:  # 使用with语句创建临时目录
    print(fd)  # C:\Users\dxj728\AppData\Local\Temp\tmpfv9k_b8m    \\ 返回临时目录
