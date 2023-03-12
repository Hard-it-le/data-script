from basic import init, admin, permission_namespace, user, role
import time

# 手动创建用户池并给公私钥即可
if __name__ == '__main__':
    init.baseUrl = "https://console.wh2.authing-inc.co"
    init.userpoolId = "640d79c230c07f5bd73686aa"
    admin.accessKey = "640d79c230c07f5bd73686aa"
    admin.accessSecret = "c1c1bbae4b5b01c1f770e2809987fa0f"
    init.token = admin.get_userpool_token(admin.accessKey, admin.accessSecret)
    print("获取token成功")
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
