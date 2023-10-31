# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:28:57 2023
Basics: Entries, Functions, and Lambdas
@author: svetlana shopova
"""

import tkinter
from tkinter import END

#set window
root = tkinter.Tk()
root.title('Basics Entries')
root.iconbitmap('thinking.ico')
root.geometry("500x500")
root.resizable(0, 0)

#Define functions
def make_label():
    '''Print a label in the app '''
    if text_entry.get():
        lbl_text = tkinter.Label(output_frame, text = text_entry.get(), 
                                 bg = '#FF0000', fg = '#FFFFFF', font = ('Arial', 25) )
        lbl_text.pack()
        text_entry.delete(0, END)

def count_up(number):
   '''Count up on the app'''
   global value
   
   lbl_text_1 = tkinter.Label(output_frame, text=number, bg='#FF0000',
                              font=('Areal', 14), fg='#FFFFFF')
   lbl_text_1.pack()
   
   value = number +1
   

#Define frames
input_frame = tkinter.Frame(root, bg='#0000FF', width = 500, height = 100)
output_frame = tkinter.Frame(root, bg = '#FF0000', width = 500, height = 400)

input_frame.pack(padx = 10, pady = 10)
output_frame.pack(padx = 10, pady = (0,10))


#add input
text_entry = tkinter.Entry(input_frame, width = 40)
text_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
#make the grid to stay the same size not the size of the widgets it contains
input_frame.grid_propagate(0)

print_button = tkinter.Button(input_frame, text="Print", command=make_label)
print_button.grid(row = 0, column = 1, padx = 5, pady = 5, ipadx = 30)

#Keep output frame size 
output_frame.propagate(0)

#pass a parameter with lambda
value = 0

count_button = tkinter.Button(input_frame, text = 'Count', command=lambda:count_up(value)) 
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()