# --coding:utf-8--
# File: TestcaseCopy_test.py
# Author: dxj728
# Time: 2021年07月16日00时
# 说明：

import os, shutil

name_path = r'D:\git\python_test\script_test\1.txt'
testcase_list = []
with open(name_path, 'r', True, 'utf-8') as f1:
    for cur_line in f1.readlines():
        testcase_list.append(cur_line.strip())

file_path = r'D:\git\python_test\script_test\old.py'
name = '8'
for i in range(len(testcase_list)):
    print('cur {}/{}'.format(i + 1, len(testcase_list)))
    
    cur_file_dir = os.path.dirname(file_path)
    new_file_dir = os.path.join(cur_file_dir, 'new_file')
    if not os.path.exists(new_file_dir):
        os.makedirs(new_file_dir)
    new_file = os.path.join(new_file_dir, testcase_list[i] + '.py')
    if os.path.exists(new_file):
        os.remove(new_file)
        print('delete exist file!')
    # shutil.copy(file_path, new_file)
    print('new file : {}'.format(new_file))
    with open(file_path, 'r', True, 'utf-8') as f2:
        with open(new_file, 'w', True, 'utf-8') as f3:
            for cur_line in f2.readlines():
                if name in cur_line:
                    cur_line = cur_line.replace(name, testcase_list[i])
                f3.write(cur_line)
