# --coding:utf-8--
# File: unittest_test.py
# Author: dxj728
# Time: 2020年04月06日23时
# 说明：单元测试调用代码

# ----------------------------unittest模块测试代码示例--------------------------------


def one_equation(a, b):
    '''
    求一元一次方程a * x + b = 0的解
    参数a - 方程中变量的系数
    参数b - 方程中的常量
    返回 方程的解
    '''
    # 如果a = 0，则方程无法求解
    if a == 0:
        raise ValueError("参数错误")
    # 返回方程的解
    else:
    #        return -b / a  # ①
        return b / a


def two_equation(a, b, c):
    '''
    求一元二次方程a * x * x + b * x + c = 0的解
    参数a - 方程中变量二次幂的系数
    参数b - 方程中变量的系数
    参数c - 方程中的常量
    返回 方程的根
    '''
    # 如果a == 0，变成一元一次方程
    if a == 0:
        raise ValueError("参数错误")
    # 有理数范围内无解
    elif b * b - 4 * a * c < 0:
        raise ValueError("方程在有理数范围内无解")
    # 方程有唯一的解
    elif b * b - 4 * a * c == 0:
        # 使用数组返回方程的解
        return -b / (2 * a)
    # 方程有两个解
    else:
        r1 = (-b + (b * b - 4 * a * c) ** 0.5) / 2 / a
        r2 = (-b - (b * b - 4 * a * c) ** 0.5) / 2 / a
        # 方程的两个解
        return r1, r2


