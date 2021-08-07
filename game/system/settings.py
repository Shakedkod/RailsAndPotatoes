import json, os
from game import globals_file as gf

global game_name, by, version, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume
game_name, by, version, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume = "name", "name", "name", "name", ["list"], "name", "name", "name", {"hi": "h"}, 900, 500, 1.0

class Game_Start(object):
    def __init__(self, data = None, open_data = None):
        self.start_width = open_data["screen width"]
        self.start_height = open_data["screen height"]
        self.caption = data["screen name"]
        self.png_icon = data["icon path - png"]

class Player_Maker(object):
    def __init__(self):
        APPDATA = os.getenv("APPDATA")
        with open(APPDATA + "\\.rails_and_potatoes\index\\player.os.dt", "r") as d_day:
            data = json.load(d_day)
        
        self.open_levels = []
        self.completed_levels = []
        for item in data["levels&cutscenes"]:
            if item["data"] == 0:
                pass
            elif item["data"] == 1:
                self.open_levels.append(item["id"])
            else:
                self.completed_levels.append(item["id"])

def init():
    with open("game/system/settings.os.dt", "r") as seting:
        data = json.load(seting)
    APPDATA = os.getenv("APPDATA")
    with open(APPDATA + "\\.rails_and_potatoes\index\\player.os.dt", "r") as seting:
        open_data = json.load(seting)
    
    global game_name, by, version, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, volume

    game_name = data["name"]
    by = data["made by"]
    teamNames = data["teamNames"]

    version = data["version"]
    lang = data["lang"]
    assets_folder_name = data["assets folder name"]
    description = data["description"]

    other = open_data["settings"]["other"]

    volume = open_data["settings"]["game start"]["volume"]

    game_start = Game_Start(data["game start"], open_data["settings"]["game start"])

    starting_screen_width = data["calculations"]["screen width"]
    starting_screen_height = data["calculations"]["screen height"]

    gf.what_is_rp = data["Active RP"]
    gf.player = Player_Maker()


def save_settings():
    global game_start, volume
    with open("game/system/settings.json", 'r') as seting:
        data = json.load(seting)
    data["game start"]["voulume"] = volume
    data["game start"]["screen width"] = game_start.start_width
    data["game start"]["screen height"] = game_start.start_height
    data["Active RP"] = gf.what_is_rp
    with open("game/system/settings.json", "w") as sett:
        json.dump(data, sett, indent=2)
        sett.close()
