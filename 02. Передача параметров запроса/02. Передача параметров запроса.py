import requests

if __name__ == '__main__':
    PAYLOAD = {
        "name": "user"
    }

    response = requests.get("https://playground.learnqa.ru/api/hello", params=PAYLOAD)
    print(response.text)
