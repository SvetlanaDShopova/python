# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:53:13 2024

@author: Svetlana Shopova
"""
import tkinter

#define window
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("notepad.ico")
root.geometry("600x600")
root.resizable(0,0)
root.config(bg="#D5D7D5")

#Define fonts and colors
text_color = "#161811"
menu_color = "#989C94"

#Define functions 


#Define Frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)


root.mainloop()