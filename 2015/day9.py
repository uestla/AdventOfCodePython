from itertools import permutations

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 9: All in a Single Night ---

https://adventofcode.com/2015/day/9
""")

    fp = open('inputs/day9.txt', 'r')

    shortest = 0
    longest = 0

    distance_pairs = {}

    for line in fp:
        pair, pair_distance = line.split(' = ')
        a, b = pair.split(' to ')

        if a not in distance_pairs:
            distance_pairs[a] = {}

        if b not in distance_pairs:
            distance_pairs[b] = {}

        distance_pairs[a][b] = int(pair_distance)
        distance_pairs[b][a] = int(pair_distance)

    fp.close()

    for route in permutations(distance_pairs.keys()):
        distance = 0

        for i in range(len(route) - 1):
            distance += distance_pairs[route[i]][route[i + 1]]

        if shortest == 0 or distance < shortest:
            shortest = distance

        if longest == 0 or distance > longest:
            longest = distance

    assert shortest == 141
    assert longest == 736

    print('Part One: ' + str(shortest))
    print('Part Two: ' + str(longest))
