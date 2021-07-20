import pygame
from pygame.locals import *
from game import system as sys, globals_file as gf
from . import entities as en, textures as t, settings as s
#*-----------------------#init#--------------------------*#
pygame.init() #init pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
#%start%-------------------------------------------------------------------%start%#

class battons_for_later:
    def __init__(self):
        #cutscenes in 0, 27, 54(for now)

        self.back_button = None
        self.next_button = None

        #c for cutscenes
        #l for levels

        #----#x = 0#----#
        self.c_0 = None
        self.c_0_completed = False
        self.l_1 = None
        self.l_1_completed = False
        self.l_1_unlocked = False
        self.l_2 = None
        self.l_2_completed = False
        self.l_2_unlocked = False
        self.l_3 = None
        self.l_3_completed = False
        self.l_3_unlocked = False
        self.l_4 = None
        self.l_4_completed = False
        self.l_4_unlocked = False

        #----#x = 1#----#
        self.l_5 = None
        self.l_5_completed = False
        self.l_5_unlocked = False
        self.l_6 = None
        self.l_6_completed = False
        self.l_6_unlocked = False
        self.l_7 = None
        self.l_7_completed = False
        self.l_7_unlocked = False
        self.l_8 = None
        self.l_8_completed = False
        self.l_8_unlocked = False
        self.l_9 = None
        self.l_9_completed = False
        self.l_9_unlocked = False

        #----#x = 2#----#
        self.l_10 = None
        self.l_10_completed = False
        self.l_10_unlocked = False
        self.l_11 = None
        self.l_11_completed = False
        self.l_11_unlocked = False
        self.l_12 = None
        self.l_12_completed = False
        self.l_12_unlocked = False
        self.l_13 = None
        self.l_13_completed = False
        self.l_13_unlocked = False
        self.l_14 = None
        self.l_14_completed = False
        self.l_14_unlocked = False

        #----#x = 3#----#
        self.l_15 = None
        self.l_15_completed = False
        self.l_15_unlocked = False
        self.l_16 = None
        self.l_16_completed = False
        self.l_16_unlocked = False
        self.l_17 = None
        self.l_17_completed = False
        self.l_17_unlocked = False
        self.l_18 = None
        self.l_18_completed = False
        self.l_18_unlocked = False
        self.l_19 = None
        self.l_19_completed = False
        self.l_19_unlocked = False

        #----#x = 4#----#
        self.l_20 = None
        self.l_20_completed = False
        self.l_20_unlocked = False
        self.l_21 = None
        self.l_21_completed = False
        self.l_21_unlocked = False
        self.l_22 = None
        self.l_22_completed = False
        self.l_22_unlocked = False
        self.l_23 = None
        self.l_23_completed = False
        self.l_23_unlocked = False
        self.l_24 = None
        self.l_24_completed = False
        self.l_24_unlocked = False
        
        #----#x = 5#----#
        self.l_25 = None
        self.l_25_completed = False
        self.l_25_unlocked = False
        self.l_26 = None
        self.l_26_completed = False
        self.l_26_unlocked = False
        self.c_27 = None
        self.c_27_completed = False
        self.c_27_unlocked = False
        self.l_28 = None
        self.l_28_completed = False
        self.l_28_unlocked = False
        self.l_29 = None
        self.l_29_completed = False
        self.l_29_unlocked = False

        #----#x = 6#----#
        self.l_30 = None
        self.l_30_completed = False
        self.l_30_unlocked = False
        self.l_31 = None
        self.l_31_completed = False
        self.l_31_unlocked = False
        self.l_32 = None
        self.l_32_completed = False
        self.l_32_unlocked = False
        self.l_33 = None
        self.l_33_completed = False
        self.l_33_unlocked = False
        self.l_34 = None
        self.l_34_completed = False
        self.l_34_unlocked = False

        #----#x = 7#----#
        self.l_35 = None
        self.l_35_completed = False
        self.l_35_unlocked = False
        self.l_36 = None
        self.l_36_completed = False
        self.l_36_unlocked = False
        self.l_37 = None
        self.l_37_completed = False
        self.l_37_unlocked = False
        self.l_38 = None
        self.l_38_completed = False
        self.l_38_unlocked = False
        self.l_39 = None
        self.l_39_completed = False
        self.l_39_unlocked = False

        #----#x = 8#----#
        self.l_40 = None
        self.l_40_completed = False
        self.l_40_unlocked = False
        self.l_41 = None
        self.l_41_completed = False
        self.l_41_unlocked = False
        self.l_42 = None
        self.l_42_completed = False
        self.l_42_unlocked = False
        self.l_43 = None
        self.l_43_completed = False
        self.l_43_unlocked = False
        self.l_44 = None
        self.l_44_completed = False
        self.l_44_unlocked = False

        #----#x = 9#----#
        self.l_45 = None
        self.l_45_completed = False
        self.l_45_unlocked = False
        self.l_46 = None
        self.l_46_completed = False
        self.l_46_unlocked = False
        self.l_47 = None
        self.l_47_completed = False
        self.l_47_unlocked = False
        self.l_48 = None
        self.l_48_completed = False
        self.l_48_unlocked = False
        self.l_49 = None
        self.l_49_completed = False
        self.l_49_unlocked = False

        #----#x = 10#----#
        self.l_50 = None
        self.l_50_completed = False
        self.l_50_unlocked = False
        self.l_51 = None
        self.l_51_completed = False
        self.l_51_unlocked = False
        self.l_52 = None
        self.l_52_completed = False
        self.l_52_unlocked = False
        self.l_53 = None
        self.l_53_completed = False
        self.l_53_unlocked = False
        self.c_54 = None
        self.c_54_completed = False
        self.c_54_unlocked = False

    #%end%-------------------------------------------------------------------%end%#


class Map:
    def __init__(self, filename, foldername):
        self.the_part = 0
        self.x = 0
        self.x_before = 0
        self.filename = filename
        self.foldername = foldername
        gf.Sounds_and_sfx_dict = sys.Music_and_SFX.load_sounds_or_sfx(gf.Sounds_and_sfx_dict, "woosh_sfx.mp3", "map", "sfx.map.woosh", s.volume)
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

        #buttons#
        self.buttons.next_button = en.Button(
            gf.screen_width - (gf.screen_width // 5),
            gf.screen_height // 100,
            168.75,
            75
        )
        self.buttons.back_button = en.Button(
            gf.screen_width // 100,
            gf.screen_height - (gf.screen_height // 8),
            168.75,
            75
        )

        #update#
        self.buttons.next_button.update()
        self.buttons.back_button.update()

        #click#
        if self.buttons.next_button.click():
            self.x += 1
        if self.buttons.back_button.click():
            self.x -= 1

        if self.x > 10:
            self.x = 0
        elif self.x < 0:
            self.x = 10
        
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

        self.buttons.next_button.draw()
        self.buttons.back_button.draw()
        
        #========================================================================================#
        if self.x_before != self.x:
            gf.Sounds_and_sfx_dict["sfx.map.woosh"].play(0)
            self.x_before = self.x
        


        if self.x == 0: #(page 0: levels: 0 - 4)  #0CUTSCENE, 1, 2, 3, 4
            #create buttons
            self.buttons.c_0 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "0.png",
                "0_h.png",
                "0_comp.png",
                completed = self.buttons.c_0_completed
            )
            self.buttons.l_1 = en.Button(
                (self.buttons.c_0.x + self.buttons.c_0.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_1_unlocked,
                completed = self.buttons.l_1_completed
            )
            self.buttons.l_2 = en.Button(
                (self.buttons.l_1.x + self.buttons.l_1.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_2_unlocked,
                completed = self.buttons.l_2_completed
            )
            self.buttons.l_3 = en.Button(
                (self.buttons.l_2.x + self.buttons.l_2.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_3_unlocked,
                completed = self.buttons.l_3_completed
            )
            self.buttons.l_4 = en.Button(
                (self.buttons.l_3.x + self.buttons.l_3.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_4_unlocked,
                completed = self.buttons.l_4_completed
                
            )

            #update buttons
            self.buttons.c_0.update()
            self.buttons.l_1.update()
            self.buttons.l_2.update()
            self.buttons.l_3.update()
            self.buttons.l_4.update()


            #%end%#
        elif self.x == 1: #(page 1: levels: 5 - 9)#5, 6, 7, 8, 9
            #create buttons
            self.buttons.l_5 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_5_unlocked,
                completed = self.buttons.l_5_completed
                
            )
            self.buttons.l_6 = en.Button(
                (self.buttons.l_5.x + self.buttons.l_5.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_6_unlocked,
                completed = self.buttons.l_6_completed
                
            )
            self.buttons.l_7 = en.Button(
                (self.buttons.l_6.x + self.buttons.l_6.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_7_unlocked,
                completed = self.buttons.l_7_completed
                
            )
            self.buttons.l_8 = en.Button(
                (self.buttons.l_7.x + self.buttons.l_7.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_8_unlocked,
                completed = self.buttons.l_8_completed
                
            )
            self.buttons.l_9 = en.Button(
                (self.buttons.l_8.x + self.buttons.l_8.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_9_unlocked,
                completed = self.buttons.l_9_completed
                
            )

            #update buttons
            self.buttons.l_5.update()
            self.buttons.l_6.update()
            self.buttons.l_7.update()
            self.buttons.l_8.update()
            self.buttons.l_9.update()


            #%end%#
        elif self.x == 2: #(page 2: levels: 10 - 14)#10, 11, 12, 13, 14
            #create buttons
            self.buttons.l_10 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_10_unlocked,
                completed = self.buttons.l_10_completed
                
            )
            self.buttons.l_11 = en.Button(
                (self.buttons.l_10.x + self.buttons.l_10.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_11_unlocked,
                completed = self.buttons.l_11_completed
                
            )
            self.buttons.l_12 = en.Button(
                (self.buttons.l_11.x + self.buttons.l_11.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_12_unlocked,
                completed = self.buttons.l_12_completed
                
            )
            self.buttons.l_13 = en.Button(
                (self.buttons.l_12.x + self.buttons.l_12.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_13_unlocked,
                completed = self.buttons.l_13_completed
                
            )
            self.buttons.l_14 = en.Button(
                (self.buttons.l_13.x + self.buttons.l_13.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_14_unlocked,
                completed = self.buttons.l_14_completed
                
            )

            #update buttons
            self.buttons.l_10.update()
            self.buttons.l_11.update()
            self.buttons.l_12.update()
            self.buttons.l_13.update()
            self.buttons.l_14.update()


            #%end%#
        elif self.x == 3: #(page 3: levels: 15 - 19)#15, 16, 17, 18, 19
            #create buttons
            self.buttons.l_15 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_15_unlocked,
                completed = self.buttons.l_15_completed
                
            )
            self.buttons.l_16 = en.Button(
                (self.buttons.l_15.x + self.buttons.l_15.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_16_unlocked,
                completed = self.buttons.l_16_completed
                
            )
            self.buttons.l_17 = en.Button(
                (self.buttons.l_16.x + self.buttons.l_16.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_17_unlocked,
                completed = self.buttons.l_17_completed
                
            )
            self.buttons.l_18 = en.Button(
                (self.buttons.l_17.x + self.buttons.l_17.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_18_unlocked,
                completed = self.buttons.l_18_completed
                
            )
            self.buttons.l_19 = en.Button(
                (self.buttons.l_18.x + self.buttons.l_18.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_19_unlocked,
                completed = self.buttons.l_19_completed
                
            )

            #update buttons
            self.buttons.l_15.update()
            self.buttons.l_16.update()
            self.buttons.l_17.update()
            self.buttons.l_18.update()
            self.buttons.l_19.update()


            #%end%#
        elif self.x == 4: #(page 4: levels: 20 - 24)#20, 21, 22, 23, 24
            #create buttons
            self.buttons.l_20 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_20_unlocked,
                completed = self.buttons.l_20_completed
                
            )
            self.buttons.l_21 = en.Button(
                (self.buttons.l_20.x + self.buttons.l_20.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_21_unlocked,
                completed = self.buttons.l_21_completed
                
            )
            self.buttons.l_22 = en.Button(
                (self.buttons.l_21.x + self.buttons.l_21.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_22_unlocked,
                completed = self.buttons.l_22_completed
                
            )
            self.buttons.l_23 = en.Button(
                (self.buttons.l_22.x + self.buttons.l_22.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_23_unlocked,
                completed = self.buttons.l_23_completed
                
            )
            self.buttons.l_24 = en.Button(
                (self.buttons.l_23.x + self.buttons.l_23.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_24_unlocked,
                completed = self.buttons.l_24_completed
                
            )

            #update buttons
            self.buttons.l_20.update()
            self.buttons.l_21.update()
            self.buttons.l_22.update()
            self.buttons.l_23.update()
            self.buttons.l_24.update()


            #%end%#
        elif self.x == 5: #(page 5: levels: 25 - 29)#25, 26, 27CUTSCENE, 28, 29
            #create buttons
            self.buttons.l_25 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_25_unlocked,
                completed = self.buttons.l_25_completed
                
            )
            self.buttons.l_26 = en.Button(
                (self.buttons.l_25.x + self.buttons.l_25.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_26_unlocked,
                completed = self.buttons.l_26_completed
                
            )
            self.buttons.c_27 = en.Button(
                (self.buttons.l_26.x + self.buttons.l_26.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.c_27_unlocked,
                completed = self.buttons.c_27_completed
                
            )
            self.buttons.l_28 = en.Button(
                (self.buttons.c_27.x + self.buttons.c_27.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_28_unlocked,
                completed = self.buttons.l_28_completed
                
            )
            self.buttons.l_29 = en.Button(
                (self.buttons.l_28.x + self.buttons.l_28.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_29_unlocked,
                completed = self.buttons.l_29_completed
                
            )

            #update buttons
            self.buttons.l_25.update()
            self.buttons.l_26.update()
            self.buttons.c_27.update()
            self.buttons.l_28.update()
            self.buttons.l_29.update()


            #%end%#
        elif self.x == 6: #(page 6: levels: 30 - 34)#30, 31, 32, 33, 34
            #create buttons
            self.buttons.l_30 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_30_unlocked,
                completed = self.buttons.l_30_completed
                
            )
            self.buttons.l_31 = en.Button(
                (self.buttons.l_30.x + self.buttons.l_30.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_31_unlocked,
                completed = self.buttons.l_31_completed
                
            )
            self.buttons.l_32 = en.Button(
                (self.buttons.l_31.x + self.buttons.l_31.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_32_unlocked,
                completed = self.buttons.l_32_completed
                
            )
            self.buttons.l_33 = en.Button(
                (self.buttons.l_32.x + self.buttons.l_32.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_33_unlocked,
                completed = self.buttons.l_33_completed
                
            )
            self.buttons.l_34 = en.Button(
                (self.buttons.l_33.x + self.buttons.l_33.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_34_unlocked,
                completed = self.buttons.l_34_completed
                
            )

            #update buttons
            self.buttons.l_30.update()
            self.buttons.l_31.update()
            self.buttons.l_32.update()
            self.buttons.l_33.update()
            self.buttons.l_34.update()


            #%end%#
        elif self.x == 7: #(page 7: levels: 35 - 39)#35, 36, 37, 38, 39
            #create buttons
            self.buttons.l_35 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_35_unlocked,
                completed = self.buttons.l_35_completed
                
            )
            self.buttons.l_36 = en.Button(
                (self.buttons.l_35.x + self.buttons.l_35.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_36_unlocked,
                completed = self.buttons.l_36_completed
                
            )
            self.buttons.l_37 = en.Button(
                (self.buttons.l_36.x + self.buttons.l_36.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_37_unlocked,
                completed = self.buttons.l_37_completed
                
            )
            self.buttons.l_38 = en.Button(
                (self.buttons.l_37.x + self.buttons.l_37.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_38_unlocked,
                completed = self.buttons.l_38_completed
                
            )
            self.buttons.l_39 = en.Button(
                (self.buttons.l_38.x + self.buttons.l_38.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_39_unlocked,
                completed = self.buttons.l_39_completed
                
            )

            #update buttons
            self.buttons.l_35.update()
            self.buttons.l_36.update()
            self.buttons.l_37.update()
            self.buttons.l_38.update()
            self.buttons.l_39.update()


            #%end%#
        elif self.x == 8: #(page 8: levels: 40 - 44)#40, 41, 42, 43, 44
            #create buttons
            self.buttons.l_40 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_40_unlocked,
                completed = self.buttons.l_40_completed
                
            )
            self.buttons.l_41 = en.Button(
                (self.buttons.l_40.x + self.buttons.l_40.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_41_unlocked,
                completed = self.buttons.l_41_completed
                
            )
            self.buttons.l_42 = en.Button(
                (self.buttons.l_41.x + self.buttons.l_41.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_42_unlocked,
                completed = self.buttons.l_42_completed
                
            )
            self.buttons.l_43 = en.Button(
                (self.buttons.l_42.x + self.buttons.l_42.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_43_unlocked,
                completed = self.buttons.l_43_completed
                
            )
            self.buttons.l_44 = en.Button(
                (self.buttons.l_43.x + self.buttons.l_43.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_44_unlocked,
                completed = self.buttons.l_44_completed
                
            )

            #update buttons
            self.buttons.l_40.update()
            self.buttons.l_41.update()
            self.buttons.l_42.update()
            self.buttons.l_43.update()
            self.buttons.l_44.update()


            #%end%#
        elif self.x == 9: #(page 9: levels: 45 - 49)#45, 46, 47, 48, 49
            #create buttons
            self.buttons.l_45 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_45_unlocked,
                completed = self.buttons.l_45_completed
                
            )
            self.buttons.l_46 = en.Button(
                (self.buttons.l_45.x + self.buttons.l_45.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_46_unlocked,
                completed = self.buttons.l_46_completed
                
            )
            self.buttons.l_47 = en.Button(
                (self.buttons.l_46.x + self.buttons.l_46.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_47_unlocked,
                completed = self.buttons.l_47_completed
                
            )
            self.buttons.l_48 = en.Button(
                (self.buttons.l_47.x + self.buttons.l_47.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_48_unlocked,
                completed = self.buttons.l_48_completed
                
            )
            self.buttons.l_49 = en.Button(
                (self.buttons.l_48.x + self.buttons.l_48.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_49_unlocked,
                completed = self.buttons.l_49_completed
                
            )

            #update buttons
            self.buttons.l_45.update()
            self.buttons.l_46.update()
            self.buttons.l_47.update()
            self.buttons.l_48.update()
            self.buttons.l_49.update()


            #%end%#
        elif self.x == 10: #(page 8: levels: 50 - 54)#50, 51, 52, 53, 54CUTSCENE
            #create buttons
            self.buttons.l_50 = en.Button(
                gf.screen_width // 50,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_50_unlocked,
                completed = self.buttons.l_50_completed
                
            )
            self.buttons.l_51 = en.Button(
                (self.buttons.l_50.x + self.buttons.l_50.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_51_unlocked,
                completed = self.buttons.l_51_completed
                
            )
            self.buttons.l_52 = en.Button(
                (self.buttons.l_51.x + self.buttons.l_51.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_52_unlocked,
                completed = self.buttons.l_52_completed
                
            )
            self.buttons.l_53 = en.Button(
                (self.buttons.l_52.x + self.buttons.l_52.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.l_53_unlocked,
                completed = self.buttons.l_53_completed
                
            )
            self.buttons.c_54 = en.Button(
                (self.buttons.l_53.x + self.buttons.l_53.width) + gf.screen_width // 100,
                gf.screen_width // 7,
                250 // 1.5,
                450 // 1.5,
                "buttons\\levels",
                "1.png",
                "1_h.png",
                "1_comp.png",
                "1_locked.png",
                unlocked = self.buttons.c_54_unlocked,
                completed = self.buttons.c_54_completed
                
            )

            #update buttons
            self.buttons.l_50.update()
            self.buttons.l_51.update()
            self.buttons.l_52.update()
            self.buttons.l_53.update()
            self.buttons.c_54.update()


            #%end%#
    #%end%-------------------------------------------------------------------%end%#
