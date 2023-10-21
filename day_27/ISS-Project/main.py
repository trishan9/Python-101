import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 27.734329
MY_LONG = 85.316139

GMAIL_USER = "trishan.python@gmail.com"
GMAIL_PASS = "jren gygk dmzm rrvu"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT + 5 <= iss_latitude or MY_LAT - 5 <= iss_latitude) and (MY_LONG + 5 <= iss_longitude or MY_LONG - 5 <= iss_longitude):
        return True
    else:
        return False


def is_dark():
    time_now = datetime.now()
    current_time = time_now.hour

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

    if current_time >= sunset:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_dark() and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(GMAIL_USER, GMAIL_PASS)
            connection.sendmail(from_addr=GMAIL_USER,
                                to_addrs="nirjalthapa5@gmail.com", msg="Go, Look the Sky!! ISS is above you")
    else:
        print("Not Close")
