import pygame
from pygame.locals import *
from . import globals_file as gf, entities as en, textures as t
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
#*-----------------------#main#--------------------------*#
class Map:
    def __init__(self, filename, foldername):
        self.the_part = 0
        self.x = 0
        self.y = 0
        self.filename = filename
        self.foldername = foldername
        self.loaded_image = pygame.image.load(
            t.change_texture(
                foldername = self.foldername,
                filename = self.filename 
                )
            )
        self.image = pygame.transform.scale(
            self.loaded_image,
            (
                gf.screen_width // 3,
                gf.screen_height // 3
                )
            )
    
    def update(self):
        self.image = pygame.transform.scale(
            self.loaded_image,
            (
                gf.screen_width // 3,
                gf.screen_height // 3
                )
            )
        self.were_is_the_click()
        #========================================================================================#
        if (self.the_part == 1) and ((self.x > 0) and (self.y > 0)):
            self.x -= 1
            self.y -= 1
        elif (self.the_part == 2) and (self.y > 0):
            self.y -= 1
        elif (self.the_part == 3) and ((self.x < 3) and (self.y > 0)):
            self.x += 1
            self.y -= 1
        elif (self.the_part == 4) and (self.x > 0):
            self.x -= 1
        elif (self.the_part == 6) and (self.x < 3):
            self.x += 1
        elif (self.the_part == 7) and ((self.x > 0) and (self.y < 3)):
            self.x -= 1
            self.y += 1
        elif (self.the_part == 8) and (self.y < 3):
            self.y += 1
        elif (self.the_part == 9) and ((self.x < 3) and (self.y < 3)):
            self.x += 1
            self.y += 1
        
        if self.x > 3:
            self.x = 3
        elif self.x < 0:
            self.x = 0
        
        if self.y > 3:
            self.y = 3
        elif self.y < 0:
            self.y = 0
        #========================================================================================#
        #------------------------------x == 0------------------------------#
        if (self.x == 0) and (self.y == 0):
            gf.screen.blit(
                self.image,
                (0, 0)
            )
        elif (self.x == 0) and (self.y == 1):
            gf.screen.blit(
                self.image,
                (
                    0,
                    gf.screen_height // 3
                    )
            )
        elif (self.x == 0) and (self.y == 2):
            gf.screen.blit(
                self.image,
                (
                    0,
                    (gf.screen_height // 3) * 2
                    )
            )
        elif (self.x == 0) and (self.y == 3):
            gf.screen.blit(
                self.image,
                (
                    0,
                    (gf.screen_height // 3) * 3
                    )
            )
        #------------------------------x == 1------------------------------#
        elif (self.x == 1) and (self.y == 0):
            gf.screen.blit(
                self.image,
                (
                    gf.screen_width // 3,
                    0
                    )
            )
        elif (self.x == 1) and (self.y == 0):
            gf.screen.blit(
                self.image,
                (
                    gf.screen_width // 3,
                    0
                    )
            )
        elif (self.x == 1) and (self.y == 1):
            gf.screen.blit(
                self.image,
                (
                    gf.screen_width // 3,
                    gf.screen_height // 3
                    )
            )
        elif (self.x == 1) and (self.y == 2):
            gf.screen.blit(
                self.image,
                (
                    gf.screen_width // 3,
                   ( gf.screen_height // 3) * 2
                    )
            )
        elif (self.x == 1) and (self.y == 3):
            gf.screen.blit(
                self.image,
                (
                    gf.screen_width // 3,
                   ( gf.screen_height // 3) * 3
                    )
            )
        #------------------------------x == 2------------------------------#
        elif (self.x == 2) and (self.y == 0):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 2,
                    0
                    )
            )
        elif (self.x == 2) and (self.y == 1):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 2,
                    gf.screen_height // 3
                    )
            )
        elif (self.x == 2) and (self.y == 2):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 2,
                    (gf.screen_height // 3) * 2
                    )
            )
        elif (self.x == 2) and (self.y == 3):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 2,
                    (gf.screen_height // 3) * 3
                    )
            )
        #------------------------------x == 3------------------------------#
        elif (self.x == 3) and (self.y == 0):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 3,
                    0
                    )
            )
        elif (self.x == 3) and (self.y == 1):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 3,
                    gf.screen_height // 3
                    )
            )
        elif (self.x == 3) and (self.y == 2):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 3,
                    (gf.screen_height // 3) * 2
                    )
            )
        elif (self.x == 3) and (self.y == 3):
            gf.screen.blit(
                self.image,
                (
                    (gf.screen_width // 3) * 3,
                    (gf.screen_height // 3) * 3
                    )
            )
        #------------------------------#*==*#------------------------------#
        #blit here

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
            self.the_part = 1
        elif O2.update():
            self.the_part = 2
        elif O3.update():
            self.the_part = 3
        elif O4.update():
            self.the_part = 4
        elif O5.update():
            self.the_part = 5
        elif O6.update():
            self.the_part = 6
        elif O7.update():
            self.the_part = 7
        elif O8.update():
            self.the_part = 8
        elif O9.update():
            self.the_part = 9
        else:
            self.the_part = 0
