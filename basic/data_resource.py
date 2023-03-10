import requests

import json
import time
from basic import init


def create_data_string_resource(namespaceCode, resourceName, resourceCode,
                                actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-string-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
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
        return res.json()["data"]["resourceCode"]


def create_data_array_resource(namespaceCode, resourceName, resourceCode,
                               actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-array-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
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
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["resourceCode"]


def create_data_tree_resource(namespaceCode, resourceName, resourceCode,
                              actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-tree-data-resource" % init.baseUrl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
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
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["resourceCode"]
