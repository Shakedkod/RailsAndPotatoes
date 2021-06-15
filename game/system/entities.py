import pygame
from pygame.locals import *
from . import resize, globals_file as gf, settings, textures
#-----------------------------------------------------------------------------------------------#
class Button:
    """this class is for buttons that you can click on them"""
    def __init__(
        self, x, y, width, height,
        texture_foldername = "buttons",
        texture_filename = "play.png",
        hover_texture_filename = "play_h.png"
        ):
        """create the button"""
        self.x = x #x pos of the button
        self.y = y #y pos of the button
        self.hover = False #is the mouse hover the button
        self.starting_width = width #the given width
        self.starting_height = height #the given height
        self.width = resize.resize_x(
            settings.starting_screen_width,
            width,
            gf.screen_width
            )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            height,
            gf.screen_height
            )
        self.rect = pygame.Rect( #create a rect for pygame hitbox
            x,
            y,
            self.width,
            self.height
            )
        self.texture = pygame.transform.scale( #change the scale of the given image
            pygame.image.load(
                textures.change_texture(
                    foldername = texture_foldername, filename = texture_filename
                    )
                ),
            (self.rect.width, self.rect.height)
            )
        self.hover_texture = pygame.transform.scale( #change the scale of the given hover image
            pygame.image.load(
                textures.change_texture(
                    foldername = texture_foldername, filename = hover_texture_filename
                    )
                ),
            (self.rect.width, self.rect.height)
            )

    def update(self):
        """update self and draw him on the screen"""
        self.mouse_hover() #go to the func hover
        self.draw() #go to the func draw

    def draw(self):
        if self.hover: #if the mouse is on the button
            gf.screen.blit(self.hover_texture, (self.x, self.y)) #show the hover texture
        else:
            gf.screen.blit(self.texture, (self.x, self.y)) #show the regular texture

    def mouse_hover(self):
        if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False

    def click(self):
        if self.hover and gf.click: #if click on the button
            gf.click = False
            return True
        else:
            return False 
#-----------------------------------------------------------------------------------------------#

class Clickable_Invisible_object:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.starting_width = width
        self.starting_height = height
        self.width = resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            self.starting_height,
            gf.screen_height
        )
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
        self.hover = False
    
    def update(self):
        self.mouse_hover()
        if gf.click and self.hover:
            gf.click = False
            return True
        else:
            return False

    def mouse_hover(self):
        if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
#-----------------------------------------------------------------------------------------------#

class Clickable_Text_object:
    def __init__(
        self, x, y, width, height,
        text = "this is the text",
        text_color = (255, 255, 255),
        font_size = gf.screen_width // 50,
        font_folder_name = "fonts",
        font_file_name = "name.ttf"
        ):

        #x and y
        self.x = x
        self.y = y

        #width and height
        self.starting_width = width
        self.starting_height = height
        self.width = resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            self.starting_height,
            gf.screen_height
        )

        #create rect
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
        
        #is the mouse hover the rect
        self.hover = False

        #font and text render
        self.font = pygame.font.Font(
            textures.change_texture(font_file_name, font_folder_name), font_size
            )
        self.text = self.font.render(text, 1, text_color)

    
    def update(self):
        #blit
        gf.screen.blit(self.text, (self.rect.x, self.rect.y))

        #is you clicked the rect
        self.mouse_hover()
        if gf.click and self.hover:
            gf.click = False
            return True
        else:
            return False

    def mouse_hover(self):
        if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
    
    def dev_checks(self):
        pygame.draw.rect(gf.screen, (255, 0, 255), self.rect)
#-----------------------------------------------------------------------------------------------#

class Just_an_image:
    def __init__(self, x, y, width, height, image_folder_name, image_file_name):
        #position
        self.x = x
        self.y = y
        
        #starting scale
        self.starting_width = width
        self.starting_height = height

        #scale
        self.width = resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            self.starting_height,
            gf.screen_height
        )

        #image loading
        self.unscaled_image = pygame.image.load(
            textures.change_texture(
                foldername = image_folder_name, filename = image_file_name
                )
        )

    
    def update(self, x, y):
        #position
        self.x = x
        self.y = y
        
        #scale
        self.width = resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = resize.resize_y(
            settings.starting_screen_height,
            self.starting_height,
            gf.screen_height
        )

        #rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #scale image
        self.image = pygame.transform.scale(
            self.unscaled_image,
            (self.rect.width, self.rect.height)
        )

        #show image
        gf.screen.blit(self.image, (self.rect.x, self.rect.y))
