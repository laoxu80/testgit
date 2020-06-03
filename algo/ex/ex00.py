'''
astr='aabbcdbaaabc'
for i in range(len(astr)):
    astr=astr.replace('ab','')
print('new:',astr)


strh='hello'
name = 'world'

print('hello %s' % name)
print('Hello {}{}'.format(name, strh))



strb='abbccddabs'
dict_b={}
for i in range(len(strb)):
    y = strb[i]
    if y not in dict_b.keys():
        dict_b[y] = 1
        #print(dict_b)
    else:
        dict_b[y] = dict_b[y]+1
print(dict_b)

print(sum(range(1,10,2)))
#1+3+5+7+9=25


def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleSort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                arr[i],arr[j]=arr[j],arr[i]



arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort2(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])
'''


nums_a = [2, 7, 11, 15]
dict_a = list(enumerate(nums_a))
print(dict_a)




















