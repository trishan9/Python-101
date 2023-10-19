import os
import random
import smtplib
import pandas as pd
from datetime import datetime
from email.message import EmailMessage

GMAIL_USER = "trishan.python@gmail.com"
GMAIL_PASS = "jren gygk dmzm rrvu"


def check_birthday():
    '''checks for birthday'''
    birthday_data = get_birthday_data()
    current_date = get_current_date()
    for birthday in birthday_data:
        if current_date["month"] == birthday["month"] and current_date["day"] == birthday["day"]:
            data = {
                "name": birthday["name"],
                "email_address": birthday["email"]
            }
            generate_birthday_message(data)


def get_birthday_data():
    '''returns birthday data by reading csv file'''
    birthday_df = pd.read_csv("birthdays.csv")
    birthday_data = []
    for _, row in birthday_df.iterrows():
        birthday_detail = {
            "name": row.first_name,
            "email": row.email,
            "month": row.month,
            "day": row.day
        }
        birthday_data.append(birthday_detail)
    return birthday_data


def get_current_date():
    '''returns today's date'''
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return {"year": year, "month": month, "day": day}


def generate_birthday_message(user_data):
    user_name = user_data["name"]
    user_email = user_data["email_address"]
    letter_templates = os.listdir("letter_templates")
    current_template = random.choice(letter_templates)
    file_path = f"letter_templates/{current_template}"
    with open(file_path, "r") as file:
        content = file.read()
        message = content.replace("[NAME]", user_name)
    send_email(user_email, message)


def send_email(email_to, email):
    '''Sends email to desired user'''
    message = generate_email(email_to, email)
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=GMAIL_USER, password=GMAIL_PASS)
    connection.send_message(message)


def generate_email(email_to, email):
    '''Returns email message by processing message and email address'''
    message = EmailMessage()
    message["Subject"] = "Birthday Wish"
    message["From"] = GMAIL_USER
    message["To"] = email_to
    message.set_content(email)
    return message


check_birthday()
