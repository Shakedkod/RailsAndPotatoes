import os, sys
from game import download
from time import sleep
from colorama import Fore
from tqdm import tqdm
#%start%-------------------------------------------------------------------%start%#


os.system("cls") #*clear the console

download.assets_check() #download the assets if necessary

#--------------------------------------------< The Loading Bars >--------------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 1
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close()
#-------------------------------------#
print (Fore.YELLOW + "system package " + Fore.GREEN + "loaded" + Fore.RESET + "") #system package loaded(not relay)
#-------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 2
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close()
#-------------------------------------#
print (Fore.YELLOW + "menus package " + Fore.GREEN + "loaded" + Fore.RESET + "") #menus package loaded(not relay and what is menus package anyway?)
#-------------------------------------#
loop = tqdm(total = 5000, position = 0) #bar 3
for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)
loop.close() #close the loop
#-------------------------------------#
print (Fore.LIGHTCYAN_EX +"Almost ready to launch" + Fore.RESET + "") #that was from before :)
sleep(1) #sleep for 1 second 

#---------------------------------------------------#
from game import main
from game import globals_file as gf

main.Main() #the main of the mains


#-----------------------------------------------------------#
#------------------------- Restart -------------------------#
#-----------------------------------------------------------#
if gf.another_one:
    gf.another_one = False #false, because we don't need infinit number of those game windows.
    os.system("py Rails_And_Potatoes.py") #creating another one of those game windows.
    sys.exit() #no worries, we are just restarting.
else:
    sys.exit() #bye bye, so sad see you going :(
