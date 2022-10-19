from lib.assertion import Assertions
from lib.base_case import BaseCase
from preparator import prepare_register_data
from lib.project_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        register_data = prepare_register_data()

        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinlotov@example.com'
        register_data = prepare_register_data(email)

        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == \
               f"Users with email '{email}' already exists", \
               f"Unexpected response content {response.content}"
