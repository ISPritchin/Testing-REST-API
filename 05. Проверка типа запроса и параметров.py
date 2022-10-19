import requests

# put-запрос
response = requests.put("https://playground.learnqa.ru/api/check_type")
print(response.text)

# get с параметрами
response = requests.get("https://playground.learnqa.ru/api/check_type",
                        params={
                            "param1": "value1",
                            "param2": "value2"
                        })
print(response.text)

# post с параметрами
response = requests.post("https://playground.learnqa.ru/api/check_type",
                         data={
                             "param1": "value1",
                             "param2": "value2"
                         })
print(response.text)
