import asyncio
from typing import Any, List, Optional

from mcp import stdio_server
from mcp.server import Server as MCPServer
import mcp.types as types

from dingtalk.dingtalk_server import DingtalkServer

class DingtalkContactsServer(DingtalkServer):
    def __init__(self):
        super().__init__()

    async def create_role_group(self, name: str) -> str:
        """
        创建角色组.

        args:
            name (str): 角色组名称
        """
        url = "https://oapi.dingtalk.com/role/add_role_group"
        data = {
            "name": name
        }
        return await self.post_old(url, json=data)


    async def add_external_contact_old(self, contact: dict) -> str:
        """
        添加企业外部联系人.

        args:
            contact (dict): 外部联系人信息，包含以下字段：
                - title (str, 可选): 职位。
                - label_ids (list[int], 必填): 标签列表。
                - share_dept_ids (list[int], 可选): 共享给的部门ID列表。
                - address (str, 可选): 地址。
                - remark (str, 可选): 备注。
                - follower_user_id (str, 必填): 负责人的userId。
                - name (str, 必填): 外部联系人的姓名。
                - state_code (str, 必填): 手机号国家码。
                - company_name (str, 可选): 外部联系人的企业名称。
                - share_user_ids (list[str], 可选): 共享给的员工userid列表。
                - mobile (str, 必填): 外部联系人的手机号。
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/create"
        data = {"contact": contact}
        return await self.post_old(url, json=data)


    async def update_contact_restriction_settings(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        subjectUserIds: Optional[List[str]] = None,
        subjectDeptIds: Optional[List[int]] = None,
        subjectTagIds: Optional[List[int]] = None,
        type: str = "excludeNode",
        excludeUserIds: Optional[List[str]] = None,
        excludeDeptIds: Optional[List[int]] = None,
        excludeTagIds: Optional[List[int]] = None,
        active: Optional[bool] = None,
        restrictInUserProfile: Optional[bool] = None,
        restrictInSearch: Optional[bool] = None
    ) -> str:
        """
        新增或修改限制查看通讯录设置.
        """
        url = "https://api.dingtalk.com/v1.0/contact/restrictions/settings"
        data = {
            "id": id,
            "name": name,
            "description": description,
            "subjectUserIds": subjectUserIds,
            "subjectDeptIds": subjectDeptIds,
            "subjectTagIds": subjectTagIds,
            "type": type,
            "excludeUserIds": excludeUserIds,
            "excludeDeptIds": excludeDeptIds,
            "excludeTagIds": excludeTagIds,
            "active": active,
            "restrictInUserProfile": restrictInUserProfile,
            "restrictInSearch": restrictInSearch
        }
        # Remove None values to avoid sending unnecessary fields
        data = {k: v for k, v in data.items() if v is not None}
        return await self.put_new(url, json=data)


    async def set_user_attribute_visibility(self, id: int = None, name: str = None, description: str = None, 
                                            objectStaffIds: list = None, objectDeptIds: list = None, 
                                            objectTagIds: list = None, hideFields: list = None, 
                                            excludeStaffIds: list = None, excludeDeptIds: list = None, 
                                            excludeTagIds: list = None, active: bool = None) -> str:
        """
        设置用户属性可见性.

        args:
            id (int, optional): 设置ID。新增时为空，修改时为需要修改的ID。
            name (str, optional): 设置的名称。
            description (str, optional): 设置的描述信息。
            objectStaffIds (list, optional): 需要隐藏字段的员工userId列表。
            objectDeptIds (list, optional): 需要隐藏字段的部门deptId列表。
            objectTagIds (list, optional): 需要隐藏字段的角色roleId列表。
            hideFields (list, optional): 需要隐藏的用户属性ID列表。
            excludeStaffIds (list, optional): 可见隐藏字段的员工userId列表。
            excludeDeptIds (list, optional): 可见隐藏字段的部门deptId列表。
            excludeTagIds (list, optional): 可见隐藏字段的角色roleId列表。
            active (bool, optional): 是否生效。
        """
        url = "https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings"
        data = {
            "id": id,
            "name": name,
            "description": description,
            "objectStaffIds": objectStaffIds,
            "objectDeptIds": objectDeptIds,
            "objectTagIds": objectTagIds,
            "hideFields": hideFields,
            "excludeStaffIds": excludeStaffIds,
            "excludeDeptIds": excludeDeptIds,
            "excludeTagIds": excludeTagIds,
            "active": active
        }
        return await self.post_new(url, json=data)


    async def add_roles_for_employees(self, roleIds: str, userIds: str) -> str:
        """
        批量增加员工角色.

        args:
            roleIds (str): 角色roleId列表，多个roleId用英文逗号（,）分隔，最多可传20个。
            userIds (str): 员工的userId列表，多个userId用英文逗号（,）分隔，最多可传20个。
        """
        url = "https://oapi.dingtalk.com/topapi/role/addrolesforemps"
        data = {
            "roleIds": roleIds,
            "userIds": userIds
        }
        return await self.post_old(url, json=data)


    async def create_role(self, roleName: str, groupId: int) -> str:
        """
        创建新角色.

        args:
            roleName (str): 角色名称
            groupId (int): 角色组ID
        """
        url = "https://oapi.dingtalk.com/role/add_role"
        data = {
            "roleName": roleName,
            "groupId": groupId
        }
        return await self.post_old(url, json=data)


    async def search_department_id(self, queryWord: str, offset: int, size: int) -> str:
        """
        搜索部门ID.

        args:
            queryWord (str): 部门名称或者部门名称拼音。
            offset (int): 分页页码。
            size (int): 分页大小。
        """
        url = "https://api.dingtalk.com/v1.0/contact/departments/search"
        data = {
            "queryWord": queryWord,
            "offset": offset,
            "size": size
        }
        return await self.post_new(url, json=data)


    async def search_user_id(self, queryWord: str, offset: int, size: int, fullMatchField: int = None) -> str:
        """
        搜索用户userId.

        args:
            queryWord (str): 用户名称、名称拼音或英文名称。
            offset (int): 分页页码。
            size (int): 分页大小。
            fullMatchField (int, optional): 是否精确匹配。1 表示精确匹配用户名称，默认为模糊匹配。
        """
        url = "https://api.dingtalk.com/v1.0/contact/users/search"
        data = {
            "queryWord": queryWord,
            "offset": offset,
            "size": size,
        }
        if fullMatchField is not None:
            data["fullMatchField"] = fullMatchField
        return await self.post_new(url, json=data)


    async def change_dingtalk_id(self, userId: str, dingTalkId: str) -> str:
        """
        修改企业账号的钉钉号.

        args:
            userId (str): 员工userId，只支持归属于本企业的企业账号userId。
            dingTalkId (str): 新的钉钉号。格式要求：
                            - 6<=长度<=20
                            - 字母开头
                            - 只包含字母、数字
                            - 不能包含违禁内容
        """
        url = "https://api.dingtalk.com/v1.0/contact/orgAccounts/dingTalkIds/change"
        data = {
            "userId": userId,
            "dingTalkId": dingTalkId
        }
        return await self.post_new(url, json=data)


    async def authorize_org_account_visibility(self, toCorpIds: list, optUserId: str, fields: list = None) -> str:
        """
        授权其他组织查看本组织的企业账号信息.

        args:
            toCorpIds (list): 被授权组织对应corpId列表。
            optUserId (str): 当前调用接口的调用者对应userId。
            fields (list, optional): 授权字段，可选值为mobile和status。默认为None。
        """
        url = "https://oapi.dingtalk.com/v1.0/contact/orgAccounts/mobiles/visibleInOtherOrg"
        data = {
            "toCorpIds": toCorpIds,
            "optUserId": optUserId,
            "fields": fields if fields else []
        }
        return await self.put_new(url, json=data)


    async def authorize_multi_org_permissions(self, joinCorpId: str, grantDeptIdList: list = None) -> str:
        """
        授权企业帐号可加入多组织.

        args:
            joinCorpId (str): 被授权的组织CorpId。
            grantDeptIdList (list): 授权的部门列表，可选。如果不传，授权整个企业。
        """
        url = "https://api.dingtalk.com/v1.0/contact/orgAccounts/multiOrgPermissions/auth"
        data = {
            "joinCorpId": joinCorpId,
            "grantDeptIdList": grantDeptIdList if grantDeptIdList else []
        }
        return await self.post_new(url, json=data)


    async def create_department_old(self, name: str, parent_id: int, hide_dept: bool = None, dept_permits: str = None, user_permits: str = None, outer_dept: bool = None, outer_dept_only_self: bool = None, outer_permit_users: str = None, outer_permit_depts: str = None, create_dept_group: bool = None, auto_approve_apply: bool = None, order: int = None, source_identifier: str = None, code: str = None) -> str:
        """
        创建部门（旧版SDK）.

        args:
            name (str): 部门名称，长度限制为1~64个字符，不允许包含字符"-"","以及","。
            parent_id (int): 父部门ID，根部门ID为1。
            hide_dept (bool, optional): 是否隐藏本部门。默认为None。
            dept_permits (str, optional): 指定可以查看本部门的其他部门列表，总数不能超过50。默认为None。
            user_permits (str, optional): 指定可以查看本部门的人员userId列表，总数不能超过50。默认为None。
            outer_dept (bool, optional): 是否限制本部门成员查看通讯录。默认为None。
            outer_dept_only_self (bool, optional): 本部门成员是否只能看到所在部门及下级部门通讯录。默认为None。
            outer_permit_users (str, optional): 指定本部门成员可查看的通讯录用户userId列表，总数不能超过50。默认为None。
            outer_permit_depts (str, optional): 指定本部门成员可查看的通讯录部门ID列表，总数不能超过50。默认为None。
            create_dept_group (bool, optional): 是否创建一个关联此部门的企业群，默认为False即不创建。默认为None。
            auto_approve_apply (bool, optional): 是否默认同意加入该部门的申请。默认为None。
            order (int, optional): 在父部门中的排序值，order值小的排序靠前。默认为None。
            source_identifier (str, optional): 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。默认为None。
            code (str, optional): 部门编码。默认为None。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/create"
        data = {
            "name": name,
            "parent_id": parent_id,
            "hide_dept": hide_dept,
            "dept_permits": dept_permits,
            "user_permits": user_permits,
            "outer_dept": outer_dept,
            "outer_dept_only_self": outer_dept_only_self,
            "outer_permit_users": outer_permit_users,
            "outer_permit_depts": outer_permit_depts,
            "create_dept_group": create_dept_group,
            "auto_approve_apply": auto_approve_apply,
            "order": order,
            "source_identifier": source_identifier,
            "code": code
        }
        return await self.post_old(url, json=data)


    async def create_sso_user(self, name: str, dept_id_list: str, userid: str = None,  
                            exclusive_account: bool = True, exclusive_account_type: str = "sso", 
                            telephone: str = None, job_number: str = None, title: str = None, 
                            email: str = None, org_email: str = None, org_email_type: str = None, 
                            work_place: str = None, remark: str = None, dept_order_list: list = None, 
                            dept_title_list: list = None, extension: str = None, senior_mode: bool = False, 
                            hired_date: int = None, manager_userid: str = None, exclusive_mobile: str = None, 
                            avatar_media_id: str = None, nickname: str = None) -> str:
        """
        创建SSO企业账号新用户.

        args:
            userid (str): 员工唯一标识ID（不可修改），长度为1~64个字符。如果不传，将自动生成一个userid。
            name (str): 员工名称，长度最大80个字符。
            dept_id_list (str): 所属部门ID列表，多个部门ID使用英文逗号隔开，每次调用最多传100个部门ID。
            exclusive_account (bool): 必须填true，表示要创建企业账号。
            exclusive_account_type (str): 必须填sso，表示SSO企业账号。
            telephone (str): 分机号，长度最大50个字符。
            job_number (str): 员工工号，长度最大为50个字符。
            title (str): 职位，长度最大为200个字符。
            email (str): 员工个人邮箱，长度最大50个字符。
            org_email (str): 员工的企业邮箱，长度最大100个字符。
            org_email_type (str): 员工的企业邮箱类型：profession（标准版）或base（基础版）。
            work_place (str): 办公地点，长度最大100个字符。
            remark (str): 备注，长度最大2000个字符。
            dept_order_list (list): 员工在对应的部门中的排序。
            dept_title_list (list): 员工在对应的部门中的职位。
            extension (str): 扩展属性，可以设置多种属性，最大长度2000个字符。
            senior_mode (bool): 是否开启高管模式，默认值false。
            hired_date (int): 入职时间，Unix时间戳，单位毫秒。
            manager_userid (str): 直属主管的userId。
            exclusive_mobile (str): 企业账号手机号。
            avatar_media_id (str): 创建本组织企业账号时可指定头像MediaId，只支持jpg/png。
            nickname (str): 创建本组织企业账号时可指定昵称。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/create"
        data = {
            "userid": userid,
            "name": name,
            "dept_id_list": dept_id_list,
            "exclusive_account": exclusive_account,
            "exclusive_account_type": exclusive_account_type,
            "telephone": telephone,
            "job_number": job_number,
            "title": title,
            "email": email,
            "org_email": org_email,
            "org_email_type": org_email_type,
            "work_place": work_place,
            "remark": remark,
            "dept_order_list": dept_order_list,
            "dept_title_list": dept_title_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "manager_userid": manager_userid,
            "exclusive_mobile": exclusive_mobile,
            "avatarMediaId": avatar_media_id,
            "nickname": nickname
        }
        return await self.post_old(url, json=data)


    async def create_dingtalk_enterprise_account(self, userid: str = None, login_id: str = None, init_password: str = None, name: str = None, dept_id_list: str = None, telephone: str = None, job_number: str = None, title: str = None, email: str = None, org_email: str = None, org_email_type: str = None, work_place: str = None, remark: str = None, dept_order_list: list = None, dept_title_list: list = None, extension: str = None, senior_mode: bool = None, hired_date: int = None, manager_userid: str = None, exclusive_mobile: str = None, avatar_media_id: str = None, nickname: str = None) -> str:
        """
        创建钉钉自建企业账号新用户.

        args:
            userid (str, optional): 员工唯一标识ID，长度为1~64个字符。如果不传，将自动生成一个userid。
            login_id (str): 钉钉自建企业账号的登录名。
            init_password (str): 钉钉自建企业账号的初始密码，至少8个字符，不能全是字母或数字。
            name (str): 员工名称，长度最大80个字符。
            dept_id_list (str): 所属部门ID列表，多个部门ID使用英文逗号隔开，最多传100个部门ID。
            telephone (str, optional): 分机号，长度最大50个字符。
            job_number (str, optional): 员工工号，长度最大50个字符。
            title (str, optional): 职位，长度最大200个字符。
            email (str, optional): 员工个人邮箱，长度最大50个字符。
            org_email (str, optional): 员工的企业邮箱，长度最大100个字符。
            org_email_type (str, optional): 员工的企业邮箱类型，可选值：profession（标准版）、base（基础版）。
            work_place (str, optional): 办公地点，长度最大100个字符。
            remark (str, optional): 备注，长度最大2000个字符。
            dept_order_list (list, optional): 员工在对应部门中的排序。
            dept_title_list (list, optional): 员工在对应部门中的职位。
            extension (str, optional): 扩展属性，最大长度2000个字符。
            senior_mode (bool, optional): 是否开启高管模式，默认值false。
            hired_date (int, optional): 入职时间，Unix时间戳，单位毫秒。
            manager_userid (str, optional): 直属主管的userid。
            exclusive_mobile (str, optional): 企业账号手机号。
            avatar_media_id (str, optional): 头像MediaId，仅支持jpg/png格式。
            nickname (str, optional): 昵称。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/create"
        data = {
            "userid": userid,
            "exclusive_account": True,
            "exclusive_account_type": "dingtalk",
            "login_id": login_id,
            "init_password": init_password,
            "name": name,
            "dept_id_list": dept_id_list,
            "telephone": telephone,
            "job_number": job_number,
            "title": title,
            "email": email,
            "org_email": org_email,
            "org_email_type": org_email_type,
            "work_place": work_place,
            "remark": remark,
            "dept_order_list": dept_order_list,
            "dept_title_list": dept_title_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "manager_userid": manager_userid,
            "exclusive_mobile": exclusive_mobile,
            "avatarMediaId": avatar_media_id,
            "nickname": nickname
        }
        return await self.post_old(url, json=data)


    async def delete_department_old(self, dept_id: int) -> str:
        """
        删除部门.

        args:
            dept_id (int): 要删除的部门ID
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/delete"
        data = {"dept_id": dept_id}
        return await self.post_old(url, json=data)


    async def delete_user(self, userid: str) -> str:
        """
        删除用户.

        args:
            userid (str): 员工的userid
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/delete"
        data = {"userid": userid}
        return await self.post_old(url, json=data)


    async def delete_staff_attribute_visibility_setting(self, settingId: int) -> str:
        """
        删除企业员工属性字段可见性设置.

        args:
            settingId (int): 设置的ID，可通过获取用户属性可见性设置接口获取id参数值。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings/{settingId}"
        return await self.delete_new(url)


    async def delete_external_contact(self, user_id: str) -> str:
        """
        删除企业外部联系人.

        args:
            user_id (str): 要删除的外部联系人的userId
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/delete"
        data = {
            "user_id": user_id
        }
        return await self.post_old(url, json=data)


    async def delete_contact_hide_setting(self, settingId: int) -> str:
        """
        删除通讯录隐藏设置.

        args:
            settingId (int): 设置ID，可通过获取通讯录隐藏设置接口获得id参数值。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/contactHideSettings/{settingId}"
        return await self.delete_new(url)


    async def delete_role(self, role_id: int) -> str:
        """
        删除角色.

        args:
            role_id (int): 要删除的角色ID
        """
        url = "https://oapi.dingtalk.com/topapi/role/deleterole"
        data = {"role_id": role_id}
        return await self.post_old(url, json=data)


    async def remove_roles_for_employees(self, roleIds: str, userIds: str) -> str:
        """
        批量删除员工角色.

        args:
            roleIds (str): 角色ID列表，多个roleId用英文逗号（,）分隔。
            userIds (str): 员工userid列表，多个userId用英文逗号（,）分隔。
        """
        url = "https://oapi.dingtalk.com/topapi/role/removerolesforemps"
        data = {
            "roleIds": roleIds,
            "userIds": userIds
        }
        return await self.post_old(url, json=data)


    async def delete_restricted_contact_setting(self, settingId: str) -> str:
        """
        删除限制查看通讯录设置.

        args:
            settingId (str): 限制查看通讯录设置ID
        """
        url = "https://oapi.dingtalk.com/v1.0/contact/restrictions/settings/delete"
        data = {"settingId": settingId}
        return await self.post_new(url, json=data)


    async def get_user_contact_info(self, unionId: str) -> str:
        """
        获取用户通讯录个人信息.

        args:
            unionId (str): 用户的unionId，传入me表示当前授权人。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/users/{unionId}"
        return await self.get_new(url)


    async def disable_org_account(self, userId: str, reason: str = None) -> str:
        """
        停用企业帐号.

        args:
            userId (str): 企业账号的userid，可通过指定方式获取。
            reason (str, optional): 企业账号停用原因。默认为None。
        """
        url = "https://api.dingtalk.com/v1.0/contact/orgAccounts/disable"
        data = {
            "userId": userId,
            "reason": reason
        }
        return await self.post_new(url, json=data)


    async def enable_org_account(self, userId: str) -> str:
        """
        启用企业帐号.

        args:
            userId (str): 企业账号的userid，可通过以下四种方式获得：
                - 根据手机号查询企业帐号用户
                - 创建SSO企业帐号
                - 创建钉钉自建企业帐号
                - 邀请其他组织企业帐号加入
        """
        url = "https://api.dingtalk.com/v1.0/contact/orgAccounts/enable"
        data = {"userId": userId}
        return await self.post_new(url, json=data)


    async def force_logout_org_account(self, userId: str, reason: str = None) -> str:
        """
        强制登出企业帐号.

        args:
            userId (str): 企业账号的userid，可通过指定方式获取。
            reason (str, optional): 企业账号强制登出的原因。默认为None。
        """
        url = "https://oapi.dingtalk.com/v1.0/contact/orgAccounts/signOut"
        data = {
            "userId": userId,
            "reason": reason
        }
        return await self.post_new(url, json=data)


    async def get_senior_settings(self, seniorStaffId: str) -> str:
        """
        获取用户高管模式设置.

        args:
            seniorStaffId (str): 用户userId，可通过通过免登码获取用户信息获得userId。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/seniorSettings?seniorStaffId={seniorStaffId}"
        return await self.get_new(url)


    async def get_restriction_settings(self, nextToken: int = None, maxResults: int = None) -> str:
        """
        获取限制查看通讯录设置列表.

        args:
            nextToken (int, optional): 分页游标。首次调用不传，非首次调用传上次返回的nextToken。
            maxResults (int, optional): 最大返回结果数，最大值100。
        """
        url = "https://api.dingtalk.com/v1.0/contact/restrictions/settings"
        params = {}
        if nextToken is not None:
            params["nextToken"] = nextToken
        if maxResults is not None:
            params["maxResults"] = maxResults
        return await self.get_new(url, params=params)


    async def get_department_detail_old(self, dept_id: int) -> str:
        """
        获取部门详情（旧版SDK）.

        args:
            dept_id (int): 部门ID
        """
        url = "https://oapi.dingtalk.com/topapi/industry/department/get"
        data = {
            "dept_id": dept_id
        }
        return await self.post_old(url, json=data)


    async def invite_other_org_user(self, outer_exclusive_corpid: str, outer_exclusive_userid: str, name: str, dept_id_list: str, userid: str = None, telephone: str = None, job_number: str = None, title: str = None, email: str = None, org_email: str = None, org_email_type: str = None, work_place: str = None, remark: str = None, dept_order_list: list = None, dept_title_list: list = None, extension: str = None, senior_mode: bool = None, hired_date: int = None, manager_userid: str = None) -> str:
        """
        邀请其他组织企业账号加入本组织.

        args:
            outer_exclusive_corpid (str): 需要添加的企业账号所属的corpId。
            outer_exclusive_userid (str): 需要添加的企业账号所属的userId。
            name (str): 员工名称，长度最大80个字符。
            dept_id_list (str): 所属部门ID列表，多个部门ID使用英文逗号隔开。
            userid (str, optional): 员工唯一标识ID，长度为1~64个字符。默认自动生成。
            telephone (str, optional): 分机号，长度最大50个字符。
            job_number (str, optional): 员工工号，长度最大为50个字符。
            title (str, optional): 职位，长度最大为200个字符。
            email (str, optional): 员工个人邮箱，长度最大50个字符。
            org_email (str, optional): 员工的企业邮箱，长度最大100个字符。
            org_email_type (str, optional): 员工的企业邮箱类型（profession: 标准版, base: 基础版）。
            work_place (str, optional): 办公地点，长度最大100个字符。
            remark (str, optional): 备注，长度最大2000个字符。
            dept_order_list (list, optional): 员工在对应部门中的排序。
            dept_title_list (list, optional): 员工在对应部门中的职位。
            extension (str, optional): 扩展属性，最大长度2000个字符。
            senior_mode (bool, optional): 是否开启高管模式，默认值false。
            hired_date (int, optional): 入职时间，Unix时间戳，单位毫秒。
            manager_userid (str, optional): 直属主管的userId。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/create"
        data = {
            "userid": userid,
            "outer_exclusive_corpid": outer_exclusive_corpid,
            "outer_exclusive_userid": outer_exclusive_userid,
            "name": name,
            "dept_id_list": dept_id_list,
            "telephone": telephone,
            "job_number": job_number,
            "title": title,
            "email": email,
            "org_email": org_email,
            "org_email_type": org_email_type,
            "work_place": work_place,
            "remark": remark,
            "dept_order_list": dept_order_list,
            "dept_title_list": dept_title_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "manager_userid": manager_userid
        }
        return await self.post_old(url, json=data)


    async def get_sub_department_ids(self, dept_id: int) -> str:
        """
        获取子部门ID列表.

        args:
            dept_id (int): 父部门ID，根部门传1。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/listsubid"
        data = {"dept_id": dept_id}
        return await self.post_old(url, json=data)


    async def get_contact_auth_scope(self) -> dict:
        """
        获取通讯录权限范围.

        返回:
            dict: 包含授权信息的字典，包括可获取通信录信息的员工userid列表、部门ID列表及企业用户字段等。
        """
        url = "https://oapi.dingtalk.com/auth/scopes"
        return await self.get_old(url)


    async def get_corp_auth_info(self, targetCorpId: str = None) -> str:
        """
        获取企业认证信息.

        args:
            targetCorpId (str): 需要获取的企业认证信息的企业corpId。
        """
        url = "https://api.dingtalk.com/v1.0/contact/organizations/authInfos"
        params = {}
        if targetCorpId:
            params["targetCorpId"] = targetCorpId
        return await self.get_new(url, params=params)


    async def get_enterprise_info(self) -> str:
        """
        获取企业信息.
        """
        url = "https://oapi.dingtalk.com/topapi/industry/organization/get"
        data = {}
        return await self.post_old(url, json=data)


    async def get_company_invite_info(self, inviterUserId: str = None, deptId: int = None) -> str:
        """
        获取企业邀请信息.

        args:
            inviterUserId (str, optional): 邀请者的userId。默认为None，表示使用当前企业创建者的userId。
            deptId (int, optional): 部门ID。默认为None。
        """
        url = "https://api.dingtalk.com/v1.0/contact/invites/infos"
        params = {}
        if inviterUserId:
            params["inviterUserId"] = inviterUserId
        if deptId:
            params["deptId"] = deptId
        return await self.get_new(url, params=params)


    async def get_department_list_old(self, dept_id: int = None, language: str = None) -> str:
        """
        获取下一级部门基础信息.

        args:
            dept_id (int, optional): 父部门ID。默认为None。
            language (str, optional): 通讯录语言，例如 'zh_CN' 或 'en_US'。默认为None。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/listsub"
        data = {}
        if dept_id is not None:
            data["dept_id"] = dept_id
        if language is not None:
            data["language"] = language
        return await self.post_old(url, json=data)


    async def get_external_contact_list(self, size: int = None, offset: int = None) -> str:
        """
        获取企业外部联系人列表.

        args:
            size (int, optional): 分页大小，最大100。
            offset (int, optional): 偏移量，从0开始。
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/list"
        data = {}
        if size is not None:
            data["size"] = size
        if offset is not None:
            data["offset"] = offset
        return await self.post_old(url, json=data)


    async def get_employee_list_by_role(self, role_id: int, size: int = 20, offset: int = 0) -> str:
        """
        获取指定角色的员工列表.

        args:
            role_id (int): 角色ID，可通过获取角色列表接口获取。
            size (int, optional): 分页大小，默认值为20，最大100。
            offset (int, optional): 分页偏移量，默认值为0。
        """
        url = "https://oapi.dingtalk.com/topapi/role/simplelist"
        data = {
            "role_id": role_id,
            "size": size,
            "offset": offset
        }
        return await self.post_old(url, json=data)


    async def get_employee_count(self, only_active: bool) -> str:
        """
        获取员工人数.

        args:
            only_active (bool): 是否只包含激活钉钉的人员数量
        """
        url = "https://oapi.dingtalk.com/topapi/user/count"
        data = {
            "only_active": only_active
        }
        return await self.post_old(url, json=data)


    async def get_user_by_mobile(self, mobile: str, support_exclusive_account_search: bool) -> str:
        """
        根据手机号查询企业账号用户.

        args:
            mobile (str): 用户的手机号
            support_exclusive_account_search (bool): 是否支持通过手机号搜索企业账号
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/getbymobile"
        data = {
            "mobile": mobile,
            "support_exclusive_account_search": support_exclusive_account_search
        }
        return await self.post_old(url, json=data)


    async def get_role_list(self, size: int = 20, offset: int = 0) -> str:
        """
        获取角色列表.

        args:
            size (int): 分页大小，默认值20，最大值200。
            offset (int): 偏移量，默认值0，从0开始。
        """
        url = "https://oapi.dingtalk.com/topapi/role/list"
        data = {
            "size": size,
            "offset": offset
        }
        return await self.post_old(url, json=data)


    async def get_external_contact_label_list(self, size: int = None, offset: int = None) -> str:
        """
        获取外部联系人标签列表.

        args:
            size (int, optional): 分页大小，最大100。默认为None。
            offset (int, optional): 偏移量，从0开始。默认为None。
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups"
        data = {}
        if size is not None:
            data["size"] = size
        if offset is not None:
            data["offset"] = offset
        return await self.post_old(url, json=data)


    async def get_department_list(self, dept_id: int, cursor: int = None, size: int = 10) -> str:
        """
        获取部门列表.

        args:
            dept_id (int): 父部门ID，行业根部门传1。
            cursor (int, optional): 分页查询的游标。默认为None。
            size (int, optional): 分页查询的大小，最大值1000。默认为10。
        """
        url = "https://oapi.dingtalk.com/topapi/industry/department/list"
        data = {
            "dept_id": dept_id,
            "cursor": cursor,
            "size": size
        }
        return await self.post_old(url, json=data)


    async def get_external_contact_detail(self, user_id: str) -> str:
        """
        获取外部联系人详情.

        args:
            user_id (str): 外部联系人userId
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/get"
        data = {"user_id": user_id}
        return await self.post_old(url, json=data)


    async def get_contact_hide_settings(self, nextToken: int = 0, maxResults: int = 100) -> str:
        """
        获取通讯录隐藏设置信息列表.

        args:
            nextToken (int): 分页游标。首次调用传0，非首次调用传上次返回的nextToken。
            maxResults (int): 分页大小，最大值100。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/contactHideSettings?nextToken={nextToken}&maxResults={maxResults}"
        return await self.get_new(url)


    async def get_department_user_list(self, dept_id: int, rol: str = None, cursor: int = None, size: int = 10) -> str:
        """
        获取部门下人员列表.

        args:
            dept_id (int): 部门id。
            rol (str, optional): 行业相关角色。默认为None。
            cursor (int, optional): 分页查询的游标。默认为None。
            size (int, optional): 分页查询的大小，最大值1000。默认为10。
        """
        url = "https://oapi.dingtalk.com/topapi/industry/user/list"
        data = {
            "dept_id": dept_id,
            "rol": rol,
            "cursor": cursor,
            "size": size
        }
        return await self.post_old(url, json=data)


    async def get_role_group_list(self, group_id: int) -> str:
        """
        获取角色组列表.

        args:
            group_id (int): 角色组的ID。
        """
        url = "https://oapi.dingtalk.com/topapi/role/getrolegroup"
        data = {
            "group_id": group_id
        }
        return await self.post_old(url, json=data)


    async def get_user_attribute_visibility_settings(self, nextToken: int = -1, maxResults: int = 100) -> str:
        """
        获取用户属性可见性设置.

        args:
            nextToken (int): 分页游标。首次调用传-1，非首次调用传上次返回的nextToken。默认值为-1。
            maxResults (int): 分页大小，最大支持100。默认值为100。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings?nextToken={nextToken}&maxResults={maxResults}"
        return await self.get_new(url)

    async def get_department_user_detail(self, dept_id: int, userid: str) -> str:
        """
        获取部门用户详情.

        args:
            dept_id (int): 部门ID
            userid (str): 员工userId
        """
        url = "https://oapi.dingtalk.com/topapi/industry/user/get"
        data = {
            "dept_id": dept_id,
            "userid": userid
        }
        return await self.post_old(url, json=data)


    async def get_role_detail_old(self, roleId: int) -> str:
        """
        获取角色详情（旧版SDK）.

        args:
            roleId (int): 角色ID
        """
        url = "https://oapi.dingtalk.com/topapi/role/getrole"
        data = {"roleId": roleId}
        return await self.post_old(url, json=data)


    async def get_department_user_details(self, dept_id: int, cursor: int, size: int, order_field: str = None, contain_access_limit: bool = None, language: str = None) -> str:
        """
        获取部门用户详情.

        args:
            dept_id (int): 部门ID，根部门传1。
            cursor (int): 分页查询的游标，初始传0，后续传返回的next_cursor值。
            size (int): 分页大小。
            order_field (str, optional): 排序规则，默认为自定义排序(custom)。可选值：entry_asc, entry_desc, modify_asc, modify_desc, custom。
            contain_access_limit (bool, optional): 是否返回访问受限的员工，默认不返回。
            language (str, optional): 通讯录语言，默认中文(zh_CN)。可选值：zh_CN, en_US。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/list"
        data = {
            "dept_id": dept_id,
            "cursor": cursor,
            "size": size,
            "order_field": order_field,
            "contain_access_limit": contain_access_limit,
            "language": language
        }
        return await self.post_old(url, json=data)


    async def get_user_detail_old(self, userid: str, language: str = "zh_CN") -> str:
        """
        查询企业账号用户详情.

        args:
            userid (str): 用户的UserId。
            language (str): 通讯录语言，默认为 'zh_CN'。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/get"
        data = {
            "userid": userid,
            "language": language
        }
        return await self.post_old(url, json=data)


    async def get_inactive_users(self, is_active: bool, offset: int, size: int, query_date: str, dept_ids: list = None) -> str:
        """
        获取未登录钉钉的员工列表.

        args:
            is_active (bool): 是否活跃，false表示未登录，true表示登录。
            offset (int): 分页查询的偏移量，从0开始。
            size (int): 分页查询的分页大小，最大100。
            query_date (str): 查询日期，格式为yyyyMMdd。
            dept_ids (list): 部门ID列表，可选参数，不传表示查询整个企业。
        """
        url = "https://oapi.dingtalk.com/topapi/inactive/user/v2/get"
        data = {
            "is_active": is_active,
            "offset": offset,
            "size": size,
            "query_date": query_date,
            "dept_ids": dept_ids if dept_ids else []
        }
        return await self.post_old(url, json=data)


    async def get_latest_ding_index(self, corpId: str) -> str:
        """
        获取企业最新钉钉指数信息.

        args:
            corpId (str): 企业ID
        """
        url = "https://api.dingtalk.com/v1.0/contact/dingIndexs"
        data = {}
        return await self.get_new(url, params=data)


    async def get_parent_departments_by_user(self, userid: str) -> str:
        """
        获取指定用户的所有父部门列表.

        args:
            userid (str): 要查询的用户的userid。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser"
        data = {
            "userid": userid
        }
        return await self.post_old(url, json=data)


    async def get_department_user_simple(self, dept_id: int, cursor: int, size: int, order_field: str = None, contain_access_limit: bool = None, language: str = None) -> str:
        """
        获取部门用户基础信息.

        args:
            dept_id (int): 部门ID，如果是根部门，该参数传1。
            cursor (int): 分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。
            size (int): 分页长度，最大值100。
            order_field (str, optional): 部门成员的排序规则。默认值为custom。
            contain_access_limit (bool, optional): 是否返回访问受限的员工。
            language (str, optional): 通讯录语言，取值。
        """
        url = "https://oapi.dingtalk.com/topapi/user/listsimple"
        data = {
            "dept_id": dept_id,
            "cursor": cursor,
            "size": size,
        }
        if order_field is not None:
            data["order_field"] = order_field
        if contain_access_limit is not None:
            data["contain_access_limit"] = contain_access_limit
        if language is not None:
            data["language"] = language
        return await self.post_old(url, json=data)


    async def get_user_id_by_unionid_old(self, unionid: str) -> str:
        """
        根据unionid获取用户userid.

        args:
            unionid (str): 用户的unionid
        """
        url = "https://oapi.dingtalk.com/topapi/user/getbyunionid"
        data = {"unionid": unionid}
        return await self.post_old(url, json=data)


    async def get_org_account_status(self, userId: str) -> str:
        """
        查询企业帐号状态.

        args:
            userId (str): 企业账号的userid
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccounts/status?userId={userId}"
        return await self.get_new(url)


    async def get_department_detail(self, dept_id: str) -> str:
        """
        获取部门详情.

        args:
            dept_id (str): 部门ID
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/get"
        data = {"dept_id": dept_id}
        return await self.post_old(url, json=data)


    async def get_admin_scope(self, userid: str) -> str:
        """
        获取管理员通讯录权限范围.

        args:
            userid (str): 管理员的userid。
        """
        url = "https://oapi.dingtalk.com/topapi/user/get_admin_scope"
        data = {"userid": userid}
        return await self.post_old(url, json=data)


    async def get_admin_list(self) -> dict:
        """
        获取管理员列表.
        """
        url = "https://oapi.dingtalk.com/topapi/user/listadmin"
        data = {}
        return await self.post_old(url, json=data)


    async def get_employee_leave_records(self, start_time: str, end_time: str = None, next_token: str = "0", max_results: int = 50) -> str:
        """
        查询离职记录列表.

        args:
            start_time (str): 开始时间，格式为 ISO 8601/RFC 3339。
            end_time (str, optional): 结束时间，格式为 ISO 8601/RFC 3339。默认为 None。
            next_token (str, optional): 分页游标，默认为 "0"。
            max_results (int, optional): 每页最大条目数，最大值为 50。默认为 50。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/empLeaveRecords"
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "nextToken": next_token,
            "maxResults": max_results
        }
        return await self.get_new(url, params=params)


    async def get_parent_departments_by_dept(self, dept_id: int) -> str:
        """
        获取指定部门的所有父部门ID列表.

        args:
            dept_id (int): 要查询的部门ID
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/listparentbydept"
        data = {"dept_id": dept_id}
        return await self.post_old(url, json=data)


    async def get_department_user_id_list(self, dept_id: int) -> str:
        """
        获取部门用户userid列表.

        args:
            dept_id (int): 部门ID，根部门传1
        """
        url = "https://oapi.dingtalk.com/topapi/user/listid"
        data = {"dept_id": dept_id}
        return await self.post_old(url, json=data)


    async def get_migration_ding_id_by_ding_id(self, dingId: str) -> str:
        """
        根据原dingId查询迁移后的dingId.

        args:
            dingId (str): 原普通账号的dingId。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccount/getMigrationDingIdByDingIds?dingId={dingId}"
        return await self.get_new(url)


    async def get_original_ding_id_by_migration_ding_id(self, migrationDingId: str) -> str:
        """
        根据迁移后的dingId查询原dingId.

        args:
            migrationDingId (str): 迁移后企业账号的dingId。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccount/getDingIdByMigrationDingIds?migrationDingId={migrationDingId}"
        return await self.get_new(url)


    async def get_union_id_by_migration_union_id(self, migrationUnionId: str) -> str:
        """
        根据迁移后的unionId查询原unionId.

        args:
            migrationUnionId (str): 迁移后企业账号的unionId。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccount/getUnionIdByMigrationUnionIds?migrationUnionId={migrationUnionId}"
        return await self.get_new(url)


    async def get_user_detail(self, userid: str, language: str = "zh_CN") -> str:
        """
        查询用户详情.

        args:
            userid (str): 用户的userId。
            language (str): 通讯录语言，默认为 "zh_CN"。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/get"
        data = {
            "userid": userid,
            "language": language
        }
        return await self.post_old(url, json=data)


    async def get_user_by_mobile(self, mobile: str) -> str:
        """
        根据手机号查询用户.

        args:
            mobile (str): 用户的手机号
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/getbymobile"
        data = {"mobile": mobile}
        return await self.post_old(url, json=data)


    async def set_department_visibility_priority(self, enable: bool) -> str:
        """
        设置通讯录部门可见性优先级.

        args:
            enable (bool): 是否开启子部门设置优先，取值：
                - True: 子部门设置优先于父部门
                - False(默认值): 父部门设置优先于子部门
        """
        url = "https://api.dingtalk.com/v1.0/contact/depts/settings/priorities"
        data = {"enable": enable}
        return await self.post_new(url, json=data)


    async def get_migration_union_id_by_union_id(self, unionId: str) -> str:
        """
        根据原unionId查询迁移后的unionId.

        args:
            unionId (str): 原普通账号的unionId。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccount/getMigrationUnionIdByUnionIds?unionId={unionId}"
        return await self.get_new(url)


    async def transfer_main_administrator(self, sourceUserId: str, targetUserId: str, effectCorpId: str) -> str:
        """
        企业帐号转交主管理员（创建者）。

        args:
            sourceUserId (str): 原企业账号userid。
            targetUserId (str): 接收专属账号userid。
            effectCorpId (str): 被转交的组织corpId。
        """
        url = "https://api.dingtalk.com/v1.0/contact/orgAccounts/mainAdministrators/change"
        data = {
            "sourceUserId": sourceUserId,
            "targetUserId": targetUserId,
            "effectCorpId": effectCorpId
        }
        return await self.post_new(url, json=data)


    async def update_department_old(
        self,
        dept_id: int,
        parent_id: int = None,
        hide_dept: bool = None,
        dept_permits: str = None,
        user_permits: str = None,
        create_dept_group: bool = None,
        order: int = None,
        name: str = None,
        source_identifier: str = None,
        outer_dept: bool = None,
        outer_permit_users: str = None,
        outer_permit_depts: str = None,
        outer_dept_only_self: bool = None,
        language: str = None,
        auto_add_user: bool = None,
        auto_approve_apply: bool = None,
        dept_manager_userid_list: str = None,
        group_contain_sub_dept: bool = None,
        group_contain_outer_dept: bool = None,
        group_contain_hidden_dept: bool = None,
        org_dept_owner: str = None,
        force_update_fields: str = None,
        code: str = None
    ) -> str:
        """
        更新部门信息（旧版SDK）.

        args:
            dept_id (int): 部门ID，必填。
            parent_id (int, optional): 父部门ID，默认为None。
            hide_dept (bool, optional): 是否隐藏本部门，默认为None。
            dept_permits (str, optional): 指定可以查看本部门的其他部门列表，默认为None。
            user_permits (str, optional): 指定可以查看本部门的用户userid列表，默认为None。
            create_dept_group (bool, optional): 是否创建一个关联此部门的企业群，默认为None。
            order (int, optional): 在父部门中的排序值，默认为None。
            name (str, optional): 部门名称，默认为None。
            source_identifier (str, optional): 部门标识字段，默认为None。
            outer_dept (bool, optional): 是否限制本部门成员查看通讯录，默认为None。
            outer_permit_users (str, optional): 指定本部门成员可查看的通讯录用户userid列表，默认为None。
            outer_permit_depts (str, optional): 指定本部门成员可查看的通讯录部门ID列表，默认为None。
            outer_dept_only_self (bool, optional): 本部门成员是否只能看到所在部门及下级部门通讯录，默认为None。
            language (str, optional): 通讯录语言，默认为None。
            auto_add_user (bool, optional): 当部门群已经创建后，有新人加入部门时是否会自动加入该群，默认为None。
            auto_approve_apply (bool, optional): 是否默认同意加入该部门的申请，默认为None。
            dept_manager_userid_list (str, optional): 部门的主管userId列表，默认为None。
            group_contain_sub_dept (bool, optional): 部门群是否包含子部门，默认为None。
            group_contain_outer_dept (bool, optional): 部门群是否包含外包部门，默认为None。
            group_contain_hidden_dept (bool, optional): 部门群是否包含隐藏部门，默认为None。
            org_dept_owner (str, optional): 企业群群主的userId，默认为None。
            force_update_fields (str, optional): 强制更新的字段，默认为None。
            code (str, optional): 部门编码，默认为None。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/department/update"
        data = {
            "dept_id": dept_id,
            "parent_id": parent_id,
            "hide_dept": hide_dept,
            "dept_permits": dept_permits,
            "user_permits": user_permits,
            "create_dept_group": create_dept_group,
            "order": order,
            "name": name,
            "source_identifier": source_identifier,
            "outer_dept": outer_dept,
            "outer_permit_users": outer_permit_users,
            "outer_permit_depts": outer_permit_depts,
            "outer_dept_only_self": outer_dept_only_self,
            "language": language,
            "auto_add_user": auto_add_user,
            "auto_approve_apply": auto_approve_apply,
            "dept_manager_userid_list": dept_manager_userid_list,
            "group_contain_sub_dept": group_contain_sub_dept,
            "group_contain_outer_dept": group_contain_outer_dept,
            "group_contain_hidden_dept": group_contain_hidden_dept,
            "org_dept_owner": org_dept_owner,
            "force_update_fields": force_update_fields,
            "code": code
        }
        return await self.post_old(url, json=data)


    async def update_contact_hide_settings(
        self,
        name: str = None,
        description: str = None,
        objectStaffIds: list = None,
        objectDeptIds: list = None,
        objectTagIds: list = None,
        excludeStaffIds: list = None,
        excludeDeptIds: list = None,
        excludeTagIds: list = None,
        active: bool = None,
        id: int = None,
        hideInUserProfile: bool = None,
        hideInSearch: bool = None
    ) -> str:
        """
        新增或更新通讯录隐藏设置.

        args:
            name (str, optional): 设置名称。
            description (str, optional): 设置描述信息。
            objectStaffIds (list, optional): 需要被隐藏的员工userId列表。
            objectDeptIds (list, optional): 需要被隐藏的部门ID列表。
            objectTagIds (list, optional): 需要被隐藏的角色roleId列表。
            excludeStaffIds (list, optional): 不受本次隐藏设置影响的员工userId列表。
            excludeDeptIds (list, optional): 不受本次隐藏设置影响的部门ID列表。
            excludeTagIds (list, optional): 不受本次隐藏设置影响的角色ID列表。
            active (bool, optional): 该设置是否激活。
            id (int, optional): 设置ID，新增时为空，修改时为需要修改的ID。
            hideInUserProfile (bool, optional): 是否同时在被查看个人资料页时隐藏。
            hideInSearch (bool, optional): 是否同时在被搜索时隐藏。
        """
        url = "https://api.dingtalk.com/v1.0/contact/contactHideSettings"
        data = {
            "name": name,
            "description": description,
            "objectStaffIds": objectStaffIds,
            "objectDeptIds": objectDeptIds,
            "objectTagIds": objectTagIds,
            "excludeStaffIds": excludeStaffIds,
            "excludeDeptIds": excludeDeptIds,
            "excludeTagIds": excludeTagIds,
            "active": active,
            "id": id,
            "hideInUserProfile": hideInUserProfile,
            "hideInSearch": hideInSearch
        }
        return await self.put_new(url, json=data)


    async def update_user_info_old(self, userid: str, name: str = None, hide_mobile: bool = None, telephone: str = None, 
                                job_number: str = None, manager_userid: str = None, title: str = None, email: str = None, 
                                org_email: str = None, work_place: str = None, remark: str = None, dept_id_list: str = None, 
                                dept_order_list: list = None, dept_title_list: list = None, extension: str = None, 
                                senior_mode: bool = None, hired_date: int = None, language: str = None, 
                                force_update_fields: str = None, org_email_type: str = None, loginId: str = None, 
                                exclusive_mobile: str = None, avatarMediaId: str = None, nickname: str = None, 
                                dept_position_list: list = None, extension_i18n: dict = None) -> str:
        """
        更新企业账号用户信息（旧版SDK）.

        args:
            userid (str): 员工的userId，必填。
            name (str, optional): 员工名称，长度最大80个字符。
            hide_mobile (bool, optional): 是否隐藏手机号。
            telephone (str, optional): 分机号，长度最大50个字符。
            job_number (str, optional): 员工工号，长度最大50个字符。
            manager_userid (str, optional): 直属主管的userId。
            title (str, optional): 职位，长度最大200个字符。
            email (str, optional): 员工邮箱，长度最大50个字符。
            org_email (str, optional): 员工的企业邮箱。
            work_place (str, optional): 办公地点，长度最大100个字符。
            remark (str, optional): 备注，长度最大2000个字符。
            dept_id_list (str, optional): 所属部门ID列表，必填。
            dept_order_list (list, optional): 员工在对应部门中的排序信息。
            dept_title_list (list, optional): 员工在对应部门中的职位信息。
            extension (str, optional): 扩展属性，长度最大2000个字符。
            senior_mode (bool, optional): 是否开启高管模式。
            hired_date (int, optional): 入职时间，UNIX时间戳，单位毫秒。
            language (str, optional): 通讯录语言。
            force_update_fields (str, optional): 强制更新的字段。
            org_email_type (str, optional): 企业邮箱类型。
            loginId (str, optional): 钉钉企业账号的登录名。
            exclusive_mobile (str, optional): 企业账号手机号。
            avatarMediaId (str, optional): 头像MediaId。
            nickname (str, optional): 企业账号的昵称。
            dept_position_list (list, optional): 部门内任职信息。
            extension_i18n (dict, optional): 扩展属性的国际化值。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/update"
        data = {
            "userid": userid,
            "name": name,
            "hide_mobile": hide_mobile,
            "telephone": telephone,
            "job_number": job_number,
            "manager_userid": manager_userid,
            "title": title,
            "email": email,
            "org_email": org_email,
            "work_place": work_place,
            "remark": remark,
            "dept_id_list": dept_id_list,
            "dept_order_list": dept_order_list,
            "dept_title_list": dept_title_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "language": language,
            "force_update_fields": force_update_fields,
            "org_email_type": org_email_type,
            "loginId": loginId,
            "exclusive_mobile": exclusive_mobile,
            "avatarMediaId": avatarMediaId,
            "nickname": nickname,
            "dept_position_list": dept_position_list,
            "extension_i18n": extension_i18n
        }
        return await self.post_old(url, json=data)


    async def update_external_contact(self, contact: dict) -> str:
        """
        更新企业外部联系人.

        args:
            contact (dict): 外部联系人信息，包含以下字段：
                - user_id (str): 外部联系人的userId，必填。
                - name (str): 外部联系人的姓名，必填。
                - follower_user_id (str): 负责人的userId，必填。
                - label_ids (list[int]): 标签列表，必填。
                - title (str, optional): 职位。
                - share_dept_ids (list[int], optional): 共享给的部门ID列表。
                - address (str, optional): 地址。
                - remark (str, optional): 备注。
                - company_name (str, optional): 外部联系人的企业名称。
                - share_user_ids (list[str], optional): 共享给的员工userid列表。
        """
        url = "https://oapi.dingtalk.com/topapi/extcontact/update"
        data = {"contact": contact}
        return await self.post_old(url, json=data)


    async def set_senior_mode(self, seniorStaffId: str, open: bool, permitStaffIds: list = None, permitDeptIds: list = None, permitTagIds: list = None, protectScenes: list = None) -> str:
        """
        设置高管模式.

        args:
            seniorStaffId (str): 需要设置的员工userid。
            open (bool): 是否开启高管模式，取值：True为开启，False为关闭。
            permitStaffIds (list, optional): 高管白名单员工userid列表。
            permitDeptIds (list, optional): 高管白名单部门列表。
            permitTagIds (list, optional): 高管白名单角色列表。
            protectScenes (list, optional): 高管拦截场景列表。
        """
        url = "https://api.dingtalk.com/v1.0/contact/seniorSettings"
        data = {
            "seniorStaffId": seniorStaffId,
            "open": open,
            "permitStaffIds": permitStaffIds if permitStaffIds else [],
            "permitDeptIds": permitDeptIds if permitDeptIds else [],
            "permitTagIds": permitTagIds if permitTagIds else [],
            "protectScenes": protectScenes if protectScenes else []
        }
        return await self.post_new(url, json=data)


    async def set_role_member_scope(self, userid: str, role_id: int, dept_ids: str = None) -> str:
        """
        设定角色成员管理范围.

        args:
            userid (str): 员工在企业中的userId。
            role_id (int): 角色ID。
            dept_ids (str, optional): 部门ID列表，多个部门id之间使用逗号分隔。默认为None。
        """
        url = "https://oapi.dingtalk.com/topapi/role/scope/update"
        data = {
            "userid": userid,
            "role_id": role_id,
            "dept_ids": dept_ids
        }
        return await self.post_old(url, json=data)


    async def update_role_name(self, roleId: int, roleName: str) -> str:
        """
        更新角色名称.

        args:
            roleId (int): 要更新的角色ID
            roleName (str): 修改后的角色名称
        """
        url = "https://oapi.dingtalk.com/role/update_role"
        data = {
            "roleId": roleId,
            "roleName": roleName
        }
        return await self.post_old(url, json=data)


    async def create_user_old(self, name: str, mobile: str, dept_id_list: str, userid: str = None, hide_mobile: bool = False, telephone: str = None, job_number: str = None, title: str = None, email: str = None, org_email: str = None, org_email_type: str = None, work_place: str = None, remark: str = None, dept_order_list: list = None, dept_title_list: list = None, extension: dict = None, senior_mode: bool = False, hired_date: int = None, manager_userid: str = None, login_email: str = None, dept_position_list: list = None, extension_i18n: dict = None) -> str:
        """
        创建用户.

        args:
            name (str): 员工名称，长度最大80个字符。
            mobile (str): 手机号码，企业内必须唯一，不可重复。
            dept_id_list (str): 所属部门id列表，每次调用最多传100个部门ID。
            userid (str, optional): 员工唯一标识ID（不可修改），企业内必须唯一。长度为1~64个字符，如果不传，将自动生成一个userid。
            hide_mobile (bool, optional): 是否隐藏手机号，默认值false。
            telephone (str, optional): 分机号，长度最大50个字符。
            job_number (str, optional): 员工工号，长度最大为50个字符。
            title (str, optional): 职位，长度最大为200个字符。
            email (str, optional): 员工个人邮箱，长度最大50个字符。
            org_email (str, optional): 员工的企业邮箱，长度最大100个字符。
            org_email_type (str, optional): 员工的企业邮箱类型。
            work_place (str, optional): 办公地点，长度最大100个字符。
            remark (str, optional): 备注，长度最大2000个字符。
            dept_order_list (list, optional): 员工在对应的部门中的排序。
            dept_title_list (list, optional): 员工在对应的部门中的职位。
            extension (dict, optional): 扩展属性，可以设置多种属性，最大长度2000个字符。
            senior_mode (bool, optional): 是否开启高管模式，默认值false。
            hired_date (int, optional): 入职时间，Unix时间戳，单位毫秒。
            manager_userid (str, optional): 直属主管的userId。
            login_email (str, optional): 登录邮箱。
            dept_position_list (list, optional): 部门内任职信息。
            extension_i18n (dict, optional): 扩展属性的国际化值。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/create"
        data = {
            "name": name,
            "mobile": mobile,
            "dept_id_list": dept_id_list,
            "userid": userid,
            "hide_mobile": hide_mobile,
            "telephone": telephone,
            "job_number": job_number,
            "title": title,
            "email": email,
            "org_email": org_email,
            "org_email_type": org_email_type,
            "work_place": work_place,
            "remark": remark,
            "dept_order_list": dept_order_list,
            "dept_title_list": dept_title_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "manager_userid": manager_userid,
            "login_email": login_email,
            "dept_position_list": dept_position_list,
            "extension_i18n": extension_i18n
        }
        return await self.post_old(url, json=data)


    async def update_user_info_old(self, userid: str, name: str = None, hide_mobile: bool = None, telephone: str = None, 
                                    job_number: str = None, manager_userid: str = None, title: str = None, email: str = None, 
                                    org_email: str = None, work_place: str = None, remark: str = None, dept_id_list: str = None, 
                                    dept_order_list: list = None, extension: str = None, senior_mode: bool = None, 
                                    hired_date: int = None, language: str = None, force_update_fields: str = None, 
                                    dept_position_list: list = None, extension_i18n: dict = None) -> str:
        """
        更新用户信息（旧版SDK）.

        args:
            userid (str): 员工的userId。
            name (str, optional): 员工名称，长度最大80个字符。
            hide_mobile (bool, optional): 是否号码隐藏。
            telephone (str, optional): 分机号，长度最大50个字符。
            job_number (str, optional): 员工工号，长度最大50个字符。
            manager_userid (str, optional): 直属主管的userId。
            title (str, optional): 职位，长度最大200个字符。
            email (str, optional): 员工邮箱，长度最大50个字符。
            org_email (str, optional): 员工的企业邮箱。
            work_place (str, optional): 办公地点，长度最大100个字符。
            remark (str, optional): 备注，长度最大2000个字符。
            dept_id_list (str, optional): 所属部门ID列表。
            dept_order_list (list, optional): 员工在对应的部门中的排序。
            extension (str, optional): 扩展属性，长度最大2000个字符。
            senior_mode (bool, optional): 是否开启高管模式。
            hired_date (int, optional): 入职时间，UNIX时间戳，单位毫秒。
            language (str, optional): 通讯录语言。
            force_update_fields (str, optional): 强制更新的字段。
            dept_position_list (list, optional): 部门内任职信息。
            extension_i18n (dict, optional): 扩展属性的国际化值。
        """
        url = "https://oapi.dingtalk.com/topapi/v2/user/update"
        data = {
            "userid": userid,
            "name": name,
            "hide_mobile": hide_mobile,
            "telephone": telephone,
            "job_number": job_number,
            "manager_userid": manager_userid,
            "title": title,
            "email": email,
            "org_email": org_email,
            "work_place": work_place,
            "remark": remark,
            "dept_id_list": dept_id_list,
            "dept_order_list": dept_order_list,
            "extension": extension,
            "senior_mode": senior_mode,
            "hired_date": hired_date,
            "language": language,
            "force_update_fields": force_update_fields,
            "dept_position_list": dept_position_list,
            "extension_i18n": extension_i18n
        }
        # Remove None values from data
        data = {k: v for k, v in data.items() if v is not None}
        return await self.post_old(url, json=data)


    async def get_owned_organizations(self, userId: str) -> str:
        """
        查询企业帐号拥有的组织.

        args:
            userId (str): 企业账号的userid，可通过多种方式获得。
        """
        url = f"https://api.dingtalk.com/v1.0/contact/orgAccounts/ownedOrganizations?userId={userId}"
        return await self.get_new(url)

    def list_tools(self) -> list[types.Tool]:
        """
        List all available tools.
        """
        return [
            types.Tool(
                name="create_role_group",
                description="调用本接口，创建角色组。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "角色组名称。",
                        },
                    },
                    "required": ["name"],
                },
            ),
            types.Tool(
                name="add_external_contact",
                description="调用本接口，添加企业外部联系人。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "contact": {
                            "type": "object",
                            "description": "外部联系人信息。",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "职位。可选参数。",
                                },
                                "label_ids": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "标签列表，可调用获取外部联系人标签列表接口查询标签信息。每次调用最多传20个labelId。",
                                },
                                "share_dept_ids": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "共享给的部门ID，可调用获取子部门ID列表接口获取，每次调用最多传20个部门ID。可选参数。",
                                },
                                "address": {
                                    "type": "string",
                                    "description": "地址。可选参数。",
                                },
                                "remark": {
                                    "type": "string",
                                    "description": "备注。可选参数。",
                                },
                                "follower_user_id": {
                                    "type": "string",
                                    "description": "负责人的userId，可通过根据手机号查询用户接口获取userId，每次调用最多传20个userId。",
                                },
                                "name": {
                                    "type": "string",
                                    "description": "外部联系人的姓名。",
                                },
                                "state_code": {
                                    "type": "string",
                                    "description": "手机号国家码。",
                                },
                                "company_name": {
                                    "type": "string",
                                    "description": "外部联系人的企业名称。可选参数。",
                                },
                                "share_user_ids": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "共享给的员工userid列表，可通过根据手机号查询用户接口获取userId，每次调用最多传20个userId。可选参数。",
                                },
                                "mobile": {
                                    "type": "string",
                                    "description": "外部联系人的手机号。",
                                },
                            },
                            "required": [
                                "label_ids",
                                "follower_user_id",
                                "name",
                                "state_code",
                                "mobile",
                            ],
                        }
                    },
                    "required": ["contact"],
                },
            ),
            types.Tool(
                name="update_or_create_contact_restriction_settings",
                description="新增或修改员工、部门、角色限制查看通讯录的设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "number",
                            "description": "设置ID。如果需要新增设置，该参数不传；如果需要修改已有的设置，需要指定该参数，通过调用获取通讯录限制可见性设置列表接口获取。",
                        },
                        "name": {
                            "type": "string",
                            "description": "设置名称。",
                        },
                        "description": {
                            "type": "string",
                            "description": "设置描述。",
                        },
                        "subjectUserIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "需要限制查看通讯录的用户userId列表，可调用获取部门用户userId接口获取userId。subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "subjectDeptIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "需要限制查看通讯录的部门ID列表，可调用获取部门列表接口获取dept_id。subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "subjectTagIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "需要限制查看通讯录的角色ID，通过调用获取角色列表接口获取。subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "type": {
                            "type": "string",
                            "description": "限制类型，有以下取值：onlySelf（只能查看自己）、onlySelfDeptAndChild（只能看到自己所在的部门及子部门）、excludeNode（默认值，只能看到白名单列表中的部门和人）。当该参数值为excludeNode时，设置的白名单才生效。",
                            "enum": ["onlySelf", "onlySelfDeptAndChild", "excludeNode"],
                        },
                        "excludeUserIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "白名单用户userId，可调用获取部门用户userId接口获取userId。excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。当type参数值为excludeNode时，设置的白名单才生效。",
                        },
                        "excludeDeptIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "白名单部门ID，通过调用获取部门列表接口获取。excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。当type参数值为excludeNode时，设置的白名单才生效。",
                        },
                        "excludeTagIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "白名单角色ID，通过调用获取角色列表接口获取。excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。当type参数值为excludeNode时，设置的白名单才生效。",
                        },
                        "active": {
                            "type": "boolean",
                            "description": "本次设置是否生效。true表示生效，false表示不生效。",
                        },
                        "restrictInUserProfile": {
                            "type": "boolean",
                            "description": "是否同时限制查看个人资料页。true表示是，false表示否。如果限制查看，在钉钉客户端点击不在可看见范围内的员工头像，不会展示当前组织的资料信息。",
                        },
                        "restrictInSearch": {
                            "type": "boolean",
                            "description": "是否同时限制搜索。true表示是，false表示否。如果限制搜索，在钉钉客户端搜索不在可看见范围内的员工，会搜索不到结果。",
                        },
                    },
                    "required": ["type"],
                },
            )
            ,
            types.Tool(
                name="set_user_attribute_visibility",
                description="设置用户属性可见性。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "设置ID。新增时为空，修改时为需要修改的ID。",
                        },
                        "name": {
                            "type": "string",
                            "description": "设置的名称。",
                        },
                        "description": {
                            "type": "string",
                            "description": "设置的描述信息。",
                        },
                        "objectStaffIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "需要隐藏字段的员工userId列表。",
                        },
                        "objectDeptIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "需要隐藏字段的部门deptId列表。",
                        },
                        "objectTagIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "需要隐藏字段的角色roleId列表。",
                        },
                        "hideFields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "需要隐藏的用户属性ID列表。企业自定义属性传属性ID，系统默认属性传默认属性名称。",
                        },
                        "excludeStaffIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "可见隐藏字段的员工userId列表。",
                        },
                        "excludeDeptIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "可见隐藏字段的部门deptId列表。",
                        },
                        "excludeTagIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "可见隐藏字段的角色roleId列表。",
                        },
                        "active": {
                            "type": "boolean",
                            "description": "是否生效。true表示生效，false表示不生效。",
                        },
                    },
                    "required": [],
                },
            ),

            types.Tool(
                name="add_roles_for_employees",
                description="批量增加员工角色。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "roleIds": {
                            "type": "string",
                            "description": "角色roleId列表，可调用获取角色列表接口获取。多个roleId用英文逗号（,）分隔，最多可传20个。",
                        },
                        "userIds": {
                            "type": "string",
                            "description": "员工的userId，可通过调用根据手机号查询用户接口获取。多个userId用英文逗号（,）分隔，最多可传20个。",
                        },
                    },
                    "required": ["roleIds", "userIds"],
                },
            )
            ,

            types.Tool(
                name="create_role",
                description="调用本接口，创建新角色。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "roleName": {
                            "type": "string",
                            "description": "角色名称。",
                        },
                        "groupId": {
                            "type": "number",
                            "description": "角色组ID。如果要加入的角色组已存在，可通过获取角色列表接口获取；如果尚未创建角色组，需先调用创建角色组接口创建角色组并获取角色组ID。",
                        },
                    },
                    "required": ["roleName", "groupId"],
                },
            )
            ,

            types.Tool(
                name="search_department_id",
                description="搜索部门ID。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "queryWord": {
                            "type": "string",
                            "description": "部门名称或者部门名称拼音。",
                        },
                        "offset": {
                            "type": "integer",
                            "description": "分页页码。",
                        },
                        "size": {
                            "type": "integer",
                            "description": "分页大小。",
                        },
                    },
                    "required": ["queryWord", "offset", "size"],
                },
            )
            ,

            types.Tool(
                name="search_user_id",
                description="调用本接口，搜索用户userId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "queryWord": {
                            "type": "string",
                            "description": "用户名称、名称拼音或英文名称。",
                        },
                        "offset": {
                            "type": "integer",
                            "description": "分页页码。",
                        },
                        "size": {
                            "type": "integer",
                            "description": "分页大小。",
                        },
                        "fullMatchField": {
                            "type": "integer",
                            "description": "是否精确匹配。1：精确匹配用户名称；不传默认模糊匹配用户名称。",
                        },
                    },
                    "required": ["queryWord", "offset", "size"],
                },
            )
            ,

            types.Tool(
                name="change_dingtalk_id",
                description="修改企业账号的钉钉号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "员工userId，只支持归属于本企业的企业账号userId。",
                        },
                        "dingTalkId": {
                            "type": "string",
                            "description": "新的钉钉号。全局唯一，不只是组织内唯一，所以不能和已经存在的冲突，发生冲突时需要更换备选值。格式要求：\n"
                                        "- 长度为6到20个字符\n"
                                        "- 字母开头\n"
                                        "- 只包含字母、数字\n"
                                        "- 不能包含违禁内容",
                        },
                    },
                    "required": ["userId", "dingTalkId"],
                },
            )
            ,

            types.Tool(
                name="authorize_org_account_visibility",
                description="授权当前组织的企业账号在加入其他组织后，可在其他组织查看企业账号信息的具体字段。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "toCorpIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "被授权组织的corpId列表。不能为空，且需与调用者的userId同时提供。",
                        },
                        "optUserId": {
                            "type": "string",
                            "description": "当前调用接口的调用者对应userId。用于数据审计，需填写当前组织下真实的员工userId。",
                        },
                        "fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "授权字段: mobile, status (mobile：表示企业账号手机号，status：表示企业账号停用状态)。如果为空或空集合，默认仅授权mobile（历史版本兼容）。",
                        },
                    },
                    "required": ["toCorpIds", "optUserId"],
                },
            )
            ,
            types.Tool(
                name="auth_multi_org_permissions",
                description="授权企业帐号可以加入多个组织，只有被授权后企业帐号才能加入外部组织。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "joinCorpId": {
                            "type": "string",
                            "description": "被授权的组织CorpId。",
                        },
                        "grantDeptIdList": {
                            "type": "array",
                            "items": {
                                "type": "integer",
                            },
                            "description": "授权的部门列表。如果不传，授权整个企业；如果传值，授权参数值对应的部门。",
                        },
                    },
                    "required": ["joinCorpId"],
                },
            ),

            types.Tool(
                name="create_department",
                description="调用本接口，创建新部门。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "部门名称。长度限制为1~64个字符，不允许包含字符\"-\",\"以及\",\"。",
                        },
                        "parent_id": {
                            "type": "number",
                            "description": "父部门ID，根部门ID为1。",
                        },
                        "hide_dept": {
                            "type": "boolean",
                            "description": "是否隐藏本部门。true：隐藏部门，隐藏后本部门将不会显示在公司通讯录中；false（默认值）：显示部门。",
                        },
                        "dept_permits": {
                            "type": "string",
                            "description": "指定可以查看本部门的其他部门列表，总数不能超过50。当hide_dept为true时，则此值生效。",
                        },
                        "user_permits": {
                            "type": "string",
                            "description": "指定可以查看本部门的人员userId列表，总数不能超过50。当hide_dept为true时，则此值生效。",
                        },
                        "outer_dept": {
                            "type": "boolean",
                            "description": "是否限制本部门成员查看通讯录。true：开启限制，开启后本部门成员只能看到限定范围内的通讯录；false（默认值）：不限制。",
                        },
                        "outer_dept_only_self": {
                            "type": "boolean",
                            "description": "本部门成员是否只能看到所在部门及下级部门通讯录。true：只能看到所在部门及下级部门通讯录；false：不能查看所有通讯录，在通讯录中仅能看到自己。当outer_dept为true时，此参数生效。",
                        },
                        "outer_permit_users": {
                            "type": "string",
                            "description": "指定本部门成员可查看的通讯录用户userId列表，总数不能超过50。当outer_dept为true时，此参数生效。",
                        },
                        "outer_permit_depts": {
                            "type": "string",
                            "description": "指定本部门成员可查看的通讯录部门ID列表，总数不能超过50。当outer_dept为true时，此参数生效。",
                        },
                        "create_dept_group": {
                            "type": "boolean",
                            "description": "是否创建一个关联此部门的企业群，默认为false即不创建。",
                        },
                        "auto_approve_apply": {
                            "type": "boolean",
                            "description": "是否默认同意加入该部门的申请。true：表示加入该部门的申请将默认同意；false：表示加入该部门的申请需要有权限的管理员同意。",
                        },
                        "order": {
                            "type": "number",
                            "description": "在父部门中的排序值，order值小的排序靠前。",
                        },
                        "source_identifier": {
                            "type": "string",
                            "description": "部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。",
                        },
                        "code": {
                            "type": "string",
                            "description": "部门编码。",
                        },
                    },
                    "required": ["name", "parent_id"],
                },
            )
            ,
            types.Tool(
                name="create_sso_enterprise_account",
                description="调用本接口创建SSO企业账号新用户。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工唯一标识ID（不可修改），长度为1~64个字符。如果不传，将自动生成一个userid。",
                        },
                        "exclusive_account": {
                            "type": "boolean",
                            "description": "必须填true，表示要创建企业账号。",
                        },
                        "exclusive_account_type": {
                            "type": "string",
                            "description": "必须填sso，表示SSO企业账号。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门ID列表，多个部门ID使用英文逗号隔开，每次调用最多传100个部门ID。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大为50个字符。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大为200个字符。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工个人邮箱，长度最大50个字符。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱，长度最大100个字符。需满足以下条件，此字段才生效：员工已开通企业邮箱。",
                        },
                        "org_email_type": {
                            "type": "string",
                            "description": "员工的企业邮箱类型：profession: 标准版；base：基础版。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序，数值越大，排序越靠前。",
                                    },
                                },
                                "required": ["dept_id", "order"],
                            },
                            "description": "员工在对应的部门中的排序。",
                        },
                        "dept_title_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "员工在部门中的职位。",
                                    },
                                },
                                "required": ["dept_id", "title"],
                            },
                            "description": "员工在对应的部门中的职位。",
                        },
                        "extension": {
                            "type": "string",
                            "description": "扩展属性，可以设置多种属性，最大长度2000个字符。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，Unix时间戳，单位毫秒。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。",
                        },
                        "exclusive_mobile": {
                            "type": "string",
                            "description": "企业账号手机号。",
                        },
                        "avatarMediaId": {
                            "type": "string",
                            "description": "创建本组织企业账号时可指定头像MediaId，只支持jpg/png。",
                        },
                        "nickname": {
                            "type": "string",
                            "description": "创建本组织企业账号时可指定昵称。",
                        },
                    },
                    "required": [
                        "exclusive_account",
                        "name",
                        "dept_id_list",
                    ],
                },
            ),

            types.Tool(
                name="create_dingtalk_enterprise_account",
                description="调用本接口创建钉钉自建企业账号新用户。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工唯一标识ID（不可修改），长度为1~64个字符。如果不传，将自动生成一个userId。",
                        },
                        "exclusive_account": {
                            "type": "boolean",
                            "description": "必须填true，表示要创建企业账号。",
                        },
                        "exclusive_account_type": {
                            "type": "string",
                            "description": "必须填dingtalk，表示钉钉自建企业账号。",
                        },
                        "login_id": {
                            "type": "string",
                            "description": "钉钉自建企业账号的登录名。",
                        },
                        "init_password": {
                            "type": "string",
                            "description": "钉钉自建企业账号的初始密码。初始密码至少8个字符，不能全是字母或者数字。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门ID列表，多个部门ID使用英文逗号隔开，每次调用最多传100个部门ID。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。分机号是唯一的，企业内不能重复。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大为50个字符。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大为200个字符。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工个人邮箱，长度最大50个字符。员工邮箱是唯一的，企业内不能重复。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱，长度最大100个字符。需满足以下条件，此字段才生效：员工已开通企业邮箱。",
                        },
                        "org_email_type": {
                            "type": "string",
                            "description": "员工的企业邮箱类型。profession: 标准版；base：基础版。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序，数值越大，排序越靠前。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的排序。",
                        },
                        "dept_title_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "员工在部门中的职位。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的职位。",
                        },
                        "extension": {
                            "type": "string",
                            "description": "扩展属性，可以设置多种属性，最大长度2000个字符。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，Unix时间戳，单位毫秒。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。",
                        },
                        "exclusive_mobile": {
                            "type": "string",
                            "description": "企业账号手机号。",
                        },
                        "avatarMediaId": {
                            "type": "string",
                            "description": "创建本组织企业账号时可指定头像MediaId，只支持jpg/png。",
                        },
                        "nickname": {
                            "type": "string",
                            "description": "创建本组织企业账号时可指定昵称。",
                        },
                    },
                    "required": [
                        "exclusive_account", 
                        "exclusive_account_type", 
                        "login_id", 
                        "init_password", 
                        "name", 
                        "dept_id_list"
                    ],
                },
            )
            ,
            types.Tool(
                name="delete_department",
                description="根据部门ID删除指定部门。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "要删除的部门ID，可通过获取部门列表接口获取dept_id参数值。",
                        },
                    },
                    "required": ["dept_id"],
                },
            ),
            types.Tool(
                name="delete_user",
                description="根据用户的userid删除指定用户。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工的userid。",
                        },
                    },
                    "required": ["userid"],
                },
            ),
            types.Tool(
                name="delete_staff_attribute_visibility_setting",
                description="调用本接口删除企业员工属性字段可见性设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "settingId": {
                            "type": "integer",
                            "description": "设置的ID，可通过以下方式获取：\n"
                                        "- 企业内部应用，通过获取用户属性可见性设置接口获取id参数值。\n"
                                        "- 第三方企业应用，通过获取用户属性可见性设置接口获取id参数值。",
                        },
                    },
                    "required": ["settingId"],
                },
            ),

            types.Tool(
                name="delete_external_contact",
                description="调用本接口，删除企业外部联系人。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "要删除的外部联系人的userId，可以调用获取外部联系人列表接口获取userid参数值。",
                        },
                    },
                    "required": ["user_id"],
                },
            )
            ,

            types.Tool(
                name="delete_contact_hide_setting",
                description="删除通讯录隐藏设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "settingId": {
                            "type": "integer",
                            "description": "设置ID，可通过获取通讯录隐藏设置接口获得id参数值。",
                        },
                    },
                    "required": ["settingId"],
                },
            )
            ,
            types.Tool(
                name="delete_role",
                description="根据角色ID删除指定的角色。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "number",
                            "description": "要删除的角色ID，可以调用获取角色列表接口获取。'默认'分组内的角色不支持修改，包括：负责人、主管、主管理员、子管理员。",
                        },
                    },
                    "required": ["role_id"],
                },
            ),
            types.Tool(
                name="batch_remove_employee_roles",
                description="调用本接口批量删除员工的角色。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "roleIds": {
                            "type": "string",
                            "description": "角色roleId列表，可调用获取角色列表接口获取。最大列表长度为20，多个roleId用英文逗号（,）分隔。",
                        },
                        "userIds": {
                            "type": "string",
                            "description": "员工的userid，可通过调用根据手机号查询用户获取userId。最大列表长度为100，多个userId用英文逗号（,）分隔。",
                        },
                    },
                    "required": ["roleIds", "userIds"],
                },
            ),
            types.Tool(
                name="delete_restricted_contact_setting",
                description="根据限制查看通讯录设置ID，执行删除操作。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "setting_id": {
                            "type": "string",
                            "description": "限制查看通讯录设置的唯一标识ID。",
                        },
                    },
                    "required": ["setting_id"],
                },
            ),

            types.Tool(
                name="get_user_contact_info",
                description="调用本接口获取企业用户通讯录中的个人信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "unionId": {
                            "type": "string",
                            "description": "用户的unionId。如需获取当前授权人的信息，unionId参数可以传me。",
                        },
                    },
                    "required": ["unionId"],
                },
            )
            ,

            types.Tool(
                name="disable_org_account",
                description="调用本接口，停用指定的企业帐号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "企业账号的userid，可通过以下四种方式获得：\n"
                                        "- 根据手机号查询企业帐号用户\n"
                                        "- 创建SSO企业帐号\n"
                                        "- 创建钉钉自建企业帐号\n"
                                        "- 邀请其他组织企业帐号加入",
                        },
                        "reason": {
                            "type": "string",
                            "description": "企业账号停用原因。可选参数。",
                        },
                    },
                    "required": ["userId"],
                },
            )
            ,

            types.Tool(
                name="enable_org_account",
                description="启用指定企业帐号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "企业账号的userid，可通过以下四种方式获得：\n"
                                        "- 根据手机号查询企业帐号用户 (https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-your-mobile-phone-number)\n"
                                        "- 创建SSO企业帐号 (https://open.dingtalk.com/document/orgapp/create-an-sso-account)\n"
                                        "- 创建钉钉自建企业帐号 (https://open.dingtalk.com/document/orgapp/create-dingtalk-user-created-dedicated-account)\n"
                                        "- 邀请其他组织企业帐号加入 (https://open.dingtalk.com/document/orgapp/invite-other-organization-specific-accounts-to-join)",
                        },
                    },
                    "required": ["userId"],
                },
            )
            ,
            types.Tool(
                name="force_logout_org_account",
                description="强制登出指定的企业帐号。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "企业账号的userid，可通过以下四种方式获得：\n"
                                        "- 根据手机号查询企业帐号用户\n"
                                        "- 创建SSO企业帐号\n"
                                        "- 创建钉钉自建企业帐号\n"
                                        "- 邀请其他组织企业帐号加入",
                        },
                        "reason": {
                            "type": "string",
                            "description": "企业账号强制登出的原因。可选参数。",
                        },
                    },
                    "required": ["userId"],
                },
            ),
            types.Tool(
                name="get_senior_mode_settings",
                description="获取用户高管模式设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "seniorStaffId": {
                            "type": "string",
                            "description": "用户userId，可通过通过免登码获取用户信息获得userId。",
                        },
                    },
                    "required": ["seniorStaffId"],
                },
            ),

            types.Tool(
                name="get_contact_restrictions_settings",
                description="获取通讯录限制可见性设置信息列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "nextToken": {
                            "type": "integer",
                            "description": "分页游标。首次调用不传，非首次调用传上次返回的nextToken。",
                        },
                        "maxResults": {
                            "type": "integer",
                            "description": "最大返回结果数，最大值100。",
                        },
                    },
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_department_detail",
                description="根据部门ID获取部门详情。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID。可通过调用获取部门列表接口获取。",
                        },
                    },
                    "required": ["dept_id"],
                },
            )
            ,
            types.Tool(
                name="invite_other_org_account",
                description="调用本接口加入其他组织企业账号进入本组织。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工唯一标识ID（不可修改），长度为1~64个字符。企业内必须唯一。如果不传，将自动生成一个userid。",
                        },
                        "outer_exclusive_corpid": {
                            "type": "string",
                            "description": "需要添加的企业账号所属的corpId。",
                        },
                        "outer_exclusive_userid": {
                            "type": "string",
                            "description": "需要添加的企业账号所属的userId。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门ID列表，多个部门ID使用英文逗号隔开，每次调用最多传100个部门ID。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。分机号是唯一的，企业内不能重复。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大为50个字符。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大为200个字符。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工个人邮箱，长度最大50个字符。员工邮箱是唯一的，企业内不能重复。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱，长度最大100个字符。需满足以下条件，此字段才生效：员工已开通企业邮箱。",
                        },
                        "org_email_type": {
                            "type": "string",
                            "description": "员工的企业邮箱类型，可选值：profession（标准版）、base（基础版）。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序，数值越大，排序越靠前。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的排序。",
                        },
                        "dept_title_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "员工在部门中的职位。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的职位。",
                        },
                        "extension": {
                            "type": "string",
                            "description": "扩展属性，可以设置多种属性，最大长度2000个字符。手机上最多只能显示10个扩展属性。该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。开启后，手机号码对所有员工隐藏；普通员工无法对其发DING、发起钉钉商务电话；高管之间可以发DING、发起钉钉商务电话。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，Unix时间戳，单位毫秒。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。",
                        },
                    },
                    "required": ["outer_exclusive_corpid", "outer_exclusive_userid", "name", "dept_id_list"],
                },
            ),
            types.Tool(
                name="get_sub_department_id_list",
                description="获取企业部门下的所有直属子部门ID列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "父部门ID，根部门传1。可通过调用获取部门列表接口获取dept_id参数值。",
                        },
                    },
                    "required": ["dept_id"],
                },
            ),
            types.Tool(
                name="get_auth_scopes",
                description="获取通讯录权限范围，调用通讯录相关接口前需要通过此接口确认权限。",
                inputSchema={
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
                outputSchema={
                    "type": "object",
                    "properties": {
                        "auth_org_scopes": {
                            "type": "object",
                            "description": "授权信息。",
                            "properties": {
                                "authed_user": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "授权可获取通信录信息的员工userid列表。",
                                    "example": ["user1", "user2"],
                                },
                                "authed_dept": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "授权可获取通信录信息的部门ID列表。",
                                    "example": [1, 2, 3],
                                },
                            },
                        },
                        "auth_user_field": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "授权可获取的企业用户字段。",
                            "example": ["name", "email"],
                        },
                        "errmsg": {
                            "type": "string",
                            "description": "返回码描述。",
                            "example": "ok",
                        },
                        "errcode": {
                            "type": "number",
                            "description": "返回码。",
                            "example": 0,
                        },
                    },
                    "required": ["auth_org_scopes", "auth_user_field", "errmsg", "errcode"],
                },
            ),
            types.Tool(
                name="get_corp_auth_info",
                description="调用本接口，获取企业认证信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "targetCorpId": {
                            "type": "string",
                            "description": "需要获取的企业认证信息的企业corpId。"
                                        "企业内部应用和第三方企业应用的基础概念详见相关文档。",
                        },
                    },
                    "required": [],
                },
            ),
            types.Tool(
                name="get_enterprise_info",
                description="调用本接口，获取行业通讯录的企业信息。",
                inputSchema={
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_enterprise_invite_info",
                description="调用本接口，获取企业的邀请信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "inviterUserId": {
                            "type": "string",
                            "description": "邀请者的userId。如果不填写，默认邀请者为当前企业创建者的userId。"
                                        "企业内部应用和第三方企业应用的UserId详情参见相关文档。",
                        },
                        "deptId": {
                            "type": "integer",
                            "description": "获取部门邀请链接的部门ID。",
                        },
                    },
                    "required": [],
                },
            ),
            types.Tool(
                name="get_department_list",
                description="根据部门ID获取下一级部门基础信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "父部门ID。企业内部应用和第三方企业应用可通过调用相关接口获取dept_id参数值。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。可选值：zh_CN（默认，中文）、en_US（英文）。",
                        },
                    },
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_external_contact_list",
                description="调用本接口，获取企业外部联系人列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "size": {
                            "type": "number",
                            "description": "支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。",
                        },
                        "offset": {
                            "type": "number",
                            "description": "支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。",
                        },
                    },
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_employee_list_by_role",
                description="获取指定角色的员工列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "number",
                            "description": "角色roleId，可通过获取角色列表接口获取id参数值。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页大小。与offset参数同时设置时才生效，此参数代表分页大小，默认值20，最大100。",
                        },
                        "offset": {
                            "type": "number",
                            "description": "分页偏移量。与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。",
                        },
                    },
                    "required": ["role_id"],
                },
            )
            ,

            types.Tool(
                name="get_employee_count",
                description="调用本接口获取员工人数。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "only_active": {
                            "type": "boolean",
                            "description": "是否只包含激活钉钉的人员数量。false：包含未激活钉钉的人员数量；true：只包含激活钉钉的人员数量。",
                        },
                    },
                    "required": ["only_active"],
                },
            )
            ,
            types.Tool(
                name="get_user_by_mobile",
                description="根据手机号查询企业账号用户。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "mobile": {
                            "type": "string",
                            "description": "用户的手机号。",
                        },
                        "support_exclusive_account_search": {
                            "type": "boolean",
                            "description": "是否支持通过手机号搜索企业账号。true：支持；false：不支持。仅适用于企业账号，且仅支持搜索当前企业创建的企业账号。",
                        },
                    },
                    "required": ["mobile", "support_exclusive_account_search"],
                },
            ),

            types.Tool(
                name="get_role_list",
                description="调用本接口，获取角色列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "size": {
                            "type": "number",
                            "description": "支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，默认值20，最大值200。",
                        },
                        "offset": {
                            "type": "number",
                            "description": "支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。",
                        },
                    },
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_external_contact_label_list",
                description="获取企业外部联系人的标签列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "size": {
                            "type": "number",
                            "description": "支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。",
                        },
                        "offset": {
                            "type": "number",
                            "description": "支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。",
                        },
                    },
                    "required": [],
                },
            )
            ,

            types.Tool(
                name="get_department_list",
                description="根据部门ID获取行业通讯录部门列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "父部门ID，行业根部门传1。",
                        },
                        "cursor": {
                            "type": "number",
                            "description": "分页查询的游标。可选参数。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页查询的大小，最大值1000。",
                        },
                    },
                    "required": ["dept_id", "size"],
                },
            )
            ,
            types.Tool(
                name="get_external_contact_details",
                description="获取企业外部联系人的详细信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "外部联系人userId。通过调用获取外部联系人列表接口获取。",
                        }
                    },
                    "required": ["user_id"],
                },
            ),
            types.Tool(
                name="get_contact_hide_settings",
                description="批量获取通讯录隐藏设置信息列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "nextToken": {
                            "type": "integer",
                            "description": "分页游标。首次调用传0，非首次调用传上次返回的nextToken。",
                        },
                        "maxResults": {
                            "type": "integer",
                            "description": "分页大小，最大值100。",
                        },
                    },
                    "required": [],
                },
            ),

            types.Tool(
                name="get_department_user_list",
                description="调用本接口，获取部门下的人员列表信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门id。企业内部应用和第三方企业应用可通过调用相关接口获取dept_id参数值。",
                        },
                        "rol": {
                            "type": "string",
                            "description": "行业相关，不同行业角色不一样。例如：家校（teacher: 老师, guardian: 监护人, student: 学生），农村（GroupManager: 组长, HeadOfHouseHold: 户主, HouseAdmin: 家庭管理员, Villager: 村民, Leaseholder: 租客）。可选参数。",
                        },
                        "cursor": {
                            "type": "number",
                            "description": "分页查询的游标。可选参数。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页查询的大小，最大值1000。",
                        },
                    },
                    "required": ["dept_id", "size"],
                },
            )
            ,

            types.Tool(
                name="get_role_group_list",
                description="调用本接口，获取角色组信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "group_id": {
                            "type": "number",
                            "description": "角色组的ID。",
                        },
                    },
                    "required": ["group_id"],
                },
            )
            ,
            types.Tool(
                name="get_user_attribute_visibility_settings",
                description="调用本接口获取用户属性可见性设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "nextToken": {
                            "type": "number",
                            "description": "分页游标。首次调用传-1，非首次调用传上次返回的nextToken。",
                        },
                        "maxResults": {
                            "type": "number",
                            "description": "分页大小，最大支持100。",
                        },
                    },
                    "required": [],
                },
            ),

            types.Tool(
                name="get_department_user_details",
                description="调用本接口获取指定部门中的用户详细信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID。只获取当前部门下的员工信息，不包含子部门内的员工。如果是根部门，该参数传1。",
                        },
                        "cursor": {
                            "type": "number",
                            "description": "分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页大小。",
                        },
                        "order_field": {
                            "type": "string",
                            "description": "部门成员的排序规则，默认不传是按自定义排序（custom）。可选值：entry_asc（按进入部门时间升序）、entry_desc（按进入部门时间降序）、modify_asc（按部门信息修改时间升序）、modify_desc（按部门信息修改时间降序）、custom（用户定义排序）。",
                        },
                        "contain_access_limit": {
                            "type": "boolean",
                            "description": "是否返回访问受限的员工。true：返回；false：不返回。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言，取值：zh_CN（中文，默认值）、en_US（英文）。",
                        },
                    },
                    "required": ["dept_id", "cursor", "size"],
                },
            )
            ,
            types.Tool(
                name="get_department_user_detail",
                description="获取部门用户详情。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID。",
                        },
                        "userid": {
                            "type": "string",
                            "description": "员工userId。",
                        },
                    },
                    "required": ["dept_id", "userid"],
                },
            ),
            types.Tool(
                name="get_role_details",
                description="根据角色ID获取指定角色详情。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "roleId": {
                            "type": "number",
                            "description": "角色ID。企业内部应用或第三方企业应用，调用获取角色列表接口获取id参数值。",
                        },
                    },
                    "required": ["roleId"],
                },
            ),

            types.Tool(
                name="get_department_user_details",
                description="调用本接口获取指定部门中的用户详细信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID，可调用获取部门列表接口获取。如果是根部门，该参数传1。只获取当前部门下的员工信息，不包含子部门内的员工。",
                        },
                        "cursor": {
                            "type": "number",
                            "description": "分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页大小。",
                        },
                        "order_field": {
                            "type": "string",
                            "description": "部门成员的排序规则，默认不传是按自定义排序（custom）。可选值：entry_asc（按进入部门时间升序）、entry_desc（按进入部门时间降序）、modify_asc（按部门信息修改时间升序）、modify_desc（按部门信息修改时间降序）、custom（用户定义排序）。",
                        },
                        "contain_access_limit": {
                            "type": "boolean",
                            "description": "是否返回访问受限的员工。true：返回；false：不返回。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。zh_CN：中文（默认值）；en_US：英文。",
                        },
                    },
                    "required": ["dept_id", "cursor", "size"],
                },
            )
            ,

            types.Tool(
                name="get_user_detail",
                description="查询企业账号用户的详细信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "用户的UserId。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。zh_CN：中文（默认值），en_US：英文。可选参数。",
                        },
                    },
                    "required": ["userid"],
                },
            )
            ,

            types.Tool(
                name="get_inactive_user_list",
                description="调用本接口查询指定日期内未登录钉钉的企业员工列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "is_active": {
                            "type": "boolean",
                            "description": "是否活跃：false表示未登录，true表示登录。",
                        },
                        "dept_ids": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "部门ID列表，可调用获取部门列表接口获取，不传表示查询整个企业。",
                        },
                        "offset": {
                            "type": "number",
                            "description": "支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。",
                        },
                        "size": {
                            "type": "number",
                            "description": "支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。",
                        },
                        "query_date": {
                            "type": "string",
                            "description": "查询日期，日期格式为：yyyyMMdd。",
                        },
                    },
                    "required": ["is_active", "offset", "size", "query_date"],
                },
            )
            ,
            types.Tool(
                name="get_ding_index",
                description="调用本接口获取企业最新钉钉指数信息。",
                inputSchema={
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            ),
            types.Tool(
                name="get_parent_departments_by_user",
                description="查询指定用户所属的所有父级部门。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "要查询的用户的userid。",
                        },
                    },
                    "required": ["userid"],
                },
            ),
            types.Tool(
                name="get_department_user_base_info",
                description="调用本接口获取指定部门的用户基础信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID，如果是根部门，该参数传1。企业内部应用可通过'获取部门列表'接口获取dept_id值。",
                        },
                        "cursor": {
                            "type": "number",
                            "description": "分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。",
                        },
                        "size": {
                            "type": "number",
                            "description": "分页长度，最大值100。",
                        },
                        "order_field": {
                            "type": "string",
                            "description": "部门成员的排序规则，默认值为custom。可选值：entry_asc（按进入部门时间升序）、entry_desc（按进入部门时间降序）、modify_asc（按部门信息修改时间升序）、modify_desc（按部门信息修改时间降序）、custom（用户定义排序）。",
                        },
                        "contain_access_limit": {
                            "type": "boolean",
                            "description": "是否返回访问受限的员工。true：是；false：否。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。zh_CN：中文（默认值）；en_US：英文。",
                        },
                    },
                    "required": ["dept_id", "cursor", "size"],
                },
            ),
            types.Tool(
                name="get_userid_by_unionid",
                description="根据unionid获取用户的userid。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "unionid": {
                            "type": "string",
                            "description": "用户的unionid。",
                        }
                    },
                    "required": ["unionid"],
                },
            ),

            types.Tool(
                name="get_org_account_status",
                description="查询某企业帐号的启用状态。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "企业账号的userid，可通过以下四种方式获得：\n"
                                        "- 根据手机号查询企业帐号用户 (https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-your-mobile-phone-number)\n"
                                        "- 创建SSO企业帐号 (https://open.dingtalk.com/document/orgapp/create-an-sso-account)\n"
                                        "- 创建钉钉自建企业帐号 (https://open.dingtalk.com/document/orgapp/create-dingtalk-user-created-dedicated-account)\n"
                                        "- 邀请其他组织企业账号加入 (https://open.dingtalk.com/document/orgapp/invite-other-organization-specific-accounts-to-join)",
                        },
                    },
                    "required": ["userId"],
                },
            )
            ,
            types.Tool(
                name="get_department_detail",
                description="根据部门ID获取指定部门详情。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID，用于指定要查询的部门。",
                        },
                    },
                    "required": ["dept_id"],
                },
            ),

            types.Tool(
                name="get_admin_scope",
                description="调用本接口获取管理员通讯录权限范围。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "管理员的userid。企业内部应用可通过'获取管理员列表'接口获取当前企业下的管理员ID；三方企业应用可通过'获取管理员列表'接口获取授权企业下的管理员ID。",
                        },
                    },
                    "required": ["userid"],
                },
            )
            ,
            types.Tool(
                name="get_admin_list",
                description="调用本接口查询管理员列表。",
                inputSchema={
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
                outputSchema={
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "请求ID。",
                        },
                        "errcode": {
                            "type": "number",
                            "description": "返回码。",
                        },
                        "errmsg": {
                            "type": "string",
                            "description": "返回码描述。",
                        },
                        "result": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "userid": {
                                        "type": "string",
                                        "description": "管理员的userid。",
                                    },
                                    "sys_level": {
                                        "type": "number",
                                        "description": "管理员角色：1：主管理员；2：子管理员。",
                                    },
                                },
                                "required": ["userid", "sys_level"],
                            },
                            "description": "返回结果。",
                        },
                    },
                    "required": ["request_id", "errcode", "errmsg", "result"],
                },
            ),
            types.Tool(
                name="get_employee_leave_records",
                description="查询企业离职记录列表，包含离职员工的离职日期、手机号码和退出企业方式等信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "startTime": {
                            "type": "string",
                            "description": "开始时间。格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。",
                        },
                        "endTime": {
                            "type": "string",
                            "description": "结束时间。格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。如果不传，开始时间距离当前时间不能超过365天；如果传参，开始时间和结束时间跨度不能超过365天。",
                        },
                        "nextToken": {
                            "type": "string",
                            "description": "分页游标。首次查询传0，非首次查询传上次调用本接口返回的nextToken。",
                        },
                        "maxResults": {
                            "type": "integer",
                            "description": "每页最大条目数，最大值50。",
                        },
                    },
                    "required": ["startTime", "maxResults"],
                },
            ),

            types.Tool(
                name="get_parent_departments_by_dept",
                description="获取指定部门的所有父部门ID列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "要查询的部门ID。可以通过以下方式获取：\n"
                                        "- 企业内部应用，调用获取部门列表接口获取dept_id参数值。\n"
                                        "- 第三方企业应用，调用获取部门列表接口获取dept_id参数值。",
                        },
                    },
                    "required": ["dept_id"],
                },
            )
            ,
            types.Tool(
                name="get_department_user_userid_list",
                description="调用本接口获取指定部门的userid列表。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门deptId，可通过以下方式获取：\n- 企业内部应用，可调用获取部门列表接口获取部门deptId。\n- 第三方企业应用，可调用获取部门列表接口获取部门deptId。\n如果是根部门，该参数传1。",
                        },
                    },
                    "required": ["dept_id"],
                },
            ),

            types.Tool(
                name="get_migration_ding_id_by_ding_ids",
                description="根据原dingId查询迁移后的dingId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dingId": {
                            "type": "string",
                            "description": "原普通账号的dingId。",
                        },
                    },
                    "required": ["dingId"],
                },
            )
            ,

            types.Tool(
                name="get_ding_id_by_migration_ding_id",
                description="根据迁移后的dingId查询原dingId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "migrationDingId": {
                            "type": "string",
                            "description": "迁移后企业账号的dingId。",
                        },
                    },
                    "required": ["migrationDingId"],
                },
            )
            ,
            types.Tool(
                name="get_union_id_by_migration_union_ids",
                description="根据迁移后的unionId查询原unionId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "migrationUnionId": {
                            "type": "string",
                            "description": "迁移后企业账号的unionId。企业内部应用或第三方企业应用可通过调用相关接口获取该值。",
                        },
                    },
                    "required": ["migrationUnionId"],
                },
            ),

            types.Tool(
                name="get_user_detail",
                description="调用本接口获取指定用户的详细信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "用户的userId。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。可选参数，默认值为zh_CN（中文）。支持的值：zh_CN（中文）、en_US（英文）。",
                        },
                    },
                    "required": ["userid"],
                },
            )
            ,

            types.Tool(
                name="get_user_by_mobile",
                description="根据手机号查询用户，获取用户的userId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "mobile": {
                            "type": "string",
                            "description": "用户的手机号。",
                        },
                    },
                    "required": ["mobile"],
                },
            )
            ,
            types.Tool(
                name="set_department_visibility_priority",
                description="设置通讯录部门可见性优先级。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "enable": {
                            "type": "boolean",
                            "description": "是否开启子部门设置优先，取值：true（子部门设置优先于父部门），false（默认值，父部门设置优先于子部门）。",
                        },
                    },
                    "required": ["enable"],
                },
            ),

            types.Tool(
                name="get_migration_union_id_by_union_ids",
                description="根据原unionId查询迁移后的unionId。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "unionId": {
                            "type": "string",
                            "description": "原普通账号的unionId。"
                                        "\n- 企业内部应用，调用通过免登码获取用户信息接口获取unionid参数值。"
                                        "\n- 第三方企业应用，调用通过免登码获取用户信息接口获取unionid参数值。",
                        },
                    },
                    "required": ["unionId"],
                },
            )
            ,
            types.Tool(
                name="change_main_administrator",
                description="将本组织内某企业账号有所有权的组织，转交给另一企业账号，如果接收的账号不在该组织内则自动加入。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "sourceUserId": {
                            "type": "string",
                            "description": "原企业账号userid，可通过以下方式获得：根据手机号查询企业帐号用户、创建SSO企业帐号、创建钉钉自建企业帐号、邀请其他组织企业帐号加入。",
                        },
                        "targetUserId": {
                            "type": "string",
                            "description": "接收专属账号userid，可通过以下方式获得：根据手机号查询专属帐号用户、创建SSO专属帐号、创建钉钉自建专属帐号、邀请其他组织专属帐号加入。",
                        },
                        "effectCorpId": {
                            "type": "string",
                            "description": "被转交的组织corpId。详情参见基础概念-CorpId。",
                        },
                    },
                    "required": ["sourceUserId", "targetUserId", "effectCorpId"],
                },
            ),
            types.Tool(
                name="update_department",
                description="调用本接口更新部门信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "dept_id": {
                            "type": "number",
                            "description": "部门ID，可通过获取部门列表接口获取dept_id参数值。",
                        },
                        "parent_id": {
                            "type": "number",
                            "description": "父部门ID，根部ID为1。可通过获取部门列表接口获取parent_id参数值。",
                        },
                        "hide_dept": {
                            "type": "boolean",
                            "description": "是否隐藏本部门：true表示隐藏部门，隐藏后本部门将不会显示在公司通讯录中；false表示显示部门。不传值则保持不变。",
                        },
                        "dept_permits": {
                            "type": "string",
                            "description": "指定可以查看本部门的其他部门列表。当hide_dept为true时，则此值生效。",
                        },
                        "user_permits": {
                            "type": "string",
                            "description": "指定可以查看本部门的用户userid列表。当hide_dept为true时，则此值生效。",
                        },
                        "create_dept_group": {
                            "type": "boolean",
                            "description": "是否创建一个关联此部门的企业群，默认为false即不创建。不传值则保持不变。",
                        },
                        "order": {
                            "type": "number",
                            "description": "在父部门中的排序值，order值小的排序靠前。",
                        },
                        "name": {
                            "type": "string",
                            "description": "部门名称，长度限制为1~64个字符，不允许包含字符‘-’‘，’以及‘,’。",
                        },
                        "source_identifier": {
                            "type": "string",
                            "description": "部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。",
                        },
                        "outer_dept": {
                            "type": "boolean",
                            "description": "是否限制本部门成员查看通讯录：true表示开启限制，开启后本部门成员只能看到限定范围内的通讯录；false表示不限制。不传值则保持不变。",
                        },
                        "outer_permit_users": {
                            "type": "string",
                            "description": "指定本部门成员可查看的通讯录用户userid列表。当outer_dept为true时，此参数生效。",
                        },
                        "outer_permit_depts": {
                            "type": "string",
                            "description": "指定本部门成员可查看的通讯录部门ID列表。当outer_dept为true时，此参数生效。",
                        },
                        "outer_dept_only_self": {
                            "type": "boolean",
                            "description": "本部门成员是否只能看到所在部门及下级部门通讯录：true表示只能看到所在部门及下级部门通讯录；false表示不能查看所有通讯录，在通讯录中仅能看到自己。当outer_dept为true时，此参数生效。不传值则保持不变。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言：zh_CN表示中文；en_US表示英文。",
                        },
                        "auto_add_user": {
                            "type": "boolean",
                            "description": "当部门群已经创建后，有新人加入部门时是否会自动加入该群：true表示自动加入群；false表示不会自动加入群。不传值则保持不变。",
                        },
                        "auto_approve_apply": {
                            "type": "boolean",
                            "description": "是否默认同意加入该部门的申请：true表示加入该部门的申请将默认同意；false表示加入该部门的申请需要有权限的管理员同意。",
                        },
                        "dept_manager_userid_list": {
                            "type": "string",
                            "description": "部门的主管userId列表，多个userid之间使用英文逗号分隔。",
                        },
                        "group_contain_sub_dept": {
                            "type": "boolean",
                            "description": "部门群是否包含子部门：true表示包含；false表示不包含。不传值则保持不变。",
                        },
                        "group_contain_outer_dept": {
                            "type": "boolean",
                            "description": "部门群是否包含外包部门：true表示包含；false表示不包含。不传值则保持不变。",
                        },
                        "group_contain_hidden_dept": {
                            "type": "boolean",
                            "description": "部门群是否包含隐藏部门：true表示包含；false表示不包含。不传值则保持不变。",
                        },
                        "org_dept_owner": {
                            "type": "string",
                            "description": "企业群群主的userId。",
                        },
                        "force_update_fields": {
                            "type": "string",
                            "description": "强制更新的字段，支持清空指定的字段，多个字段之间使用英文逗号分隔。目前支持字段: dept_manager_userid_list。",
                        },
                        "code": {
                            "type": "string",
                            "description": "部门编码。",
                        },
                    },
                    "required": ["dept_id"],
                },
            ),
            types.Tool(
                name="update_contact_hide_settings",
                description="新增或更新通讯录隐藏设置。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "设置名称。",
                        },
                        "description": {
                            "type": "string",
                            "description": "设置描述信息。",
                        },
                        "objectStaffIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "需要被隐藏的员工userId列表，可通过通过免登码获取用户信息接口获得userId参数值。注意：objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "objectDeptIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "需要被隐藏的部门ID列表，可通过获取部门列表接口获得dept_id参数值。注意：objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "objectTagIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "需要被隐藏的角色roleId列表，可通过获取角色列表接口获得id参数值。注意：objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "excludeStaffIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "不受本次隐藏设置影响的员工userId列表，可通过通过免登码获取用户信息接口获得userId参数值。注意：excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "excludeDeptIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "不受本次隐藏设置影响的部门ID列表，可通过获取部门列表接口获得dept_id参数值。注意：excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "excludeTagIds": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "不受本次隐藏设置影响的角色ID列表，可通过获取角色列表接口获得id参数值。注意：excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。",
                        },
                        "active": {
                            "type": "boolean",
                            "description": "该设置是否激活，true表示激活，false表示不激活。",
                        },
                        "id": {
                            "type": "number",
                            "description": "设置ID。新增时设置ID为空，修改时设置ID为需要修改的ID。",
                        },
                        "hideInUserProfile": {
                            "type": "boolean",
                            "description": "是否同时在被查看个人资料页时隐藏，true表示是，false表示否。",
                        },
                        "hideInSearch": {
                            "type": "boolean",
                            "description": "是否同时在被搜索时隐藏，true表示是，false表示否。",
                        },
                    },
                    "required": [],
                },
            ),
            types.Tool(
                name="update_enterprise_account_user_info",
                description="调用本接口更新指定的企业账号用户信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工的userId。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。可选参数。",
                        },
                        "hide_mobile": {
                            "type": "boolean",
                            "description": "是否号码隐藏。true：隐藏；false：不隐藏。可选参数。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。分机号是唯一的，企业内不能重复。可选参数。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大50个字符。可选参数。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。可选参数。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大200个字符。可选参数。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工邮箱，长度最大50个字符。员工邮箱是唯一的，企业内不能重复。可选参数。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱。需满足以下条件，此字段才生效：员工的企业邮箱已开通。可选参数。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。可选参数。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。可选参数。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门ID列表。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的排序。可选参数。",
                        },
                        "dept_title_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "员工在部门中的职位。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的职位。可选参数。",
                        },
                        "extension": {
                            "type": "string",
                            "description": "扩展属性，长度最大2000个字符。手机上最多只能显示10个扩展属性，并且在使用该参数前，需要先在钉钉管理后台设置通讯录信息增加该属性。该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid和corpid。可选参数。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。true：开启；false：不开启。可选参数。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，UNIX时间戳，单位毫秒。可选参数。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。zh_CN：中文（默认值）；en_US：英文。可选参数。",
                        },
                        "force_update_fields": {
                            "type": "string",
                            "description": "强制更新的字段，支持清空指定的字段，多个字段之间使用逗号分隔。目前支持字段: manager_userid、org_email。可选参数。",
                        },
                        "org_email_type": {
                            "type": "string",
                            "description": "企业账号员工的企业邮箱类型。profession: 标准版；base: 基础版。可选参数。",
                        },
                        "loginId": {
                            "type": "string",
                            "description": "钉钉企业账号的登录名。仅支持钉钉企业账号更新该字段，SSO企业账号暂不支持。可选参数。",
                        },
                        "exclusive_mobile": {
                            "type": "string",
                            "description": "企业账号手机号。可选参数。",
                        },
                        "avatarMediaId": {
                            "type": "string",
                            "description": "更新本组织企业账号时可指定头像MediaId，只支持jpg/png格式，可调用上传媒体文件接口获取。可选参数。",
                        },
                        "nickname": {
                            "type": "string",
                            "description": "企业账号的昵称。可选参数。",
                        },
                        "dept_position_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                            },
                            "description": "部门内任职信息。可选参数。",
                        },
                        "extension_i18n": {
                            "type": "object",
                            "description": "扩展属性的国际化值。可选参数。",
                        },
                    },
                    "required": ["userid", "dept_id_list"],
                },
            ),
            types.Tool(
                name="update_external_contact",
                description="调用本接口，更新企业外部联系人。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "contact": {
                            "type": "object",
                            "description": "外部联系人信息。",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "职位。",
                                },
                                "label_ids": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "标签列表，可调用获取外部联系人列表接口查询标签信息。每次调用最多传20个labelId。",
                                },
                                "share_dept_ids": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "共享给的部门ID，可调用获取子部门ID列表接口获取。每次调用最多传20个部门ID。",
                                },
                                "address": {
                                    "type": "string",
                                    "description": "地址。",
                                },
                                "remark": {
                                    "type": "string",
                                    "description": "备注。",
                                },
                                "follower_user_id": {
                                    "type": "string",
                                    "description": "负责人的userId。",
                                },
                                "name": {
                                    "type": "string",
                                    "description": "外部联系人的姓名。",
                                },
                                "user_id": {
                                    "type": "string",
                                    "description": "该外部联系人的userId，可调用获取外部联系人列表接口获取。",
                                },
                                "company_name": {
                                    "type": "string",
                                    "description": "外部联系人的企业名称。",
                                },
                                "share_user_ids": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "共享给的员工userid列表。每次调用最多传20个labelId。",
                                },
                            },
                            "required": [
                                "label_ids",
                                "follower_user_id",
                                "name",
                                "user_id",
                            ],
                        }
                    },
                    "required": ["contact"],
                },
            ),
            types.Tool(
                name="set_senior_mode",
                description="调用本接口设置员工的高管模式。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "seniorStaffId": {
                            "type": "string",
                            "description": "需要设置的员工userid。",
                        },
                        "open": {
                            "type": "boolean",
                            "description": "是否开启高管模式，取值：true：开启高管模式；false：关闭高管模式。",
                        },
                        "permitStaffIds": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "高管白名单员工userid列表。参数permitStaffIds、permitDeptIds、permitTagIds列表内元素之和最大为200。",
                        },
                        "permitDeptIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "高管白名单部门列表。参数permitStaffIds、permitDeptIds、permitTagIds列表内元素之和最大为200。",
                        },
                        "permitTagIds": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "高管白名单角色列表。参数permitStaffIds、permitDeptIds、permitTagIds列表内元素之和最大为200。",
                        },
                        "protectScenes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "高管拦截场景，取值：DING_SMS：短信Ding消息；DING_MSG：应用内Ding消息；CHAT：IM聊天（单聊、群聊）；CONFERENCE_VIDEO：视频会议；CONFERENCE：语音会议；VIDEO_CALL：视频通话；CONFERENCE_VOIP：语音通话；CALL：电话会议、办公电话；SEARCH：电话会议里搜索功能；CALL_CENTER：呼叫中心。",
                        },
                    },
                    "required": ["seniorStaffId", "open"],
                },
            ),
            types.Tool(
                name="set_role_member_management_scope",
                description="设定角色成员管理范围。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工在企业中的userId。",
                        },
                        "role_id": {
                            "type": "number",
                            "description": "角色ID，可以调用获取角色列表接口获取id参数值。",
                        },
                        "dept_ids": {
                            "type": "string",
                            "description": "部门ID列表，多个部门id之间使用逗号分隔。最多支持50个部门ID，不传则设置范围为所有人。",
                        },
                    },
                    "required": ["userid", "role_id"],
                },
            ),
            types.Tool(
                name="update_role_name",
                description="调用本接口，更新角色名称。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "roleId": {
                            "type": "number",
                            "description": "要更新的角色ID，可以调用获取角色列表接口获取。\"默认\"分组内的角色不支持修改，包括：负责人、主管、主管理员、子管理员。",
                        },
                        "roleName": {
                            "type": "string",
                            "description": "修改的角色名称。",
                        },
                    },
                    "required": ["roleId", "roleName"],
                },
            ),
            types.Tool(
                name="create_user",
                description="调用本接口创建新用户。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工唯一标识ID（不可修改），企业内必须唯一。长度为1~64个字符，如果不传，将自动生成一个userid。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。",
                        },
                        "mobile": {
                            "type": "string",
                            "description": "手机号码，企业内必须唯一，不可重复。如果是国际号码、中国香港、中国澳门和中国台湾地区号码，请使用+xx-xxxxxx的格式。如果公司注册地址是非中国大陆地区，则在添加中国大陆地区用户时，手机号要使用+86-xxxxxx格式。",
                        },
                        "hide_mobile": {
                            "type": "boolean",
                            "description": "是否隐藏手机号：true表示隐藏，false表示不隐藏。隐藏后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。分机号是唯一的，企业内不能重复。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大为50个字符。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大为200个字符。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工个人邮箱，长度最大50个字符。员工邮箱是唯一的，企业内不能重复。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱，长度最大100个字符。需满足以下条件，此字段才生效：员工的企业邮箱已开通。",
                        },
                        "org_email_type": {
                            "type": "string",
                            "description": "员工的企业邮箱类型。可选值：profession（标准版）、base（基础版）。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门id列表，每次调用最多传100个部门ID。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的排序。",
                        },
                        "dept_title_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "员工在部门中的职位。",
                                    },
                                },
                            },
                            "description": "员工在对应的部门中的职位。",
                        },
                        "extension": {
                            "type": "object",
                            "description": "扩展属性，可以设置多种属性，最大长度2000个字符。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。true表示开启，false表示不开启。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，Unix时间戳，单位毫秒。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。",
                        },
                        "login_email": {
                            "type": "string",
                            "description": "登录邮箱。仅适用于邮箱账号，非邮箱账号设置该字段不生效。",
                        },
                        "dept_position_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "description": "部门内任职信息。",
                            },
                        },
                        "extension_i18n": {
                            "type": "object",
                            "description": "扩展属性的国际化值。",
                        },
                    },
                    "required": ["name", "mobile", "dept_id_list"],
                },
            ),
            types.Tool(
                name="update_user_info",
                description="调用本接口更新指定的用户信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userid": {
                            "type": "string",
                            "description": "员工的userId。",
                        },
                        "name": {
                            "type": "string",
                            "description": "员工名称，长度最大80个字符。",
                        },
                        "hide_mobile": {
                            "type": "boolean",
                            "description": "是否隐藏手机号。true：隐藏；false：不隐藏。",
                        },
                        "telephone": {
                            "type": "string",
                            "description": "分机号，长度最大50个字符。分机号是唯一的，企业内不能重复。",
                        },
                        "job_number": {
                            "type": "string",
                            "description": "员工工号，长度最大50个字符。",
                        },
                        "manager_userid": {
                            "type": "string",
                            "description": "直属主管的userId。",
                        },
                        "title": {
                            "type": "string",
                            "description": "职位，长度最大200个字符。",
                        },
                        "email": {
                            "type": "string",
                            "description": "员工邮箱，长度最大50个字符。员工邮箱是唯一的，企业内不能重复。",
                        },
                        "org_email": {
                            "type": "string",
                            "description": "员工的企业邮箱。需满足以下条件，此字段才生效：员工的企业邮箱已开通。",
                        },
                        "work_place": {
                            "type": "string",
                            "description": "办公地点，长度最大100个字符。",
                        },
                        "remark": {
                            "type": "string",
                            "description": "备注，长度最大2000个字符。",
                        },
                        "dept_id_list": {
                            "type": "string",
                            "description": "所属部门ID列表。",
                        },
                        "dept_order_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dept_id": {
                                        "type": "number",
                                        "description": "部门ID。",
                                    },
                                    "order": {
                                        "type": "number",
                                        "description": "员工在部门中的排序。数值越大，排序越靠前。",
                                    },
                                },
                                "required": ["dept_id", "order"],
                            },
                            "description": "员工在对应的部门中的排序。",
                        },
                        "extension": {
                            "type": "string",
                            "description": "扩展属性，长度最大2000个字符。手机上最多只能显示10个扩展属性；如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去；该字段支持链接类型填写，并支持变量通配符自动替换（如userid和corpid）。",
                        },
                        "senior_mode": {
                            "type": "boolean",
                            "description": "是否开启高管模式，默认值false。true：开启；false：不开启。",
                        },
                        "hired_date": {
                            "type": "number",
                            "description": "入职时间，UNIX时间戳，单位毫秒。",
                        },
                        "language": {
                            "type": "string",
                            "description": "通讯录语言。zh_CN：中文（默认值）；en_US：英文。",
                        },
                        "force_update_fields": {
                            "type": "string",
                            "description": "强制更新的字段，支持清空指定的字段，多个字段之间使用逗号分隔。目前支持字段: manager_userid。",
                        },
                        "dept_position_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {},
                            },
                            "description": "部门内任职信息。",
                        },
                        "extension_i18n": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "zh_CN": {"type": "string"},
                                    "en_US": {"type": "string"},
                                    "ja_JP": {"type": "string"},
                                },
                            },
                            "description": "扩展属性的国际化值。",
                        },
                    },
                    "required": ["userid"],
                },
            ),

            types.Tool(
                name="get_owned_organizations",
                description="查询企业帐号在哪些企业下拥有创建者身份，并获取这些企业信息。",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "userId": {
                            "type": "string",
                            "description": "企业账号的userid，可通过以下四种方式获得："
                                        "1. 根据手机号查询企业帐号用户；"
                                        "2. 创建SSO企业帐号；"
                                        "3. 创建钉钉自建企业帐号；"
                                        "4. 邀请其他组织企业帐号加入。",
                        },
                    },
                    "required": ["userId"],
                },
            )
        ]

async def serve():
    _mcp_server = MCPServer(name="DingtalkContactsServer")
    dingtalk_server = DingtalkContactsServer()

    @_mcp_server.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        return dingtalk_server.list_tools()

    @_mcp_server.call_tool()
    async def handle_call_tool(
        name: str, arguments: dict[str, Any] | None = None
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        try:
            match name:
                case 'add_external_contact_old': 
                        result = await dingtalk_server.add_external_contact_old(**arguments)
                case 'add_roles_for_employees': 
                        result = await dingtalk_server.add_roles_for_employees(**arguments)
                case 'authorize_multi_org_permissions': 
                        result = await dingtalk_server.authorize_multi_org_permissions(**arguments)
                case 'authorize_org_account_visibility': 
                        result = await dingtalk_server.authorize_org_account_visibility(**arguments)
                case 'change_dingtalk_id': 
                        result = await dingtalk_server.change_dingtalk_id(**arguments)
                case 'cleanup': 
                        result = await dingtalk_server.cleanup(**arguments)
                case 'create_department_old':
                        result = await dingtalk_server.create_department_old(**arguments)
                case 'create_dingtalk_enterprise_account':
                        result = await dingtalk_server.create_dingtalk_enterprise_account(**arguments)
                case 'create_role':
                        result = await dingtalk_server.create_role(**arguments)
                case 'create_role_group':
                        result = await dingtalk_server.create_role_group(**arguments)
                case 'create_sso_user':
                        result = await dingtalk_server.create_sso_user(**arguments)
                case 'create_user_old':
                        result = await dingtalk_server.create_user_old(**arguments)
                case 'delete_contact_hide_setting':
                        result = await dingtalk_server.delete_contact_hide_setting(**arguments)
                case 'delete_department_old':
                        result = await dingtalk_server.delete_department_old(**arguments)
                case 'delete_external_contact':
                        result = await dingtalk_server.delete_external_contact(**arguments)
                case 'delete_restricted_contact_setting':
                        result = await dingtalk_server.delete_restricted_contact_setting(**arguments)
                case 'delete_role':
                        result = await dingtalk_server.delete_role(**arguments)
                case 'delete_staff_attribute_visibility_setting':
                        result = await dingtalk_server.delete_staff_attribute_visibility_setting(**arguments)
                case 'delete_user':
                        result = await dingtalk_server.delete_user(**arguments)
                case 'disable_org_account':
                        result = await dingtalk_server.disable_org_account(**arguments)
                case 'enable_org_account':
                        result = await dingtalk_server.enable_org_account(**arguments)
                case 'ensure_session':
                        result = await dingtalk_server.ensure_session(**arguments)
                case 'force_logout_org_account':
                        result = await dingtalk_server.force_logout_org_account(**arguments)
                case 'get_access_token':
                        result = await dingtalk_server.get_access_token(**arguments)
                case 'get_admin_list':
                        result = await dingtalk_server.get_admin_list(**arguments)
                case 'get_admin_scope':
                        result = await dingtalk_server.get_admin_scope(**arguments)
                case 'get_company_invite_info':
                        result = await dingtalk_server.get_company_invite_info(**arguments)
                case 'get_contact_auth_scope':
                        result = await dingtalk_server.get_contact_auth_scope(**arguments)
                case 'get_contact_hide_settings':
                        result = await dingtalk_server.get_contact_hide_settings(**arguments)
                case 'get_corp_auth_info':
                        result = await dingtalk_server.get_corp_auth_info(**arguments)
                case 'get_department_detail':
                        result = await dingtalk_server.get_department_detail(**arguments)
                case 'get_department_detail_old':
                        result = await dingtalk_server.get_department_detail_old(**arguments)
                case 'get_department_list':
                        result = await dingtalk_server.get_department_list(**arguments)
                case 'get_department_list_old': 
                        result = await dingtalk_server.get_department_list_old(**arguments)
                case 'get_department_user_detail':
                        result = await dingtalk_server.get_department_user_detail(**arguments)
                case 'get_department_user_details':
                        result = await dingtalk_server.get_department_user_details(**arguments)
                case 'get_department_user_id_list':
                        result = await dingtalk_server.get_department_user_id_list(**arguments)
                case 'get_department_user_list':
                        result = await dingtalk_server.get_department_user_list(**arguments)
                case 'get_department_user_simple':
                        result = await dingtalk_server.get_department_user_simple(**arguments)
                case 'get_employee_count':
                        result = await dingtalk_server.get_employee_count(**arguments)
                case 'get_employee_leave_records':
                        result = await dingtalk_server.get_employee_leave_records(**arguments)
                case 'get_employee_list_by_role':
                        result = await dingtalk_server.get_employee_list_by_role(**arguments)
                case 'get_enterprise_info':
                        result = await dingtalk_server.get_enterprise_info(**arguments)
                case 'get_external_contact_detail':
                        result = await dingtalk_server.get_external_contact_detail(**arguments)
                case 'get_external_contact_label_list':
                        result = await dingtalk_server.get_external_contact_label_list(**arguments)
                case 'get_external_contact_list':
                        result = await dingtalk_server.get_external_contact_list(**arguments)
                case 'get_inactive_users':
                        result = await dingtalk_server.get_inactive_users(**arguments)
                case 'get_latest_ding_index':
                        result = await dingtalk_server.get_latest_ding_index(**arguments)
                case 'get_migration_ding_id_by_ding_id':
                        result = await dingtalk_server.get_migration_ding_id_by_ding_id(**arguments)
                case 'get_migration_union_id_by_union_id':
                        result = await dingtalk_server.get_migration_union_id_by_union_id(**arguments)
                case 'get_new':
                        result = await dingtalk_server.get_new(**arguments)
                case 'get_old':
                        result = await dingtalk_server.get_old(**arguments)
                case 'get_org_account_status':
                        result = await dingtalk_server.get_org_account_status(**arguments)
                case 'get_original_ding_id_by_migration_ding_id':
                        result = await dingtalk_server.get_original_ding_id_by_migration_ding_id(**arguments)
                case 'get_owned_organizations':
                        result = await dingtalk_server.get_owned_organizations(**arguments)
                case 'get_parent_departments_by_dept':
                        result = await dingtalk_server.get_parent_departments_by_dept(**arguments)
                case 'get_parent_departments_by_user':
                        result = await dingtalk_server.get_parent_departments_by_user(**arguments)
                case 'get_restriction_settings':
                        result = await dingtalk_server.get_restriction_settings(**arguments)
                case 'get_role_detail_old':
                        result = await dingtalk_server.get_role_detail_old(**arguments)
                case 'get_role_group_list':
                        result = await dingtalk_server.get_role_group_list(**arguments)
                case 'get_role_list':
                        result = await dingtalk_server.get_role_list(**arguments)
                case 'get_senior_settings':
                        result = await dingtalk_server.get_senior_settings(**arguments)
                case 'get_sub_department_ids':
                        result = await dingtalk_server.get_sub_department_ids(**arguments)
                case 'get_union_id_by_migration_union_id':
                        result = await dingtalk_server.get_union_id_by_migration_union_id(**arguments)
                case 'get_user_attribute_visibility_settings':
                        result = await dingtalk_server.get_user_attribute_visibility_settings(**arguments)
                case 'get_user_by_mobile':
                        result = await dingtalk_server.get_user_by_mobile(**arguments)
                case 'get_user_contact_info':
                        result = await dingtalk_server.get_user_contact_info(**arguments)
                case 'get_user_detail':
                        result = await dingtalk_server.get_user_detail(**arguments)
                case 'get_user_detail_old':
                        result = await dingtalk_server.get_user_detail_old(**arguments)
                case 'get_user_id_by_unionid_old':
                        result = await dingtalk_server.get_user_id_by_unionid_old(**arguments)
                case 'invite_other_org_user':
                        result = await dingtalk_server.invite_other_org_user(**arguments)
                case 'post_new':
                        result = await dingtalk_server.post_new(**arguments)
                case 'post_old':
                        result = await dingtalk_server.post_old(**arguments)
                case 'remove_roles_for_employees':
                        result = await dingtalk_server.remove_roles_for_employees(**arguments)
                case 'search_department_id':
                        result = await dingtalk_server.search_department_id(**arguments)
                case 'search_user_id':
                        result = await dingtalk_server.search_user_id(**arguments)
                case 'set_department_visibility_priority':
                        result = await dingtalk_server.set_department_visibility_priority(**arguments)
                case 'set_role_member_scope':
                        result = await dingtalk_server.set_role_member_scope(**arguments)
                case 'set_senior_mode':
                        result = await dingtalk_server.set_senior_mode(**arguments)
                case 'set_user_attribute_visibility':
                        result = await dingtalk_server.set_user_attribute_visibility(**arguments)
                case 'transfer_main_administrator':
                        result = await dingtalk_server.transfer_main_administrator(**arguments)
                case 'update_contact_hide_settings':
                        result = await dingtalk_server.update_contact_hide_settings(**arguments)
                case 'update_contact_restriction_settings':
                        result = await dingtalk_server.update_contact_restriction_settings(**arguments)
                case 'update_department_old':
                        result = await dingtalk_server.update_department_old(**arguments)
                case 'update_external_contact':
                        result = await dingtalk_server.update_external_contact(**arguments)
                case 'update_role_name':
                        result = await dingtalk_server.update_role_name(**arguments)
                case 'update_user_info_old':
                        result = await dingtalk_server.update_user_info_old(**arguments)
                
            return [types.TextContent(type="text", text=str(result))]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]

    async with stdio_server() as (read_stream, write_stream):
        try:
            await _mcp_server.run(
                read_stream,
                write_stream,
                _mcp_server.create_initialization_options(),
            )
        except Exception as e:
            raise
        finally:
            await dingtalk_server.cleanup()
    
class ServerWrapper():
    """A wrapper to compat with mcp[cli]"""
    def run(self):
        asyncio.run(serve())

server = ServerWrapper()