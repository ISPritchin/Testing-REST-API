import requests


def print_response(response):
    print(response.text)
    print(response.status_code)
    print(dict(response.cookies))


if __name__ == '__main__':
    # делаем запрос с неправильным паролем
    response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data={})

    # делаем запрос с правильным паролем
    # response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data={
    #     "login": "secret_login",
    #     "password": "secret_pass",
    # })

    print_response(response)

    cookies = {}
    if response.cookies is not None:
        cookies = response.cookies

    response = requests.post("https://playground.learnqa.ru/api/check_auth_cookie",
                             cookies=cookies)
    print_response(response)
