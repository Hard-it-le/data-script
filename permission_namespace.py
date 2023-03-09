import requests

import json
import time


def create_permission_namespace(self, name, code, description="", appid=None):
    url = "%s/api/v3/create-permission-namespace/%S" % (self.baseurl, self.userpool)

    payload = json.dumps({
        "name": name,
        "code": code,
        "description": ""
    })
    headers = {
        'x-authing-userpool-id': self.userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["code"]
