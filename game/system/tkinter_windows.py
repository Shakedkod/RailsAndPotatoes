from tkinter import * #yay, tkinter with pygame
from PIL import ImageTk, Image #for images
from tkinter import messagebox #for popup boxes
from win32api import GetSystemMetrics #to get the monitor res
from game.system import textures as t, globals_file as gf, settings as s #yo, this is my system
##################################################################

def options_res():
    root = Tk() #create the window
    root.title("Rails And Potatoes") #set the title
    root.iconbitmap("game\\Inner Assets\\icon.ico") #set the icon
    root.resizable(0, 0) #you can't resize the window
    root.configure(background = "#D8B36E")

    #create the text input field
    #labels
    width_label = Label(root, text = "Width: ", bg = "#D8B36E", fg = "#545454")
    width_label.config(font=("Courier", 20))
    height_label = Label(root, text = "Height: ", bg = "#D8B36E", fg = "#545454")
    height_label.config(font=("Courier", 20))

    #text input
    width_entry = Entry(root, width = 10, bg = "white", fg = "black", borderwidth = 1)
    height_entry = Entry(root, width = 10, bg = "white", fg = "black", borderwidth = 1)

    #pack
    width_label.grid(row = 0, column = 0)
    height_label.grid(row = 1, column = 0)

    width_entry.grid(row = 0, column = 2)
    height_entry.grid(row = 1, column = 2)

    #confirm and cancel buttons
    def confirm_click():
        #get the input
        w_text = width_entry.get()
        h_text = height_entry.get()

        #the input without spaces
        w_text_without_space = w_text.replace(" ", "")
        h_text_without_space = h_text.replace(" ", "")

        #get the monitor resolution
        monitor_width = GetSystemMetrics(0)
        monitor_height = GetSystemMetrics(1)

        #if there is spaces or the fild is empty
        if ((not w_text.isspace()) and (w_text != "")) and ((not h_text.isspace()) and (h_text != "")):
            
            #if the text is just numbers
            if w_text_without_space.isdigit() and h_text_without_space.isdigit():
                
                #if the resolution is in the right specs
                if (0 < int(w_text_without_space) <= monitor_width) and (0 < int(h_text_without_space) <= monitor_height):
                    res = w_text_without_space + "x" + h_text_without_space
                    confirm_text = "are you want the window to open in the resolution: " + res

                    response = messagebox.askyesno("Confirm", confirm_text)
                    if response:
                        s.game_start.start_width = int(w_text_without_space)
                        s.game_start.start_height = int(h_text_without_space)
                        root.destroy()
                        gf.window_open = False
                        print (s.game_start.start_width)
                        print (s.game_start.start_height)
                else:
                    messagebox.showerror("Input Error", "The resolution is smaller then 0 or bigger then your monitor resolution")
                    width_entry.insert(0, "")
                    height_entry.insert(0, "")
            else:
                messagebox.showerror("Input Error", "You need to enter a number!")
                width_entry.insert(0, "")
                height_entry.insert(0, "")
        else:
            messagebox.showerror("Input Error", "You need to enter a number")
            width_entry.insert(0, "")
            height_entry.insert(0, "")
        ##########################?-end of function-?##########################
    
    def cancel_click():
        response = messagebox.askokcancel("Cancel", "are you sure?")
        if not response:
            root.destroy()
            gf.window_open = False
        ##########################?-end of function-?##########################
    
    cancel_button = Button(root, text = "Cancel", command = cancel_click, fg = "#545454", bg = "#C9860A")
    confirm_button = Button(root, text = "Confirm", command = confirm_click, fg = "#545454", bg = "#C9860A")

    cancel_button.grid(row = 2, column = 0) #packing it into the screen
    confirm_button.grid(row = 2, column = 2) #packing it into the screen
    
    #*----------------end----------------*#
    #set the window size
    root.geometry("210x100")

    #mainloop window
    root.mainloop()
