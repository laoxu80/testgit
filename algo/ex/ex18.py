# 要求用 filter()函数  求出列表 a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 总所有的奇数并构造新列表


def fun(i):
    return i % 2 == 1


arr = [1, 0, 2, 3, 4, 5, 6, 8]
newarr = filter(fun, arr)
print(list(newarr))
