import pygame, base64, ast, os
from moviepy.editor import *
from . import globals_file as gf, settings as s
from pygame.locals import *
#-----------------------------------------------------------------------#
pygame.init()
pygame.display.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init() #init pygame mixer
#%start%-----------------------------------------------------------------------%start%#

#?----------------------------------------------------------------------------------------?#
#?---------------------------------------#Cutscene#---------------------------------------?#
#?----------------------------------------------------------------------------------------?#
class Cutscene:

    @staticmethod
    def regular(name, path):
        #%start%------------------------------------%start%#
        pygame.display.set_caption(name)

        clip = VideoFileClip(
            path,
            has_mask = False,
            audio = True,
            target_resolution = (gf.screen_width, gf.screen_height)
            )
        clip.preview()

        #reload mixer
        pygame.mixer.quit()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.mixer.init()

        #display
        pygame.display.set_caption(s.game_start.caption)
        gf.screen = pygame.display.set_mode(
            (gf.screen_width, gf.screen_height),
            pygame.RESIZABLE
            )
        
        return True
        #%end%------------------------------------%end%#

    @staticmethod
    def start():
        #%start%------------------------------------%start%#


        clip = VideoFileClip(
            "",
            has_mask = False,
            audio = True,
            target_resolution = (gf.screen_width, gf.screen_height)
            )
        clip.preview()

        #reload mixer
        pygame.mixer.quit()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.mixer.init()

        #display
        pygame.display.set_caption(s.game_start.caption)
        gf.screen = pygame.display.set_mode(
            (gf.screen_width, gf.screen_height),
            pygame.RESIZABLE
            )
        
        return True
        #%end%------------------------------------%end%#

    @staticmethod
    def endgame(name, path):
        #%start%------------------------------------%start%#
        pygame.display.set_caption(name)

        clip = VideoFileClip(
            path,
            has_mask = False,
            audio = True,
            target_resolution = (gf.screen_width, gf.screen_height)
            )
        clip.preview()

        #clip = VideoFileClip(
        #    !path to the credits,
        #    has_mask = False,
        #    audio = True,
        #    target_resolution = (gf.screen_width, gf.screen_height)
        #    )
        #clip.preview()

        #reload mixer
        pygame.mixer.quit()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.mixer.init()

        #display
        pygame.display.set_caption(s.game_start.caption)
        gf.screen = pygame.display.set_mode(
            (gf.screen_width, gf.screen_height),
            pygame.RESIZABLE
            )

        #back to the main menu
        gf.where = "main menu"

        return True
        #%end%------------------------------------%end%#

    #%end%-----------------------------------------------------------------------%end%#

#?-------------------------------------------------------------------------------------------------?#
#?---------------------------------------#Encode and Decode#---------------------------------------?#
#?-------------------------------------------------------------------------------------------------?#
class Encode_and_Decode:

    @staticmethod
    def convert_dict_to_64(dict_from = {}):
        #%start%------------------------------------%start%#
        strdict = str(dict_from)
        strdict_bytes = strdict.encode("ascii")
        base64_bytes = base64.b64encode(strdict_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string
        #%end%------------------------------------%end%#

    #---------------------------------------------------------#

    @staticmethod
    def convert_64_to_dict(base64_string, cut = None):
        #%start%------------------------------------%start%#
        base64_bytess = base64_string.encode('ascii')
        message_bytess = base64.b64decode(base64_bytess)
        message = message_bytess.decode('ascii')
        return_dict = ast.literal_eval(message)
        final_dict = return_dict[cut] if cut != None else return_dict
        return final_dict
        #%end%------------------------------------%end%#
    
    #%end%-----------------------------------------------------------------------%end%#

#?---------------------------------------------------------------------------------------------?#
#?---------------------------------------#Music_and_SFX#---------------------------------------?#
#?---------------------------------------------------------------------------------------------?#
class Music_and_SFX:

    @staticmethod
    def set_volume(songs_and_sfx, volume):
        #%start%------------------------------------%start%#
        """
        give a dict of all of the sounds and sound efects and it will set the voulume to the voulume that is inserted,
        -> return the dict <-
        """
        for key in songs_and_sfx:
            pygame.mixer.Sound.set_volume(songs_and_sfx[key], volume)
        return songs_and_sfx
        #%end%------------------------------------%end%#

    @staticmethod
    def change_volume(what):
        #%start%------------------------------------%start%#
        """take input of 'up' or 'down' and change the voulume, return the voulume(float)"""
        if (what == "up") and (s.volume < 1.0):
            s.volume += .01
        elif (what == "down") and (s.volume > 0.0):
            s.volume -= .01
        return s.volume #return
        #%end%------------------------------------%end%#

    @staticmethod
    def load_sounds_or_sfx(sounds_dict, file_name, folder_name, key, voulume):
        #%start%------------------------------------%start%#
        """
        Input
        -------------------------------------------------------------------------------------------------------
        sound_dict = the list of sounds in the game - type === dict.
        file_name = the sound file name with .mp3/.ogg/... in the end - type === string.
        folder_name = the folder name of the sound file, start from ...\Assets\sounds_and_sfx\(the folder here), if 'None', the folder will be just sounds_and_sfx - type === string.
        key = the key in the dict - type === string.
        voulume = the voulume of the sounds in the game - type === float.

        Function
        -------------------------------------------------------------------------------------------------------
        load sounds and sfx to the dict (pygame.mixer.Sound)

        Return
        -------------------------------------------------------------------------------------------------------
        sounds_dict - type === dict.
        """
        appdata = os.getenv('APPDATA') #get appdata
        if folder_name == "None":
            path = appdata + "\\.rails_and_potatoes\\index\\Assets\\sounds_and_sfx\\" + file_name
        else:
            path = appdata + "\\.rails_and_potatoes\\index\\Assets\\sounds_and_sfx\\" + folder_name + "\\" +    file_name
        #?----------------------------------------load sound----------------------------------------?#
        if os.path.exists(path):
            sounds_dict[key] = pygame.mixer.Sound(path)
        else:
            path = appdata + "\\.rails_and_potatoes\\by_shakedkod.txt"
            os.remove(path)
            gf.another_one = True
            gf.where = "exit"

        #?----------------------------------------set voulume----------------------------------------?#
        pygame.mixer.Sound.set_volume(sounds_dict[key], voulume)

        #?----------------------------------------return----------------------------------------?#
        return sounds_dict
        #%end%------------------------------------%end%#

    #%end%-----------------------------------------------------------------------%end%#

#?--------------------------------------------------------------------------------------?#
#?---------------------------------------#Resize#---------------------------------------?#
#?--------------------------------------------------------------------------------------?#
class Resize:

    @staticmethod
    def resize_x(starting_screen_width, size_for_the_starting_screen_width, screen_width):
        #%start%------------------------------------%start%#
        """
        you can resize the width of your objects with the original screen width and the width of the object in that screen width
        -> returns int or float <-
        """
        x = starting_screen_width / size_for_the_starting_screen_width
        return screen_width / x
        #%end%------------------------------------%end%#
    
    @staticmethod
    def resize_y(starting_screen_height, size_for_the_starting_screen_height, screen_height):
        #%start%------------------------------------%start%#
        """
        you can resize the height of your objects with the original screen height and the height of the object in that screen height
        -> returns int or float <-
        """
        y = starting_screen_height / size_for_the_starting_screen_height
        return screen_height / y
        #%end%------------------------------------%end%#

    @staticmethod
    def resize(
        screen,
        original_screen_width = 900,
        original_screen_height = 500,
        size_for_the_original_screen_width = 10,
        size_for_the_original_screen_height = 10
        ):
        #%start%------------------------------------%start%#
        """
        you can resize your objects with the original screen size and the size of this object for the original  screen size
        -> return a tuple of the width and hight of the object in the current screen resolution <-
        """
        width = Resize.resize_x(
            original_screen_width, size_for_the_original_screen_width, screen.get_width()
            )
        hight = Resize.resize_y(
            original_screen_height, size_for_the_original_screen_height, screen.get_height()
            )
        return (width, hight)
        #%end%------------------------------------%end%#
    
    @staticmethod
    def change_xy(screen_width, screen_height, width_before, height_before, obj):
        #%start%------------------------------------%start%#
        """
        for none static objects only!
        change the pos of the object based on the resizing of the screen
        -> return object <-
        """
        if (screen_width != width_before) or (screen_height != height_before):
            obj_x = obj.x
            obj_y = obj.y
            sw = screen_width
            sh = screen_height
            first_set_px = obj_x / width_before
            first_set_py = obj_y / height_before
            obj.x = first_set_px * sw
            obj.y = first_set_py * sh
            gf.width_before = sw
            gf.height_before = sh
            return obj
        #%end%------------------------------------%end%#
    
    #%end%-----------------------------------------------------------------------%end%#

#?--------------------------------------------------------------------------------------?#
#?---------------------------------------#Levels#---------------------------------------?#
#?--------------------------------------------------------------------------------------?#
class levels:
    
    @staticmethod
    def one():
        #%start%------------------------------------%start%#
        pass
        #%end%------------------------------------%end%#
    
    #%end%-----------------------------------------------------------------------%end%#
