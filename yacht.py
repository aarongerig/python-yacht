# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list, category: int):
    total = 0
    unique = sorted(set(dice))
    first = unique[0]
    last = unique[-1]
    count = len(unique)
    count_first = dice.count(first)
    count_last = dice.count(last)

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        total = category * dice.count(category)
    elif category == FULL_HOUSE and count == 2 and count_first >= 2 and count_last >= 2:
        total = sum(dice)
    elif category == FOUR_OF_A_KIND and count <= 2:
        if count_first >= 4:
            total = first * 4
        elif count_last >= 4:
            total = last * 4
    elif (category == LITTLE_STRAIGHT and count == 5 and 6 not in unique) or\
            (category == BIG_STRAIGHT and count == 5 and 1 not in unique):
        total = 30
    elif category == CHOICE:
        total = sum(dice)
    elif category == YACHT and count == 1:
        total = 50

    return total
