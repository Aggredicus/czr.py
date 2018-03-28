# czr.py is a Caeser Cipher Tool started by Aggredicus on 3/27/18

# The tkinter GUI template was pulled from University of Cape Town with the following attribution:
# © Copyright 2013, 2014, University of Cape Town and individual contributors. This work is released under the CC BY-SA 4.0 licence. Revision 8e685e710775. 

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

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

class Czr:

    def __init__(self, master):
        self.master = master
        master.title("Caeser Cipher Tool")

        self.message = 'Enter your message here.'
        self.message_2 = 'Enter your letter shift value here.'
        self.entered_number = 'Enter your message here.'
        self.entered_number_2 = "Enter your letter shift value here.'

        self.message_label_text = IntVar()
        self.message_label_text.set(self.message)
        self.message_label = Label(master, textvariable=self.message_label_text)

        self.message_label_text_2 = IntVar()
        self.message_label_text_2.set(self.message_2)
        self.message_label_2 = Label(master, textvariable=self.message_label_text_2)
        
        self.label = Label(master, text="Message:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry_2 = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        self.encrypt_button = Button(master, text="Encrypt", command=lambda: self.update("encrypt"))
        self.decrypt_button = Button(master, text="Decrypt", command=lambda: self.update("decrypt"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.message_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.message_label_2.grid(row=2, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.entry_2.grid(row=3, column=0, columnspan=3, sticky=W+E)
        
        self.encrypt_button.grid(row=4, column=0)
        self.decrypt_button.grid(row=4, column=1)
        self.reset_button.grid(row=4, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 'Type your message here.'
            return True

        try:
            self.entered_number = str(new_text)
            return True
        except ValueError:
            return False
    
    def update(self, method):
        if method == "encrypt":
            self.message = czr_full_encrypt(self.entered_number_2, self.entered_number)
        elif method == "decrypt":
            self.message = czr_full_encrypt(-self.entered_number_2, self.entered_number)
        else: # reset
            self.message = 'Enter your message here.'

        self.message_label_text.set(self.message)
        self.message_label_text_2.set(self.message_2)
        self.entry.delete(0, END)

root = Tk()
my_gui = Czr(root)
root.mainloop()
