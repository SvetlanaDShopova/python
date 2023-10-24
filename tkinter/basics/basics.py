# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:36:01 2023

@author: svetlana shopova
"""
import tkinter

# define window
root = tkinter.Tk()

#change title of the window
root.title("Window basics")

#change the icon of the window
root.iconbitmap('thinking.ico')

#change the size of the window width x height
root.geometry('300x500')

#prevent window of resizing (x , y ) 1 - allow resizing
root.resizable(0, 1)

#change options of a component
root.config(bg ='lightblue')

#Second window
top = tkinter.Toplevel();

top.title("Second window")

top.geometry('300x250+500+50')

top.config(bg = 'yellow')



# Run root window's main loop
root.mainloop()

