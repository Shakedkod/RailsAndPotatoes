import os, sys
from game import download
from time import sleep
from colorama import Fore
from tqdm import tqdm
#%start%-------------------------------------------------------------------%start%#


os.system("cls") #*clear the console

download.assets_check() #download the assets if necessary

#-------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 1
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close()
#-------------------------------------#
print (Fore.YELLOW + "system package " + Fore.GREEN + "loaded" + Fore.RESET + "")
#-------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 2
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close()
#-------------------------------------#
print (Fore.YELLOW + "menus package " + Fore.GREEN + "loaded" + Fore.RESET + "")
#-------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 3
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close() #close the loop
#-------------------------------------#
print (Fore.LIGHTCYAN_EX +"Almost ready to launch" + Fore.RESET + "")
sleep(1) #sleep for 1 second 

#---------------------------------------------------#
from game import main
from game import globals_file as gf

main.Main()

if gf.another_one:
    gf.another_one = False
    os.system("py Rails_And_Potatoes.py")
    sys.exit()
else:
    sys.exit()