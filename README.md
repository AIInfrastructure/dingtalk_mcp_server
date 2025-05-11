# dingtalk_mcp_server
dingtalk_mcp_server 是钉钉开放接口对应的 MCP Server，让你可以使用大模型轻松操作钉钉。

# 前置条件
1. 在[钉钉开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)创建企业内部应用。
2. 给应用调用所有接口的权限
3. 参考 .env.example 创建 .env 文件，并配置应用的appkey、appsecret

# 配置与使用
## 在 Cursor 中配置
在 .cursor/mcp.json 文件中添加（需要替换成自己的路径）:

```json
{
  "mcpServers": {
    "dingtalk-contacts": {
      "command": "uv",
      "args": ["run", "src/main.py"],
      "env": {}
    }
  }
}
```

## 在 Cline 中配置
在 cline_mcp_settings.json 文件中添加（需要替换成自己的）:

```json
{
  "mcpServers": {
    "mcp-server-alipay": {
      "command": "uv",
      "args": ["run", "src/main.py"],
      "env": {},
      "disable": false,
      "autoApprove": []
    }
  }
}
```

# 调试方法
使用 MCP Inspector 进行调试:

1. 启动Inspector：
```mcp dev src/main.py```
2. 在WebUI中调试

# 支持的能力
|工具名称|描述|
|----|--|
|create_role_group|调用本接口，创建角色组。|
|add_external_contact|调用本接口，添加企业外部联系人。|
|update_or_create_contact_restriction_settings|新增或修改员工、部门、角色限制查看通讯录的设置。|
|set_user_attribute_visibility|设置用户属性可见性。|
|add_roles_for_employees|批量增加员工角色。|
|create_role|调用本接口，创建新角色。|
|search_department_id|搜索部门ID。|
|search_user_id|调用本接口，搜索用户userId。|
|change_dingtalk_id|修改企业账号的钉钉号。|
|authorize_org_account_visibility|授权当前组织的企业账号在加入其他组织后，可在其他组织查看企业账号信息的具体字段 。|
|auth_multi_org_permissions|授权企业帐号可以加入多个组织，只有被授权后企业帐号才能加入外部组织。|
|create_department|调用本接口，创建新部门。|
|create_sso_enterprise_account|调用本接口创建SSO企业账号新用户。|
|create_dingtalk_enterprise_account|调用本接口创建钉钉自建企业账号新用户。|
|delete_department|根据部门ID删除指定部门。|
|delete_user|根据用户的userid删除指定用户。|
|delete_staff_attribute_visibility_setting|调用本接口删除企业员工属性字段可见性设置。|
|delete_external_contact|调用本接口，删除企业外部联系人。|
|delete_contact_hide_setting|删除通讯录隐藏设置。|
|delete_role|根据角色ID删除指定的角色。|
|batch_remove_employee_roles|调用本接口批量删除员工的角色。|
|delete_restricted_contact_setting|根据限制查看通讯录设置ID，执行删除操作。|
|get_user_contact_info|调用本接口获取企业用户通讯录中的个人信息。|
|disable_org_account|调用本接口，停用指定的企业帐号。|
|enable_org_account|启用指定企业帐号。|
|force_logout_org_account|强制登出指定的企业帐号。|
|get_senior_mode_settings|获取用户高管模式设置。|
|get_contact_restrictions_settings|获取通讯录限制可见性设置信息列表。|
|get_department_detail|根据部门ID获取部门详情。|
|invite_other_org_account|调用本接口加入其他组织企业账号进入本组织。|
|get_sub_department_id_list|获取企业部门下的所有直属子部门ID列表。|
|get_auth_scopes|获取通讯录权限范围，调用通讯录相关接口前需要通过此接口确认权限。|
|get_corp_auth_info|调用本接口，获取企业认证信息。|
|get_enterprise_info|调用本接口，获取行业通讯录的企业信息。|
|get_enterprise_invite_info|调用本接口，获取企业的邀请信息。|
|get_department_list|根据部门ID获取下一级部门基础信息。|
|get_external_contact_list|调用本接口，获取企业外部联系人列表。|
|get_employee_list_by_role|获取指定角色的员工列表。|
|get_employee_count|调用本接口获取员工人数。|
|get_user_by_mobile|根据手机号查询企业账号用户。|
|get_role_list|调用本接口，获取角色列表。|
|get_external_contact_label_list|获取企业外部联系人的标签列表。|
|get_department_list|根据部门ID获取行业通讯录部门列表。|
|get_external_contact_details|获取企业外部联系人的详细信息。|
|get_contact_hide_settings|批量获取通讯录隐藏设置信息列表。|
|get_department_user_list|调用本接口，获取部门下的人员列表信息。|
|get_role_group_list|调用本接口，获取角色组信息。|
|get_user_attribute_visibility_settings|调用本接口获取用户属性可见性设置。|
|get_department_user_details|调用本接口获取指定部门中的用户详细信息。|
|get_department_user_detail|获取部门用户详情。|
|get_role_details|根据角色ID获取指定角色详情。|
|get_department_user_details|调用本接口获取指定部门中的用户详细信息。|
|get_user_detail|查询企业账号用户的详细信息。|
|get_inactive_user_list|调用本接口查询指定日期内未登录钉钉的企业员工列表。|
|get_ding_index|调用本接口获取企业最新钉钉指数信息。|
|get_parent_departments_by_user|查询指定用户所属的所有父级部门。|
|get_department_user_base_info|调用本接口获取指定部门的用户基础信息。|
|get_userid_by_unionid|根据unionid获取用户的userid。|
|get_org_account_status|查询某企业帐号的启用状态。|
|get_department_detail|根据部门ID获取指定部门详情。|
|get_admin_scope|调用本接口获取管理员通讯录权限范围。|
|get_admin_list|调用本接口查询管理员列表。|
|get_employee_leave_records|查询企业离职记录列表，包含离职员工的离职日期、手机号码和退出企业方式等信息。|        
|get_parent_departments_by_dept|获取指定部门的所有父部门ID列表。|
|get_department_user_userid_list|调用本接口获取指定部门的userid列表。|
|get_migration_ding_id_by_ding_ids|根据原dingId查询迁移后的dingId。|
|get_ding_id_by_migration_ding_id|根据迁移后的dingId查询原dingId。|
|get_union_id_by_migration_union_ids|根据迁移后的unionId查询原unionId。|
|get_user_detail|调用本接口获取指定用户的详细信息。|
|get_user_by_mobile|根据手机号查询用户，获取用户的userId。|
|set_department_visibility_priority|设置通讯录部门可见性优先级。|
|get_migration_union_id_by_union_ids|根据原unionId查询迁移后的unionId。|
|change_main_administrator|将本组织内某企业账号有所有权的组织，转交给另一企业账号，如果接收的账号不在该组织内则自动加入。|
|update_department|调用本接口更新部门信息。|
|update_contact_hide_settings|新增或更新通讯录隐藏设置。|
|update_enterprise_account_user_info|调用本接口更新指定的企业账号用户信息。|
|update_external_contact|调用本接口，更新企业外部联系人。|
|set_senior_mode|调用本接口设置员工的高管模式。|
|set_role_member_management_scope|设定角色成员管理范围。|
|update_role_name|调用本接口，更新角色名称。|
|create_user|调用本接口创建新用户。|
|update_user_info|调用本接口更新指定的用户信息。|
|get_owned_organizations|查询企业帐号在哪些企业下拥有创建者身份，并获取这些企业信息。|

# 注意事项
- 当前处于发布早期阶段，功能持续完善中
- 妥善保管私钥，防止泄露
