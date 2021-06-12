import os, pygame
from game.system import settings
from pygame.locals import *
pygame.init() #init
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)
pygame.mixer.init()
#seting the voulume
def set_voulume(songs_and_sfx, voulume):
    """give a dict of all of the sounds and sound efects and it will set the voulume to the voulume that is inserted,
    -> return the list <-"""
    for key, value in songs_and_sfx:
        print (key, value)
        pygame.mixer.Sound.set_volume(value, voulume)
    return songs_and_sfx

def change_voulume(what):
    """take input of 'up' or 'down' and change the voulume, return the voulume(float)"""
    if (what == "up") and (settings.voulume < 1.0):
        settings.voulume += .01
    elif (what == "down") and (settings.voulume > 0.0):
        settings.voulume -= .01
    return settings.voulume #return

def load_sounds_or_sfx(sounds_dict, file_name, folder_name, key, voulume):
    """input:
    ---------------------------------------------------------------------------------------------------------
    sound_dict = the list of sounds in the game - type === dict.

    file_name = the sound file name with .mp3/.ogg/... in the end - type === string.

    folder_name = the folder name of the sound file, start from ...\Assets\sounds_and_sfx\(the folder here), if 'None', the folder will be just sounds_and_sfx - type === string.

    key = the key in the dict - type === string.
    
    voulume = the voulume of the sounds in the game - type === float.
    ---------------------------------------------------------------------------------------------------------
    load sounds and sfx to the dict (pygame.mixer.Sound)

    return:
    ---------------------------------------------------------------------------------------------------------
    sounds_dict - type === dict."""
    appdata = os.getenv('APPDATA') #get appdata
    if folder_name == "None":
        path = appdata + "\\.rails_and_potatoes\\index\\Assets\\sounds_and_sfx\\" + file_name
    else:
        path = appdata + "\\.rails_and_potatoes\\index\\Assets\\sounds_and_sfx\\" + folder_name + "\\" + file_name
    #?----------------------------------------load sound----------------------------------------?#
    sounds_dict[key] = pygame.mixer.Sound(path)

    #?----------------------------------------set voulume----------------------------------------?#
    pygame.mixer.Sound.set_volume(sounds_dict[key], voulume)

    #?----------------------------------------return----------------------------------------?#
    return sounds_dict