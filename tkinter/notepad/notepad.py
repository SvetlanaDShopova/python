# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:53:13 2024

@author: Svetlana Shopova
"""
import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog, ttk, PhotoImage

########## Define window ##########
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("notepad.ico")
root.geometry("600x600")
root.resizable(1,1)
root.config(bg="#D5D7D5")

########## Define fonts and colors ##########
text_color = "#161811"
menu_color = "#989C94"

########## Define dropdown list values #########
font_family = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_options = ['none', 'bold', 'italic']
font_size = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
########### Define functions ##########  

def create_dropdown(list_values, r=0, c=0):
    """Create dropdown menues for font family, font size and type"""
    dropdown = ttk.Combobox(menu_frame, value=list_values, width=13,
              font=text_color, justify='center', background=menu_color)
    dropdown.option_add('*TCombobox*Listbox.Justify', 'center')
    dropdown.set(list_values[0])
    
    dropdown.grid(row=r, column=c, padx=5, pady=5)    
    return dropdown
########## Define Layout ##########

### Frames ###
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)

menu_frame.grid(row=0, column=0, padx=5, pady=5)
text_frame.grid(row=1, column=0,padx=5, pady=5)


### Layout for menu frame ###

#button new

#btn_new = create_button("new.png", 0, 0)

img_new = ImageTk.PhotoImage(Image.open("new.png"))  
btn_new =  tkinter.Button(menu_frame, image=img_new, height=30, width=30,
           bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_new.grid(row = 0, column=0, padx=5, pady=5)

img_open = ImageTk.PhotoImage(Image.open("open.png"))  
btn_open =  tkinter.Button(menu_frame, image=img_open, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_open.grid(row = 0, column=1, padx=5, pady=5)

img_save = ImageTk.PhotoImage(Image.open("save.png"))  
btn_save =  tkinter.Button(menu_frame, image=img_save, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_save.grid(row = 0, column=2, padx=5, pady=5)

box_font_family = create_dropdown(font_family, 0, 3)

box_font_size = create_dropdown(font_size, 0, 4)

box_font_options = create_dropdown(font_options, 0, 5)

#Run the root's main loop
root.mainloop()