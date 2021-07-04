import os


f = open('filename.exe', 'r+b')

appdata = os.getenv('APPDATA')
print (os.listdir(appdata + "\\.rails_and_potatoes")) #print all of the folders and files name in the directory that is given

#@-----------------------------------------------------------@#

from game.system import tkinter_windows as tkw

tkw.add_resource_pack_option([], 10)