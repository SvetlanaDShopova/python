"""
Svetlana Shopova
Simple checklist. Introducing text area
"""
import tkinter

window = tkinter.Tk()
window.iconbitmap("check.ico")
window.geometry("500x500")
window.title("Simple Checklist")
window.resizable(0, 0)


####### Fonts and color schemes ######
my_font= ("Georgia", 13)
window_color = "#F18805"
button_color = "#581F18"
background_color = "#F3C185"
font_color = "#202C59"

window.config(bg=window_color)

######## Define functions ########


####### Define layout ############

#Create frames
input_frame = tkinter.Frame(window, bg=window_color)
output_frame = tkinter.Frame(window, bg=window_color)
button_frame = tkinter.Frame(window, bg=window_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3,
                           font=my_font)
btn_list_add_item = tkinter.Button(input_frame, text="Add Item", borderwidth=2,
                                 font=my_font, bg=button_color, fg=background_color)
list_entry.grid(row=0, column=0, padx=10, pady=10)
btn_list_add_item .grid(row=0, column=1)

#Output frame layout
my_listbox = tkinter.Listbox(output_frame, height=18, width=45, borderwidth=3,
                             font=my_font, bg=background_color)
my_listbox.grid(row=0,column=0)

#Button frame layout
btn_remove_item = tkinter.Button(button_frame, text="Remove Item")
btn_clear_list =  tkinter.Button(button_frame, text="Clear List")
btn_save_list = tkinter.Button(button_frame, text="Save List")
btn_quit = tkinter.Button(button_frame, text="Quit")

#run main loop

window.mainloop()