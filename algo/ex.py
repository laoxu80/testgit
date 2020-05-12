#列表

a =[1,2,3,4,5,6,7]
b =[3,4,5,6,7,8,9]
list_a =[1]
print(type(list_a))



#元组
tuple_a = (1,2,3,2,2,4,2,)
tuple_b =('ang',)
#tuple_a.count()
print(tuple_a.count(2))
print(type(tuple_b))

#字典

dict_a = {'name':'Hanee','age':12,'gender':"男"}
dict_a['school']='four'
print(dict_a)
dict_b={}
dict_a.pop('age')
print(dict_b,dict_a)


'''
def jishu(*args):
    li=[]
    for n in (args):
        if n%2==1:
            li.append(n)
    return li
print(jishu(9,10,11,24,34,52,12,13,25))
'''

