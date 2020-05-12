"""
def make_shirt(size):
    #size = input("请输入尺码和内容：")
    print("size&content is:",size)

make_shirt(20)

def describe_city(city,country):
    print(city,'is in ',country)  

describe_city(input('请输入城市'),input('请输入国家'))

def print_info():
    print("本章学的是函数")
print_info()


def interview(name):
    if name =='laoxu':
        print(name)
        return name
    return print("error")

a = interview('jioner')

b = interview('laoxu')
"""
def eating(d,**kwargs):
    print(d)
    print(kwargs)



ars=(1,2,3)
more = {'d':'houzi', 'a':'meimei'}

eating(**more)