if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 2: I Was Told There Would Be No Math ---

https://adventofcode.com/2015/day/2
""")

    fp = open('inputs/day2.txt', 'r')

    total_area = 0
    ribbon_length = 0

    for line in fp:
        a, b, c = sorted(map(int, line.split('x', 3)))

        area1 = a * b
        area2 = a * c
        area3 = b * c

        total_area += 2 * area1 + 2 * area2 + 2 * area3 + min(area1, area2, area3)
        ribbon_length += a * b * c + 2 * a + 2 * b

    fp.close()

    assert total_area == 1_586_300
    assert ribbon_length == 3_737_498

    print('Part One: ' + str(total_area))
    print('Part Two: ' + str(ribbon_length))
