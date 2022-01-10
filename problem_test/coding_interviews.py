# --coding:utf-8--
# File: coding_interviews.py
# Author: dxj728
# Time: 2022年01月09日21时
# 说明：剑指offer题目
# leecode网站对应题序：https://leetcode-cn.com/study-plan/lcof/?progress=a3nu56j


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


'''剑指 Offer 30. 包含min函数的栈'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return min(self.stack)



'''剑指 Offer 06. 从尾到头打印链表'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution06:
    def reversePrint(self, head: ListNode):
        if head is None or head.val is None :
            return []
        self.my_list = []
        while True:
            self.my_list.append(head.val)
            if head.next is None:
                break
            else:
                head = head.next
        return self.my_list[::-1]


'''剑指 Offer 05. 替换空格'''
class Solution05:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


'''剑指 Offer 58 - II. 左旋转字符串'''
class Solution58:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]


'''剑指 Offer 03. 数组中重复的数字'''
class Solution03:
    def findRepeatNumber(self, nums: List[int]) -> int:
        cur_set = set()
        for i in range(0, len(nums)):
            cur_set.add(nums[i])
            if len(cur_set) < i + 1:
                return nums[i]


'''剑指 Offer 53 - I. 在排序数组中查找数字 I'''
class Solution53:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)


'''剑指 Offer 53 - II. 0～n-1中缺失的数字'''
class Solution53:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i != len(nums) -1:
                if nums[i+1] - nums[i] > 1:
                    return nums[i] + 1
            else:
                if nums[0] != 0:
                    return 0
                return nums[i] + 1


'''剑指 Offer 04. 二维数组中的查找'''
class Solution04:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for cur_list in matrix:
            if target in cur_list:
                return True
        return False



































