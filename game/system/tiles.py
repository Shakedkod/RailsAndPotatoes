import pygame
from . import resize, globals_file as gf, settings, textures
#-----------------------------------------------------------------------------------------------#
class tile:
    def __init__(self, id = ["T1", "M1", "F1"]):
        #900 % 4 % 4 % 4
        self.w = 14.0625 * 2
        #500 % 4 % 4 % 4
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
                    self.x = self.w * 0
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M1F2"
                    self.x = self.w * 1
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M1F3"
                    self.x = self.w * 0
                    self.y = self.h * 1
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M1F4"
                    self.x = self.w * 1
                    self.y = self.h * 1
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
                    self.x = self.w * 2
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M2F2"
                    self.x = self.w * 3
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M2F3"
                    self.x = self.w * 2
                    self.y = self.h * 1
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M2F4"
                    self.x = self.w * 3
                    self.y = self.h * 1
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F4.png"
                            )
                    }
            
            
            #M3
            elif id[1] == "M3":
                #F1
                if id[2] == "F1":
                    self.id = "T1M3F1"
                    self.x = self.w * 0
                    self.y = self.h * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M3F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M3F2"
                    self.x = self.w * 1
                    self.y = self.h * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M3F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M3F3"
                    self.x = self.w * 0
                    self.y = self.h * 3
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M3F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M3F4"
                    self.x = self.w * 1
                    self.y = self.h * 3
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M3F4.png"
                            )
                    }
            
            
            #M4
            elif id[1] == "M4":
                #F1
                if id[2] == "F1":
                    self.id = "T1M4F1"
                    self.x = self.w * 2
                    self.y = self.h * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M4F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T1M4F2"
                    self.x = self.w * 3
                    self.y = self.h * 2
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M4F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T1M4F3"
                    self.x = self.w * 2
                    self.y = self.h * 3
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M4F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T1M4F4"
                    self.x = self.w * 3
                    self.y = self.h * 3
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M4F4.png"
                            )
                    }
        
        elif id[0] == "T2":
            #M1
            if id[1] == "M1":
                #F1
                if id[2] == "F1":
                    self.id = "T2M1F1"
                    self.x = self.w * 4
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T2M1F1.png"
                            )
                    }
                #F2
                elif id[2] == "F2":
                    self.id = "T2M1F2"
                    self.x = self.w * 5
                    self.y = self.h * 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T2M1F2.png"
                            )
                    }
                #F3
                elif id[2] == "F3":
                    self.id = "T2M1F3"
                    self.x = self.w * 4
                    self.y = self.h * 1
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T2M1F3.png"
                            )
                    }
                #F4
                elif id[2] == "F4":
                    self.id = "T2M1F4"
                    self.x = self.w * 5
                    self.y = self.h * 1
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T2M1F4.png"
                            )
                    }
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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.load_images(lvl)
        gf.screen.blit(
            pygame.transform.scale(
                self.loaded_image,
                (self.rect.width, self.rect.height)
            ),
            (self.x, self.y)
        )
#-----------------------------------------------------------------------------------------------#
class Tiles:
    def __init__(self):
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

    def change_x_and_y(self):
        self = resize.tiles_xy(self)
    
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