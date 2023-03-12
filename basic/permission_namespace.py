import requests

import json
import time
from basic import init


def create_permission_namespace(name=None, code=None, description=None, appid=None):
    url = "%s/api/v3/create-permission-namespace" % (init.baseUrl)

    payload = json.dumps({
        "name": name,
        "code": code,
        "description": description
    })

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]

