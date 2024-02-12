# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:53:13 2024

@author: Svetlana Shopova
"""
import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, BOTH, IntVar, scrolledtext, END, messagebox, filedialog, ttk, PhotoImage

########## Define window ##########
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("notepad.ico")
root.geometry("600x600")
root.resizable(1,1)
root.config(bg="#D5D7D5")

########## Define fonts and colors ##########
text_color = "#161811"
menu_color = "#EAEBEA"
text_background="#FFFFFF"
dropdown_font=("Areal", 9)
########## Define dropdown list values #########
families = ['Consolas','Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_options = ['normal', 'bold', 'italic']
sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
########### Define functions ##########  
def change_font(event):
    """Change font of the selected text"""
   
    
    if box_font_options.get() == 'normal':
        my_font = (box_font_family.get(),box_font_size.get())
    else:
        my_font = (box_font_family.get(),box_font_size.get(), box_font_options.get())
    #change the font style
    #input_text.config(font=my_font)
    sel_start, sel_end = input_text.tag_ranges("sel")
    input_text.tag_add( input_text.get(sel_start, sel_end), *map(str, input_text.tag_ranges("sel")))
    input_text.tag_config(input_text.get(sel_start, sel_end), font=my_font)    
    
    
def create_dropdown(list_values, r=0, c=0, width=0):
    """Create dropdown menues for font family, font size and type"""
    dropdown = ttk.Combobox(menu_frame, value=list_values, width=width,
              font=dropdown_font, justify='center', 
              background=menu_color)
    dropdown.option_add('*TCombobox*Listbox.Justify', 'left')
    dropdown.set(list_values[0])
    dropdown.bind("<<ComboboxSelected>>", change_font)    
    
    dropdown.grid(row=r, column=c, padx=3, pady=5)  
    
    return dropdown


    
########## Define Layout ##########

### Frames ###
menu_frame = tkinter.Frame(root, bg=menu_color, width=500)
text_frame = tkinter.Frame(root, bg=text_background)

menu_frame.pack(  pady=(0,5), fill=BOTH)
text_frame.pack(padx=5, pady=5)


### Layout for menu frame ###

img_new = ImageTk.PhotoImage(Image.open("new.png"))  
btn_new =  tkinter.Button(menu_frame, image=img_new, height=30, width=30,
           bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_new.grid(row = 0, column=0, padx=5, pady=5)

img_open = ImageTk.PhotoImage(Image.open("open.png"))  
btn_open = tkinter.Button(menu_frame, image=img_open, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_open.grid(row = 0, column=1, padx=5, pady=5)

img_save = ImageTk.PhotoImage(Image.open("save.png"))  
btn_save = tkinter.Button(menu_frame, image=img_save, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_save.grid(row = 0, column=2, padx=5, pady=5)

img_print = ImageTk.PhotoImage(Image.open("print.png"))  
btn_print = tkinter.Button(menu_frame, image=img_print, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_print.grid(row = 0, column=3, padx=5, pady=5)

styl = ttk.Style()
styl.configure('TSeparator', background='#000000')
separator = ttk.Separator(menu_frame, orient='vertical', style='TSeparator')
separator.grid(row=0, column=4, padx=5, pady=5, sticky="ns")

img_cut = ImageTk.PhotoImage(Image.open("cut.png"))  
btn_cut =  tkinter.Button(menu_frame, image=img_cut, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_cut.grid(row = 0, column=5, padx=5, pady=5)

img_copy = ImageTk.PhotoImage(Image.open("copy.png"))  
btn_copy = tkinter.Button(menu_frame, image=img_copy, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_copy.grid(row = 0, column=6, padx=5, pady=5)

img_paste = ImageTk.PhotoImage(Image.open("paste.png"))  
btn_paste = tkinter.Button(menu_frame, image=img_paste, height=30, width=30,
        bg=menu_color, borderwidth=0, activebackground = menu_color)
btn_paste.grid(row = 0, column=7, padx=5, pady=5)


separator2 = ttk.Separator(menu_frame, orient='vertical', style='TSeparator')
separator2.grid(row=0, column=8, padx=5, pady=5, sticky="ns")

font_family = StringVar()
font_family.set(families[0])
box_font_family = create_dropdown(families, 0, 9, width=16)


font_size=IntVar()
font_size.set(sizes[0])
box_font_size = create_dropdown(sizes, 0, 10, width = 4)

font_option = StringVar()
font_option.set(font_options[0])
box_font_options = create_dropdown(font_options, 0, 11, width= 7)


### Layout for test frame  ###
my_font = (font_family.get(), font_size.get())

# Create input_text as a scrolltext
#Set default width and height to be more that the window size

input_text = tkinter.scrolledtext.ScrolledText(text_frame,
        bg=text_background, font=my_font, width=1000, height=100,
    highlightthickness = 0, borde=None ) 

input_text.pack(padx=5, pady=5)


#Run the root's main loop
root.mainloop()