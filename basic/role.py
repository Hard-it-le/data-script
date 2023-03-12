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


def get_role(code=None, namespaceCode=None):
    url = "%s/api/v3/get-role" % init.baseUrl

    query = {
        "code": code,
        "namespace": namespaceCode
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("GET", url, headers=headers, params=query)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def remove_assign_role(code, namespaceCode, targets):
    url = "%s/api/v3/revoke-role" % init.baseUrl

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


def delete_role(codes=None, namespaceCode=None):
    url = "%s/api/v3/delete-roles-batch" % init.baseUrl

    payload = json.dumps({
        "codeList": codes,
        "namespace": namespaceCode,
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


def create_roles_batch(roles=None):
    url = "%s/api/v3/create-roles-batch" % init.baseUrl

    payload = json.dumps(roles)

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
