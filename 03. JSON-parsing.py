import requests
from requests import JSONDecodeError

if __name__ == '__main__':
    response = requests.get("https://playground.learnqa.ru/api/hello", params={
        "name": "User"
    })

    try:
        parsed_response_text = response.json()
        print(parsed_response_text["answer"])
    except JSONDecodeError:
        print("Responce is not a JSON format")
