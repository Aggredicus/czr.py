# czr.py is a Caeser Cipher Tool started by Aggredicus on 3/27/18
# Feel free to adapt these simple tools to your own purposes, but please credit me (Aggredicus) while doing so!

# The tkinter GUI was adapted from the tkinter documentation at the following URL: http://www.tkdocs.com/tutorial/firstexample.html#code
# Tkinter Docs Attribution below:
# "All material on this site is Copyright (C) 2007-2017 Mark Roseman. This work is licensed under a Creative Commons Attribution-Noncommercial-Share Alike 2.5 Canada License. If you have any questions regarding the use of the material on this site, including possible uses not covered by the license, please don't hesitate to email Mark."

from tkinter import *
from tkinter import ttk

# Caeser Cipher

# Converts a string containing a letter into an integer representation
def num_encrypt(arg):
    if (arg.isalpha() == True):
        lowercase_letter = arg.lower()
        letter_code = ord(lowercase_letter) - 96
        return int(letter_code)
    else:
        return str(arg)
    
# Converts an integer representation of a letter into a string containing a letter
def num_decrypt(arg):
    # Checks to see if arg is a non-integer
    if (isinstance(arg, int) != True):
        print('num_decrypt received a non-integer of value ' + arg)
        return arg
    else:
        # The letter_code variable used to be for converting to int, but I kept it for
        # aesthetic reasons after implementing the section above.
        lowercase_letter = chr(arg + 96)
        return lowercase_letter

# Shifts a letter <shift_value> places to the right for each letter
def czr_encrypt(shift_value, letter):
    if (letter.isalpha() == False):
        return letter
    else:
        letter_to_num = num_encrypt(str(letter))
        shifted_num = letter_to_num + shift_value
        # Handles cipher shifts past z
        if (shifted_num > 26):
            shifted_num -= 26
        # Handles cipher shifts before a
        elif (shifted_num < 1):
            shifted_num += 26
        num_to_letter = num_decrypt(shifted_num)
        return num_to_letter

# Shifts a letter <shift_value> places to the left for each letter
def czr_decrypt(shift_value, letter):
    if (letter.isalpha() == False):
        return letter
    else:
        letter_to_num = num_encrypt(str(letter))
        shifted_num = letter_to_num - shift_value
        # Handles cipher shifts past z
    if (shifted_num > 26):
        shifted_num -= 26
    # Handles cipher shifts before a
    elif (shifted_num < 1):
        shifted_num += 26
    num_to_letter = num_decrypt(shifted_num)
    return num_to_letter

# Takes in the Caeser shift value and a full string to shift the full string <shift_value> places to the right
def czr_full_encrypt(shift_value, full_string):
    arr = list(full_string)
    encrypted_arr = []
    i = 0
    while i < len(arr):
        encrypted_arr.append(czr_encrypt(shift_value, arr[i]))
        i += 1
    final_string = ''.join(encrypted_arr)
    return final_string

# Tkinter GUI

def czr_gui_encrypt(*args):
    try:
        input_string = str(message.get())
        input_shift = int(shift.get())
        message_decrypted.set(czr_full_encrypt(input_shift, input_string))
    except ValueError:
        pass
    
root = Tk()
root.title("Caeser Shift Tool")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

shift = StringVar()
message = StringVar()
message_decrypted = StringVar()

shift_entry = ttk.Entry(mainframe, width=7, textvariable=shift)
shift_entry.grid(column=2, row=1, sticky=(W, E))
message_entry = ttk.Entry(mainframe, width=7, textvariable=message)
message_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=message_decrypted).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Encrypt", command=czr_gui_encrypt).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text='Shift Value:').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Message:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Decrypted message:").grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

shift_entry.focus()
root.bind('<Return>', czr_gui_encrypt)

root.mainloop()
