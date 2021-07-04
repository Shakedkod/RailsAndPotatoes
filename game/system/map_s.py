from tkinter.constants import NO
import pygame
from pygame.locals import *
from . import globals_file as gf, entities as en, textures as t, music, settings as s
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
#%start%-------------------------------------------------------------------%start%#

class battons_for_later:
    def __init__(self):
        #cutscenes in 0, 27, 54(for now)

        self.back = None
        self.next = None

        #c for cutscenes
        #l for levels

        #----#x = 0#----#
        self.c_0 = None
        self.l_1 = None
        self.l_2 = None
        self.l_3 = None
        self.l_4 = None

        #----#x = 1#----#
        self.l_5 = None
        self.l_6 = None
        self.l_7 = None
        self.l_8 = None
        self.l_9 = None

        #----#x = 2#----#
        self.l_10 = None
        self.l_11 = None
        self.l_12 = None
        self.l_13 = None
        self.l_14 = None

        #----#x = 3#----#
        self.l_15 = None
        self.l_16 = None
        self.l_17 = None
        self.l_18 = None
        self.l_19 = None

        #----#x = 4#----#
        self.l_20 = None
        self.l_21 = None
        self.l_22 = None
        self.l_23 = None
        self.l_24 = None
        
        #----#x = 5#----#
        self.l_25 = None
        self.l_26 = None
        self.c_27 = None
        self.l_28 = None
        self.l_29 = None

        #----#x = 6#----#
        self.l_30 = None
        self.l_31 = None
        self.l_32 = None
        self.l_33 = None
        self.l_34 = None

        #----#x = 7#----#
        self.l_35 = None
        self.l_36 = None
        self.l_37 = None
        self.l_38 = None
        self.l_39 = None

        #----#x = 8#----#
        self.l_40 = None
        self.l_41 = None
        self.l_42 = None
        self.l_43 = None
        self.l_44 = None

        #----#x = 9#----#
        self.l_45 = None
        self.l_46 = None
        self.l_47 = None
        self.l_48 = None
        self.l_49 = None

        #----#x = 10#----#
        self.l_50 = None
        self.l_51 = None
        self.l_52 = None
        self.l_53 = None
        self.c_54 = None

    #%end%-------------------------------------------------------------------%end%#


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
                gf.screen_width * 10,
                gf.screen_height
                )
            )
        self.buttons = battons_for_later()
    
    def update(self):
        self.image = pygame.transform.scale(
            self.loaded_image,
            (
                gf.screen_width * 10,
                gf.screen_height
                )
            )
        self.were_is_the_click()
        #========================================================================================#
        if ((self.the_part == 1) or (self.the_part == 4) or (self.the_part == 7)) and (self.x >= 0):
            self.x -= 1
        elif ((self.the_part == 3) or (self.the_part == 6) or (self.the_part == 9)) and (self.x <= 10):
            self.x += 1
        
        if self.x >= 10:
            self.x = 10
        elif self.x <= 0:
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
                    -1*(gf.screen_width // 10),
                    0
                    )
            )
        #------------------------------x == 2------------------------------#
        elif (self.x == 2):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 2),
                    0
                    )
            )
        #------------------------------x == 3------------------------------#
        elif (self.x == 3):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 3),
                    0
                    )
            )
        #------------------------------x == 4------------------------------#
        elif (self.x == 4):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 4),
                    0
                    )
            )
        #------------------------------x == 5------------------------------#
        elif (self.x == 5):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 5),
                    0
                    )
            )
        #------------------------------x == 6------------------------------#
        elif (self.x == 6):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 6),
                    0
                    )
            )
        #------------------------------x == 7------------------------------#
        elif (self.x == 7):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 7),
                    0
                    )
            )
        #------------------------------x == 8------------------------------#
        elif (self.x == 8):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 8),
                    0
                    )
            )
        #------------------------------x == 9------------------------------#
        elif (self.x == 9):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 9),
                    0
                    )
            )
        #------------------------------x == 10------------------------------#
        elif (self.x == 10):
            gf.screen.blit(
                self.image,
                (
                    -1*((gf.screen_width // 10) * 10),
                    0
                    )
            )
        #------------------------------#*==*#------------------------------#
        #buttons
        #self.buttons.next = en.Button(
        #    
        #)

        if self.x == 0: #(page 0: levels: 0 - 4)  #0CUTSCENE, 1, 2, 3, 4
            #create buttons
            self.buttons.c_0 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png"
            )
            self.buttons.l_1 = en.Button(
                (self.buttons.c_0.x + self.buttons.c_0.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png"
            )
            self.buttons.l_2 = en.Button(
                (self.buttons.l_1.x + self.buttons.l_1.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png"
            )
            self.buttons.l_3 = en.Button(
                (self.buttons.l_2.x + self.buttons.l_2.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png"
            )
            self.buttons.l_4 = en.Button(
                (self.buttons.l_3.x + self.buttons.l_3.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png"
            )

            #update buttons
            self.buttons.c_0.update()
            self.buttons.l_1.update()
            self.buttons.l_2.update()
            self.buttons.l_3.update()
            self.buttons.l_4.update()


            #%end%#
        elif self.x == 1: #(page 1: levels: 5 - 9)#5, 6, 7, 8, 9
            pass


            #%end%#
        elif self.x == 2: #(page 2: levels: 10 - 14)#10, 11, 12, 13, 14
            pass


            #%end%#
        elif self.x == 3: #(page 3: levels: 15 - 19)#15, 16, 17, 18, 19
            pass


            #%end%#
        elif self.x == 4: #(page 4: levels: 20 - 24)#20, 21, 22, 23, 24
            pass


            #%end%#
        elif self.x == 5: #(page 5: levels: 25 - 29)#25, 26, 27CUTSCENE, 28, 29
            pass


            #%end%#
        elif self.x == 6: #(page 6: levels: 30 - 34)#30, 31, 32, 33, 34
            pass


            #%end%#
        elif self.x == 7: #(page 7: levels: 35 - 39)#35, 36, 37, 38, 39
            pass


            #%end%#
        elif self.x == 8: #(page 8: levels: 40 - 44)#40, 41, 42, 43, 44
            pass


            #%end%#
        elif self.x == 9: #(page 9: levels: 45 - 49)#45, 46, 47, 48, 49
            pass


            #%end%#
        elif self.x == 10: #(page 8: levels: 50 - 54)#50, 51, 52, 53, 54CUTSCENE
            pass


            #%end%#
    #%end%-------------------------------------------------------------------%end%#

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
        #?--------------------------update--------------------------?#
        if O2.update():
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
    #%end%-------------------------------------------------------------------%end%#
