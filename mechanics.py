# file: mechanins.py
# author: Niklas Nordman
# description: The main mechanics of the game in its own file



import dice
from collections import Counter
import scorecard

# Amount of players

my_scorecard = scorecard.Scorecard

def player_amount():
    while True:
        amount = input("How many players? (1-4):\n")
        if amount == "1" or "2" or "3" or "4":
            return int(amount)
        else:
            print("Error. Please input a number correct player amount")
            continue


# Arrange scoreboard

#### Rolling a single round and returning players picked dices in a list mechanics ###

def roll_the_dices():

    my_dice = dice.Dice()
    rolled_dices = []
    locked_dices = []

    dices_to_roll = 5
    rolls = 3
    to_continue = True
    lap = 1

    while rolls > 0 and to_continue:
        # Loop that performs one round of rolling for a player
        while dices_to_roll > 0:
            my_dice.roll_dice()
            rolled_dices.append(my_dice.get_side())
            dices_to_roll -= 1

        # Automated lock of dices on last turn
        if lap == 3:
            forced = forced_lock(rolled_dices)
            locked = locked_pick(rolled_dices, forced, lap)
            locked_dices.append(locked)
            final_dices = single_list(locked_dices)
            return final_dices


        # Print shows the rolled dices in a list
        print(rolled_dices)

        # Function that converts the amount of list items into an integer
        amount = amount_of_dices(rolled_dices)

        # Function that prints out the selection of dices to pick
        dices_to_pick(amount)

        # Selects the locked dices and returns the index numbers of locked items
        picked = picked_dices(amount)

        # Makes a list out of the selected dices and shows them
        locked = locked_pick(rolled_dices, picked, lap)
        lap += 1

        # Add the locked numbers to the list of "rolled_dices"
        locked_dices.append(locked)
        print("\nAll locked dices during this turn: ", locked_dices)

        # Reduces the amount of rolls available to the player
        rolls -= 1
        print(rolls, " rolls left...")
        if rolls < 1:
            break


        # Convert locked dices list into integer
        locked_int = amount_of_dices(locked)

        # Reduces the amount of dices to roll on the next round
        leftover_dices = len(rolled_dices) - locked_int
        print("You have ", leftover_dices , " dices left for next round.\n")
        ask_to_continue = input("Throw more (yes/no)")
        final_dices = single_list(locked_dices)
        if len(final_dices) > 4:
            return final_dices

        elif ask_to_continue == "yes":
            dices_to_roll = leftover_dices
            rolled_dices = []
            pass
        elif ask_to_continue == "no":
            if not locked:
                forced = forced_lock(rolled_dices)
                locked = locked_pick(rolled_dices, forced, lap)
                locked_dices.append(locked)
                final_dices = single_list(locked_dices)
                return final_dices

    final_dices = single_list(locked_dices)


    #print(rolled_dices)





    print("\nOut of rolls. Place score in to the scorecard -->")
    print("Dices left to throw: ")
    print(final_dices)

    return final_dices

# Converting the amount of list items into an integer
def amount_of_dices(x):
    amount = len(x)
    return amount

# A loop that prints out the amount of arrows pointing at the rolled dices
def dices_to_pick(x):
    for item in range(x):
        print(" ▲", end=" ")


    print("\n")
    y = 1
    for item in range(x):

        print("", y, end=" ")
        x -= 1
        y += 1

def picked_dices(roll):
    locked_dices = []

    throws = roll
    print("\nLock the dices of your pick and throw the rest again."
          "\nPress 0 to stop locking dices.\n")

    while throws > 0:
            pick = int(input("Pick a dice: "))
            if pick == 0:
                break

            elif pick > roll or pick < 0:
                print("That dice doesn't exist. Pick a index number between 1 -", roll )
                continue

            else:
                throws -= 1
                pick -= 1
                locked_dices.append(pick)

    return locked_dices


# Locks down the dices that the player chooses to keep
def locked_pick(rolled_dices, picked_dices, lap):
    locked = []

    for index in picked_dices:
        locked.append(rolled_dices[index])
    print("\nlocked dices on roll", lap)
    print(locked)
    return locked

# Converting players picks from multiple lists to a singular list
def single_list(locked_list):
    # make three lists into one single list
    single_list = []
    for turn_locked in locked_list:
        for item in turn_locked:
            single_list.append(item)
    return single_list

def forced_lock(rolled_dices):
    print("Out of rolls")
    last_lock = []
    amount = len(rolled_dices)
    pick = 1
    while amount > 0:
        amount -= 1
        pick -= 1
        last_lock.append(pick)

    return last_lock


#### Implementing the players picked dices into the scorecard mechanics ###

def set_score(picked, which_score, score_or_dash):


    total = 0
    list_lenght = len(picked)

    # The function parameter 'picked' is referred as my_list since a separate object is needed for list manipulation

    my_list = []
    for item in picked:
        my_list.append(item)

    while list_lenght > 0:
        if score_or_dash == "score":
            if which_score == "ones":
                amount = my_list.count(1) * 1
                return amount

            elif which_score == "twos":
                amount = my_list.count(2) * 2
                return amount


            elif which_score == "threes":
                amount = my_list.count(3) * 3
                return amount

            elif which_score == "fours":
                amount = my_list.count(4) * 4
                return amount


            elif which_score == "fives":
                amount = my_list.count(5) * 5
                return amount


            elif which_score == "sixes":
                amount = my_list.count(6) * 6
                return amount


            elif which_score == "pair":
                # sort list in reverse so the highest values in the beginning
                my_list.sort(reverse=True)
                pair = 0
                # iterate from highest value searching for the pair to occur
                for i in my_list:
                    if my_list[0] == my_list[1]:
                        pair = my_list[0] + my_list[1]
                        return pair
                    elif my_list[1] == my_list[2]:
                        pair = my_list[1] + my_list[2]
                        return pair
                    elif my_list[2] == my_list[3]:
                        pair = my_list[2] + my_list[3]
                        return pair
                    elif my_list[3] == my_list[4]:
                        pair = my_list[3] + my_list[4]
                        return pair
                    else:
                        print("There are no pairs. Select another score or rule out a result.")
                        return None

            elif which_score == "two pair":
                pair_1_value = 0
                pair_2_value = 0
                pair_1 = []
                pair_2 = []
                to_continue = True
                # sort list in reverse so the highest values in the beginning
                my_list.sort(reverse=True)
                pair = 0
                # iterate from highest value searching for the pair to occur, and then add first pair to a list of its
                # own and remove first pair from the original list
                # while loop needed for stopping iteration after a hit
                while to_continue:
                    if my_list[0] == my_list[1]:
                        pair_1.append(my_list[0])
                        pair_1.append(my_list[1])
                        my_list.remove(my_list[0])
                        my_list.remove(my_list[0])
                        pair_1_value = sum(pair_1)
                        to_continue = False

                    elif my_list[1] == my_list[2]:
                        pair_1.append(my_list[1])
                        pair_1.append(my_list[2])
                        my_list.remove(my_list[1])
                        my_list.remove(my_list[1])
                        pair_1_value = sum(pair_1)
                        to_continue = False

                    elif my_list[2] == my_list[3]:
                        pair_1.append(my_list[2])
                        pair_1.append(my_list[3])
                        my_list.remove(my_list[2])
                        my_list.remove(my_list[2])
                        pair_1_value = sum(pair_1)
                        to_continue = False

                    elif my_list[3] == my_list[4]:
                        pair_1.append(my_list[3])
                        pair_1.append(my_list[4])
                        my_list.remove(my_list[3])
                        my_list.remove(my_list[3])
                        pair_1_value = sum(pair_1)
                        to_continue = False
                    else:
                        print("There are no two pairs. Select another score or rule out a result.")
                        return None

                # iterate the rest on my_list containing 3 elements
                to_continue = True
                while to_continue:
                    if my_list[0] == my_list[1]:
                        pair_2.append(my_list[0] + my_list[1])
                        print(pair_2)
                        my_list.remove(my_list[0])
                        my_list.remove(my_list[0])
                        pair_2_value = sum(pair_2)
                        to_continue = False

                    elif my_list[1] == my_list[2]:
                        pair_2.append(my_list[1] + my_list[2])
                        my_list.remove(my_list[1])
                        my_list.remove(my_list[1])
                        pair_2_value = sum(pair_2)
                        to_continue = False
                    else:
                        print("There are no two pairs. Select another score or rule out a result.")
                        return None

                x = pair_1_value + pair_2_value
                return x


            elif which_score == "three of a kind":
                three_of_a_kind = []
                # sort list
                my_list.sort()
                # iterate the sorted list from index 0-2 & 4-2 and test for three of a kind

                if my_list[0] == my_list[1] == my_list[2]:
                    three_of_a_kind.append(my_list[0])
                    three_of_a_kind.append(my_list[1])
                    three_of_a_kind.append(my_list[2])
                    three_of_a_kind_value = sum(three_of_a_kind)
                    return three_of_a_kind_value

                elif my_list[4] == my_list[3] == my_list[2]:
                    three_of_a_kind.append(my_list[4])
                    three_of_a_kind.append(my_list[3])
                    three_of_a_kind.append(my_list[2])
                    three_of_a_kind_value = sum(three_of_a_kind)
                    return  three_of_a_kind_value

                else:
                    print("There are no three of a kind. Select another score or rule out a result.")
                    return None


            elif which_score == "four of a kind":
                four_of_a_kind = []
                # sort list
                my_list.sort()
                # iterate the sorted list from index 0-3 & 4-1 and test for four of a kind

                if my_list[0] == my_list[1] == my_list[2] == my_list[3]:
                    four_of_a_kind.append(my_list[0])
                    four_of_a_kind.append(my_list[1])
                    four_of_a_kind.append(my_list[2])
                    four_of_a_kind.append(my_list[3])
                    four_of_a_kind_value = sum(four_of_a_kind)
                    return four_of_a_kind_value

                elif my_list[4] == my_list[3] == my_list[2] == my_list[1]:
                    four_of_a_kind.append(my_list[4])
                    four_of_a_kind.append(my_list[3])
                    four_of_a_kind.append(my_list[2])
                    four_of_a_kind.append(my_list[1])
                    four_of_a_kind_value = sum(four_of_a_kind)
                    return four_of_a_kind_value

                else:
                    print("There are no four of a kind. Select another score or rule out a result.")
                    return None


            elif which_score == "small straight":
                sum_of_ss = 15
                if 1 and 2 and 3 and 4 and 5 in my_list:
                    return sum_of_ss


            elif which_score == "large straight":
                sum_of_ls = 20
                if 6 and 2 and 3 and 4 and 5 in my_list:
                    return sum_of_ls

            elif which_score == "full house":
                pair_value = 0
                three_of_a_kind_value = 0
                pair = []
                three_of_a_kind = []
                to_continue = True
                # sort list
                my_list.sort()

                # iterate two elements from the start and end of the sorted list to find the pair first
                # remove them from sorted list and move on to search for the remaining 3 of a kind
                while to_continue:
                    if my_list[0] == my_list[1]:
                        pair.append(my_list[0])
                        pair.append(my_list[1])
                        my_list.remove(my_list[0])
                        my_list.remove(my_list[0])
                        pair_value = sum(pair)
                        to_continue = False

                    elif my_list[4] == my_list[3]:
                        pair.append(my_list[4])
                        pair.append(my_list[3])
                        my_list.remove(my_list[4])
                        my_list.remove(my_list[4])
                        pair_value = sum(pair)
                        to_continue = False

                    else:
                        print("There are no full house. Select another score or rule out a result.")
                        return None

                    if my_list[0] == my_list[1] == my_list[2]:
                        three_of_a_kind.append(my_list[0])
                        three_of_a_kind.append(my_list[1])
                        three_of_a_kind.append(my_list[2])
                        three_of_a_kind_value = sum(three_of_a_kind)
                    else:
                        print("There are no full house. Select another score or rule out a result.")
                        return None

                    x = pair_value + three_of_a_kind_value
                    return x


            elif which_score == "chance":
                for item in my_list:
                    total = sum(my_list)

                return total

            elif which_score == "yatzy":
                x = picked[0]
                counter = Counter(picked)
                total = 50
                if counter == {x: 5}:
                    return total

        else:
            break
