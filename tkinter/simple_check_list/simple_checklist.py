"""
Svetlana Shopova
Simple checklist. Introducing text area
"""
import tkinter
from tkinter import END

root = tkinter.Tk()
root.iconbitmap("check.ico")
root.geometry("500x500")
root.title("Simple Checklist")
root.resizable(0, 0)


####### Fonts and color schemes ######
my_font= ("Georgia", 13)
root_color = "#F18805"
button_color = "#581F18"
background_color = "#F3C185"
font_color = "#202C59"

root.config(bg=root_color)


######## Define functions ########

def create_button(frame, text,comm="something"):
    btn = tkinter.Button(frame, text=text,
          borderwidth=2,font=my_font, bg=button_color, 
          fg=background_color,command=comm, width=10)
    return btn

def entry_return(event):
    '''Press "Add Item" button programetically when <Enter>
    is prssed in entry field'''
    btn_list_add_item.invoke()


def add_item():
    '''Adding a new task to the list'''
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0,END)
    

####### Define layout ############

#Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = tkinter.Entry(input_frame, width=34, borderwidth=3,
                           font=my_font)
btn_list_add_item =create_button(input_frame, text="Add Item", comm=add_item)

list_entry.grid(row=0, column=0, padx=3, pady=10)
list_entry.bind("<Return>", entry_return)
btn_list_add_item .grid(row=0, column=1, ipadx=5)



#Output frame layout
scrollbar = tkinter.Scrollbar(output_frame)
scrollbar.grid(row=0, column=1, sticky="NS")
my_listbox = tkinter.Listbox(output_frame, height=18, width=46, borderwidth=3,
           font=my_font, bg=background_color, yscrollcommand=scrollbar.set)
my_listbox.grid(row=0,column=0,padx=6)


#Link scrollbar to the listbox
scrollbar.config(command=my_listbox.yview)


#Button frame layout
btn_remove_item = create_button(button_frame, text="Remove Item")
btn_clear_list =  create_button(button_frame, text="Clear List")
btn_save_list = create_button(button_frame, text="Save List")
btn_quit = create_button(button_frame, text="Quit",comm= root.destroy)


btn_remove_item.grid(row=0, column=0,pady=15, padx=3)
btn_clear_list.grid(row=0, column=1, padx=5)
btn_save_list.grid(row=0, column=2, padx=5)
btn_quit.grid(row=0, column=3, padx=5)


#run main loop

root.mainloop()