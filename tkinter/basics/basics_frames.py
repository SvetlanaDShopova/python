# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:42:05 2023
Basics: Frames

@author: svetlana shopova
"""
import tkinter
from tkinter import BOTH

#Define window
root = tkinter.Tk()
root.title("Basics Frames")
root.geometry("500x500")
root.resizable(0,0)




#Define frames
pack_frame = tkinter.Frame(root, bg = "red")
grid_frame_1 = tkinter.Frame(root, bg = 'blue')
grid_frame_2 = tkinter.LabelFrame(root, text = "Grid system rues", borderwidth = 5)

#Pack frames onto root
pack_frame.pack(fill = BOTH, expand = True)
grid_frame_1.pack(fill = 'x', expand = True)
grid_frame_2.pack(fill = BOTH, expand = True, padx = 10, pady = 10)

#pack frame
tkinter.Label(pack_frame, text = "text").pack()
tkinter.Label(pack_frame, text = "text1").pack()
tkinter.Label(pack_frame, text = "text2").pack()

#Grid 1 layout
tkinter.Label(grid_frame_1, text = "text1").grid(row = 0, column = 0)
tkinter.Label(grid_frame_1, text = "text2").grid(row = 1, column = 1)
tkinter.Label(grid_frame_1, text = "text3").grid(row = 2, column = 2)

#Grid 2
tkinter.Label(grid_frame_2, text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row = 0, column = 0, sticky='WE')

#set window's main loop
root.mainloop()
