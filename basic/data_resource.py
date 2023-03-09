import requests

import json
import time
import init


def create_data_string_resource(namespaceCode, resourceName, resourceCode,
                                actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-string-data-resource" % init.baseurl
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


def create_data_array_resource(namespaceCode, resourceName, resourceCode,
                               actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-array-data-resource" % init.baseurl
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
    url = "%s/api/v3/create-tree-data-resource" % init.baseurl
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
