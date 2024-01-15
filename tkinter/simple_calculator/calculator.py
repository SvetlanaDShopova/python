"""
A simple calculator that can perform addition, substraction,
multiplication, division, square root and power

@author: Svetlana Shopova
"""
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

#Define window
root = tkinter.Tk()
root.title("Calculator")
root.iconbitmap("calc.ico")
root.geometry("300x405")
root.resizable(0, 0)

#Define colors and fonts

bg_color = "#E4E7F8"
btn_color = "#aee8ff"
font_color = "#314D7F"
display_color = "#B1BAD8"
btn_font = ("Arial", 18)
display_font  = ("Arial", 25)
######## Functions #############
previous_number = 0
global operation

def create_button(frame, lbl, comm=None):
    btn = tkinter.Button(frame, activebackground="#81bafb",
        text=lbl, bg=btn_color, font=btn_font, fg=font_color, command=comm)
    return btn

def submit_number(number):
    """ Add a number or decimal to the display"""
    #Insert a number at theend of the display
    #display.delete(0,END)
    display.insert(END, number)
    
    #Disable decimal if is inserted
    if "." in display.get():
        point.config(state=DISABLED)
        
def equals():
    """Perform the desired mathemothics"""
   
    if operation == '+':
        value = float(previous_number) + float(display.get())
    elif operation == "^":
        value = float(previous_number) ** float(display.get())
    elif operation == "/":
        value = float(previous_number) / float(display.get())
    elif operation == "*":
        value = float(previous_number) * float(display.get())
    elif operation == "-":
        value = float(previous_number) - float(display.get())
   
    t = str(previous_number ) + " " + operation + " " + display.get() + " = " + str(value)
    display.delete(0,END)
   
    display.insert(END, value)   
    monitor.config(text=t, anchor="e")
    
def operate(operator):
    """ Store the first number of the expression and the opertation
    to be used"""
    global previous_number
    global operation
    
    if display.get() != "":        
        if previous_number != 0:
            equals()
          
    operation = operator
    previous_number = display.get()
    monitor.config(text=previous_number +" " + operation, anchor="e")        
    point.config(state=NORMAL)
    display.delete(0, END)

def square_number():
    """ Square current number"""
    if display.get() != '':
        value = float(display.get()) ** 2 
        display.delete(0,END) 
        monitor.config(text=value, anchor="e") 
        display.insert(END, value)       
        point.config(state=NORMAL)
    
def inverse_number():       
    if display.get() != '0' and display.get() !="":     
       value = 1 / float(display.get())  
       display.delete(0,END) 
    else:
        value = "Err"  
    monitor.config(text=value, anchor="e") 
    display.insert(END, value) 
    point.config(state=NORMAL)
    
def clear():
    global operation
    global previous_number
    
    previous_number=0
    operation=""
    monitor.config(text="", anchor="e") 
    display.delete(0, END)
    point.config(state=NORMAL) 
    
def entry_return(event):
    """Press "Equal" button programetically when <Enter>
    is prssed in entry field"""
    equal.invoke()

def negate():
    """ Negate a given Number"""
    val = -1 * float(display.get())
    display.delete(0, END)
    display.insert(END, val)

######### Bind number keys ##############
root.bind("<Return>", entry_return)

root.bind("0", lambda event:submit_number(0))
root.bind("1", lambda event:submit_number(1))
root.bind("2", lambda event:submit_number(2))
root.bind("3", lambda event:submit_number(3))
root.bind("4", lambda event:submit_number(4))
root.bind("5", lambda event:submit_number(5))
root.bind("6", lambda event:submit_number(6))
root.bind("7", lambda event:submit_number(7))
root.bind("8", lambda event:submit_number(8))
root.bind("9", lambda event:submit_number(9))
root.bind("-",lambda event: operate("-"))
root.bind("+",lambda event: operate("+"))
root.bind("*",lambda event: operate("*"))
root.bind("/",lambda event: operate("/"))
root.bind("=",equals)
######### Layout  ############

#Frames

display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=5, pady=(5,8))
button_frame.pack(padx=5, pady=(3,0))

#Layout for display frame
monitor = tkinter.Label(display_frame, width=50,bg=bg_color,
                    font=("Arial", 12), fg=font_color)
display = tkinter.Entry(display_frame, width=50,
        font=display_font, bg=bg_color,
        justify=RIGHT, borderwidth=0, fg=font_color)


monitor.pack(padx=5, pady=(5,0))
display.pack(padx=5,pady=(0,5))
##### Layout button frame ######

# First line
clear_button =create_button(button_frame,"Clear", comm=clear)
quit_button = create_button(button_frame,"Quit", comm=root.destroy)
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")


# Second row
inverse = create_button(button_frame,"1/x", comm=inverse_number)
square =create_button(button_frame,"x^2", comm=square_number) 
exponent = create_button(button_frame,"x^n", comm=lambda:operate("^")) 
divide = create_button(button_frame,"÷", comm=lambda:operate("/"))

inverse.grid(row=1, column=0, pady=1, sticky="WE")
square.grid(row=1, column=1, pady=1, sticky="WE")
exponent.grid(row=1, column=2, pady=1, sticky="WE")
divide.grid(row=1, column=3, pady=1, sticky="WE")

#Third row
seven = create_button(button_frame,"7", comm=lambda:submit_number(7))
eight = create_button(button_frame,"8", comm=lambda:submit_number(8))
nine =create_button(button_frame,"9", comm=lambda:submit_number(9))
multiply = create_button(button_frame,"x",comm=lambda:operate("*"))

seven.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)


#Fourth row
four = create_button(button_frame,"4", comm=lambda:submit_number(4))
five = create_button(button_frame,"5", comm=lambda:submit_number(5))
six = create_button(button_frame,"6", comm=lambda:submit_number(6))
substract = create_button(button_frame,"-", comm=lambda:operate("-"))

four.grid(row=3, column=0, pady=1, sticky="WE")
five.grid(row=3, column=1, pady=1, sticky="WE")
six.grid(row=3, column=2, pady=1, sticky="WE")
substract.grid(row=3, column=3, pady=1, sticky="WE")

#Fifth row
one = create_button(button_frame,"1", comm=lambda:submit_number(1))
two = create_button(button_frame,"2", comm=lambda:submit_number(2))
three = create_button(button_frame,"3", comm=lambda:submit_number(3))
plus = create_button(button_frame,"+", comm=lambda:operate("+"))

one.grid(row=4, column=0, pady=1, sticky="WE")
two.grid(row=4, column=1, pady=1, sticky="WE")
three.grid(row=4, column=2, pady=1, sticky="WE")
plus.grid(row=4, column=3, pady=1, sticky="WE")

#Sixth row
negate = create_button(button_frame,"+/-", comm=negate)
zero = create_button(button_frame,"0", comm=lambda:submit_number(0))
point = create_button(button_frame,".", comm=lambda:submit_number("."))
equal = tkinter.Button(button_frame, activebackground="#a3ddfb",
    text="=", bg=font_color, font=btn_font, fg=bg_color, command=equals)


negate.grid(row=5, column=0, pady=1, sticky="WE")
zero.grid(row=5, column=1, pady=1, sticky="WE")
point.grid(row=5, column=2, pady=1, sticky="WE")
equal.grid(row=5, column=3, pady=1, sticky="WE")


root.mainloop()