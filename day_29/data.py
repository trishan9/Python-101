import requests

result = requests.get(
    "https://opentdb.com/api.php?amount=10&category=18&type=boolean")
result.raise_for_status()
raw_data = result.json()

question_data = raw_data["results"]
