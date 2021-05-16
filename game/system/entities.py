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

class Player:
    """the player class"""
    def __init__(
        self, x, y, width, height,
        texture_foldername = "c",
        texture_filename = "player.png"
        ):
        """create the player"""
        self.x = x #x pos of the player in the start
        self.y = y #y pos of the player in the start
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
        self.image = pygame.image.load( #get the image and load it
            textures.change_texture(
                foldername = texture_foldername, filename = texture_filename
                )
            )
        self.texture = pygame.transform.scale( #change the scale of the given image
            self.image, (self.width, self.height)
            )
        self.rect = pygame.Rect( #create the pygame rect
            self.x,
            self.y,
            self.width,
            self.height
            )
    
    def update(self):
        """update the player and draw"""
        self.width = resize.resize_x( #change the width
            settings.starting_screen_width,
            self.starting_width,
            gf.screen_width
            )
        self.height = resize.resize_y( #change the height
            settings.starting_screen_height,
            self.starting_height,
            gf.screen_height
            )
        self.rect.width = self.width #set the new width as the rect width
        self.rect.height = self.height #set the new height as the rect height
        self.rect = resize.change_xy( #if the screen size change, we need to move the player
            gf.screen_width,
            gf.screen_height,
            gf.width_before,
            gf.height_before,
            self.rect
            )
        self.x = self.rect.x #set the new x as the self.x
        self.y = self.rect.y #set the new y as the self.y
        self.texture = pygame.transform.scale( #change the scale of the texture
            self.image, (self.width, self.height)
            )
        self.draw() #go to the draw func
    
    def draw(self):  gf.screen.blit(self.texture, (self.x, self.y)) #show the player on the screen
#-----------------------------------------------------------------------------------------------#

class Goto_Object:
    """object that dont have to be visible, if you(the player rect) toch it, you get teleported to another scene"""
    def __init__(self, x, y, width, height, goto_scene, goto_bg, texture, texture_foldername, texture_filename):
        """create the object"""
        self.goto_scene = goto_scene #the scene were the object go
        self.goto_bg = goto_bg #the bg were the object go
        self.is_on_true = False #is the player on
        self.x = x #set the x
        self.y = y #set the y
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
        self.rect = pygame.Rect( #create the pygame rect
            self.x,
            self.y,
            self.width,
            self.height
            )
        self.texture_test = texture #is there a texture
        if self.texture_test != None: #if there is a texture
            self.texture = pygame.transform.scale( #load the texture
                pygame.image.load(    
                    textures.change_texture(
                        foldername = texture_foldername, filename = texture_filename
                        )
                    ),
                (self.rect.width, self.rect.height)
                )
        self.starting_width = width #the given width
        self.starting_height = height #the given height
    
    def update(self):
        """update the object"""
        if self.texture_test != None: #if there is texture
            self.draw() #go to the func draw
        self.is_on() #go to the func is_on
        self.goto() #go to the func goto

    def goto(self):
        """if needed change the scene and the bg"""
        if self.is_on_true: #if you on it
            gf.scene = self.goto_scene #change the scene
            gf.bg = self.goto_bg #change the bg

    def is_on(self):
        """check if the player is on the object"""
        if gf.player.rect.colliderect(self.rect): #if it is
            self.is_on_true = True
        else: #if it isnt
            self.is_on_true = False
    
    def draw(self): gf.screen.blit(self.texture, (self.x, self.y)) #show the object on the screen
#-----------------------------------------------------------------------------------------------#

class puzzle:
    """create a puzzle object that if you get on it, its open the puzzle"""
    def __init__(self, x, y, width, height, texture_foldername, texture_filename, puzzle_scene):
        """create the object"""
        self.x = x #x pos
        self.y = y #y pos
        self.is_on_true = False #if you on it
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
        self.rect = pygame.Rect( #create the pygame rect
            self.x,
            self.y,
            self.width,
            self.height
            )
        self.texture = pygame.transform.scale( #load the texture
            pyame.image.load(
                textures.change_texture(
                    foldername = texture_foldername, filename = texture_filename
                    )
                ),
            (self.rect.width, self.rect.height)
            )
        self.puzzle_scene = puzzle_scene #what is the puzzle scene
    
    def update(self):
        """update the object"""
        self.draw() #go to the func draw
        self.is_on() #go to the func is_on
        self.goto() #go to the func goto

    def goto(self):
        """if need to change scene change the scene"""
        if self.is_on_true:
            gf.scene = self.puzzle_scene

    def is_on(self):
        if gf.player.rect.colliderect(self.rect): #if the player is on the object
            self.is_on_true = True
        else: #if not
            self.is_on_true = False

    def draw(self):  gf.screen.blit(self.texture, (self.x, self.y)) #show the object on the screen
#-----------------------------------------------------------------------------------------------#