from tkinter import *

COLORS = {
    "dark": "#161A20",
    "blue": "#0060E5",
    "grey": "#363E4D",
    "black": "#242933",
    "text": "#CBE1FF"
}

root = Tk()
root.title("Calculator Wagle")
root.config(width=400, height=800, background=COLORS["dark"], padx=10, pady=10)

title = Label(text="PyCalculator Wagle",
              background=COLORS["blue"], foreground="#ffffff", padx=16, pady=12, font=("Roboto", 20, "bold"))
title.grid(row=0, column=0, columnspan=4, pady=20)


def get_current():
    currrent = str(answer["text"])
    return currrent


def clear_all():
    answer.config(text="")


def backspace():
    currrent = get_current()
    new = currrent[:-1]
    answer.config(text=new)


def calculate():
    currrent = get_current()
    try:
        equals_to = round(eval(currrent), 2)
        answer.config(text=equals_to)
    except SyntaxError:
        answer.config(text="Syntax Error")
    except ZeroDivisionError:
        answer.config(text="Infinity")


def button_click(button):
    currrent = get_current()
    new = f"{currrent}{button}"
    answer.config(text=new)


# Answer Label
answer = Label(
    text="",
    background=COLORS["dark"], foreground="#ffffff", font=("Roboto", 36, "bold"), width=10,  wraplength=350)
answer.grid(row=1, column=0, pady=30, columnspan=4)


# Other Operations
ac_button = Button(
    text="AC", foreground=COLORS["text"], background=COLORS["grey"], activebackground=COLORS["grey"], activeforeground=COLORS["text"], width=12, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=clear_all)
ac_button.grid(row=2, column=0, columnspan=2, pady=3, padx=2)

back_icon = PhotoImage(file="icons/back.png")
backspace_button = Button(image=back_icon, foreground=COLORS["text"], background=COLORS["grey"], activebackground=COLORS["grey"], activeforeground=COLORS["text"], width=92, height=66, font=(
    "Roboto", 16),  pady=20, borderwidth=0, highlightthickness=0, command=backspace)
backspace_button.grid(row=2, column=2, padx=1)

equals_button = Button(
    text="=", foreground=COLORS["text"], background=COLORS["blue"], activebackground=COLORS["blue"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=calculate)
equals_button.grid(row=6, column=3, pady=3)


# Main Operation
divide_button = Button(
    text="/", foreground=COLORS["text"], background=COLORS["blue"], activebackground=COLORS["blue"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("/"))
divide_button.grid(row=2, column=3, padx=2)

multiply_button = Button(
    text="X", foreground=COLORS["text"], background=COLORS["blue"], activebackground=COLORS["blue"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("*"))
multiply_button.grid(row=3, column=3)

add_button = Button(
    text="+", foreground=COLORS["text"], background=COLORS["blue"], activebackground=COLORS["blue"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("+"))
add_button.grid(row=5, column=3, pady=1)

subtract_button = Button(
    text="-", foreground=COLORS["text"], background=COLORS["blue"], activebackground=COLORS["blue"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("-"))
subtract_button.grid(row=4, column=3, pady=3)


# Numbers
point_button = Button(
    text=".", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("."))
point_button.grid(row=6, column=2, pady=3)

zero_button = Button(
    text="0", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=12, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("0"))
zero_button.grid(row=6, column=0, padx=3, pady=3, columnspan=2)

one_button = Button(
    text="1", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("1"))
one_button.grid(row=5, column=0, padx=3, pady=1)

two_button = Button(
    text="2", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("2"))
two_button.grid(row=5, column=1, pady=1)

three_button = Button(
    text="3", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("3"))
three_button.grid(row=5, column=2, padx=3, pady=1)

four_button = Button(
    text="4", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("4"))
four_button.grid(row=4, column=0, padx=3, pady=3)

five_button = Button(
    text="5", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("5"))
five_button.grid(row=4, column=1, pady=3)

six_button = Button(
    text="6", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("6"))
six_button.grid(row=4, column=2, padx=3, pady=3)

seven_button = Button(
    text="7", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("7"))
seven_button.grid(row=3, column=0, padx=3)

eight_button = Button(
    text="8", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("8"))
eight_button.grid(row=3, column=1)

nine_button = Button(
    text="9", foreground=COLORS["text"], background=COLORS["black"], activebackground=COLORS["black"], activeforeground=COLORS["text"], width=5, font=("Roboto", 16), borderwidth=0, border=0, highlightthickness=0, pady=20, command=lambda: button_click("9"))
nine_button.grid(row=3, column=2, padx=3)


# Keybaord Bindings
root.bind('0', lambda _: button_click("0"))
root.bind('1', lambda _: button_click("1"))
root.bind('2', lambda _: button_click("2"))
root.bind('3', lambda _: button_click("3"))
root.bind('4', lambda _: button_click("4"))
root.bind('5', lambda _: button_click("5"))
root.bind('6', lambda _: button_click("6"))
root.bind('7', lambda _: button_click("7"))
root.bind('8', lambda _: button_click("8"))
root.bind('9', lambda _: button_click("9"))
root.bind('.', lambda _: button_click("."))

root.bind('+', lambda _: button_click("+"))
root.bind('-', lambda _: button_click("-"))
root.bind('*', lambda _: button_click("*"))
root.bind('/', lambda _: button_click("/"))

root.bind('<Return>', lambda _: calculate())
root.bind('<BackSpace>', lambda _: backspace())


root.mainloop()
