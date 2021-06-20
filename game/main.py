# import
from colorama import Fore
import pygame, json, os, win32gui, win32con, sys
os.system("cls") #*clear the console
print (Fore.LIGHTGREEN_EX + "Loading, please wait..." + Fore.RESET + "")
from pygame.locals import *
from .system import settings as s, globals_file as gf, tiles, music as m

#init
pygame.init() #init pygame
pygame.display.init() #init pygame display
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
s.get_setings() #update setings 
gf.Clock = pygame.time.Clock() #seting up the clock

# import
from .menus import main_menu as menu, options as opt, map as play

#TODO console close (add in the final release)
#console_hiding_part = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(console_hiding_part , win32con.SW_HIDE)

#*-----------------------#creating the window--------------------------*#
gf.screen = pygame.display.set_mode((s.game_start.start_width, s.game_start.start_height), pygame.RESIZABLE) #create the window with the right dimensions, and resize option
pygame.display.set_caption(s.game_start.caption) #giving a name to the screen
icon = pygame.image.load(s.game_start.png_icon) #get the icon pic
pygame.display.set_icon(icon) #put the icon on the window
#--------------------------------------------------------------------#
def Main(): #main
    gf.where = "main menu"
    gf.click = False
    gf.width_before = gf.screen.get_width()
    gf.height_before = gf.screen.get_height()
    gf.screen_width = gf.screen.get_width()
    gf.screen_height = gf.screen.get_height()
    gf.Tiles = tiles.Tiles()
    gf.Tiles.load_images(1)
    gf.Sounds_and_sfx_dict = m.load_sounds_or_sfx(gf.Sounds_and_sfx_dict, "main.mp3", "None", "none at all", s.voulume)

    while gf.run: #the main loop
        gf.Tiles.change_x_and_y()
        gf.screen_width = gf.screen.get_width()
        gf.screen_height = gf.screen.get_height()
        gf.mouse_x, gf.mouse_y = pygame.mouse.get_pos()
        gf.half_width = gf.screen.get_width() // 2
        gf.half_height = gf.screen.get_height() // 2
        gf.Sounds_and_sfx_dict = m.set_voulume(gf.Sounds_and_sfx_dict, s.voulume)
        if gf.where != "game":
            if gf.where == "main menu":
                menu.main_menu()
            elif gf.where == "opt":
                opt.options()
            elif gf.where == "play":
                play.map()
            elif gf.where == "exit":
                gf.run = False #stop the game
        else:
            pass #TODO Game
        
        #*-----------------events-----------------*#
        for event in pygame.event.get():
            if event.type == QUIT: #if you closing the window 
                gf.run = False #stop the game
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    gf.click = True
                else:
                    gf.click = False

        #------------------------------------------------------------------------#
        pygame.display.update() #the display needs to update so we can show staf on the screen
        gf.Clock.tick(60)

    
    if not gf.run: #quit
        #?play_time = (pygame.time.get_ticks() / (1000 * 60)) % 60
        #?appdata = os.getenv('APPDATA') #get appdata
        #?with open(appdata + "\\.rails_and_potatoes\\index\\player.data.json", "r") as f:
        #?    data = json.load(f)
        #?    f.close()
        #?data["play time"] += play_time
        #?with open(appdata + "\\.rails_and_potatoes\\index\\player.data.json", "w") as f:
        #?    json.dump(data, f, indent=2)
        #?    f.close()
        #?s.save_setings() #save the settings
        
        pygame.quit()
        sys.exit() #exit the script

if __name__ == "__main__":
    Main()