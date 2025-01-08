if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 10: Elves Look, Elves Say ---

https://adventofcode.com/2015/day/10
""")

    fp = open('inputs/day10.txt', 'r')
    sequence = fp.read()
    fp.close()

    length_one = None

    for iteration in range(50):
        counter = 1
        new_sequence = ''

        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i - 1]:
                new_sequence += str(counter) + sequence[i - 1]
                counter = 0

            counter += 1

        sequence = new_sequence + str(counter) + sequence[-1]

        if iteration == 39:
            length_one = len(sequence)

    length_two = len(sequence)

    assert length_one == 492_982
    assert length_two == 6_989_950

    print('Part One: ' + str(length_one))
    print('Part Two: ' + str(length_two))
