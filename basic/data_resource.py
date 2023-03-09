import requests

import json
import time


def create_data_string_resource(self, namespaceCode, resourceName, resourceCode,
                                actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-string-data-resource" % self.baseurl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
        "actions": actions,
        "description": description
    }
    headers = {
        'x-authing-userpool-id': self.userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)

    begin = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["resourceCode"]


def create_data_array_resource(self, namespaceCode, resourceName, resourceCode,
                               actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-array-data-resource" % self.baseurl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
        "actions": actions,
        "description": description
    }
    headers = {
        'x-authing-userpool-id': self.userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)

    begin = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["resourceCode"]


def create_data_tree_resource(self, namespaceCode, resourceName, resourceCode,
                              actions=["read", "post", "get", "delete", "wirte"], description=""):
    url = "%s/api/v3/create-tree-data-resource" % self.baseurl
    data = {
        "namespaceCode": namespaceCode,
        "resourceName": resourceName,
        "resourceCode": resourceCode,
        "description": description,
        "actions": actions,
        "description": description
    }
    headers = {
        'x-authing-userpool-id': self.userpool,
        'Authorization': self.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)

    begin = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    print(time.time() - begin)
    print(response.text)

    if response.json()["statusCode"] == 200:
        return response.json()["data"]["resourceCode"]
