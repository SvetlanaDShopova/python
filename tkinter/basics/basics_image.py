# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:58:28 2023
Basic images 
@author: svetlana shopova
"""

import tkinter
from PIL import ImageTk, Image

#Window setting
root = tkinter.Tk()
root.title("Basic Images")
root.geometry("700x700")
root.iconbitmap("thinking.ico")

#Define functions
def make_image():
    '''Using PIL for jpg '''
    #need to keep always refernce of inage out of the function
    global cat_image
    cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
    cat_label = tkinter.Label(root, image=cat_image)
    cat_label.pack()

#basics ... works for png
my_image = tkinter.PhotoImage(file="shield.png")
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_btn = tkinter.Button(root, image=my_image)
my_btn.pack()

make_image()
#run main loop
root.mainloop()