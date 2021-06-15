import json

global game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, voulume
game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, voulume = "name", "name", "name", "name", ["list"], "name", "name", "name", {"hi": "h"}, 900, 500, 1.0

class Game_Start(object):
    def __init__(self, data=None):
        self.start_width = data["screen width"]
        self.start_height = data["screen height"]
        self.caption = data["screen name"]
        self.png_icon = data["icon path - png"]

def get_setings():
    with open("game/system/settings.json", 'r') as seting:
        data = json.load(seting)
        seting.close()
    global game_name, by, virson, lang, teamNames, assets_folder_name, description, other, game_start, starting_screen_width, starting_screen_height, voulume
    game_name = data["name"]
    by = data["made by"]
    virson = data["virson"]
    lang = data["lang"]
    teamNames = data["teamNames"]
    assets_folder_name = data["assets folder name"]
    description = data["description"]
    other = data["other"]
    voulume = data["game start"]["voulume"]
    game_start = Game_Start(data["game start"])
    starting_screen_width = data["calculations"]["screen width"]
    starting_screen_height = data["calculations"]["screen height"]

def save_setings():
    global game_start, voulume
    with open("game/system/settings.json", 'r') as seting:
        data = json.load(seting)
        seting.close()
    data["game start"]["voulume"] = voulume
    data["game start"]["screen width"] = game_start.start_width
    data["game start"]["screen height"] = game_start.start_height
    with open("game/system/settings.json", "w") as sett:
        json.dump(data, sett, indent=2)
        sett.close()

