#import ast, json
#
#h = open("our.json", "r")
#h2 = json.load(h)
#h.close()
#hhh = str(h2)
#print (ast.literal_eval(hhh))



import os
from game.system import download
from time import sleep
from colorama import Fore
from game.tqdm import tqdm

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

main.Main()