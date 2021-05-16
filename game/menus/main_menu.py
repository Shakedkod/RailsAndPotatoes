import pygame
from game.system import globals_file as gf, textures, entities as en
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#*-----------------------#pygame input#--------------------------*#
#images
bg_img = pygame.image.load(textures.change_texture(filename = "main menu.png", foldername = "bg"))

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
    #panorama
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
    play = en.Button(
        gf.screen_width // 2,
        gf.screen_height // 2,
        200,
        100
        )
    play.update()
    
    if play.click():
        print ("hallo!")
    
