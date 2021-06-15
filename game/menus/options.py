import pygame
from pygame import key
from pygame.locals import *
from game.system import globals_file as gf, textures, entities as en, settings, music as m
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.font.init() #init
#*-----------------------#pygame input#--------------------------*#
#images
bg_img = pygame.image.load(textures.change_texture(filename = "options background.png", foldername = "bg"))
keymap_image = en.Just_an_image(
    10,
    20,
    600,
    500,
    "bg",
    "keymap.png"
)

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

    #-------------------------------------------------------------------------------------------#
    #                                           other                                           #
    #-------------------------------------------------------------------------------------------#
    #*create
    
    volume_option = en.Clickable_Text_object(
        gf.screen_width // 100,
        gf.screen_height // 3,
        300,
        50,
        "Volume and music",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    )

    control_option = en.Clickable_Text_object(
        gf.screen_width // 100,
        gf.screen_height // 2,
        300,
        50,
        "Keymap",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    )

    #voulume and music
    if gf.what_option == "v":
        volume_controler_down = en.Button(
            gf.screen_width // 1.5,
            gf.screen_height // 1.5,
            100,
            100,
            texture_filename = "down.png",
            hover_texture_filename = "down_h.png"
        )
        volume_controler_up = en.Button(
            gf.screen_width // 1.5,
            gf.screen_height // 3.5,
            100,
            100,
            texture_filename = "up.png",
            hover_texture_filename = "up_h.png"
        )
        
        #the text that show what the voulume is
        volume_text = title_font.render(str(int(settings.voulume * 100)), 1, gf.WHITE)
        gf.screen.blit(volume_text, (
            volume_controler_up.x,
            volume_controler_up.y + volume_controler_up.width
            ))
    


    #back to the main menu
    back = en.Button(
        gf.screen_width // 100,
        gf.screen_height // 100,
        168.75,
        75
        )

    #update
    if gf.what_option == "v":
        volume_controler_down.update()
        volume_controler_up.update()
    elif gf.what_option == "k":
        keymap_image.update(
            gf.screen_width // 3,
            0
        )
    
    
    back.update()
    #--------------------------------------------------------#
    #title
    title = title_font.render("Options", 1, gf.WHITE)
    gf.screen.blit(title, (
        gf.half_width - (title.get_width() // 2),
        gf.screen_height // 1000
    )) #blit the text onto the screen
    
    #click
    if back.click():
        gf.where = "main menu"
    
    if gf.what_option == "v":
        if volume_controler_down.click():
            m.change_voulume("down")
        elif volume_controler_up.click():
            m.change_voulume("up")
    
    #what option
    if volume_option.update():
        gf.what_option = "v"
    if control_option.update():
        gf.what_option = "k"