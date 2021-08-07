import pygame
from pygame.locals import *
from game.system import textures
from game import globals_file as gf, system as sys
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
    #arguments:
    play_button_kwargs = {
        "x": gf.screen_width // 1.5,
        "y": gf.screen_height // 3,
        "width": 225,
        "height": 100
    }
    options_button_kwargs = {
        "x": gf.screen_width // 1.5,
        "y": gf.screen_height // 1.8,
        "width": 225,
        "height": 100,
        "texture_foldername": "buttons\\main menu",
        "texture_filename": "options.png",
        "hover_texture_filename": "options_h.png"
    }
    exit_button_kwargs = {
        "x": gf.screen_width // 1.5,
        "y": gf.screen_height // 1.3,
        "width": 225,
        "height": 100,
        "texture_foldername": "buttons\\main menu",
        "texture_filename": "exit.png",
        "hover_texture_filename": "exit_h.png"
    }
    
    #create
    play = sys.Entities.Button(**play_button_kwargs)

    options = sys.Entities.Button(**options_button_kwargs)
    
    exit = sys.Entities.Button(**exit_button_kwargs)

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
