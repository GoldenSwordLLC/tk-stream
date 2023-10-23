from tkinter import IntVar, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def validate_number(x) -> bool:
    the_variable = number_variable.get()
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False


def validate_alpha(x) -> bool:
    invalid = False
    valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for each_char in ''.join(x):
        if each_char not in valid_characters:
            invalid = True
        else:
            invalid = False
    if not invalid:
        if len(x) >= 65:
            x = string_variable.get()[0:63]
            string_variable.set(x)
        else:
            string_variable.set(x)
    return invalid


root = ttk.Window()
frame = ttk.Frame(root, padding=10)
frame.pack(fill=BOTH, expand=YES)

# register the validation callback
digit_func = root.register(validate_number)
alpha_func = root.register(validate_alpha)

# validate numeric entry
ttk.Label(frame, text="Enter a number").pack()
number_variable = IntVar()
num_entry = ttk.Entry(frame, validate="key", textvariable=number_variable, validatecommand=(digit_func, '%P'))
num_entry.pack(padx=10, pady=10, expand=True)

# validate alpha entry
ttk.Label(frame, text="Enter a letter").pack()
string_variable = StringVar()
string_variable.set('')
let_entry = ttk.Entry(frame, validate="key", textvariable=string_variable, validatecommand=(alpha_func, '%P'))
let_entry.pack(padx=10, pady=10, expand=True)

root.mainloop()
