from game.system import settings
#seting the voulume
def set_voulume(songs_and_sfx, voulume):
    """give a list of all of the sounds and sound efects and it will set the voulume to the voulume that is inserted,
    -> return the list <-"""
    for song in songs_and_sfx:
        song.set_voulume(voulume)
    return songs_and_sfx

def change_voulume(what):
    """take input of 'up' or 'down' and change the voulume, return the voulume(int)"""
    if (what == 'up') and (settings.voulume < 1.0):
        settings.voulume += .01
    elif (what == 'down') and (settings.voulume > 0.0):
        settings.voulume -= .01
    return int(settings.voulume * 100) #return