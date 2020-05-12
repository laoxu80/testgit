from unittest import mock

class Login(object):
    pass

def login_succ(user,password):
    pass

llogin =Login()
llogin.loginsucc = mock.Mock(return_value="Success")
print(llogin.loginsucc())

