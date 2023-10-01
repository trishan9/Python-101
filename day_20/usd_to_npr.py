from tkinter import *

window = Tk()
window.config(padx=20, pady=40)
window.title("USD to NPR Converter")

def convert_usd_to_npr():
    usd = int(input.get())
    converted_npr = round(usd * 133.16)
    npr["text"] = converted_npr

input = Entry(width=10)
input.grid(column=1, row=0)

usd_label = Label(text="USD", font=("Inter"))
usd_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Inter"))
is_equal_to.grid(column=0, row=1)

npr = Label(text="0", font=("Inter"))
npr.grid(column=1, row=1)

npr_label = Label(text="NPR", font=("Inter"))
npr_label.grid(column=2, row=1)

convert_button = Button(text="Calculate", command=convert_usd_to_npr)
convert_button.grid(column=1, row=2)

window.mainloop()