'''
Author: 凃建强
Date: 2020-08-04 21:00:17
LastEditTime: 2020-08-04 21:05:35
LastEditors: Please set LastEditors
Description: 手动打乱一个列表
FilePath: \python_work_space\python_work_space\python_learn\003-FisherYatesShuffle.py
'''

# 想法
"""
我们可以使用Fisher–Yates shuffle[1] 算法。这个算法的基本思想是：
从列表中任选一个数字，把它跟最后一个数字交换。
从列表索引为0-(n-2)中任选一个数字，把它和倒数第二位交换。
从列表索引为0-(n-3)位中，任选一个数字，把它和倒数第三位交换。
…
从索引为0，1中任选一个数字，把它和索引为1的数字交换。
"""

import random

def shuffle(target):
    # 获取最后一个索引
    # 倒叙操作
    for change in range(len(target) - 1, 0 , -1):
        # 获取 0 - change中的随机数
        lower = random.randint(0, change)
        # 交换
        target[lower], target[change] = target[change], target[lower]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(a)

print(a)