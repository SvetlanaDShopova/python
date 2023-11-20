# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:52:28 2023
Convert units
@author: Svetlana Shopova
"""
import tkinter
from tkinter import StringVar, DISABLED

#Define window
window = tkinter.Tk()
window.title("Unit Converter")
window.iconbitmap('ruler.ico')
window.geometry("500x350")
window.resizable(0, 0)


#color and font settings
field_font = ('Georgia', 11)
field_color = '#D8DBE2'
bg_color = '#373F51'
button_color = "#58A4B0"
window.config(bg=bg_color)

#Functions
output_value = StringVar()

#Layout
input_field = tkinter.Entry(window, width=20, font=field_font, 
            bg=field_color, borderwidth=3, fg=bg_color)
output_field = tkinter.Entry(window, width=20, font=field_font, 
            bg=field_color, textvariable=output_value, state=DISABLED,
            borderwidth=3, fg=bg_color)
equal_label = tkinter.Label(window, text="=", 
             bg=bg_color, fg='#D8DBE2', font=('Georgia', 16))

input_field.grid(row=0, column=0, padx=15, pady=20)
equal_label.grid(row=0, column=1, padx=15, pady=20)
output_field.grid(row=0, column=2, padx=10, pady=20)


input_field.insert(0, 'Enter your quatity...')

#Radio buttons for category computation
category = StringVar()
category.set("temperature")
temperature = tkinter.Radiobutton(window, text="Temperature",
               variable=category, value="temperature", bg=bg_color, 
               font=field_font, fg=field_color , activebackground=button_color,
               activeforeground="#FFFFFF", selectcolor=button_color)
length = tkinter.Radiobutton(window, text="Length",
               variable=category, value="length", bg=bg_color, 
               font=field_font, fg=field_color, activebackground=button_color,
               activeforeground=field_color, selectcolor=button_color)

mass = tkinter.Radiobutton(window, text="Mass",
               variable=category, value="mass", bg=bg_color, 
               font=field_font, fg=field_color, activebackground=button_color,
               activeforeground=field_color, selectcolor=button_color)
volume = tkinter.Radiobutton(window, text="Volume",
               variable=category, value="volume", bg=bg_color, 
               font=field_font, fg=field_color, activebackground=button_color,
               activeforeground=field_color, selectcolor=button_color )

temperature.grid(row=1, column=0, padx=5, pady=10)
mass.grid(row=1, column=1, padx=5, pady=10)
volume.grid(row=1, column=2, padx=5, pady=10)
length.grid(row=2, column=0, padx=20, pady=10, ipadx=30, sticky="w")                                     

#Drop down for  
from_choice = StringVar()
to_choice = StringVar()

#run my loop of the window
window.mainloop()
