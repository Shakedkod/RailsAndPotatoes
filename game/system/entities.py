import pygame
from game.system import resize, globals_file as gf, settings, textures
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

class Animation:
    def __init__(self, x, y, starting_width, starting_height, frame_number, frames_dict = None):
        """
        first, init at the start(were we are 'loading' our images) with frame_number == 1
        second, init in the loop with frame_number == name_of_initial_object.frame
        """
        self.x = x
        self.y = y
        self.starting_width = starting_width
        self.starting_height = starting_height
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
        self.not_loaded_images = frames_dict
        self.number_of_frames = len(self.not_loaded_images) - 1 #starting from 0, because of list
        self.loaded_images = []
        for key, value in self.not_loaded_images: #loading the images
            self.loaded_images.append(
                pygame.image.load(
                    textures.change_texture(
                        value[1],
                        value[0]
                        )
                )
            )
        self.scaled_images = []
        for image in self.loaded_images:
            self.scaled_images.append(
                pygame.transform.scale(
                    image,
                    (
                        self.rect.width,
                        self.rect.height
                        )
                )
            )
        self.frame = frame_number #were are we now?, you are asking me?...
        
    def update(self):
        pass #TODO

    def animate(self):
        pass #TODO
