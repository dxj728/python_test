# --coding:utf-8--
# File: coding_interviews.py
# Author: dxj728
# Time: 2022年01月09日21时
# 说明：剑指offer题目
#


'''剑指 Offer 09. 用两个栈实现队列'''
class CQueue:

    def __init__(self):
        self.my_queue = []

    def appendTail(self, value: int) -> None:
        self.my_queue.insert(0, value)
        return None

    def deleteHead(self) -> int:
        if len(self.my_queue) != 0:
            return self.my_queue.pop()
        else:
            return -1
