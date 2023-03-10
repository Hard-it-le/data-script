from basic import init, admin

if __name__ == '__main__':
    try:
        init.baseUrl = "http://console.authing.localhost:3000"
        token = admin.get_root_token()
        init.token = token
        # roleUserPool = userpool.create_userpool(name="角色主体测试")
        # init.userpoolId = roleUserPool["id"]
        # userIds = []
        # targets = []
        # for i in range(1, 11):
        #     username = "user%d" % i
        #     password = "%d" % i
        #     user = user.create_user(username=username, password=password)
        #     userId = user["id"]
        #     userIds.append(userId)
        #     targets.append({
        #         "targetType": "USER",
        #         "targetIdentifier": userId
        #     })
        #
        # permissionNamespaceName = "示例权限空间"
        # permissionNamespaceCode = "examplePermissionNamespace"
        #
        # namespace = permission_namespace.create_permission_namespace(name=permissionNamespaceName,
        #                                                              code=permissionNamespaceCode)
        #
        # namespaceCode = namespace["code"]
        #
        # roleIds = []
        #
        # for i in range(1, 6):
        #     roleName = "角色%d" % i
        #     roleCode = "role%d" % i
        #     role = role.create_role(code=roleCode, name=roleName, namespaceCode=namespaceCode)
        #     roleIds.append(role["id"])
        #     role.assign_role(roleCode, namespaceCode, targets)
    except IOError as error:
        print(error)
