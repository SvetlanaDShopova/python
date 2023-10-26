# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:03:14 2023
Basics: Buttons and the Grid
@author: svetlana shopova
"""
import tkinter

#Define window
root = tkinter.Tk()
root.title('Button Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)

#Define layout
btn_1 = tkinter.Button(root, text = "Name")
btn_1.grid(row = 0, column = 0)

btn_2 = tkinter.Button(root, text = "Time", bg = "#00FFFF")
btn_2.grid(row = 0, column = 1)

#change color of the button if clicked
btn_3 = tkinter.Button(root, text = "Place", bg = '#00ffff', activebackground='#ff0000')
btn_3.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 15)

#span the button in three columns
btn_4 = tkinter.Button(root, text = 'Day', bg = 'black', fg = 'white', borderwidth = 5)
btn_4.grid(row = 1, column = 0, columnspan = 3, sticky='WE')

#collection of buttons
test_1 = tkinter.Button(root, text = "test")
test_2 = tkinter.Button(root, text = "test")
test_3 = tkinter.Button(root, text = "test")
test_4 = tkinter.Button(root, text = "test")
test_5 = tkinter.Button(root, text = "test")
test_6 = tkinter.Button(root, text = "test")

test_1.grid(row = 2, column = 0, padx = 5, pady = 5)
test_2.grid(row = 2, column = 1, padx = 5, pady = 5)
test_3.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = 'W')
test_4.grid(row = 3, column = 0, padx = 5, pady = 5)
test_5.grid(row = 3, column = 1, padx = 5, pady = 5)
test_6.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = 'W')



#Call root window's main loop
root.mainloop()

