import requests

import json
import time
from basic import init


def create_org(name, code, description="", appid=None):
    url = "%s/api/v3/create-permission-namespace/%S" % (init.baseUrl, init.userpoolId)

    payload = json.dumps({
        "name": name,
        "code": code,
        "description": ""
    })

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]