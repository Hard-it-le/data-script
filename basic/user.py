import requests

import json
import time

from basic import init


def create_user(username=None, password=None, email=None, phone=None):
    url = "%s/api/v3/create-user" % init.baseUrl
    data = {
        "username": username,
        "password": password,
        "email": "",
        "phone": ""
    }

    if username:
        data["username"] = username
    if phone:
        data["phone"] = phone
    if email:
        data["email"] = email

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
