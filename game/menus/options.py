import pygame
from pygame import key
from pygame.locals import *
from game import system as sys, globals_file as gf
from game.system import textures, entities as en, settings, tkinter_windows as tk
#%start%-------------------------------------------------------------------%start%#

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

#*-----------------------#main#--------------------------*#
def options():
    #-------------------------------------------------------------------------------------------#
    #                                        fonts input                                        #
    #-------------------------------------------------------------------------------------------#
    title_font = pygame.font.Font(textures.change_texture("Blackwood Castle.ttf", "fonts"), gf.screen_width // 10)
    res_font = pygame.font.Font(textures.change_texture("Goudy Mediaeval Regular.ttf", "fonts"), gf.screen_width // 25)
    title_res_font = pygame.font.Font(textures.change_texture("Goudy Mediaeval Regular.ttf", "fonts"), gf.screen_width // 20)
    
    #------------------------------------------------------------------------------------------#
    #                                        backgrownd                                        #
    #------------------------------------------------------------------------------------------#
    #panorama
    bg = pygame.transform.scale(bg_img, (gf.screen_width, gf.screen_height)) #change size
    gf.screen.blit(bg, (0, 0))

    #-------------------------------------------------------------------------------------------#
    #                                           other                                           #
    #-------------------------------------------------------------------------------------------#
    #*arguments:
    volume_controller_down_button_kwargs = {
        "x": gf.screen_width // 1.5,
        "y": gf.screen_height // 1.5,
        "width": 100,
        "height": 100,
        "texture_foldername": "buttons\\options",
        "texture_filename": "down.png",
        "hover_texture_filename": "down_h.png"
    } 
    volume_controller_up_button_kwargs = {
        "x": gf.screen_width // 1.5,
        "y": gf.screen_height // 3.5,
        "width": 100,
        "height": 100,
        "texture_foldername": "buttons\\options",
        "texture_filename": "up.png",
        "hover_texture_filename": "up_h.png"
    }

    res_now_button_kwargs = {
        "x": gf.screen_width // 1.9,
        "y": gf.screen_height // 3,
        "width": 100,
        "height": 50,
        "texture_foldername": "buttons\\options",
        "texture_filename": "change res.png",
        "hover_texture_filename": "change res h.png"
    }
    
    res_start_button_kwargs = {
        "x": gf.screen_width // 1.9,
        "y": gf.screen_height // 1.3,
        "width": 100,
        "height": 50,
        "texture_foldername": "buttons\\options",
        "texture_filename": "change res.png",
        "hover_texture_filename": "change res h.png"
    }

    back_button_kwargs = {
        "x": gf.screen_width // 100,
        "y": gf.screen_height // 100,
        "width": 168.75,
        "height": 75,
        "texture_foldername": "buttons\\other",
        "texture_filename": "back.png",
        "hover_texture_filename": "back h.png"
    }

    volume_option_entity_args = [
        gf.screen_width // 100,
        gf.screen_height // 3,
        300,
        50,
        "Volume and music",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    ]

    control_option_entity_args = [
        gf.screen_width // 100,
        gf.screen_height // 2,
        300,
        50,
        "Keymap",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    ]

    res_option_entity_args = [
        gf.screen_width // 100,
        gf.screen_height // 1.5,
        300,
        50,
        "Starting resolution",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    ]
    
    #*create:
    volume_option = en.Clickable_Text_object(*volume_option_entity_args)

    control_option = en.Clickable_Text_object(*control_option_entity_args)

    res_option = en.Clickable_Text_object(*res_option_entity_args)

    rp_option_entity_args = [
        gf.screen_width // 100,
        (res_option.y + res_option.height) + (gf.screen_height // 10),
        300,
        50,
        "Manage Resource Packs",
        gf.WHITE,
        gf.screen_width // 25,
        "fonts",
        "Livingst.ttf"
    ]

    rp_option = en.Clickable_Text_object(*rp_option_entity_args)

    #voulume and music
    if gf.what_option == "v":
        volume_controller_down = en.Button(**volume_controller_down_button_kwargs)
        volume_controller_up = en.Button(**volume_controller_up_button_kwargs)
        
        #the text that show what the voulume is
        volume_text = title_font.render(str(int(settings.volume * 100)), 1, gf.WHITE)
        gf.screen.blit(volume_text, (
            volume_controller_up.x,
            volume_controller_up.y + volume_controller_up.width
            ))
    #resolution
    elif gf.what_option == "r":
        #buttons
        res_now_button = en.Button(**res_now_button_kwargs)
        res_start_button = en.Button(**res_start_button_kwargs)
        
        #render the text
            #now
        now_res_title_text = title_res_font.render("Resolution", 1, gf.WHITE)
        width_text = res_font.render("Width: " + str(gf.screen_width), 1, gf.WHITE)
        height_text = res_font.render("Height: " + str(gf.screen_height), 1, gf.WHITE)
        
            #starting
        str_res_title_text = title_res_font.render("Starting Resolution", 1, gf.WHITE)
        str_width_text = res_font.render("Width: " + str(settings.game_start.start_width), 1, gf.WHITE)
        str_height_text = res_font.render("Height: " + str(settings.game_start.start_height), 1, gf.WHITE)

        
        #show the text on the screen
            #now
        gf.screen.blit(now_res_title_text, (
            gf.screen_width // 1.5,
            gf.screen_height // 5
        ))
        gf.screen.blit(width_text, (
            gf.screen_width // 1.5,
            gf.screen_height // 3.5
        ))
        gf.screen.blit(height_text, (
            gf.screen_width // 1.5,
            gf.screen_height // 2.5
        ))

            #starting
        gf.screen.blit(str_res_title_text, (
            gf.screen_width // 1.5 - (str_res_title_text.get_width() // 4),
            gf.screen_height // 1.7
        ))
        gf.screen.blit(str_width_text, (
            gf.screen_width // 1.5,
            gf.screen_height // 1.4
        ))
        gf.screen.blit(str_height_text, (
            gf.screen_width // 1.5,
            gf.screen_height // 1.2
        ))
    


    #back to the main menu
    back = en.Button(**back_button_kwargs)

    #update
    if gf.what_option == "v":
        volume_controller_down.update()
        volume_controller_up.update()
    elif gf.what_option == "k":
        keymap_image.update(
            gf.screen_width // 3,
            0
        )
    elif gf.what_option == "r":
        res_now_button.update()
        res_start_button.update()
    
    
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
        if volume_controller_down.click():
            sys.Music_and_SFX.change_volume("down")
        elif volume_controller_up.click():
            sys.Music_and_SFX.change_volume("up")
    if gf.what_option == "r":
        if res_now_button.click():
            gf.window_open = True
            tk.options_res()
        elif res_start_button.click():
            gf.window_open = True
            tk.start_options_res()
    
    #what option
    if volume_option.update():
        gf.what_option = "v"
    if control_option.update():
        gf.what_option = "k"
    if res_option.update():
        gf.what_option = "r"
    if rp_option.update():
        gf.what_option = "rp"
        gf.window_open = True
        tk.add_resource_pack_option([], 10)
    #%end%-------------------------------------------------------------------%end%#
