import requests

import json
import time
from basic import init



def create_data_policy():
    url = "%s/api/v3/create-data-policy" + init.baseUrl
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

    res = requests.request('POST', url, data=payload, headers=headers)
    print(time.time() - begin)
    print(res.text)

    if res.json()["statusCode"] == 200:
        return res.json()["data"]
