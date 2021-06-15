import pygame
from pygame.locals import *
from game.system import globals_file as gf, textures, entities as en
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#*-----------------------#pygame input#--------------------------*#
#images
bg_img = pygame.image.load(textures.change_texture(filename = "background.png", foldername = "bg"))

#music and sounds
# TODO
#*-----------------------#functions#--------------------------*#
# TODO
#*-----------------------#main#--------------------------*#
def main_menu():
    #-------------------------------------------------------------------------------------------#
    #                                        fonts input                                        #
    #-------------------------------------------------------------------------------------------#
    title_font = pygame.font.Font(textures.change_texture("Blackwood Castle.ttf", "fonts"), gf.screen_width // 10)
    
    #------------------------------------------------------------------------------------------#
    #                                        backgrownd                                        #
    #------------------------------------------------------------------------------------------#
    bg = pygame.transform.scale(bg_img, (gf.screen_width, gf.screen_height)) #change size
    gf.screen.blit(bg, (0, 0))
    #--------------------------------------------------------#
    #title
    title = title_font.render("Rails And Potatoes", 1, gf.WHITE)
    gf.screen.blit(title, (
        gf.half_width - (title.get_width() // 2),
        gf.screen_height // 1000
    )) #blit the text onto the screen

    #-------------------------------------------------------------------------------------------#
    #                                          buttons                                          #
    #-------------------------------------------------------------------------------------------#
    #create
    play = en.Button(
        gf.screen_width // 1.5,
        gf.screen_height // 3,
        225,
        100
        )

    options = en.Button(
        gf.screen_width // 1.5,
        gf.screen_height // 1.8,
        225,
        100
        )
    
    exit = en.Button(
        gf.screen_width // 1.5,
        gf.screen_height // 1.3,
        225,
        100
        )

    #update
    play.update()
    options.update()
    exit.update()
    
    #click
    if play.click():
        gf.where = "play"
    elif options.click():
        gf.where = "opt"
    elif exit.click():
        gf.where = "exit"
