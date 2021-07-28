import pygame
from pygame.constants import MOUSEBUTTONDOWN, QUIT
from game import globals_file as gf
from time import sleep

@staticmethod
def one():
    
    #?---------------------------------------------------------------------------------?#
    #?---------------------------------< Tiles Click >---------------------------------?#
    #?---------------------------------------------------------------------------------?#
    gf.Tiles.click()


    #!--------------------------------------------------------------------------------!#
    #!-----------------------------------< UPDATE >-----------------------------------!#
    #!--------------------------------------------------------------------------------!#
    gf.screen.fill(gf.LIGHTBLUE)
    gf.Tiles.update(1)
    
    if gf.run_level == False:

        gf.classed_map.buttons.l_1_completed = True
        gf.classed_map.buttons.l_2_unlocked = True

        gf.where = "play"
        gf.Sounds_and_sfx_dict["main"].play(-1)
        gf.start_music = True

@staticmethod
def two():
    print ("two")

@staticmethod
def three():
    print ("three")

@staticmethod
def four():
    print ("four")

@staticmethod
def five():
    print ("five")

@staticmethod
def six():
    print ("six")

@staticmethod
def seven():
    print ("seven")

@staticmethod
def eight():
    print ("eight")

@staticmethod
def nine():
    print ("nine")