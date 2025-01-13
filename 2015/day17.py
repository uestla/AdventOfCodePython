if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 17: No Such Thing as Too Much ---

https://adventofcode.com/2015/day/17
""")

    liters = 150

    fp = open('inputs/day17.txt', 'r')
    containers = list(map(int, fp.read().splitlines()))
    container_count = len(containers)
    fp.close()

    combination_count = 0

    minimum_containers_used = None
    minimum_count = 0

    for combination in range(2 ** container_count):
        combination_binary = '{0:b}'.format(combination).zfill(container_count)

        filled = 0
        used_count = 0

        for i in range(container_count):
            if combination_binary[i] == '1':
                filled += containers[i]
                used_count += 1

            if filled > liters:
                break

        if filled == liters:
            combination_count += 1

            if minimum_containers_used is None or used_count < minimum_containers_used:
                minimum_containers_used = used_count
                minimum_count = 1

            elif used_count == minimum_containers_used:
                minimum_count += 1

    assert combination_count == 654
    assert minimum_count == 57

    print('Part One: ' + str(combination_count))
    print('Part Two: ' + str(minimum_count))
