# --coding:utf-8--
# File: logging_test.py
# Author: dxj728
# Time: 2019年03月04日00时
# 说明：logging日志模块练习
# 参考博客：https://www.cnblogs.com/Nicholas0707/p/9021672.html

import logging


# 日志级别：critical>error>warning>info>debug

# 1.基本输出
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# 输出效果，在控制器上输出warning及以上级别内容

# 2.格式调整
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s%(name)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S %a')
logging.debug("debug_config")
logging.info("info_config")
logging.warning("warning_config")
logging.error("error_config")
logging.critical("critical_config")
# 输出效果：按格式输出
# 注：basicConfigp最好配置于文件顶部，第一次调用时生效，多次调用不累加，

# 3.输出文件
logging.basicConfig(level=logging.DEBUG,
					filename=r"D:\desktop\test\log.log",
					format="%(asctime)s%(name)s %(levelname)s %(pathname)s %(lineno)s: %(message)s",
					datefmt='%Y-%m-%d %H:%M:%S %a'
					)
logging.debug("debug_txt")
logging.info("info_txt")
logging.warning("warning_txt")
logging.error("error_txt")
logging.critical("critical_txt")
# 输出效果：均输出于文本中，不再显示于控制台

# 4.输出变量
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s%(name)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S %a')
logging.warning("%s is %d years old", 'dxj728', 25)
# 注：第一个格式字符串作为事件的输出，变量通过后续参数进行传递





