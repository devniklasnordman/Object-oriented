# File:         dice.py
# Author:       Niklas Nordman
# Description:  Dice that can be rolled

import random

# Class definition

class Dice:
    def __init__(self):
        self.__side = 1

    def roll_dice(self):
        throw = random.randint(1, 6)
        self.__side = throw

    def get_total(self):
        return self.__total

    def get_side(self):
        return self.__side

    def set_total(self, total):
        self.__total = total

    def set_side(self, dice_side):
        self.__side = dice_side

    def get_id(self):
        return self.__id

    def set_id(self, dice_id):
        self.__id = dice_id

    def __str__(self):
        return 'Dice ' + format(self.__id) + ' is ' + format(self.__color) + '.'