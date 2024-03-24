import requests

parameters = {
    "amount": 25,
    "type": "any type"
}

response = requests.get(url="https://opentdb.com/api.php?amount=25&category=30&difficulty=easy&type=multiple", params=parameters)
question_data = response.json()["results"]
