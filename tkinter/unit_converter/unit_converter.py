# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:52:28 2023
Convert units
@author: Svetlana Shopova
"""
import tkinter
from tkinter import StringVar, ttk, END, DISABLED

#Define window
window = tkinter.Tk()
window.title("Unit Converter")
window.iconbitmap('ruler.ico')
window.geometry("570x250")
window.resizable(0, 0)


#color and font settings
field_font = ('Georgia', 12, 'bold')
field_color = '#D8DBE2'
bg_color = '#A9BCD0'
button_color = "#58A4B0"
font_color  = "#373F51"
window.config(bg=bg_color)
#drop down lists
temperature_list = ["Celsius", "Fahrenheit", "Kelvin"]
length_list = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Mile", "Yard",
          "Foot", "Inch", "Nautical Mile"]
mass_list = [ "Kilogram", "Gram", "Miligram", "Microgram", 
             "Long ton", "Short ton", "Stone", "Pound", "Ounce", "Metric Ton"]

#conversion helpers
length_conversion = {"Kilometer":1000, "Meter": 1, "Centimeter":0.01, "Millimeter":0.001, 
            "Mile":1609.344, "Yard": 0.9144,
          "Foot":0.3048, "Inch":0.0254, "Nautical Mile":1852}
mass_conversion = {"Metric Ton":1000000, "Kilogram":1000, "Gram":1,
                   "Miligram":0.001,
                   "Microgram":0.0001, 
             "Long ton":1016041.909, "Short ton":907184.74, "Stone":6350.29318,
             "Pound":453.59237 , "Ounce": 28.34952313}

#Functions
output_value = StringVar()
category = StringVar()
category.set("temperature")

def clearOutputField(event):
    output_field.delete(0, END)


def create_dropdownlist(list_measures):   
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", foreground= "orange", 
                    background= field_color)
    global input_dropdown
    global output_dropdown
    input_dropdown = ttk.Combobox(window, value=list_measures,
                      font=field_font, justify='center', background=field_color,
                      foreground=font_color)
    output_dropdown = ttk.Combobox(window, value=list_measures,
                      font=field_font, justify='center', background=field_color,
                      foreground=font_color)
    input_dropdown.set(list_measures[0])
    output_dropdown.set(list_measures[1])
    input_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
    input_dropdown.option_add('*TCombobox*Listbox.background', field_color)
    input_dropdown.option_add('*TCombobox*Listbox.font', field_font)
    input_dropdown.option_add('*TCombobox*Listbox.fieldbackground', field_color)
    input_dropdown.bind('<<ComboboxSelected>>', clearOutputField)
    output_dropdown.bind('<<ComboboxSelected>>', clearOutputField)
    
    output_dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
    output_dropdown.option_add('*TCombobox*Listbox.background', field_color)
    output_dropdown.option_add('*TCombobox*Listbox.font', field_font)
    output_dropdown.option_add('*TCombobox*Listbox.fieldbackground', field_color)
    to_label = tkinter.Label(window, text="to", 
                              bg=bg_color, fg=font_color, font=('Georgia', 16))


    input_dropdown.grid(row=2, column=0, padx=10)
    to_label.grid(row=2, column=1)
    output_dropdown.grid(row=2, column=2, padx=10)

def set_mesures_list():
    '''Change dropdown list with mesures when different type of
    measure is choosen'''
    global input_dropdown
    global output_dropdown
    
    if category.get() == 'temperature':        
        create_dropdownlist(temperature_list)
    elif category.get() == 'length':        
        create_dropdownlist(length_list)
    elif category.get() == 'mass': 
        create_dropdownlist(mass_list)
        
   
    to_label = tkinter.Label(window, text="to", 
                             bg=bg_color, fg=font_color, font=('Georgia', 16))
    input_dropdown.grid(row=2, column=0, padx=10)
    to_label.grid(row=2, column=1)
    output_dropdown.grid(row=2, column=2, padx=10)
    
def convert():
    '''Convert units'''
    output_field.config(state='normal')
    output_field.delete(0, END)
    user_quantity = float(input_field.get())
    from_unit = input_dropdown.get()
    to_unit = output_dropdown.get()    
    #find used list    
    if category.get() == 'temperature':
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                output_value = user_quantity * (9/5) + 32
            elif to_unit == "Kelvin":
                output_value = user_quantity + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == "Celsius":
                output_value = (user_quantity - 32) * (5/9)
            elif to_unit == "Kelvin":
                output_value = (user_quantity + 459.67) * (5/9)
        else:
            if to_unit == "Celsius":
                output_value = user_quantity - 273.15
            elif to_unit == 'Fahrenheit':
                output_value = (user_quantity * 9/5) - 459.67                
    elif category.get() == 'length':
         #convert length         
         output_value =user_quantity*( 
             length_conversion[from_unit]/length_conversion[to_unit])
    elif category.get() == 'mass':  
        #convert mass
        output_value =user_quantity*( 
            mass_conversion[from_unit]/mass_conversion[to_unit])
        
    output_field.insert(0, str(round(output_value,2)))
    output_field.config(state='disabled')
    input_field.focus_set()
    
    
input_field = tkinter.Entry(window, width=20, font=field_font, 
            bg=field_color, borderwidth=3, fg=font_color)
output_field = tkinter.Entry(window, width=20, font=field_font, 
            bg=field_color, textvariable=output_value, 
            borderwidth=3, fg=font_color, state=DISABLED)
equal_label = tkinter.Label(window, text="=", 
             bg=bg_color, fg=font_color, font=('Georgia', 16, 'bold'))

input_field.grid(row=0, column=0, padx=15, pady=20)
equal_label.grid(row=0, column=1, padx=15, pady=20)
output_field.grid(row=0, column=2, padx=10, pady=20)


input_field.insert(0, 'Enter your quatity...')

#Radio buttons for category computation

temperature = tkinter.Radiobutton(window, text="Temperature",
               variable=category, value="temperature", bg=bg_color, 
               font=field_font, fg=font_color , 
               activeforeground="#FFFFFF",
               command=set_mesures_list)
length = tkinter.Radiobutton(window, text="Length",
               variable=category, value="length", bg=bg_color, 
               font=field_font, fg=font_color, 
               activeforeground=field_color, 
               command=set_mesures_list)

mass = tkinter.Radiobutton(window, text="Mass",
               variable=category, value="mass", bg=bg_color, 
               font=field_font, fg=font_color,
               activeforeground=font_color, 
               command=set_mesures_list)


temperature.grid(row=1, column=0, padx=5, pady=10)
mass.grid(row=1, column=1, padx=5, pady=10)
length.grid(row=1, column=2, padx=20, pady=10, ipadx=30, sticky="w")                                     

#Drop down for  metrics
create_dropdownlist(temperature_list)

#Create  conversion button
convert_button = tkinter.Button(window, text="Convert", 
                                font= field_font, bg=font_color, fg=field_color,
                                command=convert)
convert_button.grid(row=3, column=0, columnspan=3, pady=(40,5), ipadx=50)
#run my loop of the window
window.mainloop()
