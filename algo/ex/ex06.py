"""
class GreetingLogin:

    @staticmethod
    def login_success():
        user = input("请输入用户名")
        if user == 'admin':
            print("用户名正确，登录成功")
        else:
            print("用户名不正确，登录失败,您输入的用户名是：", user)

GreetingLogin.login_success()

# 函数


def add_min(a, b, c):
    d = a+b-c
    return d


y = add_min(a=4, c=3, b=2)
print(y)
"""
class A:


    def hello(self):
        print("it is A")

class B(A):

    def hello(self):
        print('it is B')

a1 =B()
super(a1.__class__,a1).hello()









