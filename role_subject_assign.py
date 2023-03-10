from basic import init, admin, userpool, permission_namespace, user, role
import time

# 创用户池并创建应用等基本操作
if __name__ == '__main__':
    try:
        init.baseUrl = "https://console.wh2.authing-inc.co"
        token = admin.get_root_token()
        init.token = token
        roleUserPool = userpool.create_userpool(name="角色主体测试")
        init.userpoolId = roleUserPool["id"]
        userIds = []
        targets = []
        for i in range(1, 11):
            username = "user%d" % i
            password = "%d" % i
            roleUser = user.create_user(username=username, password=password)
            time.sleep(1)
            userId = roleUser["userId"]
            userIds.append(userId)
            targets.append({
                "targetType": "USER",
                "targetIdentifier": userId
            })

        print(targets)

        permissionNamespaceName = "示例权限空间"
        permissionNamespaceCode = "examplePermissionNamespace"

        namespace = permission_namespace.create_permission_namespace(name=permissionNamespaceName,
                                                                     code=permissionNamespaceCode,
                                                                     description=permissionNamespaceName)

        namespaceCode = namespace["code"]

        roleIds = []
        roleCodes = []

        for i in range(1, 6):
            roleCode = "role%d" % i
            roleName = "角色%d" % i
            testRole = role.create_role(code=roleCode, name=roleName, namespaceCode=namespaceCode, description=roleName)
            roleIds.append(testRole["id"])
            roleCodes.append(testRole["code"])
            assignRole = role.assign_role(roleCode, namespaceCode, targets)
            time.sleep(5)
            if assignRole:
                print("角色授权成功")
            else:
                print("角色授权失败")
        print("脚本生成成功")



    except IOError as error:
        print(error)
