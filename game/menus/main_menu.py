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
    bg = pygame.transform.scale(bg_img, (gf.screen_width * 4, gf.screen_height * 2)) #change size
    rel_x = gf.bg_x % bg.get_rect().width #relative x, nice
    gf.screen.blit(bg, (rel_x - bg.get_rect().width, -(gf.screen_height // 3))) #show the bg on the screen
    if rel_x < gf.screen_width: #if, yay
        gf.screen.blit(bg, (rel_x, -(gf.screen_height // 3))) #show the bg on the screen
    gf.bg_x -= gf.screen_width / 500 #remove from bg_x one for the screen bg moving
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
    
