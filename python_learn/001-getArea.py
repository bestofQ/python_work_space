'''
Author: 凃建强
Date: 2020-08-02 23:19:27
LastEditTime: 2020-08-02 23:38:43
LastEditors: Please set LastEditors
Description: 提取地址中的 省市区
FilePath: \python_work_space\python_work_space\python_learn\001-getArea.py
'''

import cpca

def getArea(address_list):
    # 1、分词模式
    # cpca.transform
    # 输入任意的可迭代类型（如list，pandas的Series类型等），然后将其转换为一个DataFrame
    # pos_sensitive=True 可以确定字符串从那个位置提取
    # 大于-1的部分就代表提取的位置。-1则表明这个字段是靠程序推断出来的，抑或没能提取出来
    df = cpca.transform(address_list)
    print('分词模式')
    print(df)

address_list = '''杭州市滨江区网商路599号
东城区和平里街道
上海市徐汇区 xx 小区'''.split('\n')
getArea(address_list)

def getArea_1(location_str):
    # 全文模式
    # 分词不能确保百分之百分词的正确性
    # --> 引入全文模式，直接进行全文匹配
    print('全文模式')
    df_1 = cpca.transform(location_str)
    print(df_1)
    # lookahead 默认为 8
    df_2 = cpca.transform(location_str, cut=False, lookahead=8)
    print(df_2)
    return df_2

location_str = ["浙江省杭州市下城区青云街40号3楼"]
df = getArea_1(location_str)


# 地图绘制
# 需要 pip install folium
from cpca import drawer
# 模块中还自带一些简单绘图工具，可以在地图上将上面输出的数据以热力图的形式画出来.
drawer.draw_locations(df, 'df.html')