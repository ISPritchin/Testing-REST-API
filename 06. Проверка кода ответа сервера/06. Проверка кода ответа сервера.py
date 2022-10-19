import requests

if __name__ == '__main__':
    response = requests.get("https://playground.learnqa.ru/api/get_500")
    print(response.text)
    print(response.status_code)

    # запрос к URI, которого нет в API
    response = requests.get("https://playground.learnqa.ru/api/blablabla")
    print(response.text)
    print(response.status_code)

    response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
    print(response.text)
    print(response.status_code)
    print(response.history)
    print(response.history[0].url)

    response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
    print(response.text)
    print(response.status_code)
    print(response.history)
