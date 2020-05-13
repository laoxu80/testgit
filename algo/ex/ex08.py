"""
def favorite_book(bookname):
    print("我最喜欢的图书是{}".format(bookname))
favorite_book("english")

-------------------------------------------------------
实现功能：输入两个数字A、B，A为1-9的数字，B为>0的正整数。
如:输入 3， 2 则计算 3  33  的总和，即 36
   输入 1 ，3 则计算 1  11   111 的总和，即 123

def cal(a, b):
    a = int(a)
    b = int(b)
    new_a = ""
    sum_a = 0
    for i in range(1,b+1):
        new_a = str(a)+new_a
        sum_a = int(new_a) + sum_a
        print(new_a,sum_a)
    return print('总和是：', sum_a)


str_a = input("输入1-9的数字")
str_b = input('输入>0的数字')
cal(str_a, str_b)
--------------------------------------------------------
"""

def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return print(arr)

selectionSort([12,34,2,42,31,25])



