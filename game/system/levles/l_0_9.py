from game import globals_file as gf
from time import sleep

@staticmethod
def one():
    gf.run_level = True
    while gf.run_level:
        gf.Tiles.update(1)
        sleep(5)
        gf.run_level = False

@staticmethod
def two():
    print ("two")

@staticmethod
def three():
    print ("three")

@staticmethod
def four():
    print ("four")

@staticmethod
def five():
    print ("five")

@staticmethod
def six():
    print ("six")

@staticmethod
def seven():
    print ("seven")

@staticmethod
def eight():
    print ("eight")

@staticmethod
def nine():
    print ("nine")