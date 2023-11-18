from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Tkinter Revise")
root.config(padx=8)

tkinter_icon = PhotoImage(file="icons/tk.png")
heading = Label(root, text="Tkinter Revise!",
                image=tkinter_icon, compound="left", font=("Helvetica", 20), padx=5)
heading.grid(row=0, column=0, pady=10)

color = ""
file = ""


def agree_terms():
    print(isAgree.get())


def select_gender():
    print(gender.get())


def check_age():
    print(age.get())


def choose_color():
    global color
    color = colorchooser.askcolor()[1]


def open_file():
    global file
    file = filedialog.askopenfilename()


def submit_data():
    is_submitting = messagebox.askokcancel(
        title="Are you sure?", message="Are you sure that you want to submit your data?")

    if not is_submitting:
        return ""

    all_skills = [skills_list.get(index)
                  for index in skills_list.curselection()]
    skills = ", ".join(all_skills)
    print(f"Terms Accepted: {isAgree.get()}\nGender: {gender.get()}\nName: {name.get()}\nPassword: {password.get()}\nAge: {age.get()}\nColor: {color}\nFeedback: {feedback.get('1.0', END)}CV: {file}\nSkills: {skills}")


isAgree = BooleanVar()
terms = Checkbutton(root, text="I agree to the terms and conditions",
                    variable=isAgree, onvalue=True, offvalue=False, font=("Helvetica", 16), command=agree_terms)
terms.grid(row=1, column=0, pady=10)


gender = StringVar()
genders = ["male", "female", "others"]
for i, option in enumerate(genders):
    print(i)
    gender_radio = Radiobutton(root, text=option.capitalize(), font=(
        "Helvetica", 16), value=option, variable=gender, command=select_gender)
    gender_radio.grid(row=2 + i, column=0, pady=10)


name_label = Label(root, text="Your Name", font=("Helvetica", 12))
name_label.grid(row=6, column=0, pady=5)
name = Entry(root)
name.grid(row=7, column=0)

password_label = Label(root, text="Password", font=("Helvetica", 12))
password_label.grid(row=8, column=0, pady=5)
password = Entry(root, show="*")
password.grid(row=9, column=0)

age_label = Label(root, text="Age", pady=8)
age_label.grid(row=10, column=0)
age = Scale(root, from_=18, to=49, tickinterval=3)
age.grid(row=11, column=0)


skills_label = Label(root, text="Skills", pady=6)
skills_label.grid(row=12, column=0)

skills_list = Listbox(root, selectmode=MULTIPLE)
skills_list.insert(1, "ReactJS")
skills_list.insert(2, "NodeJS")
skills_list.insert(3, "Express")
skills_list.insert(4, "MongoDB")
skills_list.insert(5, "PostgreSQL")
skills_list.grid(row=13, column=0)
skills_list.config(height=skills_list.size())

color_button = Button(root, text="Your favorite Color",
                      pady=6, command=choose_color)
color_button.grid(row=14, column=0, pady=6)

feedback_level = Label(root, text="Your Feedback")
feedback_level.grid(row=15, column=0, pady=6)

feedback = Text(root, background="#f5f5f5", height=8, width=30)
feedback.grid(row=16, column=0)

open_file_button = Button(root, text="Your CV",
                          pady=6, command=open_file)
open_file_button.grid(row=17, column=0, pady=6)

submit_button = Button(text="Submit", font=(
    "Helvetica", 18), command=submit_data)
submit_button.grid(row=18, column=0, pady=10)

root.mainloop()
