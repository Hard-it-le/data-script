import requests

import json
import time
from basic import init



def create_role(code, name, namespaceCode, description):
    url = "%s/api/v3/create-role" % init.baseUrl

    payload = json.dumps({
        "code": code,
        "name": name,
        "description": description,
        "namespace": namespaceCode
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

    if response.json()["data"]["statusCode"]:
        return response.json()["data"]["statusCode"]


def assign_role(code, namespaceCode, targets):
    url = "%s/api/v3/assign-role" % init.baseUrl

    payload = json.dumps({
        "code": code,
        "namespace": namespaceCode,
        "targets": targets,
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

    if response.json()["data"]["statusCode"]:
        return response.json()["data"]["statusCode"]
