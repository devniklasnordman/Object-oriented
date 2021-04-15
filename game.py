# File:         main.py
# Author:       Niklas Nordman
# Description:  Dice rolling game

import dice
import scorecard
import mechanics as gm


def main():
    print("Lets play a game of Yatzy!")

    # Player & turn amount defined
    player_amount = gm.player_amount()
    turn_amount = 15

    # Creating a scorecard object
    my_scorecard = scorecard.Scorecard()
    print(my_scorecard)
    # Define scorecard by and delete excess players
    if player_amount == 1:
        my_scorecard.set_player_2("   |")
    else:
        pass

    old_total = 0
    # Start of the game loop
    lap = 1

    for turns in range(turn_amount):


        # Player 1 turn
        print("\nPlayer 1's turn\nYour rolled: \n")
        one_turn = gm.roll_the_dices()

        print("You rolled", one_turn)
        print("Scorecard")
        print(my_scorecard)

        # while....

        # logic to add score to the scorecard
        score_or_dash = input("\nType 'score' or dash over one result from card"
                              "by typing 'dash' ")

        which_score = input("Select result to lock or dash (ex. 'ones')\n")

        # Checks validity and returns sum of result in string format
        sum_to_scorecard = str(gm.set_score(one_turn, which_score, score_or_dash))



        # Player 1 setting scorecard values, single digit scores have spaces on each side, but
        # double digit scores have a single space after it to maintain symmetry

        dash_to_scorecard = " - "
        score_lenght = len(sum_to_scorecard)
        if score_or_dash == "score":
            if which_score == "ones":
                if score_lenght == 1:
                    my_scorecard.set_ones(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_ones("" + sum_to_scorecard + " ")

            elif which_score == "twos":
                if score_lenght == 1:
                    my_scorecard.set_twos(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_twos("" + sum_to_scorecard + " ")

            elif which_score == "threes":
                if score_lenght == 1:
                    my_scorecard.set_threes(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_threes("" + sum_to_scorecard + " ")

            elif which_score == "fours":
                if score_lenght == 1:
                    my_scorecard.set_fours(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_fours("" + sum_to_scorecard + " ")

            elif which_score == "fives":
                if score_lenght == 1:
                    my_scorecard.set_fives(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_fives("" + sum_to_scorecard + " ")

            elif which_score == "sixes":
                if score_lenght == 1:
                    my_scorecard.set_sixes(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_sixes("" + sum_to_scorecard + " ")

            elif which_score == "pair":
                if score_lenght == 1:
                    my_scorecard.set_pair(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_pair("" + sum_to_scorecard + " ")

            elif which_score == "two pair":
                if score_lenght == 1:
                    my_scorecard.set_two_pairs(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_two_pairs("" + sum_to_scorecard + " ")

            elif which_score == "three of a kind":
                if score_lenght == 1:
                    my_scorecard.set_three_of_a_kind(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_three_of_a_kind("" + sum_to_scorecard + " ")

            elif which_score == "four of a kind":
                if score_lenght == 1:
                    my_scorecard.set_four_of_a_kind(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_four_of_a_kind("" + sum_to_scorecard + " ")

            elif which_score == "small straight":
                my_scorecard.set_small_straight(sum_to_scorecard + " ")

            elif which_score == "large straight":
                my_scorecard.set_large_straight(sum_to_scorecard + " ")

            elif which_score == "full house":
                if score_lenght == 1:
                    my_scorecard.set_fullhouse(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_fullhouse("" + sum_to_scorecard + " ")

            elif which_score == "chance":
                if score_lenght == 1:
                    my_scorecard.set_chance(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_chance("" + sum_to_scorecard + " ")

            elif which_score == "yatzy":
                my_scorecard.set_yatzy(sum_to_scorecard + " ")

            # Ruling over scores with dash

        elif score_or_dash == "dash":
            if which_score == "ones":
                my_scorecard.set_ones(dash_to_scorecard)

            elif which_score == "twos":
                my_scorecard.set_twos(dash_to_scorecard)

            elif which_score == "threes":
                my_scorecard.set_threes(dash_to_scorecard)

            elif which_score == "fours":
                my_scorecard.set_fours(dash_to_scorecard)

            elif which_score == "fives":
                my_scorecard.set_fives(dash_to_scorecard)

            elif which_score == "sixes":
                my_scorecard.set_sixes(dash_to_scorecard)

            elif which_score == "pair":
                my_scorecard.set_pair(dash_to_scorecard)

            elif which_score == "two pair":
                my_scorecard.set_two_pairs(dash_to_scorecard)

            elif which_score == "three of a kind":
                my_scorecard.set_three_of_a_kind(dash_to_scorecard)

            elif which_score == "four of a kind":
                my_scorecard.set_four_of_a_kind(dash_to_scorecard)

            elif which_score == "small straight":
                my_scorecard.set_small_straight(dash_to_scorecard)

            elif which_score == "large straight":
                my_scorecard.set_large_straight(dash_to_scorecard)

            elif which_score == "full house":
                my_scorecard.set_fullhouse(dash_to_scorecard)

            elif which_score == "chance":
                my_scorecard.set_chance(dash_to_scorecard)

            elif which_score == "yatzy":
                my_scorecard.set_yatzy(dash_to_scorecard)
            print(my_scorecard)
        else:
            print("Type in 'score' or 'dash'")
            continue


        # Update total points
        to_add = int(sum_to_scorecard)
        old_total = int(my_scorecard.get_sum())
        updated_total = old_total + to_add

        if lap == 1 and score_or_dash == "score":
            if score_lenght == 1:
                my_scorecard.set_sum(" " + sum_to_scorecard + " ")
            else:
                my_scorecard.set_sum("" + sum_to_scorecard + " ")
        else:
            pass

        if score_or_dash == "score":
            total_into_str = str(updated_total)
            if score_lenght == 1:
                my_scorecard.set_sum(" " + total_into_str + " ")
            else:
                my_scorecard.set_sum("" + total_into_str + " ")
        else:
            pass


        # Bonus check
        ones_int = int(my_scorecard.get_ones())
        twos_int = int(my_scorecard.get_twos())
        threes_int = int(my_scorecard.get_threes())
        fours_int = int(my_scorecard.get_fours())
        fives_int = int(my_scorecard.get_fives())
        sixes_int = int(my_scorecard.get_sixes())

        upper_total = ones_int + twos_int + threes_int + fours_int + fives_int + sixes_int

        if upper_total > 62:
            my_scorecard.set_bonus("50")
            bonus_int = int(my_scorecard.get_bonus())
            updated_total = old_total + bonus_int
            updated_total_str = str(updated_total)
            my_scorecard.set_sum(updated_total_str)

        print(my_scorecard)

        # Player 2 turn
        if player_amount > 1:
            print("\nPlayer 2's turn\nYour rolled: \n")
            one_turn = gm.roll_the_dices()

            print("You rolled", one_turn)
            print("Scorecard")
            print(my_scorecard)

            # while....

            # logic to add score to the scorecard
            score_or_dash = input("\nType 'score' or dash over one result from card"
                                  "by typing 'dash' ")

            which_score = input("Select result to lock or dash (ex. 'ones')\n")

            # Checks validity and returns sum of result in string format
            sum_to_scorecard = str(gm.set_score(one_turn, which_score, score_or_dash))

            # Player 2 setting scorecard values, single digit scores have spaces on each side, but
            # double digit scores have a single space after it to maintain symmetry

            dash_to_scorecard = " - "
            score_lenght = len(sum_to_scorecard)
            if score_or_dash == "score":
                if which_score == "ones":
                    if score_lenght == 1:
                        my_scorecard.set_p2_ones(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_ones("" + sum_to_scorecard + " ")

                elif which_score == "twos":
                    if score_lenght == 1:
                        my_scorecard.set_p2_twos(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_twos("" + sum_to_scorecard + " ")

                elif which_score == "threes":
                    if score_lenght == 1:
                        my_scorecard.set_p2_threes(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_threes("" + sum_to_scorecard + " ")

                elif which_score == "fours":
                    if score_lenght == 1:
                        my_scorecard.set_p2_fours(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_fours("" + sum_to_scorecard + " ")

                elif which_score == "fives":
                    if score_lenght == 1:
                        my_scorecard.set_p2_fives(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_fives("" + sum_to_scorecard + " ")

                elif which_score == "sixes":
                    if score_lenght == 1:
                        my_scorecard.set_p2_sixes(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_sixes("" + sum_to_scorecard + " ")

                elif which_score == "pair":
                    if score_lenght == 1:
                        my_scorecard.set_p2_pair(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_pair("" + sum_to_scorecard + " ")

                elif which_score == "two pair":
                    if score_lenght == 1:
                        my_scorecard.set_p2_two_pairs(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_two_pairs("" + sum_to_scorecard + " ")

                elif which_score == "three of a kind":
                    if score_lenght == 1:
                        my_scorecard.set_p2_three_of_a_kind(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_three_of_a_kind("" + sum_to_scorecard + " ")

                elif which_score == "four of a kind":
                    if score_lenght == 1:
                        my_scorecard.set_p2_four_of_a_kind(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_four_of_a_kind("" + sum_to_scorecard + " ")

                elif which_score == "small straight":
                    my_scorecard.set_p2_small_straight(sum_to_scorecard + " ")

                elif which_score == "large straight":
                    my_scorecard.set_p2_large_straight(sum_to_scorecard + " ")

                elif which_score == "full house":
                    if score_lenght == 1:
                        my_scorecard.set_p2_fullhouse(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_fullhouse("" + sum_to_scorecard + " ")

                elif which_score == "chance":
                    if score_lenght == 1:
                        my_scorecard.set_p2_chance(" " + sum_to_scorecard + " ")
                    else:
                        my_scorecard.set_p2_chance("" + sum_to_scorecard + " ")

                elif which_score == "yatzy":
                    my_scorecard.set_p2_yatzy(sum_to_scorecard + " ")

                # Ruling over scores with dash

            elif score_or_dash == "dash":
                if which_score == "ones":
                    my_scorecard.set_p2_ones(dash_to_scorecard)

                elif which_score == "twos":
                    my_scorecard.set_p2_twos(dash_to_scorecard)

                elif which_score == "threes":
                    my_scorecard.set_p2_threes(dash_to_scorecard)

                elif which_score == "fours":
                    my_scorecard.set_p2_fours(dash_to_scorecard)

                elif which_score == "fives":
                    my_scorecard.set_p2_fives(dash_to_scorecard)

                elif which_score == "sixes":
                    my_scorecard.set_p2_sixes(dash_to_scorecard)

                elif which_score == "pair":
                    my_scorecard.set_p2_pair(dash_to_scorecard)

                elif which_score == "two pair":
                    my_scorecard.set_p2_two_pairs(dash_to_scorecard)

                elif which_score == "three of a kind":
                    my_scorecard.set_p2_three_of_a_kind(dash_to_scorecard)

                elif which_score == "four of a kind":
                    my_scorecard.set_p2_four_of_a_kind(dash_to_scorecard)

                elif which_score == "small straight":
                    my_scorecard.set_p2_small_straight(dash_to_scorecard)

                elif which_score == "large straight":
                    my_scorecard.set_p2_large_straight(dash_to_scorecard)

                elif which_score == "full house":
                    my_scorecard.set_p2_fullhouse(dash_to_scorecard)

                elif which_score == "chance":
                    my_scorecard.set_p2_chance(dash_to_scorecard)

                elif which_score == "yatzy":
                    my_scorecard.set_p2_yatzy(dash_to_scorecard)
                print(my_scorecard)
            else:
                print("Type in 'score' or 'dash'")
                continue

            # Update total points
            p2_to_add = int(sum_to_scorecard)
            p2_old_total = int(my_scorecard.get_p2_sum())
            p2_updated_total = p2_old_total + p2_to_add

            if lap == 1 and score_or_dash == "score":
                if score_lenght == 1:
                    my_scorecard.set_p2_sum(" " + sum_to_scorecard + " ")
                else:
                    my_scorecard.set_p2_sum("" + sum_to_scorecard + " ")
            else:
                pass

            if score_or_dash == "score":
                p2_total_into_str = str(p2_updated_total)
                if score_lenght == 1:
                    my_scorecard.set_p2_sum(" " + p2_total_into_str + " ")
                else:
                    my_scorecard.set_p2_sum("" + p2_total_into_str + " ")
            else:
                pass

            # Bonus check
            p2_ones_int = int(my_scorecard.get_p2_ones())
            p2_twos_int = int(my_scorecard.get_p2_twos())
            p2_threes_int = int(my_scorecard.get_p2_threes())
            p2_fours_int = int(my_scorecard.get_p2_fours())
            p2_fives_int = int(my_scorecard.get_p2_fives())
            p2_sixes_int = int(my_scorecard.get_p2_sixes())

            p2_upper_total = p2_ones_int + p2_twos_int + p2_threes_int + p2_fours_int + p2_fives_int + p2_sixes_int

            if p2_upper_total > 62:
                my_scorecard.set_p2_bonus("50")
                p2_bonus_int = int(my_scorecard.get_p2_bonus())
                p2_updated_total = p2_old_total + p2_bonus_int
                p2_updated_total_str = str(p2_updated_total)
                my_scorecard.set_p2_sum(p2_updated_total_str)

            print(my_scorecard)
        else:
            pass

        lap += 1



    if player_amount > 1:
        if my_scorecard.get_sum() > my_scorecard.get_p2_sum():
            print("End of game. Player 1 wins with a total of" + my_scorecard.get_sum() + "!")
        else:
            print("End of game. Player 2 wins with a total of" + my_scorecard.get_p2_sum() + "!")

    else:
        print("End of game. You got " + my_scorecard.get_sum() + " points!")


main()
