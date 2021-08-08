#--------------------------------------------< Import >--------------------------------------------#
import pygame, json, os, win32gui, win32con #regular staff

os.system("cls") #*clear the console

from colorama import Fore #colorama for colored text
print (Fore.LIGHTGREEN_EX + "Loading, please wait..." + Fore.RESET + "") #printing the text of loading to the screen

from pygame.locals import * #pygame locals
from pygame.constants import MOUSEBUTTONDOWN, QUIT
from moviepy.editor import * #the cutscence

#our functions
from . import system as sys, globals_file as gf
from .system import settings as s, tiles

#--------------------------------------------< Init >--------------------------------------------#
pygame.init() #init pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)

pygame.mixer.init() #init pygame mixer
pygame.display.init() #init pygame display

gf.Clock = pygame.time.Clock() #seting up the clock

s.init() #update settings and init them
#%start%-------------------------------------------------------------------%start%#

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
    
    from .menus import main_menu as menu, options as opt, map as play, power_level as tp #import 2.0 because of settings

    gf.where = "main menu" #what panel are we on? ho right, its the <main menu>

    gf.click = False #Do Not Touch This Red Button -> if the player click the mouse

    #appdata
    APPDATA = os.getenv("APPDATA")

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

    #!-------------------------------------------------------------------------------!#
    #!-----------------------------< Starting Cutscene >-----------------------------!#
    #!-------------------------------------------------------------------------------!#
    #load cutscence and start it
    clip = VideoFileClip(APPDATA + "\\.rails_and_potatoes\\index\\Assets\\cutscenes\\open.mp4", False, True, 200000, (gf.screen_height, gf.screen_width))
    clip.preview()
    
    #restart the mixer
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    pygame.mixer.init() #init pygame mixer

    #restarting the window
    gf.screen = pygame.display.set_mode((gf.screen_width, gf.screen_height), pygame.RESIZABLE)

    #MUSIC FOR MAIN MENU
    gf.Sounds_and_sfx_dict = sys.Music_and_SFX.load_sounds_or_sfx(
        gf.Sounds_and_sfx_dict,
        "start.mp3",
        "None",
        "start",
        s.volume
        )
    gf.Sounds_and_sfx_dict = sys.Music_and_SFX.load_sounds_or_sfx(
        gf.Sounds_and_sfx_dict,
        "main.mp3",
        "None",
        "main",
        s.volume
        )
    
    gf.Sounds_and_sfx_dict["start"].play()
    start_music_start_time = pygame.time.get_ticks()
    start_music_time = 191000

        #%start%-------------------------------------------------------------------%start%#
    #--------------------------------------------< The Main Loop >--------------------------------------------#
    while gf.run:
        gf.Tiles.change_x_and_y() #tiles update

        #screen resolution check and change
        gf.screen_width = gf.screen.get_width()
        gf.screen_height = gf.screen.get_height()
        gf.half_width = gf.screen.get_width() // 2
        gf.half_height = gf.screen.get_height() // 2

        #time
        gf.current_time = pygame.time.get_ticks()

        #mouse position on the screen
        gf.mouse_x, gf.mouse_y = pygame.mouse.get_pos()

        if not gf.start_music:
            if gf.current_time - start_music_start_time > start_music_time:
                gf.Sounds_and_sfx_dict["main"].play(-1)
                gf.start_music = True
        #--------------------------------------------------------------------#

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
            tp.levels_n_staff()
        
        #!--------------------------------------------------------------------------------!#
        #!-----------------------------------< EVENTS >-----------------------------------!#
        #!--------------------------------------------------------------------------------!#
        for event in pygame.event.get():
            if event.type == QUIT: #if you closing the window 
                gf.run = False #stop the game
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    gf.click = True
                elif event.button == 3:
                    gf.right_click = True
                else:
                    gf.click = False

        #------------------------------------------------------------------------#
        pygame.display.update() #the display needs to update so we can show staf on the screen
        gf.Clock.tick(60)
        #%end%-------------------------------------------------------------------%end%#

    
    else: #quit
        #?play_time = (pygame.time.get_ticks() / (1000 * 60)) % 60
        #?with open(APPDATA + "\\.rails_and_potatoes\\index\\player.os.dt", "r") as f:
        #?    data = json.load(f)
        #?    f.close()
        #?
        #?data["play time"] += play_time
        #?with open(APPDATA + "\\.rails_and_potatoes\\index\\player.data.json", "w") as f:
        #?    json.dump(data, f, indent=2)
        #?    f.close()

        if gf.classed_map != "None":
            gf.classed_map.save_map()
        #?s.save_settings() #save the settings
        
        pygame.quit()
    #%end%-------------------------------------------------------------------%end%#

if __name__ == "__main__":
    Main()