#--------------------------------------------< Import >--------------------------------------------#
import pygame
from pygame.locals import *

from game import system as sys, globals_file as gf
from . import settings, textures


#%start%--------< The Start >--------%start%#
#--------------------------------------------< Buttons >--------------------------------------------#
class Button:
    def __init__(
        self,
        x = 0,
        y = 0,
        width = 1,
        height = 1,
        texture_foldername = "buttons\\main menu",
        texture_filename = "play.png",
        hover_texture_filename = "play_h.png",
        completed_texture_filename = None,
        locked_texture_filename = None,
        unlocked = True,
        completed = False
        ):
        """this class is button that you can click it, it can be locked or completed for different textures and click option(can or cant click)

        Args:
            x (int, optional): the x position of the button. Defaults to 0.
            y (int, optional): the y position of the button. Defaults to 0.
            width (int, optional): the width of the button. Defaults to 1.
            height (int, optional): the height of the button. Defaults to 1.
            texture_foldername (str, optional): the name of the folder with the files of the textures. Defaults to "buttons\main menu".
            texture_filename (str, optional): the name of the file of the button texture(with .png/jpeg/... in the end). Defaults to "play.png".
            hover_texture_filename (str, optional): the name of the file of the button hover texture(with .png/jpeg/... in the end). Defaults to "play_h.png".
            completed_texture_filename (str, optional): the name of the file of the button completed texture(with .png/jpeg/... in the end). Defaults to None.
            completed_texture_filename (str or None, optional): the name of the file of the button completed texture(with .png/jpeg/... in the end). Defaults to None.
            locked_texture_filename (str or None, optional): the name of the file of the button locked texture(with .png/jpeg/... in the end). Defaults to None.
            unlocked (bool, optional): is the button locked(Bollian(True or False)). Defaults to True.
            completed (bool, optional): is the staff that happen when you clicked the button is completed. Defaults to False.
        """
    
        self.x = x #x pos of the button
        self.y = y #y pos of the button
    
        self.starting_width = width #the given width
        self.starting_height = height #the given height
    
        self.hover = False #is the mouse hover the button
        self.unlocked = unlocked
        self.completed = completed
    
        self.width = sys.Resize.resize_x(
            settings.starting_screen_width,
            width,
            gf.screen_width
            )
        self.height = sys.Resize.resize_y(
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
        
        #Textures
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
    
        if locked_texture_filename != None:
            self.locked_texture = pygame.transform.scale( #change the scale of the given image
                pygame.image.load(
                    textures.change_texture(
                        foldername = texture_foldername, filename = locked_texture_filename
                        )
                    ),
                (self.rect.width, self.rect.height)
                )
        
        if completed_texture_filename != None:
            self.completed_texture = pygame.transform.scale( #change the scale of the given hover image
                pygame.image.load(
                    textures.change_texture(
                        foldername = texture_foldername, filename = completed_texture_filename
                        )
                    ),
                (self.rect.width, self.rect.height)
                )
    
    def update(self):
        """update self and draw him on the screen
        """
        self.mouse_hover() #go to the func hover
        self.draw() #go to the func draw
    
    def draw(self):
        """draw the right texture on the screen
        """        
        if self.unlocked == False:
            gf.screen.blit(self.locked_texture, (self.x, self.y)) #show the locked texture
    
        elif self.hover: #if the mouse is on the button
            gf.screen.blit(self.hover_texture, (self.x, self.y)) #show the hover texture
    
        elif self.completed:
            gf.screen.blit(self.completed_texture, (self.x, self.y)) #show the completed texture
    
        else:
            gf.screen.blit(self.texture, (self.x, self.y)) #show the regular texture
    
    def mouse_hover(self):
        """change the hover var of the entity if the mouse is hover the button
        """        
        if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
    
    def click(self):
        """check if the user clicked on the entity

        Returns:
            bool: is the button clicked
        """
        if self.hover and gf.click and self.unlocked: #if click on the button
            gf.click = False
            return True
        else:
            return False

#----------------------------------< Clickable Invisible Object >----------------------------------#
def CIO_init(
    self,
    x = 0,
    y = 0,
    width = 1,
    height = 1
    ):
    self.x = x
    self.y = y
    self.starting_width = width
    self.starting_height = height
    self.width = sys.Resize.resize_x(
        settings.starting_screen_width,
        self.starting_width,
        gf.screen_width
    )
    self.height = sys.Resize.resize_y(
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
    
def CIO_update(self):
    self.mouse_hover()
    if gf.click and self.hover:
        gf.click = False
        return True
    else:
        return False

def CIO_mh(self):
    if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
        self.hover = True
    else:
        self.hover = False

#!=-------------------------------< Class Creation >-------------------------------!=#
Clickable_Invisible_object = type("Clickable_Invisible_object", (), {
    "__init__": CIO_init,
    "update": CIO_update,
    "mouse_hover": CIO_mh
})

#------------------------------------< Clickable Text Object >------------------------------------#
def CTO_init(
    self,
    x = 0,
    y = 0,
    width = 1,
    height = 1,
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
    self.width = sys.Resize.resize_x(
        settings.starting_screen_width,
        self.starting_width,
        gf.screen_width
    )
    self.height = sys.Resize.resize_y(
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

    
def CTO_update(self):
    #blit
    gf.screen.blit(self.text, (self.rect.x, self.rect.y))

    #is you clicked the rect
    self.mouse_hover()
    if gf.click and self.hover:
        gf.click = False
        return True
    else:
        return False

def CTO_mh(self):
    if self.rect.collidepoint(gf.mouse_x, gf.mouse_y): #if the mouse is on the button
        self.hover = True
    else:
        self.hover = False
    
def CTO_dc(self):
    pygame.draw.rect(gf.screen, (255, 0, 255), self.rect)

#!=-------------------------------< Class Creation >-------------------------------!=#
Clickable_Text_object = type("Clickable_Text_object", (), {
    "__init__": CTO_init,
    "update": CTO_update,
    "mouse_hover": CTO_mh,
    "dev_checks": CTO_dc
})

#--------------------------------------------< Just An Image >--------------------------------------------#
class Just_an_image:
    def __init__(
        self,
        x = 0,
        y = 0,
        width = 1,
        height = 1,
        image_folder_name = "folder name",
        image_file_name = "file name"
        ):
        """this entity is just an image, and no more
    
        Args:
            x (int, optional): the x coordinate of the entity. Defaults to 0.
            y (int, optional): the y coordinate of the entity. Defaults to 0.
            width (int, optional): the width of the entity. Defaults to 1.
            height (int, optional): the height of the entity. Defaults to 1.
            image_folder_name (str, optional): the image folder name. Defaults to "folder name".
            image_file_name (str, optional): the image file name with .png/jpeg/gif/... at the end. Defaults to "file name".
        """ 
        
        #position
        self.x = x
        self.y = y

        #starting scale
        self.starting_width = width
        self.starting_height = height

        #scale
        self.width = sys.Resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = sys.Resize.resize_y(
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
        self.width = sys.Resize.resize_x(
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
        )
        self.height = sys.Resize.resize_y(
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
#%end%-----------< The End >-----------%end%#
