import requests

import json
import time
import init


def create_role(self, code, name, namespace, description):
    url = "%s/api/v3/create-role" % init.baseUrl

    payload = json.dumps({
        "code": code,
        "name": name,
        "description": description,
        "namespace": namespace
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

    if response.json()["data"]["statusCode"]["id"]:
        return response.json()["data"]["statusCode"]["id"]
