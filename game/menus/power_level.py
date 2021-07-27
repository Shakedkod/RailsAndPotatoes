import pygame, os

from moviepy.editor import VideoFileClip

from game import globals_file as gf
from game import system as sys

#!-------------------------------------------------------------------------------!#
#!-----------------------------------< START >-----------------------------------!#
#!-------------------------------------------------------------------------------!#
def levels_n_staff():
    #appdata
    APPDATA = os.getenv('APPDATA')
    
    #?---------------------------------------------------------------------------?#
    #?-----------------------------------< 0 >-----------------------------------?#
    #?---------------------------------------------------------------------------?#
    if gf.level == "c0":
        #%start%--------------------------------------------------------%start%#
        if gf.start_music:
            gf.Sounds_and_sfx_dict["main"].fadeout(10)
        else:
            gf.Sounds_and_sfx_dict["start"].fadeout(10)

        #load cutscence and start it
        clip = VideoFileClip(
            APPDATA + "\\.rails_and_potatoes\\index\\Assets\\cutscenes\\open.mp4",
            False,
            True,
            200000,
            (
                gf.screen_height,
                gf.screen_width
                )
            )
        clip.preview()

        #restart the mixer
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.mixer.init() #init pygame mixer

        #restarting the window
        gf.screen = pygame.display.set_mode((gf.screen_width, gf.screen_height), pygame.RESIZABLE)

        gf.classed_map.buttons.c_0_completed = True
        gf.classed_map.buttons.l_1_unlocked = True

        gf.where = "play"
        gf.Sounds_and_sfx_dict["main"].play(-1)
        gf.start_music = True
        #%end%--------------------------------------------------------%end%#
    
    #?---------------------------------------------------------------------------?#
    #?-----------------------------------< 1 >-----------------------------------?#
    #?---------------------------------------------------------------------------?#
    elif gf.level == "l1":
        #%start%--------------------------------------------------------%start%#
        #load level and start it
        sys.levels.one()

        gf.where = "play"
        gf.Sounds_and_sfx_dict["main"].play(-1)
        gf.start_music = True

        #%end%--------------------------------------------------------%end%#

