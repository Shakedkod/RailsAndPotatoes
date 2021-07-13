import pygame
from pygame.locals import *
from game.system import globals_file as gf, textures, entities as en, map_s as ms
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#%start%-------------------------------------------------------------------%start%#


gf.classed_map = ms.Map(filename = "map_bg.png", foldername = "bg")
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
    #!gf.Tiles.update(1)
    
    #-------------------------------------------------------------------------------------------#
    #                                          buttons                                          #
    #-------------------------------------------------------------------------------------------#
    #create
    back = en.Button(
        gf.screen_width // 100,
        gf.screen_height // 100,
        168.75,
        75
        )

    #update
    back.update()

    #click
    if back.click():
        gf.where = "main menu"
    else:
        if gf.classed_map.buttons.c_0.click():
            print ("0")
        
        if gf.classed_map.buttons.l_1.click():
            print ("1")
    #%end%-------------------------------------------------------------------%end%#
