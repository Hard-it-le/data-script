import requests

import json
import time
from basic import init


def create_role(code=None, name=None, namespaceCode=None, description=None):
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
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


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
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
