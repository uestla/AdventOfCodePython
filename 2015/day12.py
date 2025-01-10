import json

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 12: JSAbacusFramework.io ---

https://adventofcode.com/2015/day/12
""")

    fp = open('inputs/day12.txt', 'r')
    data = json.load(fp)
    fp.close()

    total_sum_one = 0
    total_sum_two = 0

    def count_numbers(obj, is_red) -> None:
        global total_sum_one, total_sum_two

        if isinstance(obj, int):
            total_sum_one += obj

            if not is_red:
                total_sum_two += obj

        elif isinstance(obj, list):
            for item in obj:
                count_numbers(item, is_red)

        elif isinstance(obj, dict):
            has_red = 'red' in obj.values()

            for key in obj:
                count_numbers(obj[key], is_red or has_red)

    count_numbers(data, False)

    assert total_sum_one == 156_366
    assert total_sum_two == 96_852

    print('Part One: ' + str(total_sum_one))
    print('Part Two: ' + str(total_sum_two))
