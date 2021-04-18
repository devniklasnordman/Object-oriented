# File:         main.py
# Author:       Niklas Nordman
# Description:  Dice rolling game

import dice
import scorecard
import mechanics as gm


def main():
    print("Lets play a game of Yatzy!\n")


    while True:
        show_rules = input("Show rules? (yes/no)")
        if show_rules == "yes":
            return gm.rules()
        elif show_rules == "no":
            print("Ok then, lets go!")
            break
        else:
            print("You must choose 'yes' or 'no'.")
            continue

    # Player & turn amount defined
    player_amount = gm.player_amount()
    turn_amount = 15

    # Creating a scorecard object
    my_scorecard = scorecard.Scorecard()

    # Define scorecard by and delete excess players
    if player_amount == 1:
        my_scorecard.set_player_2("   |")
    else:
        pass

    old_total = 0
    # Start of the game loop
    lap = 1
    p1_used_scores = []
    p2_used_scores = []

    upper_total = 0
    p2_upper_total = 0

    p1_bonus = False
    p2_bonus = False

    for turns in range(turn_amount):

        # Player 1 turn
        print("\nPlayer 1's turn\nYour rolled: \n")
        one_turn = gm.roll_the_dices()

        print("Plyer 1 rolled", one_turn)
        print("Scorecard")
        print(my_scorecard)

        ## logic to add score to the scorecard ##

        score_or_dash = gm.score_or_dash()
        which_score = gm.which_score(p1_used_scores)

        # Checks validity and returns sum of result
        sum_to_scorecard = gm.set_score(one_turn, which_score, score_or_dash)
        sum_to_scorecard_type = type(sum_to_scorecard)

        # If user tries to enter a score that doesn't match the criteria the sum_to_scorecard keeps looping
        # until there is a match or the player picks to dash a score
        if score_or_dash == "score":
            while sum_to_scorecard_type != int:
                print("Your score did not match the criteria. Change to dash?")
                score_or_dash = gm.score_or_dash()
                which_score = gm.which_score(p1_used_scores)
                if score_or_dash == "dash":
                    break
                sum_to_scorecard = gm.set_score(one_turn, which_score, score_or_dash)
                sum_to_scorecard_type = type(sum_to_scorecard)


        # Convert integer into str so it can be placed in the scorecard
        sum_to_scorecard = str(sum_to_scorecard)

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
        else:
            print("Type in 'score' or 'dash'")
            continue

        # Bonus check and ignore the dashed and already added scores
        ones = my_scorecard.get_ones()
        check_ones = "ones"
        if check_ones not in p1_used_scores:
            if ones != " - ":
                ones_int = int(my_scorecard.get_ones())
                upper_total += ones_int
            else:
                pass
        else:
            pass

        twos = my_scorecard.get_twos()
        check_twos = "twos"
        if check_twos not in p1_used_scores:
            if twos != " - ":
                twos_int = int(my_scorecard.get_twos())
                upper_total += twos_int
            else:
                pass
        else:
            pass

        threes = my_scorecard.get_threes()
        check_threes = "threes"
        if check_threes not in p1_used_scores:
            if threes != " - ":
                threes_int = int(my_scorecard.get_threes())
                upper_total += threes_int
            else:
                pass
        else:
            pass

        fours = my_scorecard.get_fours()
        check_fours = "fours"
        if check_fours not in p1_used_scores:
            if fours != " - ":
                fours_int = int(my_scorecard.get_fours())
                upper_total += fours_int
            else:
                pass
        else:
            pass

        fives = my_scorecard.get_fives()
        check_fives = "fives"
        if check_fives not in p1_used_scores:
            if fives != " - ":
                fives_int = int(my_scorecard.get_fives())
                upper_total += fives_int
            else:
                pass
        else:
            pass

        sixes = my_scorecard.get_sixes()
        check_sixes = "sixes"
        if check_sixes not in p1_used_scores:
            if sixes != " - ":
                sixes_int = int(my_scorecard.sixes)
                upper_total += sixes_int
            else:
                pass
        else:
            pass


        if upper_total > 62 and not p1_bonus:
            my_scorecard.set_bonus("50 ")
            bonus_int = int(my_scorecard.get_bonus())
            old_total = int(my_scorecard.get_sum())
            updated_total = old_total + bonus_int
            updated_total_str = str(updated_total)
            my_scorecard.set_sum(updated_total_str)
            upper_total = updated_total
            p1_bonus = True

        # Update total points

        if score_or_dash == "score":
            to_add = int(sum_to_scorecard)
            old_total = int(my_scorecard.get_sum())
            updated_total = old_total + to_add

            if lap == 1 and score_or_dash == "score":
                if score_lenght == 1:
                    my_scorecard.set_sum(sum_to_scorecard + " ")
                else:
                    my_scorecard.set_sum("" + sum_to_scorecard + " ")
            else:
                pass

            if score_or_dash == "score":
                total_into_str = str(updated_total)
                total_length = len(total_into_str)
                if total_length == 1:
                    my_scorecard.set_sum(" " + total_into_str + " ")
                elif total_length == 2:
                    my_scorecard.set_sum(total_into_str + " ")
                else:
                    my_scorecard.set_sum(total_into_str)
            else:
                pass
        else:
            pass

        # After whole rolling turn put selected score into the used scores section
        p1_used_scores.append(which_score)
        print(my_scorecard)

        # Player 2 turn
        if player_amount > 1:
            print("\nPlayer 2's turn\nYour rolled: \n")
            one_turn = gm.roll_the_dices()

            print("Player 2 rolled", one_turn)
            print("Scorecard")
            print(my_scorecard)

            # logic to add score to the scorecard

            score_or_dash = gm.score_or_dash()
            which_score = gm.which_score(p2_used_scores)

            # Checks validity and returns sum of result
            sum_to_scorecard = gm.set_score(one_turn, which_score, score_or_dash)
            sum_to_scorecard_type = type(sum_to_scorecard)

            # If user tries to enter a score that doesn't match the criteria the sum_to_scorecard keeps looping
            # until there is a match or the player picks to dash a score
            if score_or_dash == "score":
                while sum_to_scorecard_type != int:
                    print("Your score did not match the criteria. Change to dash?")
                    score_or_dash = gm.score_or_dash()
                    which_score = gm.which_score(p2_used_scores)
                    if score_or_dash == "dash":
                        break
                    sum_to_scorecard = gm.set_score(one_turn, which_score, score_or_dash)
                    sum_to_scorecard_type = type(sum_to_scorecard)


            # Convert integer into str so it can be placed in the scorecard
            sum_to_scorecard = str(sum_to_scorecard)

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

            # Bonus check and ignore the dashed and already added scores
            p2_ones = my_scorecard.get_p2_ones()
            check_ones = "ones"
            if check_ones not in p2_used_scores:
                if p2_ones != " - ":
                    p2_ones_int = int(my_scorecard.get_p2_ones())
                    p2_upper_total += p2_ones_int
                else:
                    pass
            else:
                pass

            p2_twos = my_scorecard.get_p2_twos()
            check_twos = "twos"
            if check_twos not in p2_used_scores:
                if p2_twos != " - ":
                    p2_twos_int = int(my_scorecard.get_p2_twos())
                    p2_upper_total += p2_twos_int
                else:
                    pass
            else:
                pass

            p2_threes = my_scorecard.get_threes()
            check_threes = "threes"
            if check_threes not in p2_used_scores:
                if p2_threes != " - ":
                    p2_threes_int = int(my_scorecard.get_p2_threes())
                    p2_upper_total += p2_threes_int
                else:
                    pass
            else:
                pass

            p2_fours = my_scorecard.get_p2_fours()
            check_fours = "fours"
            if check_fours not in p2_used_scores:
                if p2_fours != " - ":
                    p2_fours_int = int(my_scorecard.get_p2_fours())
                    p2_upper_total += p2_fours_int
                else:
                    pass
            else:
                pass

            p2_fives = my_scorecard.get_p2_fives()
            check_fives = "fives"
            if check_fives not in p2_used_scores:
                if p2_fives != " - ":
                    p2_fives_int = int(my_scorecard.get_p2_fives())
                    p2_upper_total += p2_fives_int
                else:
                    pass
            else:
                pass

            p2_sixes = my_scorecard.get_p2_sixes()
            check_sixes = "sixes"
            if check_sixes not in p2_used_scores:
                if p2_sixes != " - ":
                    p2_sixes_int = int(my_scorecard.get_p2_sixes())
                    p2_upper_total += p2_sixes_int
                else:
                    pass
            else:
                pass

            if p2_upper_total > 62 and not p2_bonus:
                my_scorecard.set_p2_bonus("50 ")
                p2_bonus_int = int(my_scorecard.get_p2_bonus())
                p2_old_total = int(my_scorecard.get_p2_sum())
                p2_updated_total = p2_old_total + p2_bonus_int
                p2_updated_total_str = str(p2_updated_total)
                my_scorecard.set_p2_sum(p2_updated_total_str)
                p2_upper_total = p2_updated_total
                p2_bonus = True



            # Update total points

            if score_or_dash == "score":
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
                    p2_total_length = len(p2_total_into_str)
                    if p2_total_length == 1:
                        my_scorecard.set_p2_sum(" " + p2_total_into_str + " ")
                    elif p2_total_length == 2:
                        my_scorecard.set_p2_sum("" + p2_total_into_str + " ")
                    else:
                        my_scorecard.set_p2_sum(p2_total_into_str)
                else:
                    pass
            else:
                pass

            # Put selected score into the used scores section
            p2_used_scores.append(which_score)
            print(my_scorecard)
        lap += 1

    if player_amount > 1:
        if my_scorecard.get_sum() > my_scorecard.get_p2_sum():
            print("End of game. Player 1 wins with a total of " + my_scorecard.get_sum() + "!")
        else:
            print("End of game. Player 2 wins with a total of " + my_scorecard.get_p2_sum() + "!")

    else:
        print("End of game. You got " + my_scorecard.get_sum() + " points!")


main()
