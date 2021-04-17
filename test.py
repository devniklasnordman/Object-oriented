import scorecard
from collections import Counter
import mechanics as gm

def main():

    picked = [3, 3, 3, 3, 3]
    my_list = []

    for item in picked:
        my_list.append(item)

    x = my_list[0]
    counter = Counter(my_list)
    total = 50
    if counter == {x: 5}:
        print("hello")
        return total
    else:
        print("This is not yatzy. Pick again..")
        return False
main()