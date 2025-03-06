import math
from typing import Tuple

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 20: Infinite Elves and Infinite Houses ---

https://adventofcode.com/2015/day/20
""")

    fp = open('inputs/day20.txt', 'r')
    gift_threshold = int(fp.read())
    fp.close()

    visits = {}
    house_limit = 50

    def gift_counts(n: int) -> Tuple[int, int]:
        divisors = {}
        limited_divisors = {}

        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                for a in [i, n // i]:
                    divisors[a] = True

                    if a not in visits:
                        visits[a] = 0

                    if visits[a] < house_limit:
                        limited_divisors[a] = True
                        visits[a] += 1

        return sum(divisors.keys()) * 10, sum(limited_divisors.keys()) * 11

    house_no = 0
    lowest_house_no_one = None
    lowest_house_no_two = None

    while True:
        house_no += 1
        gift_count_one, gift_count_two = gift_counts(house_no)

        if lowest_house_no_one is None and gift_count_one >= gift_threshold:
            lowest_house_no_one = house_no

        if lowest_house_no_two is None and gift_count_two >= gift_threshold:
            lowest_house_no_two = house_no

        if lowest_house_no_one is not None and lowest_house_no_two is not None:
            break

    assert lowest_house_no_one == 831_600
    assert lowest_house_no_two == 884_520

    print('Part One: ' + str(lowest_house_no_one))
    print('Part Two: ' + str(lowest_house_no_two))
