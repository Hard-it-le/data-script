import requests

import json
import time
import  init


def create_permission_namespace(name, code, description="", appid=None):
    url = "%s/api/v3/create-permission-namespace/%S" % (init.baseurl, init.userpool)

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
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["code"]
