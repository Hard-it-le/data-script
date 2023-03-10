import requests

import admin
import application
import init
import userpool


class dataPermissionResource:

    def get_public_key(self):
        url = 'https://core.authing.cn/api/v2/.well-known'
        res = requests.request("GET", url)
        print(res.json())
        return res.json()["data"]["publicKey"]

