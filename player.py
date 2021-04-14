# file: player.py
# author: Niklas Nordman
# description: file contains the class for a player

import scorecard
import mechanics as gm

class Player():

    def __init__(self):
        self.__name = "Niklas"

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = input("Set first name: ")

    def __str__(self):
        return 'Name ' + format(self.__name)