# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:11:57 2023
Hello world 
Icon from http://www.iconsmind.com
@author: svetlana shopova
"""
import tkinter
from tkinter import BOTH, StringVar, END
from PIL import ImageTk, Image

#Define window
window = tkinter.Tk()
window.title("Hello GUI World!")
window.geometry("400x400")
window.resizable(0, 0)
window.iconbitmap("wave.ico")

#Define font and colors
window_color = "#FFE19C"
input_color = "#DB9D47"
output_color = "#FF784F"
window.config(bg=window_color)
output_font = ("Georgia", 12)
input_font = ("Georgia", 11)

#Functions
def submit_name():
    """Say hellow to the user"""
    
    if case_style.get() == 'normal':
        lbl_output = tkinter.Label(output_frame, text="Hello " 
          + name.get() + "! Keep learning Tkinter!", bg=output_color, font=output_font)
    else:
        lbl_output = tkinter.Label(output_frame, text=("Hello " 
         + name.get() + "! Keep learning Tkinter!").upper(),  bg=output_color, font=output_font)
    lbl_output.pack()
    
    name.delete(0, END)

    
#Layout 
#Frames
input_frame = tkinter.LabelFrame(window, bg=input_color)
output_frame = tkinter.LabelFrame(window, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#Widgets
name = tkinter.Entry(input_frame, text="Enter yout name", width=20, 
                     font=input_font)
btn_submit = tkinter.Button(input_frame, text="Submit", command=submit_name,
                            font=input_font)
name.grid(row=0, column=0, padx=20, pady=10)
btn_submit.grid(row=0,column=1, padx=20, pady=10, ipadx=20)

#Radio buttons for text display
case_style = StringVar()
case_style.set("normal")
low_case = tkinter.Radiobutton(input_frame, text="Normal Case",
               variable=case_style, value="normal", bg=input_color, 
               font=input_font)
upper_case = tkinter.Radiobutton(input_frame, text="Upper Case",
               variable=case_style, value="upper", bg=input_color, 
               font=input_font)
low_case.grid(row=1, column=0, pady=(0,10))
upper_case.grid(row=1, column=1, pady=(0,10))

#Add an image into output frame
img_smile = ImageTk.PhotoImage(Image.open("smile.png"))
lbl_smile = tkinter.Label(output_frame, image=img_smile, bg=output_color)
lbl_smile.pack()



#Run  window loop
window.mainloop()