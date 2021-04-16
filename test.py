import scorecard
from collections import Counter
import mechanics as gm

def main():
    which = "full house"
    my_list = [6, 5, 5, 6, 5]

    if which == "full house":
        pair_value = 0
        three_of_a_kind_value = 0
        pair = []
        three_of_a_kind = []
        to_continue = True
        # sort list
        my_list.sort()
        # iterate two elements from the start and end of the sorted list to find the 3 of a kind first
        # remove them from sorted list and move on to search for the remaining pair
        while to_continue:
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
                print("There are no full house. Select another score or rule out a result.")
                return None

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
                print("There are no full house. Select another score or rule out a result.")
                return None



            x = pair_value + three_of_a_kind_value

            return x
main()