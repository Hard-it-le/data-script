import requests

import json
import time


def create_role(self, code, name, namespace, description):
    url = "%s/api/v3/create-role" % self.baseurl

    payload = json.dumps({
        "code": code,
        "name": name,
        "description": description,
        "namespace": namespace
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

    if response.json()["data"]["statusCode"]["id"]:
        return response.json()["data"]["statusCode"]["id"]
