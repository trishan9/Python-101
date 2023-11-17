from tkinter import *

COLORS = {
    "dark": "#161A20",
    "blue": "#0060E5",
    "grey": "#363E4D",
    "black": "#242933",
    "text": "#CBE1FF"
}

root = Tk()
root.title("Calculator")
root.config(width=400, height=800, background=COLORS["dark"], padx=10, pady=10)

title = Label(text="Calculator",
              background=COLORS["blue"], foreground="#ffffff", padx=16, pady=6, font=("Roboto", 10, "bold"))
title.grid(row=0, column=0, columnspan=4)

answer_entry = Entry(
    background=COLORS["dark"], foreground="#ffffff", font=("Roboto", 20, "bold"), borderwidth=0)
answer_entry.grid(row=1, column=0, columnspan=4, pady=30)


root.mainloop()
