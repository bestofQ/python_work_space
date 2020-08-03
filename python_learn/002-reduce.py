'''
Author: 凃建强
Date: 2020-08-03 20:39:35
LastEditTime: 2020-08-03 20:52:10
LastEditors: Please set LastEditors
Description: 一日一技：使用异或寻找两个孤独的数
FilePath: \python_work_space\python_work_space\python_learn\002-reduce.py
'''

from functools import reduce

# 1、讲述一下reduce的使用方法
# reduce(function, iterable[, initializer])
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
# eg
# def add(x, y) :            # 两数相加
#      return x + y
# reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5

def calc_xor(x, y):
    return x ^ y

def find_the_most_right_bit_1(num):
    '''
    寻找数字 num 对应的二进制数里面，最右侧的1所在的位置
    例如对于二进制数10110100,只有当它与100做与运算时，返回
    的值才会是100本身
    '''
    if num == 0:
        return 0
    check_bit = 1
    while True:
        # 二进制数10110100，一开始 check_bit为1，两数相与，结果为0。
        # 然后1 << 1为二进制10，跟10110100 & 10 != 10，
        # 再左移一位，10 << 1 == 100。此时10110100 & 100 == 100于是返回
        if num & check_bit == check_bit:
            return check_bit
        check_bit = check_bit << 1
        print(check_bit)

def find_two_unique_num(target):
    if not target:
        raise Exception('输入的列表为空')
    xor_of_two = reduce(calc_xor, target)
    check_bit = find_the_most_right_bit_1(xor_of_two)
    group_1 = []
    group_2 = []
    for num in target:
        if num & check_bit == check_bit:
            group_1.append(num)
        else:
            group_2.append(num)
    unique_num_1 = reduce(calc_xor, group_1)
    unique_num_2 = reduce(calc_xor, group_2)
    return unique_num_1, unique_num_2

res = find_two_unique_num([1, 1, 2, 2, 6, 8, 8, 12, 24, 24])
print(res)
