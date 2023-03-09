import requests



import userpool


class dataPermissionResource:

    def __init__(self):
        self.token = ""
        self.userpool = ""
        self.baseUrl = "https://console.authing.cn"

    def get_public_key(self):
        url = 'https://core.authing.cn/api/v2/.well-known'
        res = requests.request("GET", url)
        print(res.json())
        return res.json()["data"]["publicKey"]

    # 获取 root token



if __name__ == '__main__':
    dataPermissionResource.baseUrl = "https://console.wh.authing-inc.co"
    dataPermissionResource.get_public_key()
    get_token = dataPermissionResource.get_token()
    dataPermissionResource.token = get_token
    dataPermissionResource.userpool = dataPermissionResource.create_userpool(name="公有云sss回归")
    dataPermissionResource.create_application()
    namespace_code = dataPermissionResource.create_permission_namespace()
    role_codes = []
    role_ids = []
    for i in range(1, 5):
        role_code = "角色%d" % i
        role_name = "role_name" % i
        role = dataPermissionResource.create_role(code=role_code, name=role_name, namespace=namespace_code)
        role_codes.append(role_code)
        role_ids.append(role)
    string_resource_codes = []
    for i in range(1, 5):
        stringResourceCode = dataPermissionResource.create_data_string_resource()
        string_resource_codes.append(stringResourceCode)

        arrayResourceCode = dataPermissionResource.create_data_array_resource()

        treeResourceCode = dataPermissionResource.create_data_tree_resource()
        userpool.create_userpool()
