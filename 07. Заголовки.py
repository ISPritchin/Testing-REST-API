import requests
from requests import JSONDecodeError

if __name__ == '__main__':
    response = requests.get("https://playground.learnqa.ru/api/show_all_headers")

    print(response.text)    # Заголовки запроса
    print(response.headers) # Заголовки ответа
