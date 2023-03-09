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


if __name__ == '__main__':
    try:
        init.baseUrl = "https://console.wh.authing-inc.co"
        init.token = admin.get_token()
        print("获取 token 成功")
        userpoolId = userpool.create_userpool(name="d131231223123sad311231223211312231231312321a")["id"]
        print("创建用户池成功")
        init.userpoolId = userpoolId
        app = application.create_application("12312321")
        print(app)
        print("创建应用成功")
        appId = app['appId']
        application.get_application(appId)
        print("根据应用 Id 获取应用成功")
    except IOError as error:
        print(error)
