import requests

r = requests.post(
    "https://nlp-police-department-service.herokuapp.com/application",

    json={
        'application': "I was attacked and killed",
    }
)
print(r.json().get("result", ""))
