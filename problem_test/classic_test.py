# --coding:utf-8--
# File: classic_test.py
# Author: dxj728
# Time: 2021年02月01日23时
# 说明：经典/常见编程题或面试题解法

"""GIL全局解释器锁:
    特点：Cpython中独有，每个线程在执行时都需要先获取GIL，保证同一时刻只有一个线程可以执行代码，即同一时刻只有一个线程在使用CPU，即伪多线程
    使用：
        可以通过修改tick值来修改GIL锁占用时间，一旦tick=100时，GIL锁释放
        IO操作当CPU闲置时释放GIL锁
    解决GIL锁影响
        1.更换Cpython为Jpython（不建议）
        2.使用多进程完成多线程任务
        3.使用其他语言(如C语言)去实现多线程
"""

"""------Fibonacci(斐波那契数列) 中第N个数------"""
def fib(n):
    """Fibonacci递归解法:时间复杂度0(1.618^n),最大深度1000。"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib1(n):
    """Fibonacci非递归解法：时间复杂度0(n)"""
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

# print(fib(40))      # 计算时间很长
# print(fib1(400))    # 计算时间很短，立等可取


"""------Bubble Sort(冒泡排序)------"""
arr = [6, 0, 2, 10, 14, 26, -8]


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubble_sort(arr)        # 排序内部直接生效，无需接收返回值
print(arr)


"""------Quick Sort(冒泡排序)------"""
arr = [6, 0, 2, 10, 14, 26, -8]


def quick_sort(arr, start, end):
    """快速排序：非稳定性排序，时间复杂度介于O(nlogn)与n(n2)之间(与序列有序性成反比)"""
    if start >= end:    # start>end时，证明右边已无数据
        return
    left = start
    right = end
    mid = arr[left]     # 序列分割，选取基准
    while left < right:
        while left < right and arr[right] > mid:    # 先从右推进
            right = right - 1
        arr[left] = arr[right]
        while left < right and arr[left] < mid:     # 后从左推进
            left = left + 1
        arr[right] = arr[left]
    arr[left] = mid     # 元素归位
    quick_sort(arr, start, left-1)      # 函数自调用
    quick_sort(arr, left+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)

