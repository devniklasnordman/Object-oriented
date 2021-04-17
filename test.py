import scorecard
from collections import Counter
import mechanics as gm

def main():

    picked = [5, 3, 5, 5, 6]
    my_list = []

    for item in picked:
        my_list.append(item)

    three_of_a_kind = []
    # sort list
    my_list.sort(reverse=True)
    print(my_list)
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
main()