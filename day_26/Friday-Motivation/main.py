import smtplib
from random import choice
from datetime import datetime
from email.message import EmailMessage

GMAIL_CREDENTIALS = {
    "user": "trishan.python@gmail.com",
    "password": "jren gygk dmzm rrvu"
}

subscribers = ["mailtotrishan@gmail.com", "nischaymaharjann@gmail.com",
               "abiralstha333@gmail.com", "nirjalthapa5@gmail.com", "satishwagle32@gmail.com"]

msg = EmailMessage()
now = datetime.now()
week_day = now.weekday()

if week_day == 4:
    with open("quotes.txt") as file:
        motivations = file.readlines()
        motivation = choice(motivations)

        msg["Subject"] = "Friday Motivation"
        msg["From"] = GMAIL_CREDENTIALS["user"]
        msg["To"] = subscribers
        msg.set_content(
            f"Friday Motivation for Today: {motivation}\n\n- By Trishan PyMailer")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=GMAIL_CREDENTIALS["user"], password=GMAIL_CREDENTIALS["password"])
        connection.send_message(msg)
