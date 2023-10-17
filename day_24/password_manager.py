import os
import pandas
from tkinter import *
from tkinter import messagebox
from random import shuffle, choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from pyperclip import copy

# Constants
WHITE = "#ffffff"
FONT_NAME = "Courier"

# Tkinter Config
window = Tk()
window.title("Passwordifier")
window.config(padx=100, pady=50, bg=WHITE)

# Canvas Config
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


# Password Generator
def generate_password():
    password_input.delete(0, END)
    lower = choices(list(ascii_lowercase), k=4)
    upper = choices(list(ascii_uppercase), k=4)
    numbers = choices(list(digits), k=2)
    symbols = choices(list(punctuation), k=2)

    password_list = lower + upper + numbers + symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    copy(password)


# Add Password to CSV File
def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error",
                             message="All the fields are required")
    else:
        password_data = {
            "Website": [website],
            "Email": [email],
            "Password": [password]
        }

        is_saving = messagebox.askokcancel(
            title="Please verify", message=f"Username: {email}\nPassword: {password}\nWebsite: {website}\n\nDo you want to save this?")

        if is_saving:
            password_df = pandas.DataFrame(password_data)
            if os.path.exists("password_data.csv"):
                password_df.to_csv("password_data.csv", mode="a",
                                   index=False, header=False)
            else:
                password_df.to_csv("password_data.csv", index=False)


# UI Setup
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)


website_input = Entry(width=44)
website_input.grid(row=1, column=1, columnspan=2, pady=5)

email_input = Entry(width=44)
email_input.grid(row=2, column=1, columnspan=2, pady=5)
email_input.insert(0, "mailtotrishan@gmail.com")

password_input = Entry(width=24)
password_input.grid(row=3, column=1, pady=5)


generate_password_button = Button(
    text="Generate Password", bg=WHITE, pady=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg=WHITE, width=41,
                    pady=0, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
