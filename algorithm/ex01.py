"""
a = [1,2,3,"this is a list"]
b = [4,5,6,"这是第二个列表"]
#a.extend(b)
for i in range(len(b)):
    a.append(b[i])
    print(a)
#print(a)
print(a[0],a[1],a[2],a[2::])
L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0],L[1][1],L[2][2])

website ='http://www.python.com'
b = website[11:17]
print(b)
len_of_python =len('python')
a=website.find('python')
print(a)

em =[1,2]
new_list = [4,5,6]
em.extend(new_list)
#new_em = em + new_list
em.remove(em[1])
em.insert(-1,'999')
print(em)


lista=[]
for i in [[1,2],[3,4],[5,6]]:
    lista.extend(i)
print(lista)

listb=[[1,2],[3,4],[5,6]]
li = [ j for i in listb for j in i]
print(li)




dict_a ={'name':'Hanee','age':12,'city':'shanghai'}
list=[]
for i in dict_a.values():
    list.append(i)
    print(i)
print(list)
"""
name ="奇妙的记忆"

for letter in name:
    print(letter)



