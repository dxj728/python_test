# --coding:utf-8--
# File: leecode.py
# Author: dxj728
# Time: 2021年12月12日10时
# 说明：；力扣(leecode)做题


# 2021.12.12
'''7. 整数反转'''
# def reverse(x: int) -> int:
#
#     str_x = str(x)
#     str_x = str_x[::-1] if '-' not in str_x else '-' + str_x[:0:-1]
#     ret = int(str_x)
#     if ret < -2147483648 or ret > 2147483647:
#         ret = 0
#     return ret


'''4. 寻找两个正序数组中的中位数 ----20230420'''
# def mn(nums1, nums2):
#     list1 = nums1 + nums2
#     list1.sort()
#     if len(list1) % 2 != 0:
#         mid = int(len(list1) / 2)
#         return list1[mid]
#     else:
#         mid = int(len(list1) / 2) - 1
#         return (list1[mid] + list1[mid+1]) / 2
#
# nums1 = [1, 3]
# nums2 = [2]
# y = mn(nums1, nums2)
# print(y)


"""43.字符串相乘 ----20230422"""
# def multiply(num1, num2):
#     n = int(num1) * int(num2)
#     return str(n)
#
# num1 = "2"
# num2 = "3"
# print(multiply(num1, num2))


'''3. 无重复字符的最长子串 ----20230423'''
'''未通过最后超长测例'''
# def lengthOfLongestSubstring(s):
#     list1 = list(s)
#     max_value = 0
#     for i in range(len(list1)):
#         new_list = []
#         for j in range(len(list1) - i):
#             if list1[i+j] not in new_list:
#                 new_list.append(list1[i+j])
#             else:
#                 new_list = []
#             if len(new_list) > max_value:
#                 max_value = len(new_list)
#     return max_value
#
# s = "pwwkew"
# print(lengthOfLongestSubstring(s))


'''2. 两数相加 ----20230423'''
# def addTwoNumbers(l1, l2):
#     l1.reverse()
#     l2.reverse()
#     max_len = len(l1) if len(l1) > len(l2) else len(l2)
#     min_len = len(l1) if len(l1) < len(l2) else len(l2)
#     ret_list = []
#     send_value = 0
#     for i in range(min_len):
#         ret = l1[i] + l2[i] + send_value
#         if ret >= 10:
#             ret_list.append(ret - 10)
#             send_value = 1
#         else:
#             ret_list.append(ret)
#             send_value = 0
#     for i in range(max_len - min_len):
#         new_list = l1 if len(l1) > len(l2) else l2
#         ret = new_list[i + min_len] + send_value
#         if ret >= 10:
#             ret_list.append(ret - 10)
#             send_value = 1
#         else:
#             ret_list.append(ret)
#             send_value = 0
#     return ret_list
#
#     pass
#
#
# l1 = [2,4,3]
# l2 = [5,6,4]
# print(addTwoNumbers(l1, l2))

















