# Player 1 turn
        print("\nPlayer 1's turn\nYour rolled: \n")
        one_turn = gm.roll_the_dices()

        print("You rolled", one_turn)
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
        while sum_to_scorecard_type != int:
            print("Your score did not match the criteria. Change to dash?")
            score_or_dash = gm.score_or_dash()
            which_score = gm.which_score(p1_used_scores)
            if score_or_dash == "dash":
                break
            sum_to_scorecard = gm.set_score(one_turn, which_score, score_or_dash)
            sum_to_scorecard_type = type(sum_to_scorecard)

        # After validating the result to scorecard put the selection into the used scores section
        p1_used_scores.append(which_score)
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


        # Update total points

        if score_or_dash == "score":
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
        else:
            pass

        # Bonus check and ignore the dashed scores
        upper_total = 0
        ones = my_scorecard.get_ones()
        if ones != " - ":
            ones_int = int(my_scorecard.get_ones())
            upper_total += ones_int
        else:
            pass

        twos = my_scorecard.get_twos()
        if twos != " - ":
            twos_int = int(my_scorecard.get_twos())
            upper_total += twos_int
        else:
            pass

        threes = my_scorecard.get_threes()
        if threes != " - ":
            threes_int = int(my_scorecard.get_threes())
            upper_total += threes_int
        else:
            pass

        fours = my_scorecard.get_fours()
        if fours != " - ":
            fours_int = int(my_scorecard.get_fours())
            upper_total += fours_int
        else:
            pass

        fives = my_scorecard.get_fives()
        if fives != " - ":
            fives_int = int(my_scorecard.get_fives())
            upper_total += fives_int
        else:
            pass

        sixes = my_scorecard.get_sixes()
        if sixes != " - ":
            sixes_int = int(my_scorecard.sixes)
            upper_total += sixes_int
        else:
            pass



        if upper_total > 62:
            my_scorecard.set_bonus("50")
            bonus_int = int(my_scorecard.get_bonus())
            updated_total = old_total + bonus_int
            updated_total_str = str(updated_total)
            my_scorecard.set_sum(updated_total_str)

        print(my_scorecard)