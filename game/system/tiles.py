import pygame
from . import resize, globals_file as gf, settings, textures
#-----------------------------------------------------------------------------------------------#
class tile:
    def __init__(self, id = ["T1", "M1", "F1"]):
        #900 % 4 % 4 % 4 * 2
        self.w = 14.0625 * 2
        #500 % 4 % 4 % 4 * 2
        self.h = 7.8125 * 2
        self.width = resize.resize_x( #resize
            settings.starting_screen_width,
            self.w,
            gf.screen_width
        )
        self.height = resize.resize_y( #resize
            settings.starting_screen_height,
            self.h,
            gf.screen_height
        )
        self.lvl_before = 0 #lvl
        self.loaded_image = None
        self.id_list = id 
        
        #T1
        if id[0] == "T1":
            #M1
            if id[1] == "M1":
                #F1
                if id[2] == "F1":
                    self.id = "T1M1F1"
                    self.x = 0
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M1F2"
                    self.x = 14.0625 * 2
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M1F3"
                    self.x = 0
                    self.y = 7.8125 * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M1F4"
                    self.x = 14.0625 * 2
                    self.y = 7.8125 * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F4.png"
                            )
                    }
            #M2
            elif id[1] == "M2":
                #F1
                if id[2] == "F1":
                    self.id = "T1M2F1"
                    self.x = 14.0625 * 2 * 2
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M2F2"
                    self.x = 14.0625 * 3 * 2
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M2F3"
                    self.x = 14.0625 * 2 * 2
                    self.y = 7.8125 * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M2F4"
                    self.x = 14.0625 * 3 * 2
                    self.y = 7.8125 * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F4.png"
                            )
                    }
            #M3
            elif id[1] == "M3":
                pass
            #M4
            elif id[1] == "M4":
                pass
        
        elif id[0] == "T2":
            #M1
            if id[1] == "M1":
                pass
            #M2
            elif id[1] == "M2":
                pass
            #M3
            elif id[1] == "M3":
                pass
            #M4
            elif id[1] == "M4":
                pass
        elif id[0] == "T3":
            #M1
            if id[1] == "M1":
                pass
            #M2
            elif id[1] == "M2":
                pass
            #M3
            elif id[1] == "M3":
                pass
            #M4
            elif id[1] == "M4":
                pass
        elif id[0] == "T4":
            #M1
            if id[1] == "M1":
                pass
            #M2
            elif id[1] == "M2":
                pass
            #M3
            elif id[1] == "M3":
                pass
            #M4
            elif id[1] == "M4":
                pass
        #create the rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def load_images(self, lvl = 1):
        if lvl != self.lvl_before:
            self.loaded_image = pygame.image.load(
                self.image[str(lvl)]
            )
            self.lvl_before = lvl

    def update(self, lvl = 1):
        self.width = resize.resize_x(
            settings.starting_screen_width,
            self.w,
            gf.screen_width
        )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            self.h,
            gf.screen_height
        )
        self.change_x_and_y()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.load_images(lvl)
        gf.screen.blit(
            pygame.transform.scale(
                self.loaded_image,
                (self.rect.width, self.rect.height)
            ),
            (self.x, self.y)
        )
    
    def change_x_and_y(self):
        self = resize.change_xy(
            gf.screen_width,
            gf.screen_height,
            gf.width_before,
            gf.height_before,
            self
        )
#-----------------------------------------------------------------------------------------------#
class Tiles:
    def __init__(self):
        self.T1M1F1 = tile()
        self.T1M1F2 = tile(id = ["T1", "M1", "F2"])
        self.T1M1F3 = tile(id = ["T1", "M1", "F3"])
        self.T1M1F4 = tile(id = ["T1", "M1", "F4"])
        self.T1M2F1 = tile(id = ["T1", "M2", "F1"])
        self.T1M2F2 = tile(id = ["T1", "M2", "F2"])
        self.T1M2F3 = tile(id = ["T1", "M2", "F3"])
        self.T1M2F4 = tile(id = ["T1", "M2", "F4"])
    
    def update(self, lvl = 1):
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

    def change_x_and_y(self):
        #############T1#############
        #M1
        self.T1M1F1.change_x_and_y()
        self.T1M1F2.change_x_and_y()
        self.T1M1F3.change_x_and_y()
        self.T1M1F4.change_x_and_y()
        #M2
        self.T1M2F1.change_x_and_y()
        self.T1M2F2.change_x_and_y()
        self.T1M2F3.change_x_and_y()
        self.T1M2F4.change_x_and_y()
        #M3
    
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