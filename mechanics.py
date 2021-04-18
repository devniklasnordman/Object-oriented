# file: mechanins.py
# author: Niklas Nordman
# description: The main mechanics of the game in its own file


import dice
from collections import Counter
import scorecard


# Rules

def rules():
    print("Player with the highest points wins!\n\nIn each round, a player gets three rolls of the dice,"
          " although they can choose to end their turn after one or two rolls."
          "\nAfter the first roll the player can save any dice they want and re-roll the other dice."
          "\nThis procedure is repeated after the second roll. The player has complete choice as to which dice to roll."
          "\nIt is possible to re-roll both dice that were or were not rolled before. \n"
          "\nThe Yatzy scorecard contains 15 different category boxes divided into upper and lower sections."
          "\nIn each round, after the third roll, the player must choose one of these categories."
          "\nThe score entered in the box depends on how well the five dice match the scoring rule for the category.\n"
          "\nAs an example, one of the categories is called Three of a Kind."
          "\nThe scoring rule for this category means that a player only scores if at least three of the five dice"
          "\nare the same value. If your score does not match any criteria on the available scorecard slots"
          " \nthen you have to dash one of your slots. \n"
          "\nThe game is completed after 15 rounds by each player, with each of the 15 boxes filled."
          "\nThe total score is calculated by summing all fifteen boxes, together with any bonuses. \n"
          "\nEarn a 50 points Bonus from the upper section by having over 62 points from all of the upper boxes summed "
          "\n(you get it by rolling at least 3 items in every upper box) "
          "\nYatzy means 5 of a kind and it is worth 50 points. "
          "\nThe Yatzy scorecard contains 15 scoring boxes divided into upper and lower sections.")

# Amount of players

def player_amount():
    while True:
        amount = input("\nSolo or duo? \n(type player amount 1 or 2):\n")
        if amount == "1" or "2":
            try:
                amount = int(amount)
                return amount
            except:
                print("Error. Please input a correct player amount")
        else:
            pass


#### Rolling a single round and returning players picked dices in a list mechanics ###

def roll_the_dices():
    my_dice = dice.Dice()
    locked_dices = []

    dices_to_roll = 5
    rolls = 3
    to_continue = True
    lap = 1

    while rolls > 0 and to_continue:
        rolled_dices = []
        # Loop that performs one round of rolling for a player
        while dices_to_roll > 0:
            my_dice.roll_dice()
            rolled_dices.append(my_dice.get_side())
            dices_to_roll -= 1

        # Automated roll and lock of dices on last turn
        if lap == 3:
            forced = forced_lock(rolled_dices)
            locked = locked_pick(rolled_dices, forced, lap)
            locked_dices.append(locked)
            final_dices = locked_dices
            final_len = len(final_dices)
            if final_len > 1:
                final_dices = single_list(final_dices)
            return final_dices

        # Print shows the rolled dices in a list
        print(rolled_dices)

        # Function that converts the amount of list items into an integer
        amount = amount_of_dices(rolled_dices)

        # Function that prints out the selection arrows of dices to pick
        dices_to_pick(amount)

        # Player selects the locked dices and function returns the index numbers of locked items
        picked = picked_dices(amount)

        # Makes a list out of the selected dices and shows them
        locked = locked_pick(rolled_dices, picked, lap)
        lap += 1

        # Add the locked dices to the list of "locked_dices" and convert it into a single list
        locked_dices.append(locked)

        # Show all locked dices during the turn in a single list format
        single = single_list(locked_dices)
        print("\nAll locked dices during this turn: ", single)

        # Convert locked dices list item amount into integer
        locked_int = amount_of_dices(locked)

        # If player chooses to lock all five dices the round ends immediately
        if locked_int == 5:
            print("\nPlace score in to the scorecard -->")
            final_dices = single_list(locked_dices)

            return final_dices

        # Reduces the amount of rolls available to the player
        rolls -= 1
        print(rolls, " rolls left...")
        if rolls < 1:
            break

        # Reduces the amount of dices to roll on the next round
        leftover_dices = len(rolled_dices) - locked_int
        print("You have ", leftover_dices, " dices left for next round.\n")

        # Asks if  player wants to keep rolling
        ask_to_continue = continue_or_no()

        # if player locks insufficient amount of dices and has rolls left
        # the dices on board will be automatically picked and the turn ends
        length = len(single)
        if ask_to_continue == "no" and length < 5:
            if len(single) == 5:
                return single
            else:
                for element in single:
                    if element in rolled_dices:
                        rolled_dices.remove(element)
                locked_dices.append(rolled_dices)
                final_dices = single_list(locked_dices)
                return final_dices


        # If player has already locked 5 dices the turn ends
        elif len(locked_dices) > 4:
            return locked_dices

        elif ask_to_continue == "yes":
            # Asks if player wants to reset locked dices before next roll
            reset = reset_or_no()
            if reset == "yes":
                single = single_list(locked_dices)
                reseted_dices = reset_dices(single)
                locked_dices = []
                if len(reseted_dices) == 0:
                    pass
                locked_dices.append(reseted_dices)
                single = single_list(locked_dices)
                leftover_dices = 5 - len(single)
            else:
                pass

            # Subtracts amount of locked dices from the amount of dices to roll on next round
            dices_to_roll = leftover_dices
            # Resets rolled dices list ready for next roll
            rolled_dices = []
            print("\nRoll number ", lap, " starts. \nrolling...")
            continue
        elif ask_to_continue == "no":
            if len(single) == 5:
                return single
            elif not locked and lap == 3:
                forced = forced_lock(rolled_dices)
                locked = locked_pick(rolled_dices, forced, lap)
                locked_dices.append(locked)
                final_dices = single_list(locked_dices)
                return final_dices

    final_dices = single_list(locked_dices)

    # print(rolled_dices)

    print("\nOut of rolls. Place score in to the scorecard -->")
    print("Dices left to throw: ")
    print(final_dices)

    return final_dices


## Mechanics used in the one turn of rolling ##

# Resetting locked dices takes the locked list and its length as parameter
def reset_dices(locked):
    print("These are your locked dices:", locked)
    locked_len = len(locked)
    while True:
        if locked_len == 0:
            return locked
        else:
            pass

        to_remove = reset_as_int()

        if to_remove == 0:
            return locked
        else:
            pass

        for item in locked:
            if item == to_remove:
                locked.remove(item)
                locked_len -= 1
                print("Locked dices after removal:", locked)
                break
            else:
                continue

def reset_as_int():
    while True:
        answer = input("Please enter a dice to remove (1-6):\n(Exit by pressing 0)  ")
        if answer == "1" or "2" or "3" or "4" or "5" or "6":
            try:
                answer = int(answer)
                return answer
            except:
                print("Incorrect value. Try again!")
        else:
            pass
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
        pick = input("Pick a dice: ")
        try:
            pick = int(pick)
        except:
            continue
        if pick == 0:
            #print("Please choose a number between 1 and ", throws)
            break

        elif pick > roll or pick < 0:
            print("That dice doesn't exist. Pick a index number between 1 -", roll)
            continue

        else:
            throws -= 1
            pick -= 1
            if pick not in locked_dices:
                locked_dices.append(pick)
            else:
                print("You already selected that dice. Try again!")

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


# Force append to locked list of leftover dices
def forced_lock(rolled_dices):
    last_lock = []
    amount = len(rolled_dices)
    pick = 1
    while amount > 0:
        amount -= 1
        pick -= 1
        last_lock.append(pick)

    return last_lock


# Ensure that the answer is exactly 'yes' or 'no'
def continue_or_no():
    while True:
        ask_to_continue = input("Throw more? (yes/no)")
        if ask_to_continue == "yes":
            return ask_to_continue
        elif ask_to_continue == "no":
            return ask_to_continue
        else:
            print("You must choose 'yes' or 'no'.")
            continue


# Ensure that the answer is exactly 'score' or 'dash'
def score_or_dash():
    while True:
        answer = input("\nType 'score' or dash over one result from card "
                       "by typing 'dash' ")
        if answer == "score":
            return answer
        elif answer == "dash":
            return answer
        else:
            print("You must choose 'score' or 'dash'.")
            continue


# Ensure that the answer is exactly one of the slots in scoreboard and is not already used in order to continue
def which_score(used):
    while True:
        which = input("Select result to lock or dash (ex. 'ones')")
        if which == "ones":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "twos":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "threes":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "fours":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "fives":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "sixes":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "pair":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "two pair":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "three of a kind":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "four of a kind":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "small straight":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "large straight":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "full house":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "chance":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "yatzy":
            if which in used:
                print("Used value. Pick another one or change score to dash by typing 'dash'")
                continue
            else:
                return which
        elif which == "dash":
            print("You changed score to dash.")
            return which
        else:
            print("Incorrect or already used value. Please enter a valid score in lower case. For example 'ones'"
                  "\nIf you can not assign your score anywhere you can change to dashing by typing 'dash'")
            continue

def reset_or_no():
    while True:
        answer = input("\nReset locked dices before next roll? (yes/no)")
        if answer == "yes":
            return answer
        elif answer == "no":
            return answer
        else:
            print("You must choose 'yes' or 'no'.")
            continue







#### Implementing the players picked dices into the scorecard mechanics ###

def set_score(picked, which, score_or_dash):
    total = 0
    list_length = len(picked)

    # The function parameter 'picked' is referred as my_list since a separate object is needed for list manipulation

    my_list = []
    for item in picked:
        my_list.append(item)

    while list_length > 0:
        if score_or_dash == "score":

            if which == "ones":
                ones_bool = False
                for item in my_list:
                    if item == 1:
                        ones_bool = True
                if ones_bool:
                    amount = my_list.count(1) * 1
                    return amount
                # Return False if there are no ones at all
                else:
                    return False

            elif which == "twos":
                twos_bool = False
                for item in my_list:
                    if item == 2:
                        twos_bool = True
                if twos_bool:
                    amount = my_list.count(2) * 2
                    return amount
                else:
                    return False

            elif which == "threes":
                threes_bool = False
                for item in my_list:
                    if item == 3:
                        threes_bool = True
                if threes_bool:
                    amount = my_list.count(3) * 3
                    return amount
                else:
                    return False

            elif which == "fours":
                fours_bool = False
                for item in my_list:
                    if item == 4:
                        fours_bool = True
                if fours_bool:
                    amount = my_list.count(4) * 4
                    return amount
                else:
                    return False

            elif which == "fives":
                fives_bool = False
                for item in my_list:
                    if item == 5:
                        fives_bool = True
                if fives_bool:
                    amount = my_list.count(5) * 5
                    return amount
                else:
                    return False

            elif which == "sixes":
                sixes_bool = False
                for item in my_list:
                    if item == 6:
                        sixes_bool = True
                if sixes_bool:
                    amount = my_list.count(6) * 6
                    return amount
                else:
                    return False

            elif which == "pair":
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
                        print("This is not pair. Pick again..")
                        return False

            elif which == "two pair":
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
                        print("This is not two pairs. Pick again..")
                        return False

                # iterate the rest on my_list containing 3 elements
                to_continue = True
                while to_continue:
                    if my_list[0] == my_list[1]:
                        pair_2.append(my_list[0] + my_list[1])
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
                        print("This is not two pairs. Pick again.")
                        return False

                x = pair_1_value + pair_2_value
                return x

            elif which == "three of a kind":
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

                elif my_list[1] == my_list[2] == my_list[3]:
                    three_of_a_kind.append(my_list[1])
                    three_of_a_kind.append(my_list[2])
                    three_of_a_kind.append(my_list[3])
                    three_of_a_kind_value = sum(three_of_a_kind)
                    return three_of_a_kind_value

                elif my_list[4] == my_list[3] == my_list[2]:
                    three_of_a_kind.append(my_list[4])
                    three_of_a_kind.append(my_list[3])
                    three_of_a_kind.append(my_list[2])
                    three_of_a_kind_value = sum(three_of_a_kind)
                    return three_of_a_kind_value

                else:
                    print("There are no three of a kind. Select another score or rule out a result.")
                    return False

            elif which == "four of a kind":
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
                    print("This is not four of a kind. Pick again...")
                    return False

            elif which == "small straight":
                sum_of_ss = 15
                if 1 and 2 and 3 and 4 and 5 in my_list:
                    return sum_of_ss
                else:
                    print("This is not small straight. Pick again..")
                    return False

            elif which == "large straight":
                sum_of_ls = 20
                if 6 and 2 and 3 and 4 and 5 in my_list:
                    return sum_of_ls
                else:
                    print("This is not large straight. Pick again..")
                    return False

            elif which == "full house":
                pair_value = 0
                three_of_a_kind_value = 0
                pair = []
                three_of_a_kind = []

                # sort list
                my_list.sort()
                # iterate three elements from the start and end of the sorted list to find the 3 of a kind first
                # remove them from sorted list and move on to search for the remaining pair

                if my_list[0] == my_list[1] == my_list[2]:
                    three_of_a_kind.append(my_list[0])
                    three_of_a_kind.append(my_list[1])
                    three_of_a_kind.append(my_list[2])

                    my_list.remove(my_list[0])
                    my_list.remove(my_list[0])
                    my_list.remove(my_list[0])

                    three_of_a_kind_value = sum(three_of_a_kind)

                elif my_list[4] == my_list[3] == my_list[2]:
                    three_of_a_kind.append(my_list[4])
                    three_of_a_kind.append(my_list[3])
                    three_of_a_kind.append(my_list[2])

                    my_list.remove(my_list[4])
                    my_list.remove(my_list[3])
                    my_list.remove(my_list[2])

                    three_of_a_kind_value = sum(three_of_a_kind)
                else:
                    print("This is not full house. Pick again..")
                    return False

                if my_list[0] == my_list[1]:
                    pair.append(my_list[0])
                    pair.append(my_list[1])

                    my_list.remove(my_list[0])
                    my_list.remove(my_list[0])

                    pair_value = sum(pair)


                elif my_list[4] == my_list[3]:
                    pair.append(my_list[4])
                    pair.append(my_list[3])
                    my_list.remove(my_list[4])
                    my_list.remove(my_list[4])
                    pair_value = sum(pair)



                else:
                    print("This is not full house. Pick again..")
                    return False



                x = pair_value + three_of_a_kind_value

                return x

            elif which == "chance":
                for item in my_list:
                    total = sum(my_list)

                return total

            elif which == "yatzy":
                x = my_list[0]
                counter = Counter(my_list)
                total = 50
                if counter == {x: 5}:
                    return total
                else:
                    print("This is not yatzy. Pick again..")
                    return False

        else:
            return False
