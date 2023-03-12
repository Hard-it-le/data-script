import requests

import json
import time
from basic import init


def create_data_policy(policyName, statementList, ):
    url = "%s/api/v3/create-data-policy" % init.baseUrl
    data = {
        "policyName": policyName,
        "statementList": statementList,
        "description": policyName,
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)
    begin = time.time()

    res = requests.request('POST', url, data=payload, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def delete_data_policy(policyId):
    url = "%s/api/v3/delete-data-policy" % init.baseUrl
    data = {
        "policyId": policyId,
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(data)
    begin = time.time()
    res = requests.request('POST', url, data=payload, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()


def get_data_policy(policyId):
    url = "%s/api/v3/get-data-policy" % init.baseUrl
    query = {
        "policyId": policyId,
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request('GET', url, params=query, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def list_data_policy_targets(policyId):
    url = "%s/api/v3/list-data-policy-targets" % init.baseUrl
    query = {
        "policyId": policyId,
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    res = requests.request('GET', url, params=query, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def authorize_data_policies(policyIds, targetList):
    url = "%s/api/v3/authorize-data-policies" % init.baseUrl
    data = {
        "policyIds": policyIds,
        "targetList": targetList
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    payload = json.dumps(data)
    res = requests.request('POST', url, data=payload, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]


def revoke_data_policy(policyId , targetIdentifier, targetType):
    url = "%s/api/v3/revoke-data-policy" % init.baseUrl
    data = {
        "policyId": policyId,
        "targetIdentifier": targetIdentifier,
        "targetType": targetType
    }

    headers = {
        'x-authing-userpool-id': init.userpoolId,
        'Authorization': init.token,
        'Content-Type': 'application/json'
    }
    begin = time.time()
    payload = json.dumps(data)
    res = requests.request('POST', url, data=payload, headers=headers)
    print(time.time() - begin)
    if res.status_code != 200:
        return res
    print(res.json())

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
