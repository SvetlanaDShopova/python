# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:52:28 2023
Convert units
@author: Svetlana Shopova
"""
import tkinter
from tkinter import StringVar, DISABLED, ttk

#Define window
window = tkinter.Tk()
window.title("Unit Converter")
window.iconbitmap('ruler.ico')
window.geometry("550x250")
window.resizable(0, 0)


#color and font settings
field_font = ('Georgia', 11)
field_color = '#D8DBE2'
bg_color = '#373F51'
button_color = "#58A4B0"
window.config(bg=bg_color)
#drop down lists
temperature_list = ["Celsius", "Fahrenheit", "Kelvin"]
length_list = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Mile", "Yard",
          "Foot", "Inch", "Nautical Mile"]
mass_list = ["Metric Ton", "Kilogram", "Gram", "Miligram", "Microgram", 
             "Long ton", "Short ton", "Stone", "Pound", "Ounce"]

#Functions
output_value = StringVar()
category = StringVar()
category.set("temperature")
from_choice = StringVar()
to_choice = StringVar()

def create_dropdownlist(list_measures):   
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", foreground= "orange", 
                    background= field_color)
    global input_dropdown
    global output_dropdown
    input_dropdown = ttk.Combobox(window, value=list_measures,
                      font=field_font, justify='center', background=field_color,
                      foreground=bg_color)
    output_dropdown = ttk.Combobox(window, value=list_measures,
                      font=field_font, justify='center', background=field_color,
                      foreground=bg_color)
    input_dropdown.set(list_measures[0])
    output_dropdown.set(list_measures[0])
    input_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
    input_dropdown.option_add('*TCombobox*Listbox.background', field_color)
    input_dropdown.option_add('*TCombobox*Listbox.font', field_font)
    input_dropdown.option_add('*TCombobox*Listbox.fieldbackground', field_color)
    
    
    output_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
    output_dropdown.option_add('*TCombobox*Listbox.background', field_color)
    output_dropdown.option_add('*TCombobox*Listbox.font', field_font)
    output_dropdown.option_add('*TCombobox*Listbox.fieldbackground', field_color)
    to_label = tkinter.Label(window, text="to", 
                              bg=bg_color, fg=field_color, font=('Georgia', 16))


    input_dropdown.grid(row=2, column=0, padx=10)
    to_label.grid(row=2, column=1)
    output_dropdown.grid(row=2, column=2, padx=10)

def set_mesures_list():
    '''Change dropdown list with mesures when different type of
    measure is choosen'''
    global input_dropdown
    global output_dropdown
    
    if category.get() == 'temperature':
        print("I change something: "+ category.get() )
        create_dropdownlist(temperature_list)
    elif category.get() == 'length':
        print("I change something: "+ category.get() )
        create_dropdownlist(length_list)
    elif category.get() == 'mass':        
        print("I change something: "+ category.get() )
        create_dropdownlist(mass_list)
        
   
    to_label = tkinter.Label(window, text="to", 
                             bg=bg_color, fg=field_color, font=('Georgia', 16))
    input_dropdown.grid(row=2, column=0, padx=10)
    to_label.grid(row=2, column=1)
    output_dropdown.grid(row=2, column=2, padx=10)


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

temperature = tkinter.Radiobutton(window, text="Temperature",
               variable=category, value="temperature", bg=bg_color, 
               font=field_font, fg=field_color , activebackground=button_color,
               activeforeground="#FFFFFF", selectcolor=button_color,
               command=set_mesures_list)
length = tkinter.Radiobutton(window, text="Length",
               variable=category, value="length", bg=bg_color, 
               font=field_font, fg=field_color, activebackground=button_color,
               activeforeground=field_color, selectcolor=button_color,
               command=set_mesures_list)

mass = tkinter.Radiobutton(window, text="Mass",
               variable=category, value="mass", bg=bg_color, 
               font=field_font, fg=field_color, activebackground=button_color,
               activeforeground=field_color, selectcolor=button_color,
               command=set_mesures_list)


temperature.grid(row=1, column=0, padx=5, pady=10)
mass.grid(row=1, column=1, padx=5, pady=10)
length.grid(row=1, column=2, padx=20, pady=10, ipadx=30, sticky="w")                                     

#Drop down for  metrics
create_dropdownlist(temperature_list)
# input_dropdown = ttk.Combobox(window, value=temperature_list,
#                   font=field_font, justify='center', background=field_color,
#                   foreground=bg_color)
# output_dropdown = ttk.Combobox(window, value=temperature_list,
#                   font=field_font, justify='center', background=field_color,
#                   foreground=bg_color)
# input_dropdown.set(temperature_list[0])
# output_dropdown.set(temperature_list[0])
# input_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
# output_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
# to_label = tkinter.Label(window, text="to", 
#                           bg=bg_color, fg=field_color, font=('Georgia', 16))


# input_dropdown.grid(row=2, column=0, padx=10)
# to_label.grid(row=2, column=1)
# output_dropdown.grid(row=2, column=2, padx=10)

#Create  conversion button
convert_button = tkinter.Button(window, text="Convert", 
                                font= field_font, bg=button_color)
convert_button.grid(row=3, column=0, columnspan=3, pady=(40,5), ipadx=50)
#run my loop of the window
window.mainloop()
