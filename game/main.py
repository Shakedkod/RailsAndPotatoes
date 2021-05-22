# import
from colorama import Fore
import pygame, json, os, win32gui, win32con, sys
os.system("cls") #*clear the console
print (Fore.LIGHTGREEN_EX + "Loading, please wait..." + Fore.RESET + "")
from pygame.locals import *
from .system import settings as s, globals_file as gf
from .menus import main_menu as menu, options

#init
pygame.init() #init pygame
pygame.display.init() #init pygame display
s.get_setings() #update setings 
gf.Clock = pygame.time.Clock() #seting up the clock

#TODO console close (add in the final release)
#console_hiding_part = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(console_hiding_part , win32con.SW_HIDE)

#*-----------------------#creating the window--------------------------*#
gf.screen = pygame.display.set_mode((s.game_start.start_width, s.game_start.start_height), pygame.RESIZABLE) #create the window with the right dimensions, and resize option
pygame.display.set_caption("Game Name") #giving a name to the screen
icon = pygame.image.load("game\Inner Assets\icon.png") #get the icon pic
pygame.display.set_icon(icon) #put the icon on the window
#--------------------------------------------------------------------#
def Main(): #main
    gf.where = "main menu"
    gf.click = False
    gf.width_before = gf.screen.get_width()
    gf.height_before = gf.screen.get_height()
    gf.screen_width = gf.screen.get_width()
    gf.screen_height = gf.screen.get_height()
    while gf.run: #the main loop
        gf.screen_width = gf.screen.get_width()
        gf.screen_height = gf.screen.get_height()
        gf.mouse_x, gf.mouse_y = pygame.mouse.get_pos()
        gf.half_width = gf.screen.get_width() // 2
        gf.half_height = gf.screen.get_height() // 2
        if gf.where != "game":
            if gf.where == "main menu":
                menu.main_menu()
            elif gf.where == "opt":
                pass #TODO go to options
            else:
                pass #TODO go the save menu
        else:
            pass #TODO Game
        
        #*-----------------events-----------------*#
        for event in pygame.event.get():
            if event.type == QUIT: #if you closing the window 
                s.save_setings() #save the settings
                run = False #stop the game
                pygame.quit()
                sys.exit() #exit the script
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    gf.click = True
                else:
                    gf.click = False

        #------------------------------------------------------------------------#
        pygame.display.update() #the display needs to update so we can show staf on the screen
        gf.Clock.tick(60)
    
    if not gf.run: #quit
        pygame.quit()
        sys.exit() #exit the script

if __name__ == "__main__":
    Main()