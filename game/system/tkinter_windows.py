##################################################################
#!#### IMPORT ####!#
#pygame and os
import pygame, os, shutil

# tkinter
from tkinter import * #yay, tkinter with pygame
from tkinter import messagebox #for popup boxes
from tkinter import filedialog #for file dialog to open files

# images
from PIL import ImageTk, Image #for images

#screen resolution
from win32api import GetSystemMetrics #to get the monitor res

#our files
from game.system import textures as t, globals_file as gf, settings as s #yo, this is my system
#@################################################################@#

def start_options_res():
    root = Tk() #create the window
    root.title("Change Resolution") #set the title
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
        if response:
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


#@-------------------------------------------------------------------@#
def options_res():
    root = Tk() #create the window
    root.title("Change Resolution") #set the title
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
                    confirm_text = "are you want to change the resolution to: " + res

                    response = messagebox.askyesno("Confirm", confirm_text)
                    if response:
                        gf.screen = pygame.display.set_mode(
                            (int(w_text_without_space), int(h_text_without_space)), pygame.RESIZABLE
                            )
                        root.destroy()
                        gf.window_open = False
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
        if response:
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


#@-------------------------------------------------------------------@#
def add_resource_pack_option():
    global the_files_list
    def find_all_indexes(input_str, search_str):
            l1 = []
            length = len(input_str)
            index = 0
            while index < length:
                i = input_str.find(search_str, index)
                if i == -1:
                    return l1
                l1.append(i)
                index = i + 1
            return l1
    
    root = Tk() #create the window
    root.title("Resource Packs") #set the title
    root.iconbitmap("game\\Inner Assets\\icon.ico") #set the icon
    root.resizable(0, 0) #you can't resize the window
    root.configure(background = "#D8B36E")
    APPDATA = os.getenv("APPDATA")
    the_files_list = []
    files_list = os.listdir(APPDATA + "\\.rails_and_potatoes\\Resource pack")
    for file in files_list:
        dot_list = find_all_indexes(file, ".")
        the_one_dot_we_need = int(dot_list[-1]) + 1
        the_one_dot_we_need_1 = int(dot_list[-1])
        type_of_file = file[the_one_dot_we_need:]
        name = file[:the_one_dot_we_need_1]
        if (type_of_file == "zip") or (type_of_file == "rar") or (type_of_file == "rp") or (type_of_file == "r-a-p-assets"):
            the_files_list.append((name, APPDATA + "\\.rails_and_potatoes\\Resource pack\\" + file))
    #*----------------------button funcs----------------------*#
    def open_file_dialog_box():
        global the_files_list
        filepath = filedialog.askopenfilename(
            initialdir = APPDATA + "\\.rails_and_potatoes",
            title = "Select A .zip File to add to your \"Resource Pack\" Colection",
            filetypes = [
                (
                    "Compressed (zipped) Folder, WinRAR archive, ResourcePack files, RailsAndPotatoesAssets files", "*.zip *.rar *.rp *.r-a-p-assets"
                    )
                ]
            )
        if filepath == "":
            pass
        else:
            slash_list = find_all_indexes(filepath, "/")
            the_one_slash_we_need = int(slash_list[-1]) + 1
            name = filepath[the_one_slash_we_need:-4]

            shutil.copy2(filepath, APPDATA + "/.rails_and_potatoes/Resource Pack/" + name + ".zip")

            the_files_list.append((name, APPDATA + "\\.rails_and_potatoes\\Resource Pack\\" + name))

            for element in the_files_list:
                print (element)

    #*----------------------buttons----------------------*#
        #?create
    add_file_button = Button(root, text = "Add Resource Pack File", command = open_file_dialog_box, fg = "#545454", bg = "#C9860A")

    
        #?blit (ho no, blit is pygame, not tkinter)
    add_file_button.grid(row = 0, column = 0) #packing it into the screen(row - up to down, column - left to right)
    
    #*----------------end----------------*#
    #set the window size
    root.geometry("450x250")

    #mainloop window
    root.mainloop()
