import requests

r = requests.post(
    "http://127.0.0.1:5000/application",

    json={
        'application': "I was attacked and killed",
        'type': 'issue',
        'action': 'show'
    }
)
print(r.json().get("result", ""))
