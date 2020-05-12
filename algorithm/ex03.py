'''
y=0
for i in range(101):
    y = y+i
print(y)

a =[5,6,7,9,10,23,45]
b=[]
for i in range(len(a)):
    b.append(a[len(a)-i-1])
print(b)
'''
#随意一个数n=random.randint(0, 20),
# 一个列表test_list = ['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '16']
#如果n出现在列表中，就继续随机，直到这个数不在这个列表中
import random
n = random.randint(0, 20)
test_list = ['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '16']
while str(n) in test_list:
    print('random',n)
    n = random.randint(0, 20)
    continue
else:
    print('no',n)


