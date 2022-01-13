# --coding:utf-8--
# File: dict_test.py
# Author: dxj728
# Time: 2020年12月07日22时
# 说明：dict方法学习
# 参考来源：https://www.runoob.com/python/python-dictionary.html


dict_demo = {'name': 'dxj728', 'age': 18}
print(type(dict_demo))  # <class 'dict'>
print(dict_demo['name'])    # 访问value值

'''字典创建
    1.直接{key:value}创建
    2.dict()传入列表或元组创建
    3.dict()传入关键字参数创建
'''
# dict1 = {(20, 30): 'good', 30: 'bad'}    # 元组可以做key值，但是列表不可以做key值
# dict2 = dict([('brocoli', 1.29), ('lettuce', 2.19)])
# print(dict2)        # {'brocoli': 1.29, 'lettuce': 2.19}
# dict3 = dict(a=1, b=2)
# print(dict3)    # {'a': 1, 'b': 2}

'''增删查改'''
# dict_demo['sex'] = 'boy'    # 添加key-value对，只需为不存在的key赋值
# print(dict_demo)    # {'name': 'dxj728', 'age': 18, 'sex': 'boy'}
#
# del dict_demo['age']    # 删除key-value对，使用del语句
# print(dict_demo)    # {'name': 'dxj728', 'sex': 'boy'}

# 使用in语句查询字典是否包含指定的key
# print('grade' in dict_demo)     # False

# dict_demo['name'] = 'dxj'   # 直接赋值即可覆盖修改
# print(dict_demo)    # {'name': 'dxj', 'sex': 'boy'}

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# dict_demo.clear()   # 清空dict内的所有key-value对,原字典成为空字典，直接生效
# print(dict_demo)    # {}

'''
    dict.get(key, default=None): 根据key获取对应的value值，如果key不在字典中，则返回default值,返回值生效
    dict.setdefault(key, default=None)：根据key获取对应的value值，如果key不存在字典中，则新增key-default对至原字典，再返回default值
'''
# x1 = dict_demo.get('name')
# print(x1)   # dxj728
# x2 = dict_demo.setdefault('height', 175)
# print(dict_demo)    # {'name': 'dxj728', 'age': 18, 'height': 175}
# print(x2)   # 175


'''dict.update(dict2): 把字典dict2的键/值对更新到dict里, 直接生效'''
# dict_demo.update({'height': 175, 'call': '12345'})
# print(dict_demo)    # {'name': 'dxj728', 'age': 18, 'height': 175, 'call': '12345'}

'''dict.items(): 以列表返回可遍历的(键, 值) 元组数组（迭代器），返回值生效'''
# x3 = dict_demo.items()
# print(list(x3))     # 强制转为列表后：[('name', 'dxj728'), ('age', 18)]

'''
    dict.keys(): 以列表返回一个字典所有的key值, 返回值生效
    dict.values(): 以列表返回字典中的所有的value值，返回值生效
'''
# x4 = dict_demo.keys()
# print(x4)   # ['name', 'age']
# x5 = dict_demo.values()
# print(x5)   # ['dxj728', 18]

'''
    dict.pop(key, default): 删除字典给定键 key 所对应的值，返回值为被删除的值, key未指定时返回default值，直接生效
    dict.popitem(): 随机(伪随机)弹出字典中的一个key-value对，可视为删除，返回弹出的key，value值，直接生效
'''
# x6 = dict_demo.pop('age')
# print(dict_demo)    # {'name': 'dxj728'}
# x7, x8 = dict_demo.popitem()
# print(x7, x8)   # name dxj728
# print(dict_demo)    # {}

'''dict.fromkeys(seq, default=None): 创建一个新字典，序列seq内的值作为key值，value值均统一为default值，返回值生效'''
# x9 = dict.fromkeys([1, 2, 3], 'a')
# print(x9)   # {1: 'a', 2: 'a', 3: 'a'}


'''dict.copy(): 返回一个字典的浅拷贝（一级目录深拷贝，二级目录依然同一引用），返回值生效'''
# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)

# 输出结果
# print(dict1)    # {'user': 'root', 'num': [2, 3]}
# print(dict2)    # {'user': 'root', 'num': [2, 3]}   \\ dict2 = dict1: 被改动完全一致
# print(dict3)    # {'user': 'runoob', 'num': [2, 3]} \\ dict3 = dict1.copy(): user值(一级目录)未受影响，num列表值(二级列表)依然被改动
# print(id(dict1), id(dict2), id(dict3))      # 2463125492984 2463125492984 2463125493784(内存地址1,2相同，3不同)
# print(id(dict1['num']), id(dict2['num']), id(dict3['num']))    # 2341024912392 2341024912392 2341024912392(内存地址相同，浅拷贝)

