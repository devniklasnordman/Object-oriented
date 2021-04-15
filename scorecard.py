# File: scorecard.py
# Author: Niklas Nordman
# Description:  The scorecard of my yatzy game

class Scorecard:

    # Initializing the empty scorecard containing all the default values of the players dice rolls
    def __init__(self):
        self.title = "Player      "
        self.player_1 = " 1 |"
        self.player_2 = " 2 |"
        self.player_3 = " 3 |"
        self.player_4 = " 4 |"
        self.ones = " 0 "
        self.twos = " 0 "
        self.threes = " 0 "
        self.fours = " 0 "
        self.fives = " 0 "
        self.sixes = " 0 "
        self.bonus = " 0 "
        self.pair = " 0 "
        self.two_pairs = " 0 "
        self.three_of_a_kind = " 0 "
        self.four_of_a_kind = " 0 "
        self.small_straight = " 0 "
        self.large_straight = " 0 "
        self.fullhouse = " 0 "
        self.chance = " 0 "
        self.yatzy = " 0 "
        self.sum = " 0 "

        self.p2_ones = " 0 "
        self.p2_twos = " 0 "
        self.p2_threes = " 0 "
        self.p2_fours = " 0 "
        self.p2_fives = " 0 "
        self.p2_sixes = " 0 "
        self.p2_bonus = " 0 "
        self.p2_pair = " 0 "
        self.p2_two_pairs = " 0 "
        self.p2_three_of_a_kind = " 0 "
        self.p2_four_of_a_kind = " 0 "
        self.p2_small_straight = " 0 "
        self.p2_large_straight = " 0 "
        self.p2_fullhouse = " 0 "
        self.p2_chance = " 0 "
        self.p2_yatzy = " 0 "
        self.p2_sum = " 0 "


    # Getters that returns the current value of each cell in the scorecard separately when called
    def get_title(self):
        return self.title

    # Player 1 getters

    def get_player_1(self):
        return self.player_1

    def get_ones(self):
        return self.ones

    def get_twos(self):
        return self.twos

    def get_threes(self):
        return self.threes

    def get_fours(self):
        return self.fours

    def get_fives(self):
        return self.fives

    def get_sixes(self):
        return self.sixes

    def get_bonus(self):
        return self.bonus

    def get_pair(self):
        return self.pair

    def get_two_pairs(self):
        return self.two_pairs

    def get_three_of_a_kind(self):
        return self.three_of_a_kind

    def get_four_of_a_kind(self):
        return self.four_of_a_kind

    def get_small_straight(self):
        return self.small_straight

    def get_large_straight(self):
        return self.large_straight

    def get_fullhouse(self):
        return self.fullhouse

    def get_chance(self):
        return self.chance

    def get_yatzy(self):
        return self.yatzy

    def get_sum(self):
        return self.sum

        # Player 2 getters

    def get_player_2(self):
        return self.player_2

    def get_p2_ones(self):
        return self.p2_ones

    def get_p2_twos(self):
        return self.p2_twos

    def get_p2_threes(self):
        return self.p2_threes

    def get_p2_fours(self):
        return self.p2_fours

    def get_p2_fives(self):
        return self.p2_fives

    def get_p2_sixes(self):
        return self.p2_sixes

    def get_p2_bonus(self):
        return self.p2_bonus

    def get_p2_pair(self):
        return self.p2_pair

    def get_p2_two_pairs(self):
        return self.p2_two_pairs

    def get_p2_three_of_a_kind(self):
        return self.p2_three_of_a_kind

    def get_p2_four_of_a_kind(self):
        return self.p2_four_of_a_kind

    def get_p2_small_straight(self):
        return self.p2_small_straight

    def get_p2_large_straight(self):
        return self.p2_large_straight

    def get_p2_fullhouse(self):
        return self.p2_fullhouse

    def get_p2_chance(self):
        return self.p2_chance

    def get_p2_yatzy(self):
        return self.p2_yatzy

    def get_p2_sum(self):
        return self.p2_sum


         # Setters

    def set_title(self, title):
        self.title = title

        # Player 1 setters
    def set_player_1(self, player_1):
        self.player_1 = player_1

    def set_player_2(self, player_2):
        self.player_2 = player_2

    def set_ones(self, ones):
        self.ones = ones

    def set_twos(self, twos):
        self.twos = twos

    def set_threes(self, threes):
        self.threes = threes

    def set_fours(self, fours):
        self.fours = fours

    def set_fives(self, fives):
        self.fives = fives

    def set_sixes(self, sixes):
        self.sixes = sixes

    def set_bonus(self, bonus):
        self.bonus = bonus

    def set_pair(self, pair):
        self.pair = pair

    def set_two_pairs(self, tp):
        self.two_pairs = tp

    def set_three_of_a_kind(self, tk):
        self.three_of_a_kind = tk

    def set_four_of_a_kind(self, fk):
        self.four_of_a_kind = fk

    def set_small_straight(self, ss):
        self.small_straight = ss

    def set_large_straight(self, ls):
        self.large_straight = ls

    def set_fullhouse(self, fh):
        self.fullhouse = fh

    def set_chance(self, chance):
        self.chance = chance

    def set_yatzy(self, yatzy):
        self.yatzy = yatzy

    def set_sum(self, sum):
        self.sum = sum

        # Player 2 setters
    def set_p2_ones(self, ones):
        self.p2_ones = ones

    def set_p2_twos(self, twos):
        self.p2_twos = twos

    def set_p2_threes(self, threes):
        self.p2_threes = threes

    def set_p2_fours(self, fours):
        self.p2_fours = fours

    def set_p2_fives(self, fives):
        self.p2_fives = fives

    def set_p2_sixes(self, sixes):
        self.p2_sixes = sixes

    def set_p2_bonus(self, bonus):
        self.p2_bonus = bonus

    def set_p2_pair(self, pair):
        self.p2_pair = pair

    def set_p2_two_pairs(self, tp):
        self.p2_two_pairs = tp

    def set_p2_three_of_a_kind(self, tk):
        self.p2_three_of_a_kind = tk

    def set_p2_four_of_a_kind(self, fk):
        self.p2_four_of_a_kind = fk

    def set_p2_small_straight(self, ss):
        self.p2_small_straight = ss

    def set_p2_large_straight(self, ls):
        self.p2_large_straight = ls

    def set_p2_fullhouse(self, fh):
        self.p2_fullhouse = fh

    def set_p2_chance(self, chance):
        self.p2_chance = chance

    def set_p2_yatzy(self, yatzy):
        self.p2_yatzy = yatzy

    def set_p2_sum(self, sum):
        self.p2_sum = sum



    # __str__ method shows the current value of the whole scorecard
    def __str__(self):
        return self.title + "      " + "|" + self.player_1 + self.player_2  \
        + "\n---------------------------" \
        + "\nOnes              |" + self.ones + "|" + self.p2_ones + "|"\
        + "\nTwos              |" + self.twos + "|" + self.p2_twos + "|"\
        + "\nThrees            |" + self.threes + "|" + self.p2_threes  + "|"\
        + "\nFours             |" + self.fours + "|" + self.p2_fours   + "|"\
        + "\nFives             |" + self.fives + "|" + self.p2_fives + "|"  \
        + "\nSixes             |" + self.sixes + "|" + self.p2_sixes + "|"  \
        + "\nBonus             |" + self.bonus + "|" + self.p2_bonus + "|"  \
        + "\n---------------------------" \
        + "\nPair              |" + self.pair + "|" + self.p2_pair + "|" \
        + "\nTwo pair          |" + self.two_pairs + "|" + self.p2_two_pairs + "|"  \
        + "\nThree of a kind   |" + self.three_of_a_kind + "|" + self.p2_three_of_a_kind + "|" \
        + "\nFour of a kind    |" + self.four_of_a_kind + "|" + self.p2_four_of_a_kind + "|" \
        + "\nSmall straight    |" + self.small_straight + "|" + self.p2_small_straight + "|" \
        + "\nLarge straight    |" + self.large_straight + "|" + self.p2_large_straight + "|" \
        + "\nFull house        |" + self.fullhouse + "|" + self.p2_fullhouse + "|" \
        + "\nChance            |" + self.chance + "|" + self.p2_chance + "|" \
        + "\nYatzy             |" + self.yatzy + "|" + self.p2_yatzy + "|" \
        + "\nTotal             |" + self.sum + "|" + self.p2_sum + "|" \

