import requests

API_URL = "https://api.sheety.co/d5097729a97d009f9b509907eef9921a/python/sheet1"
HEADERS = {
    "Authorization": "Bearer trishansecret123@"
}

response = requests.get(API_URL, headers=HEADERS)
result = response.json()["sheet1"]

print(result)


def add_data(data):
    response = requests.post(API_URL, headers=HEADERS, json=data)
    print(response.json())


add_data({
    "sheet1": {
        "name": "Smu Pokharel",
        "email": "smu@gmail.com"
    }
})
