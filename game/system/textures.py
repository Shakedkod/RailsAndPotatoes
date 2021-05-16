import os
#-----------------------------------------------------------#
def change_texture(filename = "menu.png", foldername = "bg"):
    #input: (filename -> name.end) and (foldername -> name)
    #find if in the resources folder there is an active one with the texture name
    #if there is, its return the file path
    #else its return the regular file path
    #output: file path -> C:\users\name\appdata\roaming\.game_name\index\Assets\foldername\filename
    #the output need to be inputed in the pygame.image.load() function
    appdata = os.getenv('APPDATA') #find appdata
    pack_path = appdata + "\\.game_name\\Resource pack\\active\Assets\\"
    pack_path += foldername + "\\" + filename
    if os.path.exists(pack_path):
        return pack_path
    else:
        path = appdata + "\\.game_name\\index\\Assets\\"
        return path + foldername + "\\" + filename