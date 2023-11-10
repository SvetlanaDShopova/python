# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:04:42 2023

Basics of  radio buttons
@author: Svetlana Shopova
"""

import tkinter
from tkinter import IntVar



#Define the window
root = tkinter.Tk()
root.title("Basics Radio Button")
root.geometry("350x350")
root.resizable(0,0)
root.iconbitmap("thinking.ico")

def make_label():
    '''Print to the screen'''
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text="1 one 1")
    elif number.get() == 2:
        num_label = tkinter.Label(output_frame, text="2 two 2")
    
    num_label.pack()
    

#Define  Frimes
input_frame = tkinter.LabelFrame(root, text='This is fun!', width=350, height=100)
output_frame = tkinter.Frame(root, width=350, height=250)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=10)

number = IntVar()
number.set(1)
#Define widgets
radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one!', variable=number, value=1)
radio_2 = tkinter.Radiobutton(input_frame, text='Print the number two!', variable=number, value=2)
btn_print = tkinter.Button(input_frame, text="Print the number", command=make_label)

radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
btn_print.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


#run main window loop
root.mainloop()

