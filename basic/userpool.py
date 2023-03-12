import requests

import json
import time
from basic import init

userpoolType = "B2C"
userpoolName = "示例用户池"


def create_userpool(sceneCode=userpoolType, name=userpoolName, userpool="59f86b4832eb28071bdd9214"):
    url = "%s/api/v2/userpools/createWithType" % init.baseUrl

    payload = json.dumps({
        "sceneCode": sceneCode,
        "name": name
    })

    headers = {
        'x-authing-userpool-id': userpool,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return print(res.content)
    print(res.json())

    if res.json()["code"] == 200:
        return res.json()["data"]
