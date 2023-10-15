import math
from tkinter import *
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 1
pomodoros = 0
timer = None


# ---------------------------- TKINTER AND CANVAS SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro GUI Application")
window.config(padx=100, pady=75, bg=YELLOW)
canvas = Canvas(width=360, height=260, bg=YELLOW, highlightthickness=0)


def reset_timer():
    global reps, timer, pomodoros
    reps = 1
    pomodoros = 0
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_label, text="00:00")
    check_mark.config(text="")
    window.after_cancel(timer)


def end_pomodoro():
    reset_timer()
    title.config(text="4 Pomodoros Completed🎉", fg=PINK)


def set_timer_duration():
    if reps % 8 == 0:
        title.config(text="Long Break", fg=RED)
        timer_duration = LONG_BREAK_MIN * 60
    elif reps % 2 == 0:
        title.config(text="Short Break", fg=PINK)
        timer_duration = SHORT_BREAK_MIN * 60
    else:
        title.config(text="Work!", fg=GREEN)
        timer_duration = WORK_MIN * 60
    start_timer(timer_duration)


def start_timer(duration):
    global reps, timer, pomodoros
    minutes = math.floor(duration / 60)
    seconds = math.floor(duration % 60)

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_label, text=f"{minutes}:{seconds}")

    if duration > 0:
        timer = window.after(1000, start_timer, duration - 1)
    else:
        if reps % 2 != 0:
            pomodoros += 1
            checks = ""
            for _ in range(0, pomodoros):
                checks += "✔"
            check_mark.config(text=checks)

        reps += 1
        if reps <= 8:
            playsound('sound.wav')
            set_timer_duration()
        else:
            playsound('sound.wav')
            end_pomodoro()


# ---------------------------- UI SETUP ------------------------------- #
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(row=0, column=1)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(180, 130, image=tomato_image)

timer_label = canvas.create_text(
    180, 155, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0,
                      bg="#ffffff", command=set_timer_duration)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0,
                      bg="#ffffff", command=reset_timer)
reset_button.grid(row=2, column=2)

pomodoros_count = Label(text="Pomodoros:", bg=YELLOW,
                        font=(FONT_NAME, 18, "bold"))
pomodoros_count.grid(row=3, column=1)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(row=4, column=1)


window.mainloop()
