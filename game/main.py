#--------------------------------------------< Import >--------------------------------------------#
import pygame, json, os, win32gui, win32con #regular staff
from pygame.locals import * #pygame locals

os.system("cls") #*clear the console

from colorama import Fore #colorama for colored text
print (Fore.LIGHTGREEN_EX + "Loading, please wait..." + Fore.RESET + "") #printing the text of loading to the screen

#our functions
from . import system as sys, tiles
from . import globals_file as gf
from .system import settings as s
#%start%-------------------------------------------------------------------%start%#

#--------------------------------------------< Init >--------------------------------------------#

    #pygame
pygame.init() #init pygame
pygame.display.init() #init pygame display
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
gf.Clock = pygame.time.Clock() #seting up the clock

    #settings
s.get_setings() #update settings and init them

#------------------------------------< Closing the Console >------------------------------------#
#TODO add in the final release!
#//console_hiding_part = win32gui.GetForegroundWindow()
#//win32gui.ShowWindow(console_hiding_part , win32con.SW_HIDE)

#*-----------------------------------------< Creating The Window >-----------------------------------------*#
gf.screen = pygame.display.set_mode((s.game_start.start_width, s.game_start.start_height), pygame.RESIZABLE) #create the pygame window with the right dimensions, and resize option

pygame.display.set_caption(s.game_start.caption) #giving a name to the screen
icon = pygame.image.load(s.game_start.png_icon) #get the icon pic
pygame.display.set_icon(icon) #put the icon on the window


#?-------------------------------------------< Main >-------------------------------------------?#
def Main(): #main
    from .menus import main_menu as menu, options as opt, map as play #import 2.0 because of settings

    gf.where = "main menu" #what panel are we on? ho right, its the <main menu>

    gf.click = False #Do Not Touch This Red Button -> if the player click the mouse

    #Screen Resolution
    gf.width_before = gf.screen.get_width()
    gf.height_before = gf.screen.get_height()
    gf.screen_width = gf.screen.get_width()
    gf.screen_height = gf.screen.get_height()

    #INIT tiles for the levels
    gf.Tiles = tiles.Tiles()
    gf.Tiles.load_images(1)

    #TODO load the music of the main menu
    gf.Sounds_and_sfx_dict = sys.Music_and_SFX.load_sounds_or_sfx(gf.Sounds_and_sfx_dict, "main.mp3", "None", "none at all", s.volume)


        #%start%-------------------------------------------------------------------%start%#
    #--------------------------------------------< The Main Loop >--------------------------------------------#
    while gf.run:
        gf.Tiles.change_x_and_y() #tiles update

        #screen resolution check and change
        gf.screen_width = gf.screen.get_width()
        gf.screen_height = gf.screen.get_height()
        gf.half_width = gf.screen.get_width() // 2
        gf.half_height = gf.screen.get_height() // 2

        #mouse position on the screen
        gf.mouse_x, gf.mouse_y = pygame.mouse.get_pos()

        #set volume
        gf.Sounds_and_sfx_dict = sys.Music_and_SFX.set_volume(gf.Sounds_and_sfx_dict, s.volume)

        #fine the screen we need to go to
        if gf.where != "game": #Selection

            if gf.where == "main menu": #the famous main menu panel
                menu.main_menu() #go to the main menu, you also can go, just click.= ho, you are already there? impressive... impressive...
            
            elif gf.where == "opt": #the helpful option panel
                opt.options() #go to the options, you also can go, just click. (did you have a deja vu too, or it is just me?)
            
            elif gf.where == "play": #we need to find the map panel
                play.map() #go to the map, you also can go, just click. (I feel I being repetitive today)
            
            elif gf.where == "exit": #"wait, were are you going to" panel
                gf.run = False #stop the game

        else:
            pass #TODO Game, That is important?
        
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
        #%end%-------------------------------------------------------------------%end%#

    
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
    #%end%-------------------------------------------------------------------%end%#


if __name__ == "__main__":
    Main()