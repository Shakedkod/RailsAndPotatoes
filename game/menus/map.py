import pygame
from pygame.locals import *
from game.system import textures, entities as en, map_s as ms
from game import globals_file as gf, system as s_sys
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#%start%-------------------------------------------------------------------%start%#

classed_map_kwargs = {
    "filename": "map_bg.png",
    "foldername": "bg"
    }
gf.classed_map = ms.Map(**classed_map_kwargs)
#music and sounds
# TODO
#*-----------------------#functions#--------------------------*#
# TODO
#*-----------------------#main#--------------------------*#
def map():
    #-------------------------------------------------------------------------------------------#
    #                                        fonts input                                        #
    #-------------------------------------------------------------------------------------------#
    title_font = pygame.font.Font(textures.change_texture("Blackwood Castle.ttf", "fonts"), gf.screen_width // 20)
    
    #--------------------------------------------------------#
    #title
    title = title_font.render("Map", 1, gf.WHITE)
    gf.screen.blit(title, (
        gf.half_width - (title.get_width() // 2),
        gf.screen_height // 1000
    )) #blit the text onto the screen
    
    gf.classed_map.update()
    
    #-------------------------------------------------------------------------------------------#
    #                                          buttons                                          #
    #-------------------------------------------------------------------------------------------#
    #arguments:
    back_button_kwargs = {
        "x": gf.screen_width // 100,
        "y": gf.screen_height // 100,
        "width": 168.75,
        "height": 75,
        "texture_foldername": "buttons\\other",
        "texture_filename": "back.png",
        "hover_texture_filename": "back h.png"
    }

    #create
    back = en.Button(**back_button_kwargs)

    #update
    back.update()

    #click
    if back.click():
        gf.where = "main menu"
    else:
        if gf.classed_map.buttons.c_0.click():
            gf.where = "game"
            gf.level = "c0"
        
        if gf.classed_map.buttons.l_1.click():
            #update were
            gf.where = "game"
            gf.level = "l1"
            gf.run_level = True
    #%end%-------------------------------------------------------------------%end%#
