import requests

import json
import time
from basic import init



def create_application(name='示例应用', ):
    url = "%s/api/v3/create-application" % init.baseUrl

    payload = json.dumps({
        "appName": name,
        "description": "脚本应用",
    })

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def get_application(appId):
    url = "%s/api/v3/get-application" % init.baseUrl

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    query ={
        "appId": appId
    }
    begin = time.time()
    res = requests.request("GET", url, headers=headers, params=query)
    print(time.time() - begin)
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
