import unittest,requests
'''
url_a ='http://10.43.75.106:12601/sms/sendMessage'
data ={"mobileNo":18721678721,'userName':'ecarx_approver1'}
se=requests.Session()
header = {'token':123456}
res = se.request(method='get',url=url_a,params=data,headers=header)
'''
class LoginTest(unittest.TestCase):
    name= input("loginname")
    def setUp(self):
        return self

    def tearDown(self):
        return self

    def test_login(self):
        if self.name=='admin':
            print("right")
            return self.name
        else:
            print('false')
            return print("name wrong")



L = LoginTest()
L.test_login()
#if __name__=='_main_':


