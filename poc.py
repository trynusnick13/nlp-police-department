import requests

r = requests.post(
    # "https://nlp-police-department-service.herokuapp.com/application",
    "http://192.168.1.34:5000/application",

    json={
        'application': "AAAAAAA",
    }
)
print(r.json().get("result", ""))
