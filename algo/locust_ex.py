
from locust import TaskSet, HttpUser, task, between
import json

"""
新建一个类，继承TashSet
"""


class LocustGet(TaskSet):
    # 获取商品的列表
    # 装饰器，表示用户的行为，
    @task(1)
    # 定义一个方法
    def get_types(self):
        # 怎么发起get请求呢？在requests里面也有自己的方法
        url = "/admin/login/login"
        self.client.get(url)

class LocustPost(TaskSet):
    @task(1)
    def post_types(self):
        headers = {"content-type":"application/json"}
        params = {"ids":"111"}
        data =json.dump(eval(str(params)))
        data = data.encode("utf-8")
        url = "/admin/api/sys/ad/delete"
        self.client.post(url,data,headers=headers)




# 运行一个Http请求

class HttpRun(HttpUser):

   # tasks = [LocustGet]
    tasks = [LocustPost]

    wait_time = between(1, 5)
   # min_wait = 3000 # 单位毫秒
   # max_wait = 6000

    host = "https://tadmin.daguanlian.com:443"


if __name__=="__main__":
    import os
    os.system("locust -f locust_ex.py HttpRun")



