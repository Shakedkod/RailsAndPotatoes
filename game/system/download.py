import os, wget
from stat import S_IXUSR
from time import sleep
from colorama import Fore
from zipfile import ZipFile

def download(
    is_zip = True, url = "https://www.python.org/static/img/python-logo@2x.png", foldername = ".folder", filename = "name.zip"
    ):
    """this fanc install to appdata what you want(in a file that end with .zip) from the internet"""
    appdata = os.getenv('APPDATA') #get appdata
    check_path = appdata + "\\"
    check_path += foldername
    if not os.path.exists(check_path):
        os.makedirs(check_path)
    path = check_path + "\\"
    path += filename
    ############################################
    wget.download(url, path)
    if is_zip:
        with ZipFile(path, 'r') as zipObj:
            zipObj.extractall(path=check_path)
        os.remove(path)

def assets_check():
    appdata = os.getenv('APPDATA') #get appdata
    path = appdata + r"\.rails_and_potatoes\by_shakedkod.txt"
    check_path = appdata + "\\.rails_and_potatoes\\"
    if not os.path.exists(path):
        print (Fore.RED + "download assets, please wait...")
        download(
            url = r"https://www.dropbox.com/s/gaem86fgyqo872g/RailsAndPotatoes.assets?dl=1",
            foldername= ".rails_and_potatoes",
            filename = "RailsAndPotatoes.assets"
            )
        read_path = appdata + r"\.rails_and_potatoes\index\Assets"
        os.chmod(read_path, S_IXUSR)

        #remove tmp files
        #the logs folder
        if os.path.exists(check_path + "Logs\\log.log"):
            os.remove(check_path + "Logs\\log.log")
        #the Resource Pack folder
        if os.path.exists(check_path + "Resource pack\\for exsample.txt"):
            os.remove(check_path + "Resource pack\\for exsample.txt")
        #the Screen Shots folder
        if os.path.exists(check_path + "Screen Shots\\for screen shots.txt"):
            os.remove(check_path + "Screen Shots\\for screen shots.txt")

        print (Fore.RESET + "")
        print (Fore.YELLOW + "assets" + Fore.GREEN + " loaded" + Fore.RESET + "")
        sleep(2)
