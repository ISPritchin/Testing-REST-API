import pytest

from lib.base_case import BaseCase
from lib.assertion import Assertions
from preparator import prepare_register_data
from lib.project_requests import MyRequests


class TestUserEdit(BaseCase):
    @pytest.mark.parametrize("field, value", [
        ("firstName", "Ivan"),
        ("lastName", "Pritchin")
    ])
    def test_edit_just_created_user(self, field: str, value: str):
        register_data = prepare_register_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # Login
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={field: value})

        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(
            response4,
            field,
            value,
            f"Wrong {field} of the user after edit"
        )
