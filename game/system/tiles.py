import pygame, json, os
from pygame.locals import *
from game import system as sys, globals_file as gf
from . import settings, textures
#%start%-------------------------------------------------------------------%start%#

def tiles_xy(self):
    def change(self):
        obj_x_position = self.x
        obj_y_position = self.y
        sw = gf.screen_width
        sh = gf.screen_height
        self.x = (obj_x_position / gf.width_before) * sw
        self.y = (obj_y_position / gf.height_before) * sh
        return self
    
    if (gf.screen_width != gf.width_before) or (gf.screen_height != gf.height_before):
        #T1M1
        self.T1M1F1 = change(self.T1M1F1)
        self.T1M1F2 = change(self.T1M1F2)
        self.T1M1F3 = change(self.T1M1F3)
        self.T1M1F4 = change(self.T1M1F4)
        #T1M2
        self.T1M2F1 = change(self.T1M2F1)
        self.T1M2F2 = change(self.T1M2F2)
        self.T1M2F3 = change(self.T1M2F3)
        self.T1M2F4 = change(self.T1M2F4)
        #T1M3
        self.T1M3F1 = change(self.T1M3F1)
        self.T1M3F2 = change(self.T1M3F2)
        self.T1M3F3 = change(self.T1M3F3)
        self.T1M3F4 = change(self.T1M3F4)
        #T1M4
        self.T1M4F1 = change(self.T1M4F1)
        self.T1M4F2 = change(self.T1M4F2)
        self.T1M4F3 = change(self.T1M4F3)
        self.T1M4F4 = change(self.T1M4F4)
        #T2M1
        self.T2M1F1 = change(self.T2M1F1)
        self.T2M1F2 = change(self.T2M1F2)
        self.T2M1F3 = change(self.T2M1F3)
        self.T2M1F4 = change(self.T2M1F4)
        #T2M2
        self.T2M2F1 = change(self.T2M2F1)
        self.T2M2F2 = change(self.T2M2F2)
        self.T2M2F3 = change(self.T2M2F3)
        self.T2M2F4 = change(self.T2M2F4)
        #T2M3
        self.T2M3F1 = change(self.T2M3F1)
        self.T2M3F2 = change(self.T2M3F2)
        self.T2M3F3 = change(self.T2M3F3)
        self.T2M3F4 = change(self.T2M3F4)
        #T2M4
        self.T2M4F1 = change(self.T2M4F1)
        self.T2M4F2 = change(self.T2M4F2)
        self.T2M4F3 = change(self.T2M4F3)
        self.T2M4F4 = change(self.T2M4F4)
        #T3M1
        self.T3M1F1 = change(self.T3M1F1)
        self.T3M1F2 = change(self.T3M1F2)
        self.T3M1F3 = change(self.T3M1F3)
        self.T3M1F4 = change(self.T3M1F4)
        #T3M2
        self.T3M2F1 = change(self.T3M2F1)
        self.T3M2F2 = change(self.T3M2F2)
        self.T3M2F3 = change(self.T3M2F3)
        self.T3M2F4 = change(self.T3M2F4)
        #T3M3
        self.T3M3F1 = change(self.T3M3F1)
        self.T3M3F2 = change(self.T3M3F2)
        self.T3M3F3 = change(self.T3M3F3)
        self.T3M3F4 = change(self.T3M3F4)
        #T3M4
        self.T3M4F1 = change(self.T3M4F1)
        self.T3M4F2 = change(self.T3M4F2)
        self.T3M4F3 = change(self.T3M4F3)
        self.T3M4F4 = change(self.T3M4F4)
        #T4M1
        self.T4M1F1 = change(self.T4M1F1)
        self.T4M1F2 = change(self.T4M1F2)
        self.T4M1F3 = change(self.T4M1F3)
        self.T4M1F4 = change(self.T4M1F4)
        #T4M2
        self.T4M2F1 = change(self.T4M2F1)
        self.T4M2F2 = change(self.T4M2F2)
        self.T4M2F3 = change(self.T4M2F3)
        self.T4M2F4 = change(self.T4M2F4)
        #T4M3
        self.T4M3F1 = change(self.T4M3F1)
        self.T4M3F2 = change(self.T4M3F2)
        self.T4M3F3 = change(self.T4M3F3)
        self.T4M3F4 = change(self.T4M3F4)
        #T4M4
        self.T4M4F1 = change(self.T4M4F1)
        self.T4M4F2 = change(self.T4M4F2)
        self.T4M4F3 = change(self.T4M4F3)
        self.T4M4F4 = change(self.T4M4F4)
        #T5M1
        self.T5M1F1 = change(self.T5M1F1)
        self.T5M1F2 = change(self.T5M1F2)
        self.T5M1F3 = change(self.T5M1F3)
        self.T5M1F4 = change(self.T5M1F4)
        #T5M2
        self.T5M2F1 = change(self.T5M2F1)
        self.T5M2F2 = change(self.T5M2F2)
        self.T5M2F3 = change(self.T5M2F3)
        self.T5M2F4 = change(self.T5M2F4)
        #T5M3
        self.T5M3F1 = change(self.T5M3F1)
        self.T5M3F2 = change(self.T5M3F2)
        self.T5M3F3 = change(self.T5M3F3)
        self.T5M3F4 = change(self.T5M3F4)
        #T5M4
        self.T5M4F1 = change(self.T5M4F1)
        self.T5M4F2 = change(self.T5M4F2)
        self.T5M4F3 = change(self.T5M4F3)
        self.T5M4F4 = change(self.T5M4F4)
        #T6M1
        self.T6M1F1 = change(self.T6M1F1)
        self.T6M1F2 = change(self.T6M1F2)
        self.T6M1F3 = change(self.T6M1F3)
        self.T6M1F4 = change(self.T6M1F4)
        #T6M2
        self.T6M2F1 = change(self.T6M2F1)
        self.T6M2F2 = change(self.T6M2F2)
        self.T6M2F3 = change(self.T6M2F3)
        self.T6M2F4 = change(self.T6M2F4)
        #T6M3
        self.T6M3F1 = change(self.T6M3F1)
        self.T6M3F2 = change(self.T6M3F2)
        self.T6M3F3 = change(self.T6M3F3)
        self.T6M3F4 = change(self.T6M3F4)
        #T6M4
        self.T6M4F1 = change(self.T6M4F1)
        self.T6M4F2 = change(self.T6M4F2)
        self.T6M4F3 = change(self.T6M4F3)
        self.T6M4F4 = change(self.T6M4F4)
        #T7M1
        self.T7M1F1 = change(self.T7M1F1)
        self.T7M1F2 = change(self.T7M1F2)
        self.T7M1F3 = change(self.T7M1F3)
        self.T7M1F4 = change(self.T7M1F4)
        #T7M2
        self.T7M2F1 = change(self.T7M2F1)
        self.T7M2F2 = change(self.T7M2F2)
        self.T7M2F3 = change(self.T7M2F3)
        self.T7M2F4 = change(self.T7M2F4)
        #T7M3
        self.T7M3F1 = change(self.T7M3F1)
        self.T7M3F2 = change(self.T7M3F2)
        self.T7M3F3 = change(self.T7M3F3)
        self.T7M3F4 = change(self.T7M3F4)
        #T7M4
        self.T7M4F1 = change(self.T7M4F1)
        self.T7M4F2 = change(self.T7M4F2)
        self.T7M4F3 = change(self.T7M4F3)
        self.T7M4F4 = change(self.T7M4F4)
        #T8M1
        self.T8M1F1 = change(self.T8M1F1)
        self.T8M1F2 = change(self.T8M1F2)
        self.T8M1F3 = change(self.T8M1F3)
        self.T8M1F4 = change(self.T8M1F4)
        #T8M2
        self.T8M2F1 = change(self.T8M2F1)
        self.T8M2F2 = change(self.T8M2F2)
        self.T8M2F3 = change(self.T8M2F3)
        self.T8M2F4 = change(self.T8M2F4)
        #T8M3
        self.T8M3F1 = change(self.T8M3F1)
        self.T8M3F2 = change(self.T8M3F2)
        self.T8M3F3 = change(self.T8M3F3)
        self.T8M3F4 = change(self.T8M3F4)
        #T8M4
        self.T8M4F1 = change(self.T8M4F1)
        self.T8M4F2 = change(self.T8M4F2)
        self.T8M4F3 = change(self.T8M4F3)
        self.T8M4F4 = change(self.T8M4F4)
        #T9M1
        self.T9M1F1 = change(self.T9M1F1)
        self.T9M1F2 = change(self.T9M1F2)
        self.T9M1F3 = change(self.T9M1F3)
        self.T9M1F4 = change(self.T9M1F4)
        #T9M2
        self.T9M2F1 = change(self.T9M2F1)
        self.T9M2F2 = change(self.T9M2F2)
        self.T9M2F3 = change(self.T9M2F3)
        self.T9M2F4 = change(self.T9M2F4)
        #T9M3
        self.T9M3F1 = change(self.T9M3F1)
        self.T9M3F2 = change(self.T9M3F2)
        self.T9M3F3 = change(self.T9M3F3)
        self.T9M3F4 = change(self.T9M3F4)
        #T9M4
        self.T9M4F1 = change(self.T9M4F1)
        self.T9M4F2 = change(self.T9M4F2)
        self.T9M4F3 = change(self.T9M4F3)
        self.T9M4F4 = change(self.T9M4F4)
        #T10M1
        self.T10M1F1 = change(self.T10M1F1)
        self.T10M1F2 = change(self.T10M1F2)
        self.T10M1F3 = change(self.T10M1F3)
        self.T10M1F4 = change(self.T10M1F4)
        #T10M2
        self.T10M2F1 = change(self.T10M2F1)
        self.T10M2F2 = change(self.T10M2F2)
        self.T10M2F3 = change(self.T10M2F3)
        self.T10M2F4 = change(self.T10M2F4)
        #T10M3
        self.T10M3F1 = change(self.T10M3F1)
        self.T10M3F2 = change(self.T10M3F2)
        self.T10M3F3 = change(self.T10M3F3)
        self.T10M3F4 = change(self.T10M3F4)
        #T10M4
        self.T10M4F1 = change(self.T10M4F1)
        self.T10M4F2 = change(self.T10M4F2)
        self.T10M4F3 = change(self.T10M4F3)
        self.T10M4F4 = change(self.T10M4F4)
        #T11M1
        self.T11M1F1 = change(self.T11M1F1)
        self.T11M1F2 = change(self.T11M1F2)
        self.T11M1F3 = change(self.T11M1F3)
        self.T11M1F4 = change(self.T11M1F4)
        #T11M2
        self.T11M2F1 = change(self.T11M2F1)
        self.T11M2F2 = change(self.T11M2F2)
        self.T11M2F3 = change(self.T11M2F3)
        self.T11M2F4 = change(self.T11M2F4)
        #T11M3
        self.T11M3F1 = change(self.T11M3F1)
        self.T11M3F2 = change(self.T11M3F2)
        self.T11M3F3 = change(self.T11M3F3)
        self.T11M3F4 = change(self.T11M3F4)
        #T11M4
        self.T11M4F1 = change(self.T11M4F1)
        self.T11M4F2 = change(self.T11M4F2)
        self.T11M4F3 = change(self.T11M4F3)
        self.T11M4F4 = change(self.T11M4F4)
        #T12M1
        self.T12M1F1 = change(self.T12M1F1)
        self.T12M1F2 = change(self.T12M1F2)
        self.T12M1F3 = change(self.T12M1F3)
        self.T12M1F4 = change(self.T12M1F4)
        #T12M2
        self.T12M2F1 = change(self.T12M2F1)
        self.T12M2F2 = change(self.T12M2F2)
        self.T12M2F3 = change(self.T12M2F3)
        self.T12M2F4 = change(self.T12M2F4)
        #T12M3
        self.T12M3F1 = change(self.T12M3F1)
        self.T12M3F2 = change(self.T12M3F2)
        self.T12M3F3 = change(self.T12M3F3)
        self.T12M3F4 = change(self.T12M3F4)
        #T12M4
        self.T12M4F1 = change(self.T12M4F1)
        self.T12M4F2 = change(self.T12M4F2)
        self.T12M4F3 = change(self.T12M4F3)
        self.T12M4F4 = change(self.T12M4F4)
        #T13M1
        self.T13M1F1 = change(self.T13M1F1)
        self.T13M1F2 = change(self.T13M1F2)
        self.T13M1F3 = change(self.T13M1F3)
        self.T13M1F4 = change(self.T13M1F4)
        #T13M2
        self.T13M2F1 = change(self.T13M2F1)
        self.T13M2F2 = change(self.T13M2F2)
        self.T13M2F3 = change(self.T13M2F3)
        self.T13M2F4 = change(self.T13M2F4)
        #T13M3
        self.T13M3F1 = change(self.T13M3F1)
        self.T13M3F2 = change(self.T13M3F2)
        self.T13M3F3 = change(self.T13M3F3)
        self.T13M3F4 = change(self.T13M3F4)
        #T13M4
        self.T13M4F1 = change(self.T13M4F1)
        self.T13M4F2 = change(self.T13M4F2)
        self.T13M4F3 = change(self.T13M4F3)
        self.T13M4F4 = change(self.T13M4F4)
        #T14M1
        self.T14M1F1 = change(self.T14M1F1)
        self.T14M1F2 = change(self.T14M1F2)
        self.T14M1F3 = change(self.T14M1F3)
        self.T14M1F4 = change(self.T14M1F4)
        #T14M2
        self.T14M2F1 = change(self.T14M2F1)
        self.T14M2F2 = change(self.T14M2F2)
        self.T14M2F3 = change(self.T14M2F3)
        self.T14M2F4 = change(self.T14M2F4)
        #T14M3
        self.T14M3F1 = change(self.T14M3F1)
        self.T14M3F2 = change(self.T14M3F2)
        self.T14M3F3 = change(self.T14M3F3)
        self.T14M3F4 = change(self.T14M3F4)
        #T14M4
        self.T14M4F1 = change(self.T14M4F1)
        self.T14M4F2 = change(self.T14M4F2)
        self.T14M4F3 = change(self.T14M4F3)
        self.T14M4F4 = change(self.T14M4F4)
        #T15M1
        self.T15M1F1 = change(self.T15M1F1)
        self.T15M1F2 = change(self.T15M1F2)
        self.T15M1F3 = change(self.T15M1F3)
        self.T15M1F4 = change(self.T15M1F4)
        #T15M2
        self.T15M2F1 = change(self.T15M2F1)
        self.T15M2F2 = change(self.T15M2F2)
        self.T15M2F3 = change(self.T15M2F3)
        self.T15M2F4 = change(self.T15M2F4)
        #T15M3
        self.T15M3F1 = change(self.T15M3F1)
        self.T15M3F2 = change(self.T15M3F2)
        self.T15M3F3 = change(self.T15M3F3)
        self.T15M3F4 = change(self.T15M3F4)
        #T15M4
        self.T15M4F1 = change(self.T15M4F1)
        self.T15M4F2 = change(self.T15M4F2)
        self.T15M4F3 = change(self.T15M4F3)
        self.T15M4F4 = change(self.T15M4F4)
        #T16M1
        self.T16M1F1 = change(self.T16M1F1)
        self.T16M1F2 = change(self.T16M1F2)
        self.T16M1F3 = change(self.T16M1F3)
        self.T16M1F4 = change(self.T16M1F4)
        #T16M2
        self.T16M2F1 = change(self.T16M2F1)
        self.T16M2F2 = change(self.T16M2F2)
        self.T16M2F3 = change(self.T16M2F3)
        self.T16M2F4 = change(self.T16M2F4)
        #T16M3
        self.T16M3F1 = change(self.T16M3F1)
        self.T16M3F2 = change(self.T16M3F2)
        self.T16M3F3 = change(self.T16M3F3)
        self.T16M3F4 = change(self.T16M3F4)
        #T16M4
        self.T16M4F1 = change(self.T16M4F1)
        self.T16M4F2 = change(self.T16M4F2)
        self.T16M4F3 = change(self.T16M4F3)
        self.T16M4F4 = change(self.T16M4F4)

        gf.width_before, gf.height_before = gf.screen_width, gf.screen_height
        return self

#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
#@#----------------------------------------------------------------------------#@#
class tile:
    def __init__(self, o = 1, id = ["T1", "M1", "F1"]):
        """the class of the lonely tile, create a tile entity

        Args:
            o (int, optional): the part of the screen that the tile is belonging to(1 - 4). Defaults to 1.
            id (list, optional): the id of the tile([T: 1-16][M: 1-4][F: 1-4]). Defaults to ["T1", "M1", "F1"].
        """

        #900 % 4 % 4 % 4
        self.w = 14.0625 * 4
        #500 % 4 % 4 % 4
        self.h = 7.8125 * 4
        self.width = sys.Resize.resize_x( #resize
            settings.starting_screen_width,
            self.w,
            gf.screen_width
        )
        self.height = sys.Resize.resize_y( #resize
            settings.starting_screen_height,
            self.h,
            gf.screen_height
        )
        self.lvl_before = 0 #lvl
        self.loaded_image = None
        self.id_list = id 
        self.rail = False

        #T1
        if o == 1:
            if id[0] == "T1":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T1M1F1"
                        self.x = self.w * 0
                        self.y = self.h * 0
                        self.up = "None"
                        self.down = "T1M1F3"
                        self.left = "None"
                        self.right = "T1M1F2"
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T1M1F2"
                        self.x = self.w * 1
                        self.y = self.h * 0
                        self.up = "None"
                        self.down = "T1M1F4"
                        self.left = "T1M1F1"
                        self.right = "T1M2F1"
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T1M1F3"
                        self.x = self.w * 0
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T1M1F4"
                        self.x = self.w * 1
                        self.y = self.h * 1
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T1M2F1"
                        self.x = self.w * 2
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T1M2F2"
                        self.x = self.w * 3
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T1M2F3"
                        self.x = self.w * 2
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T1M2F4"
                        self.x = self.w * 3
                        self.y = self.h * 1
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T1M3F1"
                        self.x = self.w * 0
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T1M3F2"
                        self.x = self.w * 1
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T1M3F3"
                        self.x = self.w * 0
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T1M3F4"
                        self.x = self.w * 1
                        self.y = self.h * 3
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T1M4F1"
                        self.x = self.w * 2
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T1M4F2"
                        self.x = self.w * 3
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T1M4F3"
                        self.x = self.w * 2
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T1M4F4"
                        self.x = self.w * 3
                        self.y = self.h * 3
                        

            elif id[0] == "T2":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T2M1F1"
                        self.x = self.w * 4
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T2M1F2"
                        self.x = self.w * 5
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T2M1F3"
                        self.x = self.w * 4
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T2M1F4"
                        self.x = self.w * 5
                        self.y = self.h * 1
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T2M2F1"
                        self.x = self.w * 6
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T2M2F2"
                        self.x = self.w * 7
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T2M2F3"
                        self.x = self.w * 6
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T2M2F4"
                        self.x = self.w * 7
                        self.y = self.h * 1
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T2M3F1"
                        self.x = self.w * 4
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T2M3F2"
                        self.x = self.w * 5
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T2M3F3"
                        self.x = self.w * 4
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T2M3F4"
                        self.x = self.w * 5
                        self.y = self.h * 3
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T2M4F1"
                        self.x = self.w * 6
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T2M4F2"
                        self.x = self.w * 7
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T2M4F3"
                        self.x = self.w * 6
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T2M4F4"
                        self.x = self.w * 7
                        self.y = self.h * 3
                        
            elif id[0] == "T3":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T3M1F1"
                        self.x = self.w * 0
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T3M1F2"
                        self.x = self.w * 1
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T3M1F3"
                        self.x = self.w * 0
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T3M1F4"
                        self.x = self.w * 1
                        self.y = self.h * 5
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T3M2F1"
                        self.x = self.w * 2
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T3M2F2"
                        self.x = self.w * 3
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T3M2F3"
                        self.x = self.w * 2
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T3M2F4"
                        self.x = self.w * 3
                        self.y = self.h * 5
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T3M3F1"
                        self.x = self.w * 0
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T3M3F2"
                        self.x = self.w * 1
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T3M3F3"
                        self.x = self.w * 0
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T3M3F4"
                        self.x = self.w * 1
                        self.y = self.h * 7
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T3M3F1"
                        self.x = self.w * 2
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T3M3F2"
                        self.x = self.w * 3
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T3M3F3"
                        self.x = self.w * 2
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T3M3F4"
                        self.x = self.w * 3
                        self.y = self.h * 7
                        
            elif id[0] == "T4":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T4M1F1"
                        self.x = self.w * 4
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T4M1F2"
                        self.x = self.w * 5
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T4M1F3"
                        self.x = self.w * 4
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T4M1F4"
                        self.x = self.w * 5
                        self.y = self.h * 5
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T4M2F1"
                        self.x = self.w * 6
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T4M2F2"
                        self.x = self.w * 7
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T4M2F3"
                        self.x = self.w * 6
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T4M2F4"
                        self.x = self.w * 7
                        self.y = self.h * 5
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T4M3F1"
                        self.x = self.w * 4
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T4M3F2"
                        self.x = self.w * 5
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T4M3F3"
                        self.x = self.w * 4
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T4M3F4"
                        self.x = self.w * 5
                        self.y = self.h * 7
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T4M4F1"
                        self.x = self.w * 6
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T4M4F2"
                        self.x = self.w * 7
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T4M4F3"
                        self.x = self.w * 6
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T4M4F4"
                        self.x = self.w * 7
                        self.y = self.h * 7
                        
        ###########################################!######################################
        #o2
        elif o == 2:    
            if id[0] == "T5":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T5M1F1"
                        self.x = self.w * 8
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T5M1F2"
                        self.x = self.w * 9
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T5M1F3"
                        self.x = self.w * 8
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T5M1F4"
                        self.x = self.w * 9
                        self.y = self.h * 1
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T5M2F1"
                        self.x = self.w * 10
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T5M2F2"
                        self.x = self.w * 11
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T5M2F3"
                        self.x = self.w * 10
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T5M2F4"
                        self.x = self.w * 11
                        self.y = self.h * 1
                        


                #M3
                elif id[1] == "M3": 
                    #F1
                    if id[2] == "F1":
                        self.id = "T5M3F1"
                        self.x = self.w * 8
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T5M3F2"
                        self.x = self.w * 9
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T5M3F3"
                        self.x = self.w * 8
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T5M3F4"
                        self.x = self.w * 9
                        self.y = self.h * 3
                        


                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T5M4F1"
                        self.x = self.w * 10
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T5M4F2"
                        self.x = self.w * 11
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T5M4F3"
                        self.x = self.w * 10
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T5M4F4"
                        self.x = self.w * 11
                        self.y = self.h * 3
                        

            elif id[0] == "T6":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T6M1F1"
                        self.x = self.w * 12
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T6M1F2"
                        self.x = self.w * 13
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T6M1F3"
                        self.x = self.w * 12
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T6M1F4"
                        self.x = self.w * 13
                        self.y = self.h * 1
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T6M2F1"
                        self.x = self.w * 14
                        self.y = self.h * 0
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T6M2F2"
                        self.x = self.w * 15
                        self.y = self.h * 0
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T6M2F3"
                        self.x = self.w * 14
                        self.y = self.h * 1
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T6M2F4"
                        self.x = self.w * 15
                        self.y = self.h * 1
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T6M3F1"
                        self.x = self.w * 12
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T6M3F2"
                        self.x = self.w * 13
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T6M3F3"
                        self.x = self.w * 12
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T6M3F4"
                        self.x = self.w * 13
                        self.y = self.h * 3
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T6M4F1"
                        self.x = self.w * 14
                        self.y = self.h * 2
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T6M4F2"
                        self.x = self.w * 15
                        self.y = self.h * 2
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T6M4F3"
                        self.x = self.w * 14
                        self.y = self.h * 3
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T6M4F4"
                        self.x = self.w * 15
                        self.y = self.h * 3
                        
            elif id[0] == "T7":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T7M1F1"
                        self.x = self.w * 8
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T7M1F2"
                        self.x = self.w * 9
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T7M1F3"
                        self.x = self.w * 8
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T7M1F4"
                        self.x = self.w * 9
                        self.y = self.h * 5
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T7M2F1"
                        self.x = self.w * 10
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T7M2F2"
                        self.x = self.w * 11
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T7M2F3"
                        self.x = self.w * 10
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T7M2F4"
                        self.x = self.w * 11
                        self.y = self.h * 5
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T7M3F1"
                        self.x = self.w * 8
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T7M3F2"
                        self.x = self.w * 9
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T7M3F3"
                        self.x = self.w * 8
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T7M3F4"
                        self.x = self.w * 9
                        self.y = self.h * 7
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T7M4F1"
                        self.x = self.w * 10
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T7M4F2"
                        self.x = self.w * 11
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T7M4F3"
                        self.x = self.w * 10
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T7M4F4"
                        self.x = self.w * 11
                        self.y = self.h * 7
                        
            elif id[0] == "T8":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T8M1F1"
                        self.x = self.w * 12
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T8M1F2"
                        self.x = self.w * 13
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T8M1F3"
                        self.x = self.w * 12
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T8M1F4"
                        self.x = self.w * 13
                        self.y = self.h * 5
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T8M2F1"
                        self.x = self.w * 14
                        self.y = self.h * 4
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T8M2F2"
                        self.x = self.w * 15
                        self.y = self.h * 4
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T8M2F3"
                        self.x = self.w * 14
                        self.y = self.h * 5
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T8M2F4"
                        self.x = self.w * 15
                        self.y = self.h * 5
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T8M3F1"
                        self.x = self.w * 12
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T8M3F2"
                        self.x = self.w * 13
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T8M3F3"
                        self.x = self.w * 12
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T8M3F4"
                        self.x = self.w * 13
                        self.y = self.h * 7
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T8M4F1"
                        self.x = self.w * 14
                        self.y = self.h * 6
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T8M4F2"
                        self.x = self.w * 15
                        self.y = self.h * 6
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T8M4F3"
                        self.x = self.w * 14
                        self.y = self.h * 7
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T8M4F4"
                        self.x = self.w * 15
                        self.y = self.h * 7
                        
        ###########################################!######################################
        #o3
        elif o == 3:
            if id[0] == "T9":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T9M1F1"
                        self.x = self.w * 0
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T9M1F2"
                        self.x = self.w * 1
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T9M1F3"
                        self.x = self.w * 0
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T9M1F4"
                        self.x = self.w * 1
                        self.y = self.h * 9
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T9M2F1"
                        self.x = self.w * 2
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T9M2F2"
                        self.x = self.w * 3
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T9M2F3"
                        self.x = self.w * 2
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T9M2F4"
                        self.x = self.w * 3
                        self.y = self.h * 9
                        


                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T9M3F1"
                        self.x = self.w * 0
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T9M3F2"
                        self.x = self.w * 1
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T9M3F3"
                        self.x = self.w * 0
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T9M3F4"
                        self.x = self.w * 1
                        self.y = self.h * 11
                        


                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T9M4F1"
                        self.x = self.w * 2
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T9M4F2"
                        self.x = self.w * 3
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T9M4F3"
                        self.x = self.w * 2
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T9M4F4"
                        self.x = self.w * 3
                        self.y = self.h * 11
                        
            elif id[0] == "T10":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T10M1F1"
                        self.x = self.w * 4
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T10M1F2"
                        self.x = self.w * 5
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T10M1F3"
                        self.x = self.w * 4
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T10M1F4"
                        self.x = self.w * 5
                        self.y = self.h * 9
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T10M2F1"
                        self.x = self.w * 6
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T10M2F2"
                        self.x = self.w * 7
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T10M2F3"
                        self.x = self.w * 6
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T10M2F4"
                        self.x = self.w * 7
                        self.y = self.h * 9
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T10M3F1"
                        self.x = self.w * 4
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T10M3F2"
                        self.x = self.w * 5
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T10M3F3"
                        self.x = self.w * 4
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T10M3F4"
                        self.x = self.w * 5
                        self.y = self.h * 11
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T10M4F1"
                        self.x = self.w * 6
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T10M4F2"
                        self.x = self.w * 7
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T10M4F3"
                        self.x = self.w * 6
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T10M4F4"
                        self.x = self.w * 7
                        self.y = self.h * 11
                        
            elif id[0] == "T11":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T11M1F1"
                        self.x = self.w * 0
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T11M1F2"
                        self.x = self.w * 1
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T11M1F3"
                        self.x = self.w * 0
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T11M1F4"
                        self.x = self.w * 1
                        self.y = self.h * 13
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T11M2F1"
                        self.x = self.w * 2
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T11M2F2"
                        self.x = self.w * 3
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T11M2F3"
                        self.x = self.w * 2
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T11M2F4"
                        self.x = self.w * 3
                        self.y = self.h * 13
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T11M3F1"
                        self.x = self.w * 0
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T11M3F2"
                        self.x = self.w * 1
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T11M3F3"
                        self.x = self.w * 0
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T11M3F4"
                        self.x = self.w * 1
                        self.y = self.h * 15
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T11M4F1"
                        self.x = self.w * 2
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T11M4F2"
                        self.x = self.w * 3
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T11M4F3"
                        self.x = self.w * 2
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T11M4F4"
                        self.x = self.w * 3
                        self.y = self.h * 15
                        
            
            elif id[0] == "T12":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T12M1F1"
                        self.x = self.w * 4
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T12M1F2"
                        self.x = self.w * 5
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T12M1F3"
                        self.x = self.w * 4
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T12M1F4"
                        self.x = self.w * 5
                        self.y = self.h * 13
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T12M2F1"
                        self.x = self.w * 6
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T12M2F2"
                        self.x = self.w * 7
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T12M2F3"
                        self.x = self.w * 6
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T12M2F4"
                        self.x = self.w * 7
                        self.y = self.h * 13
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T12M3F1"
                        self.x = self.w * 4
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T12M3F2"
                        self.x = self.w * 5
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T12M3F3"
                        self.x = self.w * 4
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T12M3F4"
                        self.x = self.w * 5
                        self.y = self.h * 15
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T12M4F1"
                        self.x = self.w * 6
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T12M4F2"
                        self.x = self.w * 7
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T12M4F3"
                        self.x = self.w * 6
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T12M4F4"
                        self.x = self.w * 7
                        self.y = self.h * 15
                        
        ###########################################!######################################
        #o4
        elif o == 4:
            if id[0] == "T13":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T13M1F1"
                        self.x = self.w * 8
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T13M1F2"
                        self.x = self.w * 9
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T13M1F3"
                        self.x = self.w * 8
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T13M1F4"
                        self.x = self.w * 9
                        self.y = self.h * 9
                        


                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T13M2F1"
                        self.x = self.w * 10
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T13M2F2"
                        self.x = self.w * 11
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T13M2F3"
                        self.x = self.w * 10
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T13M2F4"
                        self.x = self.w * 11
                        self.y = self.h * 9
                        


                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T13M3F1"
                        self.x = self.w * 8
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T13M3F2"
                        self.x = self.w * 9
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T13M3F3"
                        self.x = self.w * 8
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T13M3F4"
                        self.x = self.w * 9
                        self.y = self.h * 11
                        


                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T13M4F1"
                        self.x = self.w * 10
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T13M4F2"
                        self.x = self.w * 11
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T13M4F3"
                        self.x = self.w * 10
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T13M4F4"
                        self.x = self.w * 11
                        self.y = self.h * 11
                        

            elif id[0] == "T14":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T14M1F1"
                        self.x = self.w * 12
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T14M1F2"
                        self.x = self.w * 13
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T14M1F3"
                        self.x = self.w * 12
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T14M1F4"
                        self.x = self.w * 13
                        self.y = self.h * 9
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T14M2F1"
                        self.x = self.w * 14
                        self.y = self.h * 8
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T14M2F2"
                        self.x = self.w * 15
                        self.y = self.h * 8
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T14M2F3"
                        self.x = self.w * 14
                        self.y = self.h * 9
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T14M2F4"
                        self.x = self.w * 15
                        self.y = self.h * 9
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T14M3F1"
                        self.x = self.w * 12
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T14M3F2"
                        self.x = self.w * 13
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T14M3F3"
                        self.x = self.w * 12
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T14M3F4"
                        self.x = self.w * 13
                        self.y = self.h * 11
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T14M4F1"
                        self.x = self.w * 14
                        self.y = self.h * 10
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T14M4F2"
                        self.x = self.w * 15
                        self.y = self.h * 10
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T14M4F3"
                        self.x = self.w * 14
                        self.y = self.h * 11
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T14M4F4"
                        self.x = self.w * 15
                        self.y = self.h * 11
                        
            elif id[0] == "T15":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T15M1F1"
                        self.x = self.w * 8
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T15M1F2"
                        self.x = self.w * 9
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T15M1F3"
                        self.x = self.w * 8
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T15M1F4"
                        self.x = self.w * 9
                        self.y = self.h * 13
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T15M2F1"
                        self.x = self.w * 10
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T15M2F2"
                        self.x = self.w * 11
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T15M2F3"
                        self.x = self.w * 10
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T15M2F4"
                        self.x = self.w * 11
                        self.y = self.h * 13
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T15M3F1"
                        self.x = self.w * 8
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T15M3F2"
                        self.x = self.w * 9
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T15M3F3"
                        self.x = self.w * 8
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T15M3F4"
                        self.x = self.w * 9
                        self.y = self.h * 15
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T15M4F1"
                        self.x = self.w * 10
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T15M4F2"
                        self.x = self.w * 11
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T15M4F3"
                        self.x = self.w * 10
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T15M4F4"
                        self.x = self.w * 11
                        self.y = self.h * 15
                        
            
            elif id[0] == "T16":
                #M1
                if id[1] == "M1":
                    #F1
                    if id[2] == "F1":
                        self.id = "T16M1F1"
                        self.x = self.w * 12
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T16M1F2"
                        self.x = self.w * 13
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T16M1F3"
                        self.x = self.w * 12
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T16M1F4"
                        self.x = self.w * 13
                        self.y = self.h * 13
                        
                #M2
                elif id[1] == "M2":
                    #F1
                    if id[2] == "F1":
                        self.id = "T16M2F1"
                        self.x = self.w * 14
                        self.y = self.h * 12
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T16M2F2"
                        self.x = self.w * 15
                        self.y = self.h * 12
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T16M2F3"
                        self.x = self.w * 14
                        self.y = self.h * 13
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T16M2F4"
                        self.x = self.w * 15
                        self.y = self.h * 13
                        
                #M3
                elif id[1] == "M3":
                    #F1
                    if id[2] == "F1":
                        self.id = "T16M3F1"
                        self.x = self.w * 12
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T16M3F2"
                        self.x = self.w * 13
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T16M3F3"
                        self.x = self.w * 12
                        self.y = self.h * 15
                        
                    #F4
                    elif id[2] == "F4":
                        self.id = "T16M3F4"
                        self.x = self.w * 13
                        self.y = self.h * 15
                        
                #M4
                elif id[1] == "M4":
                    #F1
                    if id[2] == "F1":
                        self.id = "T16M4F1"
                        self.x = self.w * 14
                        self.y = self.h * 14
                        
                    #F2
                    elif id[2] == "F2":
                        self.id = "T16M4F2"
                        self.x = self.w * 15
                        self.y = self.h * 14
                        
                    #F3
                    elif id[2] == "F3":
                        self.id = "T16M4F3"
                        self.x = self.w * 14
                        self.y = self.h * 15

                    #F4
                    elif id[2] == "F4":
                        self.id = "T16M4F4"
                        self.x = self.w * 15
                        self.y = self.h * 15




        #!--------------------------------------------------------------------------!#
        #!------------------------------< Tiles Prop >------------------------------!#
        #!--------------------------------------------------------------------------!#
        data = {}
        appdata = os.getenv('APPDATA') #get appdata
        o1_path = appdata + "\\.rails_and_potatoes\\index\\Assets\\tiles\\properties\\O1\\"
        o2_path = appdata + "\\.rails_and_potatoes\\index\\Assets\\tiles\\properties\\O2\\"
        o3_path = appdata + "\\.rails_and_potatoes\\index\\Assets\\tiles\\properties\\O3\\"
        o4_path = appdata + "\\.rails_and_potatoes\\index\\Assets\\tiles\\properties\\O4\\"
        
        #?----------------------------------------------------------------------?#
        #?--------------------------------< O1 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        with open(o1_path + "T1.tp", "r") as f:
            data["T1"] = json.load(f)
            f.close()
        with open(o1_path + "T2.tp", "r") as f:
            data["T2"] = json.load(f)
            f.close()
        with open(o1_path + "T3.tp", "r") as f:
            data["T3"] = json.load(f)
            f.close()
        with open(o1_path + "T4.tp", "r") as f:
            data["T4"] = json.load(f)
            f.close()
        
        #?----------------------------------------------------------------------?#
        #?--------------------------------< O2 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        with open(o2_path + "T5.tp", "r") as f:
            data["T5"] = json.load(f)
            f.close()
        with open(o2_path + "T6.tp", "r") as f:
            data["T6"] = json.load(f)
            f.close()
        with open(o2_path + "T7.tp", "r") as f:
            data["T7"] = json.load(f)
            f.close()
        with open(o2_path + "T8.tp", "r") as f:
            data["T8"] = json.load(f)
            f.close()
        
        #?----------------------------------------------------------------------?#
        #?--------------------------------< O3 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        with open(o3_path + "T9.tp", "r") as f:
            data["T9"] = json.load(f)
            f.close()
        with open(o3_path + "T10.tp", "r") as f:
            data["T10"] = json.load(f)
            f.close()
        with open(o3_path + "T11.tp", "r") as f:
            data["T11"] = json.load(f)
            f.close()
        with open(o3_path + "T12.tp", "r") as f:
            data["T12"] = json.load(f)
            f.close()
        
        #?----------------------------------------------------------------------?#
        #?--------------------------------< O4 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        with open(o4_path + "T13.tp", "r") as f:
            data["T13"] = json.load(f)
            f.close()
        with open(o4_path + "T14.tp", "r") as f:
            data["T14"] = json.load(f)
            f.close()
        with open(o4_path + "T15.tp", "r") as f:
            data["T15"] = json.load(f)
            f.close()
        with open(o4_path + "T16.tp", "r") as f:
            data["T16"] = json.load(f)
            f.close()





        #!----------------------------------------------------------------------!#
        #!------------------------------< Images >------------------------------!#
        #!----------------------------------------------------------------------!#
        self.image = {}
        self.type = {}
        level_1_foldername = "tiles\\lvl1"




        #?----------------------------------------------------------------------?#
        #?----------------------------< RailsImage >----------------------------?#
        #?----------------------------------------------------------------------?#
        self.image["1-r"] = textures.change_texture(
            filename = "rail.png",
            foldername = level_1_foldername
            )





        #?----------------------------------------------------------------------?#
        #?--------------------------------< O1 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        if o == 1:

            #------------------------------------------------------------------------#
            #---------------------------------< T1 >---------------------------------#
            #------------------------------------------------------------------------#
            if id[0] == "T1":
                #--> type <--#
                self.type["1"] = data["T1"][self.id]["1"]
                self.type["2"] = data["T1"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )

            #------------------------------------------------------------------------#
            #---------------------------------< T2 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T2":
                #--> type <--#
                self.type["1"] = data["T2"][self.id]["1"]
                self.type["2"] = data["T2"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #------------------------------------------------------------------------#
            #---------------------------------< T3 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T3":
                #--> type <--#
                self.type["1"] = data["T3"][self.id]["1"]
                self.type["2"] = data["T3"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )

            #------------------------------------------------------------------------#
            #---------------------------------< T4 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T4":
                #--> type <--#
                self.type["1"] = data["T4"][self.id]["1"]
                self.type["2"] = data["T4"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            

        #?----------------------------------------------------------------------?#
        #?--------------------------------< O2 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        elif o == 2:

            #------------------------------------------------------------------------#
            #---------------------------------< T5 >---------------------------------#
            #------------------------------------------------------------------------#
            if id[0] == "T5":
                #--> type <--#
                self.type["1"] = data["T5"][self.id]["1"]
                self.type["2"] = data["T5"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #------------------------------------------------------------------------#
            #---------------------------------< T6 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T6":
                #--> type <--#
                self.type["1"] = data["T6"][self.id]["1"]
                self.type["2"] = data["T6"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #------------------------------------------------------------------------#
            #---------------------------------< T7 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T7":
                #--> type <--#
                self.type["1"] = data["T7"][self.id]["1"]
                self.type["2"] = data["T7"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #------------------------------------------------------------------------#
            #---------------------------------< T8 >---------------------------------#
            #------------------------------------------------------------------------#
            elif id[0] == "T8":
                #--> type <--#
                self.type["1"] = data["T8"][self.id]["1"]
                self.type["2"] = data["T8"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
        

        #?----------------------------------------------------------------------?#
        #?--------------------------------< O3 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        elif o == 3:

            #------------------------------------------------------------------------#
            #---------------------------------< T9 >---------------------------------#
            #------------------------------------------------------------------------#
            if id[0] == "T9":
                #--> type <--#
                self.type["1"] = data["T9"][self.id]["1"]
                self.type["2"] = data["T9"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T10 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T10":
                #--> type <--#
                self.type["1"] = data["T10"][self.id]["1"]
                self.type["2"] = data["T10"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T11 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T11":
                #--> type <--#
                self.type["1"] = data["T11"][self.id]["1"]
                self.type["2"] = data["T11"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T12 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T12":
                #--> type <--#
                self.type["1"] = data["T12"][self.id]["1"]
                self.type["2"] = data["T12"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
        

        #?----------------------------------------------------------------------?#
        #?--------------------------------< O4 >--------------------------------?#
        #?----------------------------------------------------------------------?#
        elif o == 4:

            #-----------------------------------------------------------------------#
            #--------------------------------< T13 >--------------------------------#
            #-----------------------------------------------------------------------#
            if id[0] == "T13":
                #--> type <--#
                self.type["1"] = data["T13"][self.id]["1"]
                self.type["2"] = data["T13"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T14 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T14":
                #--> type <--#
                self.type["1"] = data["T14"][self.id]["1"]
                self.type["2"] = data["T14"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T15 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T15":
                #--> type <--#
                self.type["1"] = data["T15"][self.id]["1"]
                self.type["2"] = data["T15"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
            
            #-----------------------------------------------------------------------#
            #--------------------------------< T16 >--------------------------------#
            #-----------------------------------------------------------------------#
            elif id[0] == "T16":
                #--> type <--#
                self.type["1"] = data["T16"][self.id]["1"]
                self.type["2"] = data["T16"][self.id]["2"]

                #--> images <--#
                self.image["1"] = textures.change_texture(
                    filename = self.type["1"] + ".png",
                    foldername = level_1_foldername
                )
                self.image["2"] = textures.change_texture(
                    filename = self.type["2"] + ".png",
                    foldername = level_1_foldername
                )
        #%end%--------------------------------%end%#
        
        #create the rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #%end%-------------------------------------------------------------------%end%#




    def load_images(self, lvl = 1):      
        if lvl != self.lvl_before:
            if not self.rail:
                self.loaded_image = pygame.image.load(
                    self.image[str(lvl)]
                )
            else:
                self.loaded_image = pygame.image.load(
                    self.image[str(lvl) + "-r"]
                )
            self.lvl_before = lvl
    #%end%-------------------------------------------------------------------%end%#




    def update(self, lvl = 1):
        """this func updates the tile

        Args:
            lvl (int, optional): the level that need to be checked in. Defaults to 1.
        """        
        self.width = sys.Resize.resize_x(
            settings.starting_screen_width,
            self.w,
            gf.screen_width
        )
        self.height = sys.Resize.resize_y(
            settings.starting_screen_height,
            self.h,
            gf.screen_height
        )
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.load_images(lvl)
        gf.screen.blit(
            pygame.transform.scale(
                self.loaded_image,
                (self.rect.width, self.rect.height)
            ),
            (self.x, self.y)
        )
    #%end%-------------------------------------------------------------------%end%#


    def click(self, level = 1):
        """
        this func checks if the user/player clicked on the tile

        Args:
            level (int, optional): the level that need to be checked in. Defaults to 1.
        """             
        if self.rect.collidepoint((gf.mouse_x, gf.mouse_y)):
            if gf.click:
                if self.type[str(level)].endswith(("blocker", "start", "end", "pickup", "dropdown")) == False:
                    self.rail = True 
                    self.lvl_before -= 1
                    self.load_images(level)
                    gf.click = False
                else:
                    gf.click = False
            elif gf.right_click:
                if (
                    self.type[str(level)].endswith(("blocker", "start", "end", "pickup", "dropdown")) == False
                    ) and (
                        self.rail == True
                    ):
                    self.rail = False
                    self.lvl_before -= 1
                    self.load_images(level)
                    gf.right_click = False
                else:
                    gf.right_click = False
        
        return self.__str__()

    #%end%-------------------------------------------------------------------%end%#


    def __str__(self):
        return self.id
    #%end%-------------------------------------------------------------------%end%#
#!-------------------------------------------------------------------!#









#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
class Tiles:
    def __init__(self):
        """this class is creating generating tiles
        """
        
        #T1M1
        self.T1M1F1 = tile()
        self.T1M1F2 = tile(id = ["T1", "M1", "F2"])
        self.T1M1F3 = tile(id = ["T1", "M1", "F3"])
        self.T1M1F4 = tile(id = ["T1", "M1", "F4"])
        #T1M2
        self.T1M2F1 = tile(id = ["T1", "M2", "F1"])
        self.T1M2F2 = tile(id = ["T1", "M2", "F2"])
        self.T1M2F3 = tile(id = ["T1", "M2", "F3"])
        self.T1M2F4 = tile(id = ["T1", "M2", "F4"])
        #T1M3
        self.T1M3F1 = tile(id = ["T1", "M3", "F1"])
        self.T1M3F2 = tile(id = ["T1", "M3", "F2"])
        self.T1M3F3 = tile(id = ["T1", "M3", "F3"])
        self.T1M3F4 = tile(id = ["T1", "M3", "F4"])
        #T1M4
        self.T1M4F1 = tile(id = ["T1", "M4", "F1"])
        self.T1M4F2 = tile(id = ["T1", "M4", "F2"])
        self.T1M4F3 = tile(id = ["T1", "M4", "F3"])
        self.T1M4F4 = tile(id = ["T1", "M4", "F4"])

        #T2M1
        self.T2M1F1 = tile(id = ["T2", "M1", "F1"])
        self.T2M1F2 = tile(id = ["T2", "M1", "F2"])
        self.T2M1F3 = tile(id = ["T2", "M1", "F3"])
        self.T2M1F4 = tile(id = ["T2", "M1", "F4"])
        #T2M2
        self.T2M2F1 = tile(id = ["T2", "M2", "F1"])
        self.T2M2F2 = tile(id = ["T2", "M2", "F2"])
        self.T2M2F3 = tile(id = ["T2", "M2", "F3"])
        self.T2M2F4 = tile(id = ["T2", "M2", "F4"])
        #T2M3
        self.T2M3F1 = tile(id = ["T2", "M3", "F1"])
        self.T2M3F2 = tile(id = ["T2", "M3", "F2"])
        self.T2M3F3 = tile(id = ["T2", "M3", "F3"])
        self.T2M3F4 = tile(id = ["T2", "M3", "F4"])
        #T2M4
        self.T2M4F1 = tile(id = ["T2", "M4", "F1"])
        self.T2M4F2 = tile(id = ["T2", "M4", "F2"])
        self.T2M4F3 = tile(id = ["T2", "M4", "F3"])
        self.T2M4F4 = tile(id = ["T2", "M4", "F4"])

        #T3M1
        self.T3M1F1 = tile(id = ["T3", "M1", "F1"])
        self.T3M1F2 = tile(id = ["T3", "M1", "F2"])
        self.T3M1F3 = tile(id = ["T3", "M1", "F3"])
        self.T3M1F4 = tile(id = ["T3", "M1", "F4"])
        #T3M2
        self.T3M2F1 = tile(id = ["T3", "M2", "F1"])
        self.T3M2F2 = tile(id = ["T3", "M2", "F2"])
        self.T3M2F3 = tile(id = ["T3", "M2", "F3"])
        self.T3M2F4 = tile(id = ["T3", "M2", "F4"])
        #T3M3
        self.T3M3F1 = tile(id = ["T3", "M3", "F1"])
        self.T3M3F2 = tile(id = ["T3", "M3", "F2"])
        self.T3M3F3 = tile(id = ["T3", "M3", "F3"])
        self.T3M3F4 = tile(id = ["T3", "M3", "F4"])
        #T3M4
        self.T3M4F1 = tile(id = ["T3", "M4", "F1"])
        self.T3M4F2 = tile(id = ["T3", "M4", "F2"])
        self.T3M4F3 = tile(id = ["T3", "M4", "F3"])
        self.T3M4F4 = tile(id = ["T3", "M4", "F4"])

        #T4M1
        self.T4M1F1 = tile(id = ["T4", "M1", "F1"])
        self.T4M1F2 = tile(id = ["T4", "M1", "F2"])
        self.T4M1F3 = tile(id = ["T4", "M1", "F3"])
        self.T4M1F4 = tile(id = ["T4", "M1", "F4"])
        #T4M2
        self.T4M2F1 = tile(id = ["T4", "M2", "F1"])
        self.T4M2F2 = tile(id = ["T4", "M2", "F2"])
        self.T4M2F3 = tile(id = ["T4", "M2", "F3"])
        self.T4M2F4 = tile(id = ["T4", "M2", "F4"])
        #T4M3
        self.T4M3F1 = tile(id = ["T4", "M3", "F1"])
        self.T4M3F2 = tile(id = ["T4", "M3", "F2"])
        self.T4M3F3 = tile(id = ["T4", "M3", "F3"])
        self.T4M3F4 = tile(id = ["T4", "M3", "F4"])
        #T4M4
        self.T4M4F1 = tile(id = ["T4", "M4", "F1"])
        self.T4M4F2 = tile(id = ["T4", "M4", "F2"])
        self.T4M4F3 = tile(id = ["T4", "M4", "F3"])
        self.T4M4F4 = tile(id = ["T4", "M4", "F4"])

        #T5M1
        self.T5M1F1 = tile(o = 2, id = ["T5", "M1", "F1"])
        self.T5M1F2 = tile(o = 2, id = ["T5", "M1", "F2"])
        self.T5M1F3 = tile(o = 2, id = ["T5", "M1", "F3"])
        self.T5M1F4 = tile(o = 2, id = ["T5", "M1", "F4"])
        #T5M2
        self.T5M2F1 = tile(o = 2, id = ["T5", "M2", "F1"])
        self.T5M2F2 = tile(o = 2, id = ["T5", "M2", "F2"])
        self.T5M2F3 = tile(o = 2, id = ["T5", "M2", "F3"])
        self.T5M2F4 = tile(o = 2, id = ["T5", "M2", "F4"])
        #T5M3
        self.T5M3F1 = tile(o = 2, id = ["T5", "M3", "F1"])
        self.T5M3F2 = tile(o = 2, id = ["T5", "M3", "F2"])
        self.T5M3F3 = tile(o = 2, id = ["T5", "M3", "F3"])
        self.T5M3F4 = tile(o = 2, id = ["T5", "M3", "F4"])
        #T5M4
        self.T5M4F1 = tile(o = 2, id = ["T5", "M4", "F1"])
        self.T5M4F2 = tile(o = 2, id = ["T5", "M4", "F2"])
        self.T5M4F3 = tile(o = 2, id = ["T5", "M4", "F3"])
        self.T5M4F4 = tile(o = 2, id = ["T5", "M4", "F4"])

        #T6M1
        self.T6M1F1 = tile(o = 2, id = ["T6", "M1", "F1"])
        self.T6M1F2 = tile(o = 2, id = ["T6", "M1", "F2"])
        self.T6M1F3 = tile(o = 2, id = ["T6", "M1", "F3"])
        self.T6M1F4 = tile(o = 2, id = ["T6", "M1", "F4"])
        #T6M2
        self.T6M2F1 = tile(o = 2, id = ["T6", "M2", "F1"])
        self.T6M2F2 = tile(o = 2, id = ["T6", "M2", "F2"])
        self.T6M2F3 = tile(o = 2, id = ["T6", "M2", "F3"])
        self.T6M2F4 = tile(o = 2, id = ["T6", "M2", "F4"])
        #T6M3
        self.T6M3F1 = tile(o = 2, id = ["T6", "M3", "F1"])
        self.T6M3F2 = tile(o = 2, id = ["T6", "M3", "F2"])
        self.T6M3F3 = tile(o = 2, id = ["T6", "M3", "F3"])
        self.T6M3F4 = tile(o = 2, id = ["T6", "M3", "F4"])
        #T6M4
        self.T6M4F1 = tile(o = 2, id = ["T6", "M4", "F1"])
        self.T6M4F2 = tile(o = 2, id = ["T6", "M4", "F2"])
        self.T6M4F3 = tile(o = 2, id = ["T6", "M4", "F3"])
        self.T6M4F4 = tile(o = 2, id = ["T6", "M4", "F4"])

        #T7M1
        self.T7M1F1 = tile(o = 2, id = ["T7", "M1", "F1"])
        self.T7M1F2 = tile(o = 2, id = ["T7", "M1", "F2"])
        self.T7M1F3 = tile(o = 2, id = ["T7", "M1", "F3"])
        self.T7M1F4 = tile(o = 2, id = ["T7", "M1", "F4"])
        #T7M2
        self.T7M2F1 = tile(o = 2, id = ["T7", "M2", "F1"])
        self.T7M2F2 = tile(o = 2, id = ["T7", "M2", "F2"])
        self.T7M2F3 = tile(o = 2, id = ["T7", "M2", "F3"])
        self.T7M2F4 = tile(o = 2, id = ["T7", "M2", "F4"])
        #T7M3
        self.T7M3F1 = tile(o = 2, id = ["T7", "M3", "F1"])
        self.T7M3F2 = tile(o = 2, id = ["T7", "M3", "F2"])
        self.T7M3F3 = tile(o = 2, id = ["T7", "M3", "F3"])
        self.T7M3F4 = tile(o = 2, id = ["T7", "M3", "F4"])
        #T7M4
        self.T7M4F1 = tile(o = 2, id = ["T7", "M4", "F1"])
        self.T7M4F2 = tile(o = 2, id = ["T7", "M4", "F2"])
        self.T7M4F3 = tile(o = 2, id = ["T7", "M4", "F3"])
        self.T7M4F4 = tile(o = 2, id = ["T7", "M4", "F4"])

        #T8M1
        self.T8M1F1 = tile(o = 2, id = ["T8", "M1", "F1"])
        self.T8M1F2 = tile(o = 2, id = ["T8", "M1", "F2"])
        self.T8M1F3 = tile(o = 2, id = ["T8", "M1", "F3"])
        self.T8M1F4 = tile(o = 2, id = ["T8", "M1", "F4"])
        #T8M2
        self.T8M2F1 = tile(o = 2, id = ["T8", "M2", "F1"])
        self.T8M2F2 = tile(o = 2, id = ["T8", "M2", "F2"])
        self.T8M2F3 = tile(o = 2, id = ["T8", "M2", "F3"])
        self.T8M2F4 = tile(o = 2, id = ["T8", "M2", "F4"])
        #T8M3
        self.T8M3F1 = tile(o = 2, id = ["T8", "M3", "F1"])
        self.T8M3F2 = tile(o = 2, id = ["T8", "M3", "F2"])
        self.T8M3F3 = tile(o = 2, id = ["T8", "M3", "F3"])
        self.T8M3F4 = tile(o = 2, id = ["T8", "M3", "F4"])
        #T8M4
        self.T8M4F1 = tile(o = 2, id = ["T8", "M4", "F1"])
        self.T8M4F2 = tile(o = 2, id = ["T8", "M4", "F2"])
        self.T8M4F3 = tile(o = 2, id = ["T8", "M4", "F3"])
        self.T8M4F4 = tile(o = 2, id = ["T8", "M4", "F4"])

        #T9M1
        self.T9M1F1 = tile(o = 3, id = ["T9", "M1", "F1"])
        self.T9M1F2 = tile(o = 3, id = ["T9", "M1", "F2"])
        self.T9M1F3 = tile(o = 3, id = ["T9", "M1", "F3"])
        self.T9M1F4 = tile(o = 3, id = ["T9", "M1", "F4"])
        #T9M2
        self.T9M2F1 = tile(o = 3, id = ["T9", "M2", "F1"])
        self.T9M2F2 = tile(o = 3, id = ["T9", "M2", "F2"])
        self.T9M2F3 = tile(o = 3, id = ["T9", "M2", "F3"])
        self.T9M2F4 = tile(o = 3, id = ["T9", "M2", "F4"])
        #T9M3
        self.T9M3F1 = tile(o = 3, id = ["T9", "M3", "F1"])
        self.T9M3F2 = tile(o = 3, id = ["T9", "M3", "F2"])
        self.T9M3F3 = tile(o = 3, id = ["T9", "M3", "F3"])
        self.T9M3F4 = tile(o = 3, id = ["T9", "M3", "F4"])
        #T9M4
        self.T9M4F1 = tile(o = 3, id = ["T9", "M4", "F1"])
        self.T9M4F2 = tile(o = 3, id = ["T9", "M4", "F2"])
        self.T9M4F3 = tile(o = 3, id = ["T9", "M4", "F3"])
        self.T9M4F4 = tile(o = 3, id = ["T9", "M4", "F4"])

        #T10M1
        self.T10M1F1 = tile(o = 3, id = ["T10", "M1", "F1"])
        self.T10M1F2 = tile(o = 3, id = ["T10", "M1", "F2"])
        self.T10M1F3 = tile(o = 3, id = ["T10", "M1", "F3"])
        self.T10M1F4 = tile(o = 3, id = ["T10", "M1", "F4"])
        #T10M2
        self.T10M2F1 = tile(o = 3, id = ["T10", "M2", "F1"])
        self.T10M2F2 = tile(o = 3, id = ["T10", "M2", "F2"])
        self.T10M2F3 = tile(o = 3, id = ["T10", "M2", "F3"])
        self.T10M2F4 = tile(o = 3, id = ["T10", "M2", "F4"])
        #T10M3
        self.T10M3F1 = tile(o = 3, id = ["T10", "M3", "F1"])
        self.T10M3F2 = tile(o = 3, id = ["T10", "M3", "F2"])
        self.T10M3F3 = tile(o = 3, id = ["T10", "M3", "F3"])
        self.T10M3F4 = tile(o = 3, id = ["T10", "M3", "F4"])
        #T10M4
        self.T10M4F1 = tile(o = 3, id = ["T10", "M4", "F1"])
        self.T10M4F2 = tile(o = 3, id = ["T10", "M4", "F2"])
        self.T10M4F3 = tile(o = 3, id = ["T10", "M4", "F3"])
        self.T10M4F4 = tile(o = 3, id = ["T10", "M4", "F4"])

        #T11M1
        self.T11M1F1 = tile(o = 3, id = ["T11", "M1", "F1"])
        self.T11M1F2 = tile(o = 3, id = ["T11", "M1", "F2"])
        self.T11M1F3 = tile(o = 3, id = ["T11", "M1", "F3"])
        self.T11M1F4 = tile(o = 3, id = ["T11", "M1", "F4"])
        #T11M2
        self.T11M2F1 = tile(o = 3, id = ["T11", "M2", "F1"])
        self.T11M2F2 = tile(o = 3, id = ["T11", "M2", "F2"])
        self.T11M2F3 = tile(o = 3, id = ["T11", "M2", "F3"])
        self.T11M2F4 = tile(o = 3, id = ["T11", "M2", "F4"])
        #T11M3
        self.T11M3F1 = tile(o = 3, id = ["T11", "M3", "F1"])
        self.T11M3F2 = tile(o = 3, id = ["T11", "M3", "F2"])
        self.T11M3F3 = tile(o = 3, id = ["T11", "M3", "F3"])
        self.T11M3F4 = tile(o = 3, id = ["T11", "M3", "F4"])
        #T11M4
        self.T11M4F1 = tile(o = 3, id = ["T11", "M4", "F1"])
        self.T11M4F2 = tile(o = 3, id = ["T11", "M4", "F2"])
        self.T11M4F3 = tile(o = 3, id = ["T11", "M4", "F3"])
        self.T11M4F4 = tile(o = 3, id = ["T11", "M4", "F4"])

        #T12M1
        self.T12M1F1 = tile(o = 3, id = ["T12", "M1", "F1"])
        self.T12M1F2 = tile(o = 3, id = ["T12", "M1", "F2"])
        self.T12M1F3 = tile(o = 3, id = ["T12", "M1", "F3"])
        self.T12M1F4 = tile(o = 3, id = ["T12", "M1", "F4"])
        #T12M2
        self.T12M2F1 = tile(o = 3, id = ["T12", "M2", "F1"])
        self.T12M2F2 = tile(o = 3, id = ["T12", "M2", "F2"])
        self.T12M2F3 = tile(o = 3, id = ["T12", "M2", "F3"])
        self.T12M2F4 = tile(o = 3, id = ["T12", "M2", "F4"])
        #T12M3
        self.T12M3F1 = tile(o = 3, id = ["T12", "M3", "F1"])
        self.T12M3F2 = tile(o = 3, id = ["T12", "M3", "F2"])
        self.T12M3F3 = tile(o = 3, id = ["T12", "M3", "F3"])
        self.T12M3F4 = tile(o = 3, id = ["T12", "M3", "F4"])
        #T12M4
        self.T12M4F1 = tile(o = 3, id = ["T12", "M4", "F1"])
        self.T12M4F2 = tile(o = 3, id = ["T12", "M4", "F2"])
        self.T12M4F3 = tile(o = 3, id = ["T12", "M4", "F3"])
        self.T12M4F4 = tile(o = 3, id = ["T12", "M4", "F4"])

        #T13M1
        self.T13M1F1 = tile(o = 4, id = ["T13", "M1", "F1"])
        self.T13M1F2 = tile(o = 4, id = ["T13", "M1", "F2"])
        self.T13M1F3 = tile(o = 4, id = ["T13", "M1", "F3"])
        self.T13M1F4 = tile(o = 4, id = ["T13", "M1", "F4"])
        #T13M2
        self.T13M2F1 = tile(o = 4, id = ["T13", "M2", "F1"])
        self.T13M2F2 = tile(o = 4, id = ["T13", "M2", "F2"])
        self.T13M2F3 = tile(o = 4, id = ["T13", "M2", "F3"])
        self.T13M2F4 = tile(o = 4, id = ["T13", "M2", "F4"])
        #T13M3
        self.T13M3F1 = tile(o = 4, id = ["T13", "M3", "F1"])
        self.T13M3F2 = tile(o = 4, id = ["T13", "M3", "F2"])
        self.T13M3F3 = tile(o = 4, id = ["T13", "M3", "F3"])
        self.T13M3F4 = tile(o = 4, id = ["T13", "M3", "F4"])
        #T13M4
        self.T13M4F1 = tile(o = 4, id = ["T13", "M4", "F1"])
        self.T13M4F2 = tile(o = 4, id = ["T13", "M4", "F2"])
        self.T13M4F3 = tile(o = 4, id = ["T13", "M4", "F3"])
        self.T13M4F4 = tile(o = 4, id = ["T13", "M4", "F4"])

        #T14M1
        self.T14M1F1 = tile(o = 4, id = ["T14", "M1", "F1"])
        self.T14M1F2 = tile(o = 4, id = ["T14", "M1", "F2"])
        self.T14M1F3 = tile(o = 4, id = ["T14", "M1", "F3"])
        self.T14M1F4 = tile(o = 4, id = ["T14", "M1", "F4"])
        #T14M2
        self.T14M2F1 = tile(o = 4, id = ["T14", "M2", "F1"])
        self.T14M2F2 = tile(o = 4, id = ["T14", "M2", "F2"])
        self.T14M2F3 = tile(o = 4, id = ["T14", "M2", "F3"])
        self.T14M2F4 = tile(o = 4, id = ["T14", "M2", "F4"])
        #T14M3
        self.T14M3F1 = tile(o = 4, id = ["T14", "M3", "F1"])
        self.T14M3F2 = tile(o = 4, id = ["T14", "M3", "F2"])
        self.T14M3F3 = tile(o = 4, id = ["T14", "M3", "F3"])
        self.T14M3F4 = tile(o = 4, id = ["T14", "M3", "F4"])
        #T14M4
        self.T14M4F1 = tile(o = 4, id = ["T14", "M4", "F1"])
        self.T14M4F2 = tile(o = 4, id = ["T14", "M4", "F2"])
        self.T14M4F3 = tile(o = 4, id = ["T14", "M4", "F3"])
        self.T14M4F4 = tile(o = 4, id = ["T14", "M4", "F4"])

        #T15M1
        self.T15M1F1 = tile(o = 4, id = ["T15", "M1", "F1"])
        self.T15M1F2 = tile(o = 4, id = ["T15", "M1", "F2"])
        self.T15M1F3 = tile(o = 4, id = ["T15", "M1", "F3"])
        self.T15M1F4 = tile(o = 4, id = ["T15", "M1", "F4"])
        #T15M2
        self.T15M2F1 = tile(o = 4, id = ["T15", "M2", "F1"])
        self.T15M2F2 = tile(o = 4, id = ["T15", "M2", "F2"])
        self.T15M2F3 = tile(o = 4, id = ["T15", "M2", "F3"])
        self.T15M2F4 = tile(o = 4, id = ["T15", "M2", "F4"])
        #T15M3
        self.T15M3F1 = tile(o = 4, id = ["T15", "M3", "F1"])
        self.T15M3F2 = tile(o = 4, id = ["T15", "M3", "F2"])
        self.T15M3F3 = tile(o = 4, id = ["T15", "M3", "F3"])
        self.T15M3F4 = tile(o = 4, id = ["T15", "M3", "F4"])
        #T15M4
        self.T15M4F1 = tile(o = 4, id = ["T15", "M4", "F1"])
        self.T15M4F2 = tile(o = 4, id = ["T15", "M4", "F2"])
        self.T15M4F3 = tile(o = 4, id = ["T15", "M4", "F3"])
        self.T15M4F4 = tile(o = 4, id = ["T15", "M4", "F4"])

        #T16M1
        self.T16M1F1 = tile(o = 4, id = ["T16", "M1", "F1"])
        self.T16M1F2 = tile(o = 4, id = ["T16", "M1", "F2"])
        self.T16M1F3 = tile(o = 4, id = ["T16", "M1", "F3"])
        self.T16M1F4 = tile(o = 4, id = ["T16", "M1", "F4"])
        #T16M2
        self.T16M2F1 = tile(o = 4, id = ["T16", "M2", "F1"])
        self.T16M2F2 = tile(o = 4, id = ["T16", "M2", "F2"])
        self.T16M2F3 = tile(o = 4, id = ["T16", "M2", "F3"])
        self.T16M2F4 = tile(o = 4, id = ["T16", "M2", "F4"])
        #T16M3
        self.T16M3F1 = tile(o = 4, id = ["T16", "M3", "F1"])
        self.T16M3F2 = tile(o = 4, id = ["T16", "M3", "F2"])
        self.T16M3F3 = tile(o = 4, id = ["T16", "M3", "F3"])
        self.T16M3F4 = tile(o = 4, id = ["T16", "M3", "F4"])
        #T16M4
        self.T16M4F1 = tile(o = 4, id = ["T16", "M4", "F1"])
        self.T16M4F2 = tile(o = 4, id = ["T16", "M4", "F2"])
        self.T16M4F3 = tile(o = 4, id = ["T16", "M4", "F3"])
        self.T16M4F4 = tile(o = 4, id = ["T16", "M4", "F4"])
        #%end%-------------------------------------------------------------------%end%#


    def click(self, level = 1):
        """this func check if the player/user clicked one of the tiles, the check is for all the tiles_xy

        Args:
            level (int, optional): the level that you checking on. Defaults to 1.
        """    
        #############T1#############
        #M1
        self.T1M1F1.click(level = level)
        self.T1M1F2.click(level = level)
        self.T1M1F3.click(level = level)
        self.T1M1F4.click(level = level)
        #M2
        self.T1M2F1.click(level = level)
        self.T1M2F2.click(level = level)
        self.T1M2F3.click(level = level)
        self.T1M2F4.click(level = level)
        #M3
        self.T1M3F1.click(level = level)
        self.T1M3F2.click(level = level)
        self.T1M3F3.click(level = level)
        self.T1M3F4.click(level = level)
        #M4
        self.T1M4F1.click(level = level)
        self.T1M4F2.click(level = level)
        self.T1M4F3.click(level = level)
        self.T1M4F4.click(level = level)
        #############T2#############
        #M1
        self.T2M1F1.click(level = level)
        self.T2M1F2.click(level = level)
        self.T2M1F3.click(level = level)
        self.T2M1F4.click(level = level)
        #M2
        self.T2M2F1.click(level = level)
        self.T2M2F2.click(level = level)
        self.T2M2F3.click(level = level)
        self.T2M2F4.click(level = level)
        #M3
        self.T2M3F1.click(level = level)
        self.T2M3F2.click(level = level)
        self.T2M3F3.click(level = level)
        self.T2M3F4.click(level = level)
        #M4
        self.T2M4F1.click(level = level)
        self.T2M4F2.click(level = level)
        self.T2M4F3.click(level = level)
        self.T2M4F4.click(level = level)

        #############T3#############
        #M1
        self.T3M1F1.click(level = level)
        self.T3M1F2.click(level = level)
        self.T3M1F3.click(level = level)
        self.T3M1F4.click(level = level)
        #M2
        self.T3M2F1.click(level = level)
        self.T3M2F2.click(level = level)
        self.T3M2F3.click(level = level)
        self.T3M2F4.click(level = level)
        #M3
        self.T3M3F1.click(level = level)
        self.T3M3F2.click(level = level)
        self.T3M3F3.click(level = level)
        self.T3M3F4.click(level = level)
        #M4
        self.T3M4F1.click(level = level)
        self.T3M4F2.click(level = level)
        self.T3M4F3.click(level = level)
        self.T3M4F4.click(level = level)
        #############T4#############
        #M1
        self.T4M1F1.click(level = level)
        self.T4M1F2.click(level = level)
        self.T4M1F3.click(level = level)
        self.T4M1F4.click(level = level)
        #M2
        self.T4M2F1.click(level = level)
        self.T4M2F2.click(level = level)
        self.T4M2F3.click(level = level)
        self.T4M2F4.click(level = level)
        #M3
        self.T4M3F1.click(level = level)
        self.T4M3F2.click(level = level)
        self.T4M3F3.click(level = level)
        self.T4M3F4.click(level = level)
        #M4
        self.T4M4F1.click(level = level)
        self.T4M4F2.click(level = level)
        self.T4M4F3.click(level = level)
        self.T4M4F4.click(level = level)
        #############T5#############
        #M1
        self.T5M1F1.click(level = level)
        self.T5M1F2.click(level = level)
        self.T5M1F3.click(level = level)
        self.T5M1F4.click(level = level)
        #M2
        self.T5M2F1.click(level = level)
        self.T5M2F2.click(level = level)
        self.T5M2F3.click(level = level)
        self.T5M2F4.click(level = level)
        #M3
        self.T5M3F1.click(level = level)
        self.T5M3F2.click(level = level)
        self.T5M3F3.click(level = level)
        self.T5M3F4.click(level = level)
        #M4
        self.T5M4F1.click(level = level)
        self.T5M4F2.click(level = level)
        self.T5M4F3.click(level = level)
        self.T5M4F4.click(level = level)

        #############T6#############
        #M1
        self.T6M1F1.click(level = level)
        self.T6M1F2.click(level = level)
        self.T6M1F3.click(level = level)
        self.T6M1F4.click(level = level)
        #M2
        self.T6M2F1.click(level = level)
        self.T6M2F2.click(level = level)
        self.T6M2F3.click(level = level)
        self.T6M2F4.click(level = level)
        #M3
        self.T6M3F1.click(level = level)
        self.T6M3F2.click(level = level)
        self.T6M3F3.click(level = level)
        self.T6M3F4.click(level = level)
        #M4
        self.T6M4F1.click(level = level)
        self.T6M4F2.click(level = level)
        self.T6M4F3.click(level = level)
        self.T6M4F4.click(level = level)
        #############T7#############
        #M1
        self.T7M1F1.click(level = level)
        self.T7M1F2.click(level = level)
        self.T7M1F3.click(level = level)
        self.T7M1F4.click(level = level)
        #M2
        self.T7M2F1.click(level = level)
        self.T7M2F2.click(level = level)
        self.T7M2F3.click(level = level)
        self.T7M2F4.click(level = level)
        #M3
        self.T7M3F1.click(level = level)
        self.T7M3F2.click(level = level)
        self.T7M3F3.click(level = level)
        self.T7M3F4.click(level = level)
        #M4
        self.T7M4F1.click(level = level)
        self.T7M4F2.click(level = level)
        self.T7M4F3.click(level = level)
        self.T7M4F4.click(level = level)
        #############T8#############
        #M1
        self.T8M1F1.click(level = level)
        self.T8M1F2.click(level = level)
        self.T8M1F3.click(level = level)
        self.T8M1F4.click(level = level)
        #M2
        self.T8M2F1.click(level = level)
        self.T8M2F2.click(level = level)
        self.T8M2F3.click(level = level)
        self.T8M2F4.click(level = level)
        #M3
        self.T8M3F1.click(level = level)
        self.T8M3F2.click(level = level)
        self.T8M3F3.click(level = level)
        self.T8M3F4.click(level = level)
        #M4
        self.T8M4F1.click(level = level)
        self.T8M4F2.click(level = level)
        self.T8M4F3.click(level = level)
        self.T8M4F4.click(level = level)
        #############T9#############
        #M1
        self.T9M1F1.click(level = level)
        self.T9M1F2.click(level = level)
        self.T9M1F3.click(level = level)
        self.T9M1F4.click(level = level)
        #M2
        self.T9M2F1.click(level = level)
        self.T9M2F2.click(level = level)
        self.T9M2F3.click(level = level)
        self.T9M2F4.click(level = level)
        #M3
        self.T9M3F1.click(level = level)
        self.T9M3F2.click(level = level)
        self.T9M3F3.click(level = level)
        self.T9M3F4.click(level = level)
        #M4
        self.T9M4F1.click(level = level)
        self.T9M4F2.click(level = level)
        self.T9M4F3.click(level = level)
        self.T9M4F4.click(level = level)
        #############T10#############
        #M1
        self.T10M1F1.click(level = level)
        self.T10M1F2.click(level = level)
        self.T10M1F3.click(level = level)
        self.T10M1F4.click(level = level)
        #M2
        self.T10M2F1.click(level = level)
        self.T10M2F2.click(level = level)
        self.T10M2F3.click(level = level)
        self.T10M2F4.click(level = level)
        #M3
        self.T10M3F1.click(level = level)
        self.T10M3F2.click(level = level)
        self.T10M3F3.click(level = level)
        self.T10M3F4.click(level = level)
        #M4
        self.T10M4F1.click(level = level)
        self.T10M4F2.click(level = level)
        self.T10M4F3.click(level = level)
        self.T10M4F4.click(level = level)
        #############T11#############
        #M1
        self.T11M1F1.click(level = level)
        self.T11M1F2.click(level = level)
        self.T11M1F3.click(level = level)
        self.T11M1F4.click(level = level)
        #M2
        self.T11M2F1.click(level = level)
        self.T11M2F2.click(level = level)
        self.T11M2F3.click(level = level)
        self.T11M2F4.click(level = level)
        #M3
        self.T11M3F1.click(level = level)
        self.T11M3F2.click(level = level)
        self.T11M3F3.click(level = level)
        self.T11M3F4.click(level = level)
        #M4
        self.T11M4F1.click(level = level)
        self.T11M4F2.click(level = level)
        self.T11M4F3.click(level = level)
        self.T11M4F4.click(level = level)
        #############T12#############
        #M1
        self.T12M1F1.click(level = level)
        self.T12M1F2.click(level = level)
        self.T12M1F3.click(level = level)
        self.T12M1F4.click(level = level)
        #M2
        self.T12M2F1.click(level = level)
        self.T12M2F2.click(level = level)
        self.T12M2F3.click(level = level)
        self.T12M2F4.click(level = level)
        #M3
        self.T12M3F1.click(level = level)
        self.T12M3F2.click(level = level)
        self.T12M3F3.click(level = level)
        self.T12M3F4.click(level = level)
        #M4
        self.T12M4F1.click(level = level)
        self.T12M4F2.click(level = level)
        self.T12M4F3.click(level = level)
        self.T12M4F4.click(level = level)
        #############T13#############
        #M1
        self.T13M1F1.click(level = level)
        self.T13M1F2.click(level = level)
        self.T13M1F3.click(level = level)
        self.T13M1F4.click(level = level)
        #M2
        self.T13M2F1.click(level = level)
        self.T13M2F2.click(level = level)
        self.T13M2F3.click(level = level)
        self.T13M2F4.click(level = level)
        #M3
        self.T13M3F1.click(level = level)
        self.T13M3F2.click(level = level)
        self.T13M3F3.click(level = level)
        self.T13M3F4.click(level = level)
        #M4
        self.T13M4F1.click(level = level)
        self.T13M4F2.click(level = level)
        self.T13M4F3.click(level = level)
        self.T13M4F4.click(level = level)
        #############T14#############
        #M1
        self.T14M1F1.click(level = level)
        self.T14M1F2.click(level = level)
        self.T14M1F3.click(level = level)
        self.T14M1F4.click(level = level)
        #M2
        self.T14M2F1.click(level = level)
        self.T14M2F2.click(level = level)
        self.T14M2F3.click(level = level)
        self.T14M2F4.click(level = level)
        #M3
        self.T14M3F1.click(level = level)
        self.T14M3F2.click(level = level)
        self.T14M3F3.click(level = level)
        self.T14M3F4.click(level = level)
        #M4
        self.T14M4F1.click(level = level)
        self.T14M4F2.click(level = level)
        self.T14M4F3.click(level = level)
        self.T14M4F4.click(level = level)
        #############T15#############
        #M1
        self.T15M1F1.click(level = level)
        self.T15M1F2.click(level = level)
        self.T15M1F3.click(level = level)
        self.T15M1F4.click(level = level)
        #M2
        self.T15M2F1.click(level = level)
        self.T15M2F2.click(level = level)
        self.T15M2F3.click(level = level)
        self.T15M2F4.click(level = level)
        #M3
        self.T15M3F1.click(level = level)
        self.T15M3F2.click(level = level)
        self.T15M3F3.click(level = level)
        self.T15M3F4.click(level = level)
        #M4
        self.T15M4F1.click(level = level)
        self.T15M4F2.click(level = level)
        self.T15M4F3.click(level = level)
        self.T15M4F4.click(level = level)
        #############T16#############
        #M1
        self.T16M1F1.click(level = level)
        self.T16M1F2.click(level = level)
        self.T16M1F3.click(level = level)
        self.T16M1F4.click(level = level)
        #M2
        self.T16M2F1.click(level = level)
        self.T16M2F2.click(level = level)
        self.T16M2F3.click(level = level)
        self.T16M2F4.click(level = level)
        #M3
        self.T16M3F1.click(level = level)
        self.T16M3F2.click(level = level)
        self.T16M3F3.click(level = level)
        self.T16M3F4.click(level = level)
        #M4
        self.T16M4F1.click(level = level)
        self.T16M4F2.click(level = level)
        self.T16M4F3.click(level = level)
        self.T16M4F4.click(level = level)
    #%end%-------------------------------------------------------------------%end%#


    def update(self, lvl = 1):
        self.change_x_and_y()
        #############T1#############
        #M1
        self.T1M1F1.update(lvl)
        self.T1M1F2.update(lvl)
        self.T1M1F3.update(lvl)
        self.T1M1F4.update(lvl)
        #M2
        self.T1M2F1.update(lvl)
        self.T1M2F2.update(lvl)
        self.T1M2F3.update(lvl)
        self.T1M2F4.update(lvl)
        #M3
        self.T1M3F1.update(lvl)
        self.T1M3F2.update(lvl)
        self.T1M3F3.update(lvl)
        self.T1M3F4.update(lvl)
        #M4
        self.T1M4F1.update(lvl)
        self.T1M4F2.update(lvl)
        self.T1M4F3.update(lvl)
        self.T1M4F4.update(lvl)
        #############T2#############
        #M1
        self.T2M1F1.update(lvl)
        self.T2M1F2.update(lvl)
        self.T2M1F3.update(lvl)
        self.T2M1F4.update(lvl)
        #M2
        self.T2M2F1.update(lvl)
        self.T2M2F2.update(lvl)
        self.T2M2F3.update(lvl)
        self.T2M2F4.update(lvl)
        #M3
        self.T2M3F1.update(lvl)
        self.T2M3F2.update(lvl)
        self.T2M3F3.update(lvl)
        self.T2M3F4.update(lvl)
        #M4
        self.T2M4F1.update(lvl)
        self.T2M4F2.update(lvl)
        self.T2M4F3.update(lvl)
        self.T2M4F4.update(lvl)

        #############T3#############
        #M1
        self.T3M1F1.update(lvl)
        self.T3M1F2.update(lvl)
        self.T3M1F3.update(lvl)
        self.T3M1F4.update(lvl)
        #M2
        self.T3M2F1.update(lvl)
        self.T3M2F2.update(lvl)
        self.T3M2F3.update(lvl)
        self.T3M2F4.update(lvl)
        #M3
        self.T3M3F1.update(lvl)
        self.T3M3F2.update(lvl)
        self.T3M3F3.update(lvl)
        self.T3M3F4.update(lvl)
        #M4
        self.T3M4F1.update(lvl)
        self.T3M4F2.update(lvl)
        self.T3M4F3.update(lvl)
        self.T3M4F4.update(lvl)
        #############T4#############
        #M1
        self.T4M1F1.update(lvl)
        self.T4M1F2.update(lvl)
        self.T4M1F3.update(lvl)
        self.T4M1F4.update(lvl)
        #M2
        self.T4M2F1.update(lvl)
        self.T4M2F2.update(lvl)
        self.T4M2F3.update(lvl)
        self.T4M2F4.update(lvl)
        #M3
        self.T4M3F1.update(lvl)
        self.T4M3F2.update(lvl)
        self.T4M3F3.update(lvl)
        self.T4M3F4.update(lvl)
        #M4
        self.T4M4F1.update(lvl)
        self.T4M4F2.update(lvl)
        self.T4M4F3.update(lvl)
        self.T4M4F4.update(lvl)
        #############T5#############
        #M1
        self.T5M1F1.update(lvl)
        self.T5M1F2.update(lvl)
        self.T5M1F3.update(lvl)
        self.T5M1F4.update(lvl)
        #M2
        self.T5M2F1.update(lvl)
        self.T5M2F2.update(lvl)
        self.T5M2F3.update(lvl)
        self.T5M2F4.update(lvl)
        #M3
        self.T5M3F1.update(lvl)
        self.T5M3F2.update(lvl)
        self.T5M3F3.update(lvl)
        self.T5M3F4.update(lvl)
        #M4
        self.T5M4F1.update(lvl)
        self.T5M4F2.update(lvl)
        self.T5M4F3.update(lvl)
        self.T5M4F4.update(lvl)

        #############T6#############
        #M1
        self.T6M1F1.update(lvl)
        self.T6M1F2.update(lvl)
        self.T6M1F3.update(lvl)
        self.T6M1F4.update(lvl)
        #M2
        self.T6M2F1.update(lvl)
        self.T6M2F2.update(lvl)
        self.T6M2F3.update(lvl)
        self.T6M2F4.update(lvl)
        #M3
        self.T6M3F1.update(lvl)
        self.T6M3F2.update(lvl)
        self.T6M3F3.update(lvl)
        self.T6M3F4.update(lvl)
        #M4
        self.T6M4F1.update(lvl)
        self.T6M4F2.update(lvl)
        self.T6M4F3.update(lvl)
        self.T6M4F4.update(lvl)
        #############T7#############
        #M1
        self.T7M1F1.update(lvl)
        self.T7M1F2.update(lvl)
        self.T7M1F3.update(lvl)
        self.T7M1F4.update(lvl)
        #M2
        self.T7M2F1.update(lvl)
        self.T7M2F2.update(lvl)
        self.T7M2F3.update(lvl)
        self.T7M2F4.update(lvl)
        #M3
        self.T7M3F1.update(lvl)
        self.T7M3F2.update(lvl)
        self.T7M3F3.update(lvl)
        self.T7M3F4.update(lvl)
        #M4
        self.T7M4F1.update(lvl)
        self.T7M4F2.update(lvl)
        self.T7M4F3.update(lvl)
        self.T7M4F4.update(lvl)
        #############T8#############
        #M1
        self.T8M1F1.update(lvl)
        self.T8M1F2.update(lvl)
        self.T8M1F3.update(lvl)
        self.T8M1F4.update(lvl)
        #M2
        self.T8M2F1.update(lvl)
        self.T8M2F2.update(lvl)
        self.T8M2F3.update(lvl)
        self.T8M2F4.update(lvl)
        #M3
        self.T8M3F1.update(lvl)
        self.T8M3F2.update(lvl)
        self.T8M3F3.update(lvl)
        self.T8M3F4.update(lvl)
        #M4
        self.T8M4F1.update(lvl)
        self.T8M4F2.update(lvl)
        self.T8M4F3.update(lvl)
        self.T8M4F4.update(lvl)
        #############T9#############
        #M1
        self.T9M1F1.update(lvl)
        self.T9M1F2.update(lvl)
        self.T9M1F3.update(lvl)
        self.T9M1F4.update(lvl)
        #M2
        self.T9M2F1.update(lvl)
        self.T9M2F2.update(lvl)
        self.T9M2F3.update(lvl)
        self.T9M2F4.update(lvl)
        #M3
        self.T9M3F1.update(lvl)
        self.T9M3F2.update(lvl)
        self.T9M3F3.update(lvl)
        self.T9M3F4.update(lvl)
        #M4
        self.T9M4F1.update(lvl)
        self.T9M4F2.update(lvl)
        self.T9M4F3.update(lvl)
        self.T9M4F4.update(lvl)
        #############T10#############
        #M1
        self.T10M1F1.update(lvl)
        self.T10M1F2.update(lvl)
        self.T10M1F3.update(lvl)
        self.T10M1F4.update(lvl)
        #M2
        self.T10M2F1.update(lvl)
        self.T10M2F2.update(lvl)
        self.T10M2F3.update(lvl)
        self.T10M2F4.update(lvl)
        #M3
        self.T10M3F1.update(lvl)
        self.T10M3F2.update(lvl)
        self.T10M3F3.update(lvl)
        self.T10M3F4.update(lvl)
        #M4
        self.T10M4F1.update(lvl)
        self.T10M4F2.update(lvl)
        self.T10M4F3.update(lvl)
        self.T10M4F4.update(lvl)
        #############T11#############
        #M1
        self.T11M1F1.update(lvl)
        self.T11M1F2.update(lvl)
        self.T11M1F3.update(lvl)
        self.T11M1F4.update(lvl)
        #M2
        self.T11M2F1.update(lvl)
        self.T11M2F2.update(lvl)
        self.T11M2F3.update(lvl)
        self.T11M2F4.update(lvl)
        #M3
        self.T11M3F1.update(lvl)
        self.T11M3F2.update(lvl)
        self.T11M3F3.update(lvl)
        self.T11M3F4.update(lvl)
        #M4
        self.T11M4F1.update(lvl)
        self.T11M4F2.update(lvl)
        self.T11M4F3.update(lvl)
        self.T11M4F4.update(lvl)
        #############T12#############
        #M1
        self.T12M1F1.update(lvl)
        self.T12M1F2.update(lvl)
        self.T12M1F3.update(lvl)
        self.T12M1F4.update(lvl)
        #M2
        self.T12M2F1.update(lvl)
        self.T12M2F2.update(lvl)
        self.T12M2F3.update(lvl)
        self.T12M2F4.update(lvl)
        #M3
        self.T12M3F1.update(lvl)
        self.T12M3F2.update(lvl)
        self.T12M3F3.update(lvl)
        self.T12M3F4.update(lvl)
        #M4
        self.T12M4F1.update(lvl)
        self.T12M4F2.update(lvl)
        self.T12M4F3.update(lvl)
        self.T12M4F4.update(lvl)
        #############T13#############
        #M1
        self.T13M1F1.update(lvl)
        self.T13M1F2.update(lvl)
        self.T13M1F3.update(lvl)
        self.T13M1F4.update(lvl)
        #M2
        self.T13M2F1.update(lvl)
        self.T13M2F2.update(lvl)
        self.T13M2F3.update(lvl)
        self.T13M2F4.update(lvl)
        #M3
        self.T13M3F1.update(lvl)
        self.T13M3F2.update(lvl)
        self.T13M3F3.update(lvl)
        self.T13M3F4.update(lvl)
        #M4
        self.T13M4F1.update(lvl)
        self.T13M4F2.update(lvl)
        self.T13M4F3.update(lvl)
        self.T13M4F4.update(lvl)
        #############T14#############
        #M1
        self.T14M1F1.update(lvl)
        self.T14M1F2.update(lvl)
        self.T14M1F3.update(lvl)
        self.T14M1F4.update(lvl)
        #M2
        self.T14M2F1.update(lvl)
        self.T14M2F2.update(lvl)
        self.T14M2F3.update(lvl)
        self.T14M2F4.update(lvl)
        #M3
        self.T14M3F1.update(lvl)
        self.T14M3F2.update(lvl)
        self.T14M3F3.update(lvl)
        self.T14M3F4.update(lvl)
        #M4
        self.T14M4F1.update(lvl)
        self.T14M4F2.update(lvl)
        self.T14M4F3.update(lvl)
        self.T14M4F4.update(lvl)
        #############T15#############
        #M1
        self.T15M1F1.update(lvl)
        self.T15M1F2.update(lvl)
        self.T15M1F3.update(lvl)
        self.T15M1F4.update(lvl)
        #M2
        self.T15M2F1.update(lvl)
        self.T15M2F2.update(lvl)
        self.T15M2F3.update(lvl)
        self.T15M2F4.update(lvl)
        #M3
        self.T15M3F1.update(lvl)
        self.T15M3F2.update(lvl)
        self.T15M3F3.update(lvl)
        self.T15M3F4.update(lvl)
        #M4
        self.T15M4F1.update(lvl)
        self.T15M4F2.update(lvl)
        self.T15M4F3.update(lvl)
        self.T15M4F4.update(lvl)
        #############T16#############
        #M1
        self.T16M1F1.update(lvl)
        self.T16M1F2.update(lvl)
        self.T16M1F3.update(lvl)
        self.T16M1F4.update(lvl)
        #M2
        self.T16M2F1.update(lvl)
        self.T16M2F2.update(lvl)
        self.T16M2F3.update(lvl)
        self.T16M2F4.update(lvl)
        #M3
        self.T16M3F1.update(lvl)
        self.T16M3F2.update(lvl)
        self.T16M3F3.update(lvl)
        self.T16M3F4.update(lvl)
        #M4
        self.T16M4F1.update(lvl)
        self.T16M4F2.update(lvl)
        self.T16M4F3.update(lvl)
        self.T16M4F4.update(lvl)
    #%end%-------------------------------------------------------------------%end%#
    def change_x_and_y(self):
        self = tiles_xy(self)
    #%end%-------------------------------------------------------------------%end%#

    def load_images(self, lvl = 1):
        #############T1#############
        #M1
        self.T1M1F1.load_images(lvl)
        self.T1M1F2.load_images(lvl)
        self.T1M1F3.load_images(lvl)
        self.T1M1F4.load_images(lvl)
        #M2
        self.T1M2F1.load_images(lvl)
        self.T1M2F2.load_images(lvl)
        self.T1M2F3.load_images(lvl)
        self.T1M2F4.load_images(lvl)
        #M3
        self.T1M3F1.load_images(lvl)
        self.T1M3F2.load_images(lvl)
        self.T1M3F3.load_images(lvl)
        self.T1M3F4.load_images(lvl)
        #M4
        self.T1M4F1.load_images(lvl)
        self.T1M4F2.load_images(lvl)
        self.T1M4F3.load_images(lvl)
        self.T1M4F4.load_images(lvl)

        #############T2#############
        #M1
        self.T2M1F1.load_images(lvl)
        self.T2M1F2.load_images(lvl)
        self.T2M1F3.load_images(lvl)
        self.T2M1F4.load_images(lvl)
        #M2
        self.T2M2F1.load_images(lvl)
        self.T2M2F2.load_images(lvl)
        self.T2M2F3.load_images(lvl)
        self.T2M2F4.load_images(lvl)
        #M3
        self.T2M3F1.load_images(lvl)
        self.T2M3F2.load_images(lvl)
        self.T2M3F3.load_images(lvl)
        self.T2M3F4.load_images(lvl)
        #M4
        self.T2M4F1.load_images(lvl)
        self.T2M4F2.load_images(lvl)
        self.T2M4F3.load_images(lvl)
        self.T2M4F4.load_images(lvl)
        #############T3#############
        #M1
        self.T3M1F1.load_images(lvl)
        self.T3M1F2.load_images(lvl)
        self.T3M1F3.load_images(lvl)
        self.T3M1F4.load_images(lvl)
        #M2
        self.T3M2F1.load_images(lvl)
        self.T3M2F2.load_images(lvl)
        self.T3M2F3.load_images(lvl)
        self.T3M2F4.load_images(lvl)
        #M3
        self.T3M3F1.load_images(lvl)
        self.T3M3F2.load_images(lvl)
        self.T3M3F3.load_images(lvl)
        self.T3M3F4.load_images(lvl)
        #M4
        self.T3M4F1.load_images(lvl)
        self.T3M4F2.load_images(lvl)
        self.T3M4F3.load_images(lvl)
        self.T3M4F4.load_images(lvl)
        #############T4#############
        #M1
        self.T4M1F1.load_images(lvl)
        self.T4M1F2.load_images(lvl)
        self.T4M1F3.load_images(lvl)
        self.T4M1F4.load_images(lvl)
        #M2
        self.T4M2F1.load_images(lvl)
        self.T4M2F2.load_images(lvl)
        self.T4M2F3.load_images(lvl)
        self.T4M2F4.load_images(lvl)
        #M3
        self.T4M3F1.load_images(lvl)
        self.T4M3F2.load_images(lvl)
        self.T4M3F3.load_images(lvl)
        self.T4M3F4.load_images(lvl)
        #M4
        self.T4M4F1.load_images(lvl)
        self.T4M4F2.load_images(lvl)
        self.T4M4F3.load_images(lvl)
        self.T4M4F4.load_images(lvl)
        #############T5#############
        #M1
        self.T5M1F1.load_images(lvl)
        self.T5M1F2.load_images(lvl)
        self.T5M1F3.load_images(lvl)
        self.T5M1F4.load_images(lvl)
        #M2
        self.T5M2F1.load_images(lvl)
        self.T5M2F2.load_images(lvl)
        self.T5M2F3.load_images(lvl)
        self.T5M2F4.load_images(lvl)
        #M3
        self.T5M3F1.load_images(lvl)
        self.T5M3F2.load_images(lvl)
        self.T5M3F3.load_images(lvl)
        self.T5M3F4.load_images(lvl)
        #M4
        self.T5M4F1.load_images(lvl)
        self.T5M4F2.load_images(lvl)
        self.T5M4F3.load_images(lvl)
        self.T5M4F4.load_images(lvl)

        #############T6#############
        #M1
        self.T6M1F1.load_images(lvl)
        self.T6M1F2.load_images(lvl)
        self.T6M1F3.load_images(lvl)
        self.T6M1F4.load_images(lvl)
        #M2
        self.T6M2F1.load_images(lvl)
        self.T6M2F2.load_images(lvl)
        self.T6M2F3.load_images(lvl)
        self.T6M2F4.load_images(lvl)
        #M3
        self.T6M3F1.load_images(lvl)
        self.T6M3F2.load_images(lvl)
        self.T6M3F3.load_images(lvl)
        self.T6M3F4.load_images(lvl)
        #M4
        self.T6M4F1.load_images(lvl)
        self.T6M4F2.load_images(lvl)
        self.T6M4F3.load_images(lvl)
        self.T6M4F4.load_images(lvl)
        #############T7#############
        #M1
        self.T7M1F1.load_images(lvl)
        self.T7M1F2.load_images(lvl)
        self.T7M1F3.load_images(lvl)
        self.T7M1F4.load_images(lvl)
        #M2
        self.T7M2F1.load_images(lvl)
        self.T7M2F2.load_images(lvl)
        self.T7M2F3.load_images(lvl)
        self.T7M2F4.load_images(lvl)
        #M3
        self.T7M3F1.load_images(lvl)
        self.T7M3F2.load_images(lvl)
        self.T7M3F3.load_images(lvl)
        self.T7M3F4.load_images(lvl)
        #M4
        self.T7M4F1.load_images(lvl)
        self.T7M4F2.load_images(lvl)
        self.T7M4F3.load_images(lvl)
        self.T7M4F4.load_images(lvl)
        #############T8#############
        #M1
        self.T8M1F1.load_images(lvl)
        self.T8M1F2.load_images(lvl)
        self.T8M1F3.load_images(lvl)
        self.T8M1F4.load_images(lvl)
        #M2
        self.T8M2F1.load_images(lvl)
        self.T8M2F2.load_images(lvl)
        self.T8M2F3.load_images(lvl)
        self.T8M2F4.load_images(lvl)
        #M3
        self.T8M3F1.load_images(lvl)
        self.T8M3F2.load_images(lvl)
        self.T8M3F3.load_images(lvl)
        self.T8M3F4.load_images(lvl)
        #M4
        self.T8M4F1.load_images(lvl)
        self.T8M4F2.load_images(lvl)
        self.T8M4F3.load_images(lvl)
        self.T8M4F4.load_images(lvl)
        #############T9#############
        #M1
        self.T9M1F1.load_images(lvl)
        self.T9M1F2.load_images(lvl)
        self.T9M1F3.load_images(lvl)
        self.T9M1F4.load_images(lvl)
        #M2
        self.T9M2F1.load_images(lvl)
        self.T9M2F2.load_images(lvl)
        self.T9M2F3.load_images(lvl)
        self.T9M2F4.load_images(lvl)
        #M3
        self.T9M3F1.load_images(lvl)
        self.T9M3F2.load_images(lvl)
        self.T9M3F3.load_images(lvl)
        self.T9M3F4.load_images(lvl)
        #M4
        self.T9M4F1.load_images(lvl)
        self.T9M4F2.load_images(lvl)
        self.T9M4F3.load_images(lvl)
        self.T9M4F4.load_images(lvl)
        #############T10#############
        #M1
        self.T10M1F1.load_images(lvl)
        self.T10M1F2.load_images(lvl)
        self.T10M1F3.load_images(lvl)
        self.T10M1F4.load_images(lvl)
        #M2
        self.T10M2F1.load_images(lvl)
        self.T10M2F2.load_images(lvl)
        self.T10M2F3.load_images(lvl)
        self.T10M2F4.load_images(lvl)
        #M3
        self.T10M3F1.load_images(lvl)
        self.T10M3F2.load_images(lvl)
        self.T10M3F3.load_images(lvl)
        self.T10M3F4.load_images(lvl)
        #M4
        self.T10M4F1.load_images(lvl)
        self.T10M4F2.load_images(lvl)
        self.T10M4F3.load_images(lvl)
        self.T10M4F4.load_images(lvl)
        #############T11#############
        #M1
        self.T11M1F1.load_images(lvl)
        self.T11M1F2.load_images(lvl)
        self.T11M1F3.load_images(lvl)
        self.T11M1F4.load_images(lvl)
        #M2
        self.T11M2F1.load_images(lvl)
        self.T11M2F2.load_images(lvl)
        self.T11M2F3.load_images(lvl)
        self.T11M2F4.load_images(lvl)
        #M3
        self.T11M3F1.load_images(lvl)
        self.T11M3F2.load_images(lvl)
        self.T11M3F3.load_images(lvl)
        self.T11M3F4.load_images(lvl)
        #M4
        self.T11M4F1.load_images(lvl)
        self.T11M4F2.load_images(lvl)
        self.T11M4F3.load_images(lvl)
        self.T11M4F4.load_images(lvl)
        #############T12#############
        #M1
        self.T12M1F1.load_images(lvl)
        self.T12M1F2.load_images(lvl)
        self.T12M1F3.load_images(lvl)
        self.T12M1F4.load_images(lvl)
        #M2
        self.T12M2F1.load_images(lvl)
        self.T12M2F2.load_images(lvl)
        self.T12M2F3.load_images(lvl)
        self.T12M2F4.load_images(lvl)
        #M3
        self.T12M3F1.load_images(lvl)
        self.T12M3F2.load_images(lvl)
        self.T12M3F3.load_images(lvl)
        self.T12M3F4.load_images(lvl)
        #M4
        self.T12M4F1.load_images(lvl)
        self.T12M4F2.load_images(lvl)
        self.T12M4F3.load_images(lvl)
        self.T12M4F4.load_images(lvl)

        #############T13#############
        #M1
        self.T13M1F1.load_images(lvl)
        self.T13M1F2.load_images(lvl)
        self.T13M1F3.load_images(lvl)
        self.T13M1F4.load_images(lvl)
        #M2
        self.T13M2F1.load_images(lvl)
        self.T13M2F2.load_images(lvl)
        self.T13M2F3.load_images(lvl)
        self.T13M2F4.load_images(lvl)
        #M3
        self.T13M3F1.load_images(lvl)
        self.T13M3F2.load_images(lvl)
        self.T13M3F3.load_images(lvl)
        self.T13M3F4.load_images(lvl)
        #M4
        self.T13M4F1.load_images(lvl)
        self.T13M4F2.load_images(lvl)
        self.T13M4F3.load_images(lvl)
        self.T13M4F4.load_images(lvl)
        #############T14#############
        #M1
        self.T14M1F1.load_images(lvl)
        self.T14M1F2.load_images(lvl)
        self.T14M1F3.load_images(lvl)
        self.T14M1F4.load_images(lvl)
        #M2
        self.T14M2F1.load_images(lvl)
        self.T14M2F2.load_images(lvl)
        self.T14M2F3.load_images(lvl)
        self.T14M2F4.load_images(lvl)
        #M3
        self.T14M3F1.load_images(lvl)
        self.T14M3F2.load_images(lvl)
        self.T14M3F3.load_images(lvl)
        self.T14M3F4.load_images(lvl)
        #M4
        self.T14M4F1.load_images(lvl)
        self.T14M4F2.load_images(lvl)
        self.T14M4F3.load_images(lvl)
        self.T14M4F4.load_images(lvl)
        #############T15#############
        #M1
        self.T15M1F1.load_images(lvl)
        self.T15M1F2.load_images(lvl)
        self.T15M1F3.load_images(lvl)
        self.T15M1F4.load_images(lvl)
        #M2
        self.T15M2F1.load_images(lvl)
        self.T15M2F2.load_images(lvl)
        self.T15M2F3.load_images(lvl)
        self.T15M2F4.load_images(lvl)
        #M3
        self.T15M3F1.load_images(lvl)
        self.T15M3F2.load_images(lvl)
        self.T15M3F3.load_images(lvl)
        self.T15M3F4.load_images(lvl)
        #M4
        self.T15M4F1.load_images(lvl)
        self.T15M4F2.load_images(lvl)
        self.T15M4F3.load_images(lvl)
        self.T15M4F4.load_images(lvl)
        #############T16#############
        #M1
        self.T16M1F1.load_images(lvl)
        self.T16M1F2.load_images(lvl)
        self.T16M1F3.load_images(lvl)
        self.T16M1F4.load_images(lvl)
        #M2
        self.T16M2F1.load_images(lvl)
        self.T16M2F2.load_images(lvl)
        self.T16M2F3.load_images(lvl)
        self.T16M2F4.load_images(lvl)
        #M3
        self.T16M3F1.load_images(lvl)
        self.T16M3F2.load_images(lvl)
        self.T16M3F3.load_images(lvl)
        self.T16M3F4.load_images(lvl)
        #M4
        self.T16M4F1.load_images(lvl)
        self.T16M4F2.load_images(lvl)
        self.T16M4F3.load_images(lvl)
        self.T16M4F4.load_images(lvl)
        #%end%-------------------------------------------------------------------%end%#
    
    def rail_init(self, level = 1):
        id = self.click(level = level)

        ##up
        

        ##down


        ##left


        ##right

        #-------------------------------------#
