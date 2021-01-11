# --coding:utf-8--
# File: string_test.py
# Author: dxj728
# Time: 2019年08月18日21时
# 说明：string方法学习
# 参考来源:	https://www.runoob.com/python3/python3-string.html

import string

# 注：string 不支持单字符类型，单字符在python也视为一个字符串使用

str_demo = 'hello world!'
str_demo2 = """长字符串，可跨行"""
str_demo3 = r'原始字符串：会对反斜线进行自动转义'
r_str = r'hello world\n'		# 原始字符串，所见即所得（系统内部自动转义）
u_str = u'你好！'			# 仅python2中使用，表示utf-8字符(python2默认为8位ascii码)，python默认均为Unicode字符
print(str_demo, r_str, u_str)

str1 = str_demo[0:5]		# 字符串截取，返回截取后字符串
print(str_demo, str1)		# ('hello world!', 'hello')

"""运算符"""
str2 = str_demo * 2		# 重复输出字符串
str3 = 'a' in str_demo		# 包含指定字符串则返回True
str4 = 'a' not in str_demo 		# 不包含指定字符串返回False
print(str2, str3, str4)			# ('hello world!hello world!', False, True)

"""字符串格式化: 格式化参数 = 备注1"""
str5 = 'my name is %s, and %d years old' % ('dxj', 18)
str6 = 'my name is {0}, and {1} years old'.format('dxj', 18)
print(str5, str6)			# my name is dxj, and 18 years old

"""转成字符串"""
p = 99.8
str_p1 = str(p)             # 将其他类型转换为字符串
str_p2 = repr(p)            # 将其他类型转换为字符串
print(str_p1)               # 99.8
print(str_p1)               # 99.8
print(repr(str_demo))       # 'hello world!'    \\ 对字符串再次转换为带引号的形式

"""字符串合并与分割：行界符定义 = 备注2"""
str9 = str_demo.split('e', maxsplit=1)		# 以特定字符串分割截取字符串(分割后生成子字符串均不携带该字符串)，若最大截取次数maxsplit指定，则截取maxsplit次，返回maxsplit+1个字符串
str10 = str_demo.splitlines(keepends=False)		# 以行界符分割，返回字符串列表list，若参数keepends=False，则返回值不包括换行符，为True则包含

str11 = str_demo.strip('a')		# 去掉字符串两边的指定字符(默认指定字符为空格)
str12 = str_demo.lstrip('a')		# 去掉字符串左边(前面)的指定字符(默认指定字符为空格)
str13 = str_demo.rstrip('a')		# 去掉字符串右边(后面)的指定字符(默认指定字符为空格)

str14 = 'a'.join([])		# 以指定字符串为分隔符，将list或tuple中各元素合并为一个新的字符串

str15 = str_demo.partition('a')		# 以指定的分隔符将字符串(从左往右)进行分割，返回一个3元的元组，[1]为分隔符左边的子串，[2]为分隔符本身吗，[3]为分隔符右边的子串
str16 = str_demo.rpartition('a')		# 同上，方向换为从右往左(从后往前)

str17 = str_demo.replace('old', 'new', 1)		# 使用new子字符串替换字符串中的old子字符串，若指定第3参数，则替换不超过max次

str18 = str_demo.ljust(50, '*')		# 返回指定长度字符串，字符串内容居左，若原始长度超过指定长度，则返回原始字符串，否则填充指定字符串(默认为ascii空格)
str19 = str_demo.rjust(50, '*')		# 同上，字符串内容居右
str20 = str_demo.center(50, '*')		# 同上，字符串内容居中
str21 = str_demo.zfill(10)			# 同上，从左开始用0填充字符串至指定长度

# 字符串查找与判断
str22 = str_demo.find('a', 0, 10)		# 检测字符串中是否包含子字符串，如果指定 beg（开始）和 end（结束）范围，则检查是否包含在指定范围内，如果包含子字符串，则返回开始的索引值(下标，从0开始)，否则返回-1。
str23 = str_demo.rfind('a', 0, 10)		# 同上，从右开始(从后往前)
str24 = str_demo.count('a', 0, 10)		# 查找指定字符串出现的次数，并可指定查找开始和结束范围

str25 = str_demo.index('e', 0, 10)		# 同find()方法，但指定子字符串找不到时会报ValueError异常

str26 = str_demo.isdigit()		# 判断字符串是否只由数字构成，是返回True，否则返回False
str27 = str_demo.isalpha()		# 判断字符串是否只由字母构成，是返回True，否则返回False
str28 = str_demo.isalnum()		# 判断字符串是否只由字母或数字构成，是返回True，否则返回False
str29 = str_demo.isspace()		# 判断字符串是否只由空格构成，是返回True，否则返回False

str30 = str_demo.istitle()		# 判断字符串是否标题化(首字母大写，忽略非字母)，是返回True，否则返回False
str31 = str_demo.isupper()		# 判断字符串中所有的字母是否都为大写
str32 = str_demo.islower()		# 判断字符串中所有的字母是否都为小写

str33 = str_demo.startswith('a')		# 判断字符串是否以指定字符开始
str34 = str_demo.endswith('a')		# 判断字符串是否以指定字符结束

"""字符串变换"""
str35 = str_demo.title()			# 返回标题化字符串(首字母大写)
str36 = str_demo.swapcase()		# 字符串大小写反转
str37 = str_demo.upper()			# 字符串均转为大写
str38 = str_demo.lower()			# 字符串均转为小写
str39 = str_demo.expandtabs(tabsize=8)		# 将字符串中的tab符号('\t')转换为空格，默认的空格数(tabsize参数)是8；

trantab = str_demo.maketrans('de', '45')		# 创建字符映射的转换表，第1,2参数逐一对应转换关系
str40 = str_demo.translate(trantab)			# 对字符串执行转换，第2参数为需要删除的参数
print(str40)        # h5llo worl4!


"""bytes类型: 由多个字节构成，以字节为单位进行操作，支持方法与字符串相同，同是不可变类型
	str-->bytes类型方法：
		1.字符串均由ASCII字符组成，则通过前缀b实现
		2.调用bytes()函数(即bytes类型的构造方法)，将字符串按照指定的字符集(默认为UTF-8)转换成bytes类型
		3.调用字符串的encode()方法将字符串按指定字符集(默认为UTF-8)转换成bytes类型
"""
b1 = b'Hi'
print(b1)       # b'Hi'
b2 = bytes('Hi', encoding='utf-8')
print(b2)       # b'Hi'
b3 = 'Hi'.encode('utf-8')
print(b3)       # b'Hi'

"""str<-->bytes相互转换(编解码)"""
cb_en = 'python编程语言'.encode('utf-8')
print(cb_en)        # b'python\xe7\xbc\x96\xe7\xa8\x8b\xe8\xaf\xad\xe8\xa8\x80'
cb_de = cb_en.decode(encoding='utf-8')
print(cb_de)        # python编程语言
