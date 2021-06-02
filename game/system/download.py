import os, wget
from stat import S_IREAD
from time import sleep
from colorama import Fore
from zipfile import ZipFile

def download(url = "https://www.python.org/static/img/python-logo@2x.png", foldername = ".folder", filename = "name.zip"):
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
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall(path=check_path)
    os.remove(path)

def assets_check():
    appdata = os.getenv('APPDATA') #get appdata
    path = appdata + r"\.rails_and_potatoes\by_shakedkod.txt"
    if not os.path.exists(path):
        print (Fore.RED + "download assets, please wait...")
        download(
            url = r"https://www.dropbox.com/s/cc09m2o8qxs555n/.assets.zip?dl=1",
            foldername= ".rails_and_potatoes",
            filename = "assets.zip"
            )
        read_path = appdata + r"\.rails_and_potatoes\index\Assets"
        os.chmod(read_path, S_IREAD)
        print (Fore.RESET + "")
        print (Fore.YELLOW + "assets" + Fore.GREEN + " loaded" + Fore.RESET + "")
        sleep(2)
        return False
    else:
        return True