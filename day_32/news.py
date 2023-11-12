import requests
from datetime import datetime

COUNTRY = "in"
CATEGORY = "technology"
API_KEY = "6cae578ae02e438dab4aea7af8e45b50"

response = requests.get(
    "https://newsapi.org/v2/top-headlines", params=f"country={COUNTRY}&category={CATEGORY}&apiKey={API_KEY}")
response.raise_for_status()
result = response.json()["articles"]

for article in result:
    print(article)

formatted_date = datetime.now()
print(formatted_date.strftime("%Y/%m/%d"))
