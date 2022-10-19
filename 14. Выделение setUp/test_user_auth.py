import pytest
import requests


class TestUserAuth:
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login",
                                  data=data)
        assert "auth_sid" in response1.cookies, 'There is no auth cookie in the response1'
        assert "x-csrf-token" in response1.headers, 'There is no CSRF token header in the response1'
        assert "user_id" in response1.json(), 'There is no user_id in the response1'

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user_positive(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), 'There is no user_id in the second response'
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == self.user_id_from_auth_method, 'User id from auth method is not equal ' \
                                                                           'to user id from check method'

    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_auth_user_negative(self, condition):
        if condition == "no_cookie":
            response = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert "user_id" in response.json(), "There is no user_id in the second response"

        user_id_from_check_method = response.json()["user_id"]

        assert user_id_from_check_method == 0, f'User is authorized with condition {condition}'
