if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 1: Not Quite Lisp ---

https://adventofcode.com/2015/day/1
""")

    fp = open('inputs/day1.txt', 'r')

    floor = 0
    char_pos = 0
    basement_pos = None

    for line in fp:
        for c in line:
            floor += 1 if c == '(' else -1

            if basement_pos is None:
                char_pos += 1

                if floor == -1:
                    basement_pos = char_pos

    fp.close()

    assert floor == 232
    assert basement_pos == 1_783

    print('Part One: ' + str(floor))
    print('Part Two: ' + str(basement_pos))
