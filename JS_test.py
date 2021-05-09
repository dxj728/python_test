# --coding:utf-8--
# File: JS_test.py
# Author: dxj728
# Time: 2021年01月20日23时
# 说明：

# while True:
#     try:
#         s=input()
#         while len(s)>8:
#             print(s[:8])
#             s=s[8:]
#         print(s.ljust(8, "0"))
#     except:
#         break


# str_num = input().strip()
# print(str_num[::-1])


# n = int(input().strip())
# msg_list = [input().strip() for _ in range(n)]
# msg_list.sort()
# print('\n'.join(map(str, msg_list)))


# str1 = input().strip()
# str2 = input().strip()
# n = str1.lower().count(str2.lower())
# print(n)

# str1 = input().strip()
# str_list = list(str1)


# msg_list = input().strip().split()
# print(len(msg_list[-1]))

# while True:
#     try:
#         n = int(input().strip())
#         num_list = [int(input().strip()) for _ in range(n)]
#         num_list = list(set(num_list))
#         num_list.sort()
#         print('\n'.join(map(str, num_list)))
#     except EOFError:
#         break


# while True:
#     try:
#         x = input().strip()
#         print(int(x, base=16))
#     except EOFError:
#         break


# def deal_list(num_list):
#     num_dict = {}
#     for index, value in num_list:
#         if index not in num_dict.keys():
#             num_dict[index] = value
#         else:
#             num_dict[index] = num_dict[index] + value
#     num_list = list(num_dict.keys())
#     num_list.sort()
#     ret_list = []
#     for i in num_list:
#         tmp = '{} {}'.format(i, num_dict[i])
#         ret_list.append(tmp)
#     return ret_list
#
#
# n = int(input().strip())0129
# num_list = [list(map(int, input().strip().split())) for _ in range(n)]
# num_list = deal_list(num_list)
# print('\n'.join(map(str, num_list)))
        
        
# x = 'abcabd'
# print(x[::-1])
        
        
# while True:
#     try:
#         x = input().strip()
#         y = set(list(x))
#         print(len(y))
#     except EOFError:
#         break
        
        
# x = input().split()
# x.reverse()
# print(' '.join(x))

# import sys
#
# def deal_str(s, value_list):
#     list1 = []
#     for value in value_list:
#         if value[0] == s:
#             list1.append(value)
#     if len(list1) == 0:
#         return 0, 0
#     elif len(list1) == 1:
#         return 1, list1[0]
#     else:
#         length = 0
#         list2 = []
#         for value in list1:
#             if len(value) > length:
#                 list2 = []
#                 list2.append(value)
#                 length = len(value)
#             elif len(value) == length:
#                 list2.append(value)
#         if len(list2) == 1:
#             return 1, list2[0]
#         elif len(list2) > 1:
#             list2.sort()
#             return 1, list2[0]
#
#
# if __name__ == '__main__':
#     k = int(sys.stdin.readline().strip())
#     n = int(sys.stdin.readline().strip())
#     value_list = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         value_list.append(line)
#     start = value_list[k]
#     start_list = []
#     start_list.append(start)
#     value_list.remove(start)
#     while True:
#         ret_num, ret_str = deal_str(start[-1], value_list)
#         if ret_num == 0:
#             break
#         else:
#             start_list.append(ret_str)
#             start = ret_str
#             value_list.remove(ret_str)
#     print(''.join(start_list))
#
#
# """
# 0
# 6
# word
# dd
# da
# dc
# dword
# d
# """
        




# import sys
#
#
# def deal_num(value_list):
#     if len(value_list) < 3:
#         return 0
#     else:
#         ret_list = []
#         for a in value_list:
#             test_list = value_list.copy()
#             test_list.remove(a)
#             for b in test_list:
#                 test_list2 = test_list.copy()
#                 test_list2.remove(b)
#                 for c in test_list2:
#                     if a == b + 2 * c:
#                         ret_list.append(str(a))
#                         ret_list.append(str(b))
#                         ret_list.append(str(c))
#         if len(ret_list) == 0:
#             return 0
#         else:
#             return ret_list
#
#
# if __name__ == '__main__':
#     n = int(sys.stdin.readline().strip())
#     a = sys.stdin.readline().strip()
#     value_list = list(map(int, a.split()))
#     ret = deal_num(value_list)
#     if ret == 0:
#         print(0)
#     else:
#         print(" ".join(ret))

#
# """
# 4
# 2 7 3 0
#
# 3
# 1 1 1
#
# """
#
#
# import sys
#
# def get_sum(cur_list):
#     if len(cur_list) == 0 or cur_list == None:
#         return []
#     else:
#         cur_list = cur_list[::-1]
#         sum_list = []
#         for i in range(0, len(cur_list)):
#             sum = 0
#             while i >= 0:
#                 sum = sum + cur_list[i]
#                 i = i - 1
#             sum_list.append(sum)
#         return sum_list
#
#
# def check_list(ret_list):
#     cur_list = ret_list[0:-1]
#     cur_value = ret_list[-1]
#     sum_list = get_sum(cur_list)
#     if cur_value in sum_list:
#         index = sum_list.index(cur_value)
#         length = index + 2
#         while length:
#             ret_list.pop()
#             length = length - 1
#         ret_list.append(2 * cur_value)
#         ret_list = check_list(ret_list)
#     return ret_list
#
# def deal_value(value_list):
#     if len(value_list) == 0:
#         return False
#     else:
#         ret_list = []
#         for i in range(0, len(value_list)):
#             ret_list.append(value_list[i])
#             if len(ret_list) >= 1:
#                 ret_list = check_list(ret_list)
#         return ret_list
#
# if __name__ == '__main__':
#     line = sys.stdin.readline().strip()
#     value_list = list(map(int, line.split()))
#     ret_list = deal_value(value_list)
#     ret_list = ret_list[::-1]
#     ret_list = list(map(str, ret_list))
#     print(' '.join(ret_list))
#
# """
# 5 10 20 50 85 1
# 6 7 8 13 9
#
# """
    
    
    