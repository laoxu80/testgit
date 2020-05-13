import requests
import json

class LoginToken:
    def __init__(self,loginname,password,smscode=""):
        self.loginname = loginname
        self.password = password
        self.smscode = smscode

    def login_param(self):
        return {'loginName': self.loginname, "password": self.password, "smsCode": self.smscode}

    def login_token(self):
        url_login = "https://tadmin.daguanlian.com/admin/login/login"
        #login_param = {'loginName': "admin", "password": 111111, "smsCode": ""}
        res_token = requests.get(url_login, self.login_param())
        token_dict = json.loads(res_token.text)
        return token_dict['data']['token']


if __name__ == "__main__":
    admin = LoginToken("admin",111111)
    print(admin.login_token())


"""
url_dgl = "https://tadmin.daguanlian.com/admin/api/sys/ad/getAdPositions"
headers_dgl = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NUb2tlblByZWZpeCI6IjhNdndlaGQrdkVRZVlwUFZiNWpKNGJwbUlnbWZlYkg4S2NIQzB4ekhOelk9IiwiZXhwIjoxNTg2MjI3MzExLCJ1c2VySWQiOiJDcXVYK1JNOGZVcldDRDdHWUlpOFo2T0Qrd0VHc1phSiIsImN1cnJlbnRUaW1lUHJlZml4IjoiOE12d2VoZCt2RVRyUy9rTGMrL3NlZWh5TkxmdHd2VFlkUjlEMWhzb3hmOD0ifQ.DhKkIwCHIPnl8Os1OoYZAilkEqGYhrDPNuA85M0Cj_Q"}

res = requests.get(url_dgl,headers=headers_dgl)
res_dict = json.loads(res.text)
print(type(res_dict['data']))
for i in res_dict.keys():
    print(i,res_dict[i])
"""





