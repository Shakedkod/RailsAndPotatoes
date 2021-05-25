import pygame
from . import resize, globals_file as gf, settings, textures
#-----------------------------------------------------------------------------------------------#
class tile:
    def __init__(self, id = ["T1", "M1", "F1"]):
        #900 % 4 % 4 % 4 * 2
        self.w = 14.0625 * 2
        #500 % 4 % 4 % 4 * 2
        self.h = 7.8125 * 2
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
        self.lvl_before = 0
        self.loaded_image = None
        self.id_list = id
        if id[0] == "T1":
            if id[1] == "M1":
                if id[2] == "F1":
                    self.id = "T1M1F1"
                    self.x = 0
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F1.png"
                            )
                    }
                elif id[2] == "F2":
                    self.id = "T1M1F2"
                    self.x = 14.0625
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F2.png"
                            )
                    }
                elif id[2] == "F3":
                    self.id = "T1M1F3"
                    self.x = 0
                    self.y = 7.8125
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F3.png"
                            )
                    }
                elif id[2] == "F4":
                    self.id = "T1M1F4"
                    self.x = 14.0625
                    self.y = 7.8125
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M1F4.png"
                            )
                    }
            elif id[1] == "M2":
                if id[2] == "F1":
                    self.id = "T1M2F1"
                    self.x = 0
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F1.png"
                            )
                    }
                elif id[2] == "F2":
                    self.id = "T1M2F2"
                    self.x = 14.0625
                    self.y = 0
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F2.png"
                            )
                    }
                elif id[2] == "F3":
                    self.id = "T1M2F3"
                    self.x = 0
                    self.y = 7.8125
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F3.png"
                            )
                    }
                elif id[2] == "F4":
                    self.id = "T1M2F4"
                    self.x = 14.0625
                    self.y = 7.8125
                    self.image = {
                        "1": textures.change_texture(
                            foldername = "tiles\\lvl1", filename = "T1M2F4.png"
                            )
                    }
            elif id[1] == "M3":
                pass
            elif id[1] == "M4":
                pass
        elif id[0] == "T2":
            if id[1] == "M1":
                pass
            elif id[1] == "M2":
                pass
            elif id[1] == "M3":
                pass
            elif id[1] == "M4":
                pass
        elif id[0] == "T3":
            if id[1] == "M1":
                pass
            elif id[1] == "M2":
                pass
            elif id[1] == "M3":
                pass
            elif id[1] == "M4":
                pass
        elif id[0] == "T4":
            if id[1] == "M1":
                pass
            elif id[1] == "M2":
                pass
            elif id[1] == "M3":
                pass
            elif id[1] == "M4":
                pass
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
    
    def update(self, lvl = 1):
        self.T1M1F1.update(lvl)

    def change_x_and_y(self):
        self.T1M1F1.change_x_and_y()
    
    def load_images(self, lvl = 1):
        self.T1M1F1.load_images(lvl)