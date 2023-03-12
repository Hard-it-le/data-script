import requests

import json
import time
from basic import init


def create_data_string_resource(namespaceCode, resourceName, resourceCode,
                                actions=None, description=""):
    if actions is None:
        actions = ["read", "post", "get", "delete", "wire"]
    url = "%s/api/v3/create-string-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "actions": actions,
        "description": description
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)
    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def create_data_array_resource(namespaceCode, resourceName, resourceCode,
                               actions=None, description=""):
    if actions is None:
        actions = ["read", "post", "get", "delete", "wirte"]
    url = "%s/api/v3/create-array-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "actions": actions,
        "description": description
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)

    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def create_data_tree_resource(namespaceCode, resourceName, resourceCode,
                              actions=None, description=""):
    if actions is None:
        actions = ["read", "post", "get", "delete", "wirte"]
    url = "%s/api/v3/create-tree-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "actions": actions,
        "description": description
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }

    payload = json.dumps(data)

    begin = time.time()
    res = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def get_data_resource(namespaceCode=None, resourceCode=None):
    url = "%s/api/v3/get-data-resource" % init.baseUrl
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }

    query = {
        "namespaceCode": namespaceCode,
        "resourceCode": resourceCode
    }

    begin = time.time()
    res = requests.request("PUT", url, headers=headers, params=query)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def delete_data_resource(namespaceCode=None, resourceCode=None):
    url = "%s/api/v3/delete-data-resource" % init.baseUrl
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    data = {
        "namespaceCode": namespaceCode,
        "resourceCode": resourceCode
    }
    payload = json.dumps(data)
    begin = time.time()
    res = requests.request("PUT", url, headers=headers, data=payload)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def list_data_resources():
    url = "%s/api/v3/list-data-resources" % init.baseUrl
    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    query = {
        "namespaceCode": None,
        "resourceCode": None
    }
    begin = time.time()
    res = requests.request("GET", url, headers=headers, params=query)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
