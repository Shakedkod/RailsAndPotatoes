##################################################################
#!#### IMPORT ####!#
#pygame and os
import pygame, os, shutil, json

# tkinter
from tkinter import * #yay, tkinter with pygame
from tkinter import messagebox #for popup boxes
from tkinter import filedialog #for file dialog to open files

# images
from PIL import ImageTk, Image #for images

#screen resolution
from win32api import GetSystemMetrics #to get the monitor res

#unzip RP zip file
from zipfile import ZipFile #YAY .zip?

#our files
from game import globals_file as gf
from game.system import textures as t, settings as s #yo, this is my system
#%start%-------------------------------------------------------------------%start%#








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
                    confirm_text = "Do you want the window to open in the resolution: " + res

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
#%end%-------------------------------------------------------------------%end%#







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
                    confirm_text = "Do you want to change the resolution to: " + res

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
#%end%-------------------------------------------------------------------%end%#








#@-------------------------------------------------------------------@#
def add_resource_pack_option(filessss, bty): #📚
    global the_files_list, bt_y, items_names, dropdown_menu, dm_clicked
    the_files_list = filessss
    bt_y = bty
    #?------------get appdata and------------?#
    global path_of_path
    APPDATA = os.getenv("APPDATA")
    path_of_path = APPDATA + "\\.rails_and_potatoes\\Resource pack\\UlBNanager.cnAtbG9hZGVy"

    #---------------------find all the indexses of staff in a string---------------------#
    def find_all_indexes(input_str, search_str):                                         #
            l1 = []                                                                      #
            length = len(input_str)                                                      #
            index = 0                                                                    #
            while index < length:                                                        #
                i = input_str.find(search_str, index)                                    #
                if i == -1:                                                              #
                    return l1                                                            #
                l1.append(i)                                                             #
                index = i + 1                                                            #
            return l1                                                                    #
    #------------------------------------------------------------------------------------#
    
    #?------------tk window, create------------?#
    root = Tk() #create the window
    root.title("Resource Packs") #set the title
    root.iconbitmap("game\\Inner Assets\\icon.ico") #set the icon
    root.resizable(0, 0) #you can't resize the window
    root.configure(background = "#D8B36E")

    bg_image = Image.open(APPDATA + "\\.rails_and_potatoes\\index\\Assets\\bg\\rp-chooser.png")
    bg_image = bg_image.resize((450, 250), Image.ANTIALIAS)
    bg_loaded_img = ImageTk.PhotoImage(bg_image)
    bg_image_lable = Label(image = bg_loaded_img).place(x=0, y=0, relwidth=1, relheight=1)
    dm_clicked = StringVar() #the var for wut is chosen by the user


    #?------------files that already in the folder(Resource pack)------------?#
    files_list = os.listdir(APPDATA + "\\.rails_and_potatoes\\Resource pack\\")
    for file in files_list: #add the files to the list
        dot_list = find_all_indexes(file, ".")
        the_one_dot_we_need = int(dot_list[0]) + 1
        the_one_dot_we_need_1 = int(dot_list[-1])
        type_of_file = file[the_one_dot_we_need:]
        name = file[:the_one_dot_we_need_1]
        if (type_of_file == "zip") or (type_of_file == "rar") or (type_of_file == "rp") or (type_of_file == "r-a-p-assets"):
            the_files_list.append((name, APPDATA + "\\.rails_and_potatoes\\Resource pack\\" + file))
    
    #*----------------------------------------------button funcs----------------------------------------------*#
    def the_chossen_one(): #if the button is clicked
        global dm_clicked, dropdown_menu
        APPDATA = os.getenv("APPDATA")
        the_chossen_one_var = dm_clicked.get()
        if the_chossen_one_var == "None":
            pass
        else:
            if the_chossen_one_var == "Default":
                gf.what_is_rp = None
                root.destroy()
                gf.window_open = False
                gf.another_one = True
                gf.where = "exit"
            else:
                if os.path.exists(
                    APPDATA + "\\.rails_and_potatoes\\Resource pack\\ZiUn.z\\" + the_chossen_one_var):
                    #@#############################################################################@#
                    #@                               activate the RP                               @#
                    #@#############################################################################@#
                    gf.what_is_rp = the_chossen_one_var
                    root.destroy() #destroy the active tkinter window
                    gf.window_open = False
                    gf.another_one = True #Activate the Restart process
                    gf.where = "exit" #exit the current game
                else:
                    with ZipFile(APPDATA + "\\.rails_and_potatoes\\Resource pack\\" + the_chossen_one_var + ".zip", 'r') as zipObj: #opening the zip file
                        zipObj.extractall( #extracting all the files from the zip file
                            path = APPDATA + "\\.rails_and_potatoes\\Resource pack\\ZiUn.z\\" + the_chossen_one_var)

                    #@#############################################################################@#
                    #@                               add to the list                               @#
                    #@#############################################################################@#
                    with open(APPDATA + "\\.rails_and_potatoes\\Resource pack\\UlBNanager.cnAtbG9hZGVy", "r") as j_file:
                        data = json.load(j_file) #load the file of the data of the Resource Packs (why?🙃)

                    data["dW56aXBlZCBmaWxlcw=="].append(the_chossen_one_var) #add this file into the data of the Resource Packs


                    with open(APPDATA + "\\.rails_and_potatoes\\Resource pack\\UlBNanager.cnAtbG9hZGVy", "w")  as j_file:
                        json.dump(data, j_file, indent=2) #return the updated data of the Resource Packs to its file
                    
                    #@#############################################################################@#
                    #@                               activate the RP                               @#
                    #@#############################################################################@#
                    gf.what_is_rp = the_chossen_one_var
                    root.destroy()
                    gf.window_open = False
                    gf.another_one = True
                    gf.where = "exit"
    

    def open_file_dialog_box():
        global the_files_list, bt_y, dropdown_menu, dm_clicked
        filepath = filedialog.askopenfilename(
            initialdir = APPDATA + "\\.rails_and_potatoes",
            title = "Select A .zip File to add to your \"Resource Pack\" Colection",
            filetypes = [
                (
                    "Compressed (zipped) Folder, WinRAR archive, ResourcePack files, RailsAndPotatoesAssets files", "*.zip *.rar *.rp *.r-a-p-assets"
                    )
                ]
            )

        #if you chosse a file(in else)
        if filepath == "":
            pass
        else:
            slash_list = find_all_indexes(filepath, "/") #find in the path all the "/"
            the_one_slash_we_need = int(slash_list[-1]) + 1 #find the one we need and add 1 to it becuse
            name = filepath[the_one_slash_we_need:-4] #the name is generated here

            shutil.copy2(filepath, APPDATA + "/.rails_and_potatoes/Resource Pack/" + name + ".zip") #we copy the file TODO - add the box that ask you if to delete the original one

            the_files_list.append((name, APPDATA + "\\.rails_and_potatoes\\Resource Pack\\" + name + ".zip")) #add it to the files list
            
            #@#############################################################################@#
            #@                               create the menu                               @#
            #@#############################################################################@#

            dropdown_menu.destroy()


            #Update the names
            items_names = []
            for file in the_files_list: #add the files to the list
                items_names.append(file[0]) #apppppend name, tank(thank) you 🙃

            dm_clicked.set("None") #set the var to None
            dropdown_menu = OptionMenu(root, dm_clicked, "Default", *items_names) #create the menu
            dropdown_menu["menu"].config(bg="#834B00", fg = "white") #COLORS IS FUN

            dropdown_menu.grid(row = 1, column = 2) #show the dropdown menu on the screen

            #@#############################################################################@#
            #@                             delete the original                             @#
            #@#############################################################################@#
            delete_the_or_yes_or_no = messagebox.askyesno("RP installer", "Do you want to delete the original file?\nthe file will steal be avileble at the the game folder at %appdata%") #DO YOU WANT THIS SIR?
            if delete_the_or_yes_or_no:
                os.remove(filepath) #remove the original file
            
            #@#############################################################################@#
            #@                               add to the list                               @#
            #@#############################################################################@#
            with open(APPDATA + "\\.rails_and_potatoes\\Resource pack\\UlBNanager.cnAtbG9hZGVy", "r") as j_file:
                data = json.load(j_file) #load the file of the data of the Resource Packs (why?🙃)
            
            data["emlwIGZpbGVz"].append(file[0]) #add this file into the data of the Resource Packs

            with open(APPDATA + "\\.rails_and_potatoes\\Resource pack\\UlBNanager.cnAtbG9hZGVy", "w") as j_file:
                json.dump(data, j_file, indent=2) #return the updated data of the Resource Packs to its file
    #?---------------------------------------------End of FUNC---------------------------------------------?#

    #Json -> find the name of the active RP
    with open(path_of_path, "r") as file:
        data = json.load(file)
    
    path_to_the_image = data["bG9hZGVk"]
    if path_to_the_image == "default":
        path_to_the_image = APPDATA + "\\.rails_and_potatoes\\index\\logo.png"
        name_active = "Default"
    else:
        name_active = path_to_the_image
        path_to_the_image = APPDATA + "\\.rails_and_potatoes\\R" + path_to_the_image + "\\"

    #*----------------------buttons----------------------*#

        #?create
    add_file_button = Button(root, text = "Add Resource Pack File", command = open_file_dialog_box, bg="#834B00", fg = "white")

    confirm_button = Button(root, text = "Confirm", command = the_chossen_one, bg="#834B00", fg = "white").grid(row = 3, column = 2)

    
        #?blit (ho no, blit is pygame, not tkinter)
    add_file_button.grid(row = 0, column = 0) #packing it into the screen(row - up to down, column - left to right)

    lable_of_the_dropdown = Label(root, text = "Change ResourcePack here:", fg = "white", bg = "#834B00").grid(row = 0, column = 2)

    defult_lable = Label(root, text = "Active Resource Pack:", bg = "#D8B36E", fg = "black").grid(row = bt_y - (len(the_files_list) + 1), column = 0)

    name_lable = Label(root, text = name_active, fg = "#403E39", bg = "#E89C0D").grid(row = bt_y - (len(the_files_list) - 1), column = 0)

    #a blank slate(for spaces here)
    blank_slate = Label(root, text = "                                     ", bg = "#81a0b9").grid(row = 0, column = 1)
    blank2_slate = Label(root, text = "", bg = "#bbbbb9").grid(row = 2, column = 2)

    
    #-----------------------------------image-----------------------------------#
    
    #IMAGE
    image = Image.open(path_to_the_image)
    image = image.resize((80, 80), Image.ANTIALIAS)

    loaded_img = ImageTk.PhotoImage(image)
    image_lable = Label(image = loaded_img).grid(row = bt_y - (len(the_files_list)), column = 0) #show the image on the sceen

    #dropdown_menu
    items_names = []
    for file in the_files_list: #add the files to the list
        items_names.append(file[0]) #apppppend name, tank(thank) you 🙃

    dm_clicked.set("None") #set the var to None
    dropdown_menu = OptionMenu(root, dm_clicked, "Default", *items_names) #create the menu
    dropdown_menu["menu"].config(bg="#834B00", fg = "white") #COLORS IS FUN

    dropdown_menu.grid(row = 1, column = 2) #show the dropdown menu on the screen

    

    
    #*----------------end----------------*#
    #set the window size
    root.geometry("450x250")

    #mainloop window
    root.mainloop()
#%end%-------------------------------------------------------------------%end%#
