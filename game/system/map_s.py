import pygame, json
from os import getenv
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


        #get the data for the levels
        APPDATA = getenv("APPDATA")
        with open(APPDATA + "\\.rails_and_potatoes\\index\\player.os.dt", "r") as oort_studios_data_file:
            data = json.load(oort_studios_data_file)
            oort_studios_data_file.close()
        
        data = data["levels&cutscenes"]

        #c for cutscenes
        #l for levels

        #----#x = 0#----#
        self.c_0 = None
        self.c_0_completed = False if (data[0]["data"] == 1) or (data[0]["data"] == 0) else True



        self.l_1 = None
        if data[1]["data"] == 0:
            self.l_1_completed = False
            self.l_1_unlocked = False
        elif data[1]["data"] == 1:
            self.l_1_unlocked = True
            self.l_1_completed = False
        else:
            self.l_1_unlocked = True
            self.l_1_completed = True
        


        self.l_2 = None
        if data[2]["data"] == 0:
            self.l_2_completed = False
            self.l_2_unlocked = False
        elif data[2]["data"] == 1:
            self.l_2_unlocked = True
            self.l_2_completed = False
        else:
            self.l_2_unlocked = True
            self.l_2_completed = True


        self.l_3 = None
        if data[3]["data"] == 0:
            self.l_3_completed = False
            self.l_3_unlocked = False
        elif data[3]["data"] == 1:
            self.l_3_unlocked = True
            self.l_3_completed = False
        else:
            self.l_3_unlocked = True
            self.l_3_completed = True


        self.l_4 = None
        if data[4]["data"] == 0:
            self.l_4_completed = False
            self.l_4_unlocked = False
        elif data[4]["data"] == 1:
            self.l_4_unlocked = True
            self.l_4_completed = False
        else:
            self.l_4_unlocked = True
            self.l_4_completed = True

        #----#x = 1#----#
        self.l_5 = None
        if data[5]["data"] == 0:
            self.l_5_completed = False
            self.l_5_unlocked = False
        elif data[5]["data"] == 1:
            self.l_5_unlocked = True
            self.l_5_completed = False
        else:
            self.l_5_unlocked = True
            self.l_5_completed = True


        self.l_6 = None
        if data[6]["data"] == 0:
            self.l_6_completed = False
            self.l_6_unlocked = False
        elif data[6]["data"] == 1:
            self.l_6_unlocked = True
            self.l_6_completed = False
        else:
            self.l_6_unlocked = True
            self.l_6_completed = True


        self.l_7 = None
        if data[7]["data"] == 0:
            self.l_7_completed = False
            self.l_7_unlocked = False
        elif data[7]["data"] == 1:
            self.l_7_unlocked = True
            self.l_7_completed = False
        else:
            self.l_7_unlocked = True
            self.l_7_completed = True


        self.l_8 = None
        if data[8]["data"] == 0:
            self.l_8_completed = False
            self.l_8_unlocked = False
        elif data[8]["data"] == 1:
            self.l_8_unlocked = True
            self.l_8_completed = False
        else:
            self.l_8_unlocked = True
            self.l_8_completed = True


        self.l_9 = None
        if data[9]["data"] == 0:
            self.l_9_completed = False
            self.l_9_unlocked = False
        elif data[9]["data"] == 1:
            self.l_9_unlocked = True
            self.l_9_completed = False
        else:
            self.l_9_unlocked = True
            self.l_9_completed = True

        #----#x = 2#----#
        self.l_10 = None
        if data[10]["data"] == 0:
            self.l_10_completed = False
            self.l_10_unlocked = False
        elif data[10]["data"] == 1:
            self.l_10_unlocked = True
            self.l_10_completed = False
        else:
            self.l_10_unlocked = True
            self.l_10_completed = True


        self.l_11 = None
        if data[11]["data"] == 0:
            self.l_11_completed = False
            self.l_11_unlocked = False
        elif data[11]["data"] == 1:
            self.l_11_unlocked = True
            self.l_11_completed = False
        else:
            self.l_11_unlocked = True
            self.l_11_completed = True


        self.l_12 = None
        if data[12]["data"] == 0:
            self.l_12_completed = False
            self.l_12_unlocked = False
        elif data[12]["data"] == 1:
            self.l_12_unlocked = True
            self.l_12_completed = False
        else:
            self.l_12_unlocked = True
            self.l_12_completed = True


        self.l_13 = None
        if data[13]["data"] == 0:
            self.l_13_completed = False
            self.l_13_unlocked = False
        elif data[13]["data"] == 1:
            self.l_13_unlocked = True
            self.l_13_completed = False
        else:
            self.l_13_unlocked = True
            self.l_13_completed = True


        self.l_14 = None
        if data[14]["data"] == 0:
            self.l_14_completed = False
            self.l_14_unlocked = False
        elif data[14]["data"] == 1:
            self.l_14_unlocked = True
            self.l_14_completed = False
        else:
            self.l_14_unlocked = True
            self.l_14_completed = True

        #----#x = 3#----#
        self.l_15 = None
        if data[15]["data"] == 0:
            self.l_15_completed = False
            self.l_15_unlocked = False
        elif data[15]["data"] == 1:
            self.l_15_unlocked = True
            self.l_15_completed = False
        else:
            self.l_15_unlocked = True
            self.l_15_completed = True


        self.l_16 = None
        if data[16]["data"] == 0:
            self.l_16_completed = False
            self.l_16_unlocked = False
        elif data[16]["data"] == 1:
            self.l_16_unlocked = True
            self.l_16_completed = False
        else:
            self.l_16_unlocked = True
            self.l_16_completed = True


        self.l_17 = None
        if data[17]["data"] == 0:
            self.l_17_completed = False
            self.l_17_unlocked = False
        elif data[17]["data"] == 1:
            self.l_17_unlocked = True
            self.l_17_completed = False
        else:
            self.l_17_unlocked = True
            self.l_17_completed = True


        self.l_18 = None
        if data[18]["data"] == 0:
            self.l_18_completed = False
            self.l_18_unlocked = False
        elif data[18]["data"] == 1:
            self.l_18_unlocked = True
            self.l_18_completed = False
        else:
            self.l_18_unlocked = True
            self.l_18_completed = True


        self.l_19 = None
        if data[19]["data"] == 0:
            self.l_19_completed = False
            self.l_19_unlocked = False
        elif data[19]["data"] == 1:
            self.l_19_unlocked = True
            self.l_19_completed = False
        else:
            self.l_19_unlocked = True
            self.l_19_completed = True

        #----#x = 4#----#
        self.l_20 = None
        if data[20]["data"] == 0:
            self.l_20_completed = False
            self.l_20_unlocked = False
        elif data[20]["data"] == 1:
            self.l_20_unlocked = True
            self.l_20_completed = False
        else:
            self.l_20_unlocked = True
            self.l_20_completed = True


        self.l_21 = None
        if data[21]["data"] == 0:
            self.l_21_completed = False
            self.l_21_unlocked = False
        elif data[21]["data"] == 1:
            self.l_21_unlocked = True
            self.l_21_completed = False
        else:
            self.l_21_unlocked = True
            self.l_21_completed = True


        self.l_22 = None
        if data[22]["data"] == 0:
            self.l_22_completed = False
            self.l_22_unlocked = False
        elif data[22]["data"] == 1:
            self.l_22_unlocked = True
            self.l_22_completed = False
        else:
            self.l_22_unlocked = True
            self.l_22_completed = True


        self.l_23 = None
        if data[23]["data"] == 0:
            self.l_23_completed = False
            self.l_23_unlocked = False
        elif data[23]["data"] == 1:
            self.l_23_unlocked = True
            self.l_23_completed = False
        else:
            self.l_23_unlocked = True
            self.l_23_completed = True


        self.l_24 = None
        if data[24]["data"] == 0:
            self.l_24_completed = False
            self.l_24_unlocked = False
        elif data[24]["data"] == 1:
            self.l_24_unlocked = True
            self.l_24_completed = False
        else:
            self.l_24_unlocked = True
            self.l_24_completed = True
        
        #----#x = 5#----#
        self.l_25 = None
        if data[25]["data"] == 0:
            self.l_25_completed = False
            self.l_25_unlocked = False
        elif data[255]["data"] == 1:
            self.l_25_unlocked = True
            self.l_25_completed = False
        else:      
            self.l_25_unlocked = True
            self.l_25_completed = True


        self.l_26 = None
        if data[26]["data"] == 0:
            self.l_26_completed = False
            self.l_26_unlocked = False
        elif data[26]["data"] == 1:
            self.l_26_unlocked = True
            self.l_26_completed = False
        else:      
            self.l_26_unlocked = True
            self.l_26_completed = True


        self.c_27 = None
        if data[27]["data"] == 0:
            self.c_27_completed = False
            self.c_27_unlocked = False
        elif data[277]["data"] == 1:
            self.c_27_unlocked = True
            self.c_27_completed = False
        else:      
            self.c_27_unlocked = True
            self.c_27_completed = True


        self.l_28 = None
        if data[28]["data"] == 0:
            self.l_28_completed = False
            self.l_28_unlocked = False
        elif data[28]["data"] == 1:
            self.l_28_unlocked = True
            self.l_28_completed = False
        else:      
            self.l_28_unlocked = True
            self.l_28_completed = True


        self.l_29 = None
        if data[29]["data"] == 0:
            self.l_29_completed = False
            self.l_29_unlocked = False
        elif data[29]["data"] == 1:
            self.l_29_unlocked = True
            self.l_29_completed = False
        else:      
            self.l_29_unlocked = True
            self.l_29_completed = True



        #----#x = 6#----#
        self.l_30 = None
        if data[30]["data"] == 0:
            self.l_30_completed = False
            self.l_30_unlocked = False
        elif data[30]["data"] == 1:
            self.l_30_unlocked = True
            self.l_30_completed = False
        else:       
            self.l_30_unlocked = True
            self.l_30_completed = True


        self.l_31 = None
        if data[31]["data"] == 0:
            self.l_31_completed = False
            self.l_31_unlocked = False
        elif data[31]["data"] == 1:
            self.l_31_unlocked = True
            self.l_31_completed = False
        else:       
            self.l_31_unlocked = True
            self.l_31_completed = True


        self.l_32 = None
        if data[32]["data"] == 0:
            self.l_32_completed = False
            self.l_32_unlocked = False
        elif data[32]["data"] == 1:
            self.l_32_unlocked = True
            self.l_32_completed = False
        else:       
            self.l_32_unlocked = True
            self.l_32_completed = True


        self.l_33 = None
        if data[33]["data"] == 0:
            self.l_33_completed = False
            self.l_33_unlocked = False
        elif data[33]["data"] == 1:
            self.l_33_unlocked = True
            self.l_33_completed = False
        else:       
            self.l_33_unlocked = True
            self.l_33_completed = True


        self.l_34 = None
        if data[34]["data"] == 0:
            self.l_34_completed = False
            self.l_34_unlocked = False
        elif data[34]["data"] == 1:
            self.l_34_unlocked = True
            self.l_34_completed = False
        else:       
            self.l_34_unlocked = True
            self.l_34_completed = True

        #----#x = 7#----#
        self.l_35 = None
        if data[35]["data"] == 0:
            self.l_35_completed = False
            self.l_35_unlocked = False
        elif data[35]["data"] == 1:
            self.l_35_unlocked = True
            self.l_35_completed = False
        else:       
            self.l_35_unlocked = True
            self.l_35_completed = True


        self.l_36 = None
        if data[36]["data"] == 0:
            self.l_36_completed = False
            self.l_36_unlocked = False
        elif data[36]["data"] == 1:
            self.l_36_unlocked = True
            self.l_36_completed = False
        else:       
            self.l_36_unlocked = True
            self.l_36_completed = True


        self.l_37 = None
        if data[37]["data"] == 0:
            self.l_37_completed = False
            self.l_37_unlocked = False
        elif data[37]["data"] == 1:
            self.l_37_unlocked = True
            self.l_37_completed = False
        else:       
            self.l_37_unlocked = True
            self.l_37_completed = True


        self.l_38 = None
        if data[38]["data"] == 0:
            self.l_38_completed = False
            self.l_38_unlocked = False
        elif data[38]["data"] == 1:
            self.l_38_unlocked = True
            self.l_38_completed = False
        else:      
            self.l_38_unlocked = True
            self.l_38_completed = True


        self.l_39 = None
        if data[39]["data"] == 0:
            self.l_39_completed = False
            self.l_39_unlocked = False
        elif data[39]["data"] == 1:
            self.l_39_unlocked = True
            self.l_39_completed = False
        else:       
            self.l_39_unlocked = True
            self.l_39_completed = True

        #----#x = 8#----#
        self.l_40 = None
        if data[40]["data"] == 0:
            self.l_40_completed = False
            self.l_40_unlocked = False
        elif data[40]["data"] == 1:
            self.l_40_unlocked = True
            self.l_40_completed = False
        else:       
            self.l_40_unlocked = True
            self.l_40_completed = True


        self.l_41 = None
        if data[41]["data"] == 0:
            self.l_41_completed = False
            self.l_41_unlocked = False
        elif data[41]["data"] == 1:
            self.l_41_unlocked = True
            self.l_41_completed = False
        else:       
            self.l_41_unlocked = True
            self.l_41_completed = True


        self.l_42 = None
        if data[42]["data"] == 0:
            self.l_42_completed = False
            self.l_42_unlocked = False
        elif data[42]["data"] == 1:
            self.l_42_unlocked = True
            self.l_42_completed = False
        else:       
            self.l_42_unlocked = True
            self.l_42_completed = True


        self.l_43 = None
        if data[43]["data"] == 0:
            self.l_43_completed = False
            self.l_43_unlocked = False
        elif data[43]["data"] == 1:
            self.l_43_unlocked = True
            self.l_43_completed = False
        else:       
            self.l_43_unlocked = True
            self.l_43_completed = True


        self.l_44 = None
        if data[44]["data"] == 0:
            self.l_44_completed = False
            self.l_44_unlocked = False
        elif data[44]["data"] == 1:
            self.l_44_unlocked = True
            self.l_44_completed = False
        else:      
            self.l_44_unlocked = True
            self.l_44_completed = True

        #----#x = 9#----#
        self.l_45 = None
        if data[45]["data"] == 0:
            self.l_45_completed = False
            self.l_45_unlocked = False
        elif data[45]["data"] == 1:
            self.l_45_unlocked = True
            self.l_45_completed = False
        else:       
            self.l_45_unlocked = True
            self.l_45_completed = True


        self.l_46 = None
        if data[46]["data"] == 0:
            self.l_46_completed = False
            self.l_46_unlocked = False
        elif data[46]["data"] == 1:
            self.l_46_unlocked = True
            self.l_46_completed = False
        else:       
            self.l_46_unlocked = True
            self.l_46_completed = True


        self.l_47 = None
        if data[47]["data"] == 0:
            self.l_47_completed = False
            self.l_47_unlocked = False
        elif data[47]["data"] == 1:
            self.l_47_unlocked = True
            self.l_47_completed = False
        else:       
            self.l_47_unlocked = True
            self.l_47_completed = True


        self.l_48 = None
        if data[48]["data"] == 0:
            self.l_48_completed = False
            self.l_48_unlocked = False
        elif data[48]["data"] == 1:
            self.l_48_unlocked = True
            self.l_48_completed = False
        else:       
            self.l_48_unlocked = True
            self.l_48_completed = True


        self.l_49 = None
        if data[49]["data"] == 0:
            self.l_49_completed = False
            self.l_49_unlocked = False
        elif data[49]["data"] == 1:
            self.l_49_unlocked = True
            self.l_49_completed = False
        else:      
            self.l_49_unlocked = True
            self.l_49_completed = True

        #----#x = 10#----#
        self.l_50 = None
        if data[50]["data"] == 0:
            self.l_50_completed = False
            self.l_50_unlocked = False
        elif data[50]["data"] == 1:
            self.l_50_unlocked = True
            self.l_50_completed = False
        else:       
            self.l_50_unlocked = True
            self.l_50_completed = True


        self.l_51 = None
        if data[50]["data"] == 0:
            self.l_51_completed = False
            self.l_51_unlocked = False
        elif data[50]["data"] == 1:
            self.l_51_unlocked = True
            self.l_51_completed = False
        else:       
            self.l_51_unlocked = True
            self.l_51_completed = True


        self.l_52 = None
        if data[52]["data"] == 0:
            self.l_52_completed = False
            self.l_52_unlocked = False
        elif data[52]["data"] == 1:
            self.l_52_unlocked = True
            self.l_52_completed = False
        else:       
            self.l_52_unlocked = True
            self.l_52_completed = True


        self.l_53 = None
        if data[53]["data"] == 0:
            self.l_53_completed = False
            self.l_53_unlocked = False
        elif data[53]["data"] == 1:
            self.l_53_unlocked = True
            self.l_53_completed = False
        else:       
            self.l_53_unlocked = True
            self.l_53_completed = True


        self.c_54 = None
        if data[54]["data"] == 0:
            self.c_54_completed = False
            self.c_54_unlocked = False
        elif data[5]["data"] == 1:
            self.c_54_unlocked = True
            self.c_54_completed = False
        else:       
            self.c_54_unlocked = True
            self.c_54_completed = True

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



    def save_map(self):
        APPDATA = getenv("APPDATA")
        with open(APPDATA + "\\.rails_and_potatoes\\index\\player.os.dt", "r") as oort_studios_data_file:
            dt = json.load(oort_studios_data_file)
            oort_studios_data_file.close()
        
        data = dt["levels&cutscenes"]


        #cutscene -> 0#
        data[0]["data"] = 2 if self.buttons.c_0_completed else 1


        #level -> 1#
        if self.buttons.l_1_unlocked and self.buttons.l_1_completed:
            data[1]["data"] = 2
        elif self.buttons.l_1_unlocked:
            data[1]["data"] = 1
        else:
            data[1]["data"] = 0


        #level -> 2#
        if self.buttons.l_2_unlocked and self.buttons.l_2_completed:
            data[2]["data"] = 2
        elif self.buttons.l_2_unlocked:
            data[2]["data"] = 1
        else:
            data[2]["data"] = 0


        #level -> 3#
        if self.buttons.l_3_unlocked and self.buttons.l_3_completed:
            data[3]["data"] = 2
        elif self.buttons.l_3_unlocked:
            data[3]["data"] = 1
        else:
            data[3]["data"] = 0


        #level -> 4#
        if self.buttons.l_4_unlocked and self.buttons.l_4_completed:
            data[4]["data"] = 2
        elif self.buttons.l_4_unlocked:
            data[4]["data"] = 1
        else:
            data[4]["data"] = 0


        #level -> 5#
        if self.buttons.l_5_unlocked and self.buttons.l_5_completed:
            data[5]["data"] = 2
        elif self.buttons.l_5_unlocked:
            data[5]["data"] = 1
        else:
            data[5]["data"] = 0


        #level -> 6#
        if self.buttons.l_6_unlocked and self.buttons.l_6_completed:
            data[6]["data"] = 2
        elif self.buttons.l_6_unlocked:
            data[6]["data"] = 1
        else:
            data[6]["data"] = 0


        #level -> 7#
        if self.buttons.l_7_unlocked and self.buttons.l_7_completed:
            data[7]["data"] = 2
        elif self.buttons.l_7_unlocked:
            data[7]["data"] = 1
        else:
            data[7]["data"] = 0


        #level -> 8#
        if self.buttons.l_8_unlocked and self.buttons.l_8_completed:
            data[8]["data"] = 2
        elif self.buttons.l_8_unlocked:
            data[8]["data"] = 1
        else:
            data[8]["data"] = 0


        #level -> 9#
        if self.buttons.l_9_unlocked and self.buttons.l_9_completed:
            data[9]["data"] = 2
        elif self.buttons.l_9_unlocked:
            data[9]["data"] = 1
        else:
            data[9]["data"] = 0


        #level -> 10#
        if self.buttons.l_10_unlocked and self.buttons.l_10_completed:
            data[10]["data"] = 2
        elif self.buttons.l_10_unlocked:
            data[10]["data"] = 1
        else:
            data[10]["data"] = 0


        #level -> 11#
        if self.buttons.l_11_unlocked and self.buttons.l_11_completed:
            data[11]["data"] = 2
        elif self.buttons.l_11_unlocked:
            data[11]["data"] = 1
        else:
            data[11]["data"] = 0


        #level -> 12#
        if self.buttons.l_12_unlocked and self.buttons.l_12_completed:
            data[12]["data"] = 2
        elif self.buttons.l_12_unlocked:
            data[12]["data"] = 1
        else:
            data[12]["data"] = 0


        #level -> 13#
        if self.buttons.l_13_unlocked and self.buttons.l_13_completed:
            data[13]["data"] = 2
        elif self.buttons.l_13_unlocked:
            data[13]["data"] = 1
        else:
            data[13]["data"] = 0


        #level -> 14#
        if self.buttons.l_14_unlocked and self.buttons.l_14_completed:
            data[14]["data"] = 2
        elif self.buttons.l_14_unlocked:
            data[14]["data"] = 1
        else:
            data[14]["data"] = 0


        #level -> 15#
        if self.buttons.l_15_unlocked and self.buttons.l_15_completed:
            data[15]["data"] = 2
        elif self.buttons.l_15_unlocked:
            data[15]["data"] = 1
        else:
            data[15]["data"] = 0


        #level -> 16#
        if self.buttons.l_16_unlocked and self.buttons.l_16_completed:
            data[16]["data"] = 2
        elif self.buttons.l_16_unlocked:
            data[16]["data"] = 1
        else:
            data[16]["data"] = 0


        #level -> 17#
        if self.buttons.l_17_unlocked and self.buttons.l_17_completed:
            data[17]["data"] = 2
        elif self.buttons.l_17_unlocked:
            data[17]["data"] = 1
        else:
            data[17]["data"] = 0


        #level -> 18#
        if self.buttons.l_18_unlocked and self.buttons.l_18_completed:
            data[18]["data"] = 2
        elif self.buttons.l_18_unlocked:
            data[18]["data"] = 1
        else:
            data[18]["data"] = 0


        #level -> 19#
        if self.buttons.l_19_unlocked and self.buttons.l_19_completed:
            data[19]["data"] = 2
        elif self.buttons.l_19_unlocked:
            data[19]["data"] = 1
        else:
            data[19]["data"] = 0


        #level -> 20#
        if self.buttons.l_20_unlocked and self.buttons.l_20_completed:
            data[20]["data"] = 2
        elif self.buttons.l_20_unlocked:
            data[20]["data"] = 1
        else:
            data[20]["data"] = 0


        #level -> 21#
        if self.buttons.l_21_unlocked and self.buttons.l_21_completed:
            data[21]["data"] = 2
        elif self.buttons.l_21_unlocked:
            data[21]["data"] = 1
        else:
            data[21]["data"] = 0


        #level -> 22#
        if self.buttons.l_22_unlocked and self.buttons.l_22_completed:
            data[22]["data"] = 2
        elif self.buttons.l_22_unlocked:
            data[22]["data"] = 1
        else:
            data[22]["data"] = 0


        #level -> 23#
        if self.buttons.l_23_unlocked and self.buttons.l_23_completed:
            data[23]["data"] = 2
        elif self.buttons.l_23_unlocked:
            data[23]["data"] = 1
        else:
            data[23]["data"] = 0


        #level -> 24#
        if self.buttons.l_24_unlocked and self.buttons.l_24_completed:
            data[24]["data"] = 2
        elif self.buttons.l_24_unlocked:
            data[24]["data"] = 1
        else:
            data[24]["data"] = 0


        #level -> 25#
        if self.buttons.l_25_unlocked and self.buttons.l_25_completed:
            data[25]["data"] = 2
        elif self.buttons.l_25_unlocked:
            data[25]["data"] = 1
        else:
            data[25]["data"] = 0


        #level -> 26#
        if self.buttons.l_26_unlocked and self.buttons.l_26_completed:
            data[26]["data"] = 2
        elif self.buttons.l_26_unlocked:
            data[26]["data"] = 1
        else:
            data[26]["data"] = 0


        #level -> 27#
        if self.buttons.c_27_unlocked and self.buttons.c_27_completed:
            data[27]["data"] = 2
        elif self.buttons.c_27_unlocked:
            data[27]["data"] = 1
        else:
            data[27]["data"] = 0


        #level -> 28#
        if self.buttons.l_28_unlocked and self.buttons.l_28_completed:
            data[28]["data"] = 2
        elif self.buttons.l_28_unlocked:
            data[28]["data"] = 1
        else:
            data[28]["data"] = 0


        #level -> 29#
        if self.buttons.l_29_unlocked and self.buttons.l_29_completed:
            data[29]["data"] = 2
        elif self.buttons.l_29_unlocked:
            data[29]["data"] = 1
        else:
            data[29]["data"] = 0


        #level -> 30#
        if self.buttons.l_30_unlocked and self.buttons.l_30_completed:
            data[30]["data"] = 2
        elif self.buttons.l_30_unlocked:
            data[30]["data"] = 1
        else:
            data[30]["data"] = 0


        #level -> 31#
        if self.buttons.l_31_unlocked and self.buttons.l_31_completed:
            data[31]["data"] = 2
        elif self.buttons.l_31_unlocked:
            data[31]["data"] = 1
        else:
            data[31]["data"] = 0


        #level -> 32#
        if self.buttons.l_32_unlocked and self.buttons.l_32_completed:
            data[32]["data"] = 2
        elif self.buttons.l_32_unlocked:
            data[32]["data"] = 1
        else:
            data[32]["data"] = 0


        #level -> 33#
        if self.buttons.l_33_unlocked and self.buttons.l_33_completed:
            data[33]["data"] = 2
        elif self.buttons.l_33_unlocked:
            data[33]["data"] = 1
        else:
            data[33]["data"] = 0


        #level -> 34#
        if self.buttons.l_34_unlocked and self.buttons.l_34_completed:
            data[34]["data"] = 2
        elif self.buttons.l_34_unlocked:
            data[34]["data"] = 1
        else:
            data[34]["data"] = 0


        #level -> 35#
        if self.buttons.l_35_unlocked and self.buttons.l_35_completed:
            data[35]["data"] = 2
        elif self.buttons.l_35_unlocked:
            data[35]["data"] = 1
        else:
            data[35]["data"] = 0


        #level -> 36#
        if self.buttons.l_36_unlocked and self.buttons.l_36_completed:
            data[36]["data"] = 2
        elif self.buttons.l_36_unlocked:
            data[36]["data"] = 1
        else:
            data[36]["data"] = 0


        #level -> 37#
        if self.buttons.l_37_unlocked and self.buttons.l_37_completed:
            data[37]["data"] = 2
        elif self.buttons.l_37_unlocked:
            data[37]["data"] = 1
        else:
            data[37]["data"] = 0


        #level -> 38#
        if self.buttons.l_38_unlocked and self.buttons.l_38_completed:
            data[38]["data"] = 2
        elif self.buttons.l_38_unlocked:
            data[38]["data"] = 1
        else:
            data[38]["data"] = 0


        #level -> 39#
        if self.buttons.l_39_unlocked and self.buttons.l_39_completed:
            data[39]["data"] = 2
        elif self.buttons.l_39_unlocked:
            data[39]["data"] = 1
        else:
            data[39]["data"] = 0


        #level -> 40#
        if self.buttons.l_40_unlocked and self.buttons.l_40_completed:
            data[40]["data"] = 2
        elif self.buttons.l_40_unlocked:
            data[40]["data"] = 1
        else:
            data[40]["data"] = 0


        #level -> 41#
        if self.buttons.l_41_unlocked and self.buttons.l_41_completed:
            data[41]["data"] = 2
        elif self.buttons.l_41_unlocked:
            data[41]["data"] = 1
        else:
            data[41]["data"] = 0


        #level -> 42#
        if self.buttons.l_42_unlocked and self.buttons.l_42_completed:
            data[42]["data"] = 2
        elif self.buttons.l_42_unlocked:
            data[42]["data"] = 1
        else:
            data[42]["data"] = 0


        #level -> 43#
        if self.buttons.l_43_unlocked and self.buttons.l_43_completed:
            data[43]["data"] = 2
        elif self.buttons.l_43_unlocked:
            data[43]["data"] = 1
        else:
            data[43]["data"] = 0


        #level -> 44#
        if self.buttons.l_44_unlocked and self.buttons.l_44_completed:
            data[44]["data"] = 2
        elif self.buttons.l_44_unlocked:
            data[44]["data"] = 1
        else:
            data[44]["data"] = 0


        #level -> 45#
        if self.buttons.l_45_unlocked and self.buttons.l_45_completed:
            data[45]["data"] = 2
        elif self.buttons.l_45_unlocked:
            data[45]["data"] = 1
        else:
            data[45]["data"] = 0


        #level -> 46#
        if self.buttons.l_46_unlocked and self.buttons.l_46_completed:
            data[46]["data"] = 2
        elif self.buttons.l_46_unlocked:
            data[46]["data"] = 1
        else:
            data[46]["data"] = 0


        #level -> 47#
        if self.buttons.l_47_unlocked and self.buttons.l_47_completed:
            data[47]["data"] = 2
        elif self.buttons.l_47_unlocked:
            data[47]["data"] = 1
        else:
            data[47]["data"] = 0


        #level -> 48#
        if self.buttons.l_48_unlocked and self.buttons.l_48_completed:
            data[48]["data"] = 2
        elif self.buttons.l_48_unlocked:
            data[48]["data"] = 1
        else:
            data[48]["data"] = 0


        #level -> 49#
        if self.buttons.l_49_unlocked and self.buttons.l_49_completed:
            data[49]["data"] = 2
        elif self.buttons.l_49_unlocked:
            data[49]["data"] = 1
        else:
            data[49]["data"] = 0


        #level -> 50#
        if self.buttons.l_50_unlocked and self.buttons.l_50_completed:
            data[50]["data"] = 2
        elif self.buttons.l_50_unlocked:
            data[50]["data"] = 1
        else:
            data[50]["data"] = 0


        #level -> 51#
        if self.buttons.l_51_unlocked and self.buttons.l_51_completed:
            data[51]["data"] = 2
        elif self.buttons.l_51_unlocked:
            data[51]["data"] = 1
        else:
            data[51]["data"] = 0


        #level -> 52#
        if self.buttons.l_52_unlocked and self.buttons.l_52_completed:
            data[52]["data"] = 2
        elif self.buttons.l_52_unlocked:
            data[52]["data"] = 1
        else:
            data[52]["data"] = 0


        #level -> 53#
        if self.buttons.l_53_unlocked and self.buttons.l_53_completed:
            data[53]["data"] = 2
        elif self.buttons.l_53_unlocked:
            data[53]["data"] = 1
        else:
            data[53]["data"] = 0


        #level -> 54#
        if self.buttons.c_54_unlocked and self.buttons.c_54_completed:
            data[54]["data"] = 2
        elif self.buttons.c_54_unlocked:
            data[54]["data"] = 1
        else:
            data[54]["data"] = 0
        

        #@the return@#
        dt["levels&cutscenes"] = data


        with open(APPDATA + "\\.rails_and_potatoes\\index\\player.os.dt", "w") as oort_studios_data_file:
            json.dump(dt, oort_studios_data_file, indent=2)
            oort_studios_data_file.close()

    #%end%-------------------------------------------------------------------%end%#
