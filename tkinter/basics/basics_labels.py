# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:54:58 2023

Explore labels and Pack system

@author:  svetlana shopova
"""

import tkinter

root = tkinter.Tk()

#set window settings
root.title("Label Basics")
root.iconbitmap("thinking.ico")
root.geometry("400x400")
root.resizable(0,0)
root.config(bg="lightblue")

#create widgets
label_1 = tkinter.Label(root, text="Hello my name is Svetlana")
label_1.pack()

label_2 = tkinter.Label(root, text="New Label", font=('Arial', 18, 'bold'))
label_2.pack()

label_3 = tkinter.Label()
label_3.config(text='Label 3')
label_3.config(font=('Georgia', 10))
label_3.config(bg='#FF0000')
#add padding between widgets
label_3.pack(padx=10, pady=50)

label_4 = tkinter.Label(root, text='Hello my name is John', bg="#000000", fg='white')
#add only padding on the bottom pady(x,y)
# and pading inside the widget ipadx, ipady
# anchor widget to one of the cardinal directions - w(est), e(ast),n(orth),s(south)
label_4.pack(pady=(0,10), ipadx=50, ipady=10, anchor='w')

#expand widget to the borders of the window
label_5 = tkinter.Label(root, text='I am a hero', bg='#ffffff', fg='#123456')
label_5.pack(fill='y', expand=True)





#Run the root window's main loop
root.mainloop()