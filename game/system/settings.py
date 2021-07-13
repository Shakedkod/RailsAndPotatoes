import json, os
from . import globals_file as gf

global game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume
game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume = "name", "name", "name", "name", ["list"], "name", "name", "name", {"hi": "h"}, 900, 500, 1.0

class Game_Start(object):
    def __init__(self, data=None):
        self.start_width = data["screen width"]
        self.start_height = data["screen height"]
        self.caption = data["screen name"]
        self.png_icon = data["icon path - png"]

class Player_Maker(object):
    class Cutscenes:
        def __init__(self, data = None):
            self.start = {
                "name": data["start"][0],
                "viewed": data["start"][1]
            }
            self.end = {
                "name": data["end"][0],
                "viewed": data["end"][1]
            }
    
    def __init__(self):
        APPDATA = os.getenv("APPDATA")
        with open(APPDATA + "\\.rails_and_potatoes\index\\player.data", "r") as d_day:
            data = json.load(d_day)
            d_day.close()
        self.unlocked_levels = data["unlocked levels"]
        self.complete_levels = data["complete levels"]
        self.cutscenes = Player_Maker.Cutscenes(data = data["cutscenes"])

def get_setings():
    with open("game/system/settings.json", 'r') as seting:
        data = json.load(seting)
        seting.close()
    global game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume
    game_name = data["name"]
    by = data["made by"]
    virson = data["virson"]
    lang = data["lang"]
    teamNames = data["teamNames"]
    assets_folder_name = data["assets folder name"]
    description = data["description"]
    other = data["other"]
    volume = data["game start"]["volume"]
    game_start = Game_Start(data["game start"])
    starting_screen_width = data["calculations"]["screen width"]
    starting_screen_height = data["calculations"]["screen height"]
    gf.what_is_rp = data["Active RP"]
    gf.player = Player_Maker()


def save_setings():
    global game_start, volume
    with open("game/system/settings.json", 'r') as seting:
        data = json.load(seting)
        seting.close()
    data["game start"]["voulume"] = volume
    data["game start"]["screen width"] = game_start.start_width
    data["game start"]["screen height"] = game_start.start_height
    data["Active RP"] = gf.what_is_rp
    with open("game/system/settings.json", "w") as sett:
        json.dump(data, sett, indent=2)
        sett.close()

