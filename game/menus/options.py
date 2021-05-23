import pygame
from game.system import globals_file as gf, textures, entities as en, settings
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#*-----------------------#pygame input#--------------------------*#
#images
bg_img = pygame.image.load(textures.change_texture(filename = "opt and play.png", foldername = "bg"))

#music and sounds
# TODO
#*-----------------------#functions#--------------------------*#
# TODO
#*-----------------------#main#--------------------------*#
def options():
    #-------------------------------------------------------------------------------------------#
    #                                        fonts input                                        #
    #-------------------------------------------------------------------------------------------#
    title_font = pygame.font.Font(textures.change_texture("Blackwood Castle.ttf", "fonts"), gf.screen_width // 10)
    
    #------------------------------------------------------------------------------------------#
    #                                        backgrownd                                        #
    #------------------------------------------------------------------------------------------#
    #panorama
    bg = pygame.transform.scale(bg_img, (gf.screen_width, gf.screen_height)) #change size
    gf.screen.blit(bg, (0, 0))
    #--------------------------------------------------------#
    #title
    title = title_font.render("Options", 1, gf.WHITE)
    gf.screen.blit(title, (
        gf.half_width - (title.get_width() // 2),
        gf.screen_height // 1000
    )) #blit the text onto the screen

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