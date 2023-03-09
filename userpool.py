import requests

import json
import time

userpoolType = "B2C"
userpoolName = "示例用户池"


def create_userpool(self, sceneCode=userpoolType, name=userpoolName, userpool="59f86b4832eb28071bdd9214"):
    url = "%s/api/v2/userpools/createWithType" % self.baseUrl

    payload = json.dumps({
        "sceneCode": sceneCode,
        "name": name
    })

    headers = {
        'x-authing-userpool-id': userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res.text)

    if res.json()["code"] == 200:
        return res.json()["data"]["id"]


