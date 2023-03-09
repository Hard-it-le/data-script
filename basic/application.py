import requests

import json
import time


def create_application(self, name='示例应用', ):
    url = "%s/api/v3/create-application" % self.baseUrl

    payload = json.dumps({
        "appName": name,
        "description": "脚本应用",
    })

    headers = {
        'x-authing-userpool-id': self.userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]["appId"]
