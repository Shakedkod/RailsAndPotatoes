import pygame
from pygame.locals import *
from . import globals_file as gf, entities as en, textures as t, music, settings as s
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
#*-----------------------#main#--------------------------*#
class Map:
    def __init__(self, filename, foldername):
        self.the_part = 0
        self.x = 0
        self.x_before = 0
        self.filename = filename
        self.foldername = foldername
        gf.Sounds_and_sfx_dict = music.load_sounds_or_sfx(gf.Sounds_and_sfx_dict, "woosh_sfx.mp3", "map", "sfx.map.woosh", s.voulume)
        self.loaded_image = pygame.image.load(
            t.change_texture(
                foldername = self.foldername,
                filename = self.filename 
                )
            )
        self.image = pygame.transform.scale(
            self.loaded_image,
            (
                gf.screen_width * 3,
                gf.screen_height
                )
            )
    
    def update(self):
        self.image = pygame.transform.scale(
            self.loaded_image,
            (
                gf.screen_width * 3,
                gf.screen_height
                )
            )
        self.were_is_the_click()
        #========================================================================================#
        if ((self.the_part == 1) or (self.the_part == 4) or (self.the_part == 7)) and (self.x > 0):
            self.x -= 1
        elif ((self.the_part == 3) or (self.the_part == 6) or (self.the_part == 9)) and (self.x < 3):
            self.x += 1
        
        if self.x > 3:
            self.x = 3
        elif self.x < 0:
            self.x = 0
        #========================================================================================#
        if self.x_before != self.x:
            gf.Sounds_and_sfx_dict["sfx.map.woosh"].play(0)
            self.x_before = self.x
        
        #------------------------------x == 0------------------------------#
        if (self.x == 0):
            gf.screen.blit(
                self.image,
                (0, 0)
            )
        #------------------------------x == 1------------------------------#
        elif (self.x == 1):
            gf.screen.blit(
                self.image,
                (
                    -1*(gf.screen_width // 3),
                    0
                    )
            )
        #------------------------------x == 2------------------------------#
        elif (self.x == 2):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 3) * 2),
                    0
                    )
            )
        #------------------------------x == 3------------------------------#
        elif (self.x == 3):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 3) * 3),
                    0
                    )
            )
        #------------------------------#*==*#------------------------------#

    def were_is_the_click(self):
        O1 = en.Clickable_Invisible_object(
            0,
            0,
            300,
            166.6666666666667
            )
        O2 = en.Clickable_Invisible_object(
            O1.width,
            0,
            300,
            166.6666666666667
            )
        O3 = en.Clickable_Invisible_object(
            O1.width * 2,
            0,
            300,
            166.6666666666667
            )
        O4 = en.Clickable_Invisible_object(
            0,
            O1.height,
            300,
            166.6666666666667
            )
        O5 = en.Clickable_Invisible_object(
            O1.width,
            O1.height,
            300,
            166.6666666666667
            )
        O6 = en.Clickable_Invisible_object(
            O1.width * 2,
            O1.height,
            300,
            166.6666666666667
            )
        O7 = en.Clickable_Invisible_object(
            0,
            O1.height * 2,
            300,
            166.6666666666667
            )
        O8 = en.Clickable_Invisible_object(
            O1.width,
            O1.height * 2,
            300,
            166.6666666666667
            )
        O9 = en.Clickable_Invisible_object(
            O1.width * 2,
            O1.height * 2,
            300,
            166.6666666666667
            )
        if O1.update():
            self.the_part = 1 #top left
        elif O2.update():
            self.the_part = 2 #top center
        elif O3.update():
            self.the_part = 3 #top right
        elif O4.update():
            self.the_part = 4 #middle left
        elif O5.update():
            self.the_part = 5 #middle center
        elif O6.update():
            self.the_part = 6 #middle right
        elif O7.update():
            self.the_part = 7 #bottom left
        elif O8.update():
            self.the_part = 8 #bottom center
        elif O9.update():
            self.the_part = 9 #bottom right
        else:
            self.the_part = 0 #not eny
