import json

if __name__ == '__main__':
    STRING_AS_JSON_FORMAT = """ 
    {
        "answer" : "Hello, User"
    }
    """

    obj = json.loads(STRING_AS_JSON_FORMAT)
    print(obj["answer"])
