from typing import Any, List

from requests import Response
import json


class Assertions:
    @staticmethod
    def get_json_as_dict(response):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Responce is not in JSON format. Response text is {response.text}'

        return response_as_dict

    @staticmethod
    def assert_code_status(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            f'Unexpected status code! \n' \
            f'Expected: {expected_status_code} \n' \
            f'Actual: {response.status_code} \n'

        return Assertions

    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value: Any, error_message: str):
        response_as_dict = Assertions.get_json_as_dict(response)

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        assert response_as_dict[name] == expected_value, error_message

        return Assertions

    @staticmethod
    def assert_json_has_key(response: Response, name: str):
        response_as_dict = Assertions.get_json_as_dict(response)

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"

        return Assertions

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str):
        response_as_dict = Assertions.get_json_as_dict(response)

        assert name not in response_as_dict, f"Response JSON shouldn't have key {name}. But it's present"

        return Assertions

    @staticmethod
    def assert_json_has_keys(response: Response, include_keys: List[str], exclude_keys=None):
        if exclude_keys is None:
            exclude_keys = []

        for key in include_keys:
            Assertions.assert_json_has_key(response, key)
        for key in exclude_keys:
            Assertions.assert_json_has_not_key(response, key)

        return Assertions
