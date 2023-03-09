import json
import time
import base64
import requests

rootAccount = "root"
rootPassword = "JUOHwvRq6ExdWwyXCWyHYQRwTqy+eN1ZMgtRyn1Nxn5nQmHOQCoF1Ng/EAIRhAzgkrg" \
               "/ezxkAA9JGAa9WrD6LrBFtzmFb0KVMw70jtk4wmnAIaQ8BibbdP0Mlck0ggIM0EGCw6Y8ltpAX9crW3LGW0UAOmqHeuqAGeL" \
               "+kU3qGoI="
rootAppId = "632be09f2c97fc1c48929b66"

import  init


def get_token(account=rootAccount, password=rootPassword, appId=rootAppId):
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
        'x-authing-userpool-id': '59f86b4832eb28071bdd9214',
        'content-type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)

    print(time.time() - begin)
    print(res.json())

    if res.json()['code'] == 200:
        return res.json()["data"]["token"]
