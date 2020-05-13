"""
i = 1
count = 0
list_p = []
while i < 11:
    gender = int(input("请输入性别，女请输入1，男请输入2："))
    if gender == 1:
        age = int(input("请输入年龄："))
        if age in range(10, 13):
            print("可以加入球队")
            list_p.append(age)
            count = count + 1
        else:
            print("不可以加入球队")
    else:
        print("请输入下一个：")
    print("已询问次数：", i)
    i = i+1
    print("累计加入球队人数", count, "人。年龄分别是", list_p)
# print("球队总人数：",count,list_p)

student = {'name':'zhaobo','age':22,'hobby':'sing'}
list=[]
for i in student.items():
    list.append(i)
    print(list)

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end='\t')
    print()

# 冒泡排序
a=[1,3,6,9,4,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i],a[j])
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        print(a)
"""












