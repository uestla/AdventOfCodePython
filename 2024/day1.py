if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 1: Historian Hysteria ---

https://adventofcode.com/2024/day/1
""")

    fp = open('inputs/day1.txt', 'r')

    lefts = []
    rights = []
    right_counts = {}

    for line in fp:
        left, right = map(int, line.split())
        lefts.append(left)

        rights.append(right)
        right_counts[right] = right_counts[right] + 1 if right in right_counts else 1

    fp.close()

    lefts.sort()
    rights.sort()

    distance = 0
    similarity = 0

    for index, a in enumerate(lefts):
        distance += abs(a - rights[index])
        similarity += a * (right_counts[a] if a in right_counts else 0)

    assert distance == 1_666_427
    assert similarity == 24_316_233

    print('Part One: ' + str(distance))
    print('Part Two: ' + str(similarity))
