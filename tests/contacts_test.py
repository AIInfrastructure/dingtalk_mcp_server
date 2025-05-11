import unittest
from unittest.mock import AsyncMock, patch

# Assuming contacts.py contains a class called ContactsAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')  # Adjust the path to import the DingtalkContactsServer class
from dingtalk.contacts import DingtalkContactsServer

class TestContactsAPI(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        """Setup method to initialize the ContactsAPI instance."""
        self.contacts_api = DingtalkContactsServer()

    async def asyncTearDown(self):
        await self.contacts_api.cleanup()
        return await super().asyncTearDown()

    async def test_get_user_detail(self):
        result = await self.contacts_api.get_employee_count(True)
        print(result)
       

    @patch("dingtalk.contacts.DingtalkContactsServer.post_old", new_callable=AsyncMock)
    async def test_create_department_success(self, mock_post_old):
        # Mock response data
        mock_post_old.return_value = {"errcode": 0, "errmsg": "ok", "dept_id": 12345}

        # Call the function with test parameters
        result = await self.contacts_api.create_department_old(
            name="Engineering",
            parent_id=1,
            hide_dept=False,
            dept_permits="",
            user_permits="",
            outer_dept=False,
            outer_dept_only_self=False,
            create_dept_group=False,
            auto_approve_apply=True,
            order=1,
            source_identifier="eng_team",
            code="ENG"
        )

        # Assertions
        self.assertEqual(result["dept_id"], 12345)
        mock_post_old.assert_called_once()

    @patch("dingtalk.contacts.DingtalkContactsServer.post_old", new_callable=AsyncMock)
    async def test_get_department_user_details_success(self, mock_get_new):
        # Mock response data
        mock_get_new.return_value = {
            "users": [
                {
                    "userid": "123",
                    "name": "John Doe",
                    "email": "john@example.com"
                }
            ],
            "next_cursor": 100
        }

        result = await self.contacts_api.get_department_user_details(
            dept_id=12345,
            cursor=0,
            size=10
        )

        self.assertIn("users", result)
        self.assertEqual(len(result["users"]), 1)
        mock_get_new.assert_called_once()
