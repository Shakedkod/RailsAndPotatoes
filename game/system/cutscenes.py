import pygame
from moviepy.editor import *
from . import globals_file as gf, settings as s
#-----------------------------------------------------------------------#
pygame.init()
pygame.display.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
#%start%-----------------------------------------------------------------------%start%#

def regular(name, path):
    #%start%------------------------------------%start%#
    pygame.display.set_caption(name)
    
    clip = VideoFileClip(
        path,
        has_mask = False,
        audio = True,
        target_resolution = (gf.screen_width, gf.screen_height)
        )
    clip.preview()

    #reload mixer
    pygame.mixer.quit()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    pygame.mixer.init()

    #display
    pygame.display.set_caption(s.game_start.caption)
    gf.screen = pygame.display.set_mode(
        (gf.screen_width, gf.screen_height),
        pygame.RESIZABLE
        )
    #%end%------------------------------------%end%#


def endgame(name, path):
    #%start%------------------------------------%start%#
    pygame.display.set_caption(name)
    
    clip = VideoFileClip(
        path,
        has_mask = False,
        audio = True,
        target_resolution = (gf.screen_width, gf.screen_height)
        )
    clip.preview()

    #clip = VideoFileClip(
    #    !path to the credits,
    #    has_mask = False,
    #    audio = True,
    #    target_resolution = (gf.screen_width, gf.screen_height)
    #    )
    #clip.preview()

    #reload mixer
    pygame.mixer.quit()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    pygame.mixer.init()

    #display
    pygame.display.set_caption(s.game_start.caption)
    gf.screen = pygame.display.set_mode(
        (gf.screen_width, gf.screen_height),
        pygame.RESIZABLE
        )
    
    #back to the main menu
    gf.where = "main menu"
    #%end%------------------------------------%end%#

#%end%-----------------------------------------------------------------------%end%#
