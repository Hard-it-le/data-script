import json
import time
import requests
from basic import init

rootAccount = "root"
rootPassword = "JUOHwvRq6ExdWwyXCWyHYQRwTqy+eN1ZMgtRyn1Nxn5nQmHOQCoF1Ng/EAIRhAzgkrg" \
               "/ezxkAA9JGAa9WrD6LrBFtzmFb0KVMw70jtk4wmnAIaQ8BibbdP0Mlck0ggIM0EGCw6Y8ltpAX9crW3LGW0UAOmqHeuqAGeL" \
               "+kU3qGoI="
rootAppId = "59f86b4832eb28071bdd9214"

accessKey = ""
accessSecret = ""


def get_root_token(account=rootAccount, password=rootPassword, appId=rootAppId):
    url = "%s/api/v2/login/account" % init.baseUrl
    payload = json.dumps({
        "account": account,
        "password": password,
        "customData": [],
        "autoRegister": True,
        "withCustomData": False
    })
    headers = {
        'x-authing-app-id': appId,
        'x-authing-userpool-id': "59f86b4832eb28071bdd9214",
        'Content-Type': "application/json"
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        res.encoding = 'utf8'
        return print(res.content)
    print(res.json())

    if res.json()['code'] == 200:
        return res.json()["data"]["token"]


def get_userpool_token(accessKey=accessKey, accessSecret=accessSecret):
    url = "%s/api/v3/get-management-token" % init.baseUrl
    payload = json.dumps({
        "accessKeyId": accessKey,
        "accessKeySecret": accessSecret,
    })
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'content-type': 'application/json'
    }

    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()['statusCode'] == 200:
        return res.json()["data"]["access_token"]
