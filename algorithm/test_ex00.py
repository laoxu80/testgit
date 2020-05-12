"""
面试题

# 1,一行代码实现1-100的和
sum_a = sum(range(1,101))
print(sum_a)

# 2, 如何在函数内部修改一个全部变量
a =6
def fn():
    global a
    a=4
fn()
print(a)

#import sys,os,datetime,calendar,math,keyword,pytest,re
# 3,列出5个python的标准库
os
re
sys
calendar
math

# 4,字典如何删除键和合并两个字典
dict_a ={'a':123,'b':234}
del dict_a['a']
print(dict_a)
dict_b ={'c':876}
dict_a.update(dict_b)
print(dict_a)

# 5,列表去重
list_a=[1,2,3,1,4,2,5]
set_a = set(list_a)
print(set_a)
print([x for x in set_a])

# 6,
list = [1,2,3,4,5]
def fn(x):
    return x**2
res=map(fn,list)
print(type(res))
print([i for i in res if i >10])
"""
import random
import numpy as np
int_a = random.randint(1,10)
print(int_a)


