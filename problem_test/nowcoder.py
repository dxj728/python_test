# --coding:utf-8--
# File: nowcoder.py
# Author: dxj728
# Time: 2023年04月23日22时
# 说明：牛客编程练习


'''华为研发工程师编程题'''
'''1.汽水瓶
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足1≤n≤100

注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。

输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

示例1
输入例子：
3
10
81
0
输出例子：
1
5
40
例子说明：
样例 1 解释：用三个空瓶换一瓶汽水，剩一个空瓶无法继续交换
样例 2 解释：用九个空瓶换三瓶汽水，剩四个空瓶再用三个空瓶换一瓶汽水，剩两个空瓶，向老板借一个空瓶再用三个空瓶换一瓶汽水喝完得一个空瓶还给老板'''

# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     start = int(a[0])
#     if start == 0:
#         break
#     if start < 2:
#         print(0)
#     end = 0
#     while start > 2:
#         end = end + int(start / 3)
#         start = int(start / 3) + start % 3
#
#     if start == 2:
#         end = end + 1
#     print(end)

'''
2.明明的随机数
明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围：1≤n≤1000 ，输入的数字大小满足 1≤val≤500
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
第一行先输入随机整数的个数 N 。
接下来的 N 行每行输入一个整数，代表明明生成的随机数。
具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果

示例1
输入例子：
3
2
2
1
输出例子：
1
2
例子说明：
输入解释：
第一个数字是3，也即这个小样例的N=3，说明用计算机生成了3个1到500之间的随机整数，接下来每行一个随机数字，共3行，也即这3个随机数字为：
2
2
1
所以样例的输出为：
1
2
'''

# import sys
#
# new_list = []
#
# for line in sys.stdin:
#     a = line.split()
#     new_list.append(int(a[0]))
#
# new_list = new_list[1:]
# ret_list = []
#
# for x in new_list:
#     if x not in ret_list:
#         ret_list.append(x)
# ret_list.sort()
#
# for x in ret_list:
#     print(x)
#
#     # print(int(a[0]) + int(a[1]))

'''3.进制转换
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1≤n≤2 31 −1
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

示例1
输入例子：
0xAA
输出例子：
170'''

# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     x = int(a[0], base=16)
#     print(x)

    
'''BM50 两数之和'''
# class Solution:
#     def twoSum(self , numbers: List[int], target: int) -> List[int]:
#         # write code here
#         for i in range(0, len(numbers)):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     ret_list = [i+1, j+1]
#                     ret_list.sort()
#                     return ret_list

# class Solution:     ## 参照解题
#     def twoSum(self, numbers, target):
#         # write code here
#         new_dict = {}
#         for i, num in enumerate(numbers):
#             if (target-num) in new_dict:
#                 return [new_dict[target-num]+1, i+1]
#             new_dict[num] = i

# a = Solution()
# print(a.twoSum([0,4,3,0],0))


'''BM54 三数之和'''
# class Solution:
#     def threeSum(self, numbers):
#         # write code here
#         if len(numbers) < 3:
#             return []
#         ret_list = []
#         for i in range(0, len(numbers)):
#             print(i, numbers[i])
#             for j in range(i+1, len(numbers)):
#                 print(j, numbers[j])
#                 for k in range(j+1, len(numbers)):
#                     if numbers[i]+numbers[j]+numbers[k] == 0:
#                         new_list = [numbers[i],numbers[j],numbers[k]]
#                         new_list.sort()
#                         if numbers[i] == 0 and numbers[j] == 0 and numbers[k] == 0:
#                             print('1')
#                         if new_list not in ret_list:
#                             ret_list.append(new_list)
#         ret_list.sort()
#         return ret_list
#
#
# a = Solution()
# print(a.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

























