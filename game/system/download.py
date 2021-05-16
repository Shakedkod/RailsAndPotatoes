import os, wget
from stat import S_IREAD
from time import sleep
from colorama import Fore
from zipfile import ZipFile

def download(url = "https://www.python.org/static/img/python-logo@2x.png", foldername = ".folder", filename = "name.png"):
    """this fanc install to appdata what you want from the internet"""
    appdata = os.getenv('APPDATA') #get appdata
    check_path = appdata + "\\"
    check_path += foldername
    if not os.path.exists(check_path):
        os.makedirs(check_path)
    path = check_path + "\\"
    path += filename
    ############################################
    wget.download(url, path)
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall(path=check_path)
    os.remove(path)

def assets_check():
    appdata = os.getenv('APPDATA') #get appdata
    path = appdata + r"\.game_name\by_shakedkod.txt"
    if not os.path.exists(path):
        print (Fore.RED + "download assets, please wait...")
        download(
            url = r"https://www.dropbox.com/s/96gsss9rtvuqjo3/.assets.zip?dl=1",
            foldername= ".game_name",
            filename = "assets.zip"
            )
        read_path = appdata + r"\.game_name\index\Assets"
        os.chmod(read_path, S_IREAD)
        print (Fore.RESET + "")
        print (Fore.YELLOW + "assets" + Fore.GREEN + " loaded" + Fore.RESET + "")
        sleep(2)
        return False
    else:
        return True