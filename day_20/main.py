from tkinter import *

window = Tk()
window.title("Trishan Wagle")
window.minsize(width=700, height=500)

def button_click():
    my_label["text"] = input.get()


my_label = Label(text="Hello Tkinter", font=("Inter", 16))
my_label.grid(column=0, row=0)

my_button = Button(text="Click Me!", fg="white", bg="blue", command=button_click)
my_button.grid(column=1, row=1)

my_button = Button(text="New Button", fg="white", bg="blue", command=button_click)
my_button.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)

window.mainloop()