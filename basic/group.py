import json
import time
import requests
from basic import init


def create_group(name=None, code=None, type="static"):
    url = "%s/api/v3/create-group" % init.baseUrl

    payload = json.dumps({
        "code": code,
        "name": name,
        "type": type
    })

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def get_group(code=None):
    url = "%s/api/v3/get-group" % init.baseUrl
    query = {
        "code": code
    }
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("GET", url, headers=headers, query=query)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def delete_groups(codes=None):
    url = "%s/api/v3/delete-groups_batch" % init.baseUrl
    data = json.dumps({
        "codeList": codes
    })
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=data)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def add_group_user(code=None, userIds=None):
    url = "%s/api/v3/add-group-members" % init.baseUrl
    data = json.dumps({
        "code": code,
        "userIds": userIds
    })
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=data)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def remove_group_user(code=None, userIds=None):
    url = "%s/api/v3/remove-group-members" % init.baseUrl
    data = json.dumps({
        "code": code,
        "userIds": userIds
    })
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=data)
    print(time.time() - begin)
    print(res)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
