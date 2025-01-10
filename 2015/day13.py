from itertools import permutations

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 13: Knights of the Dinner Table ---

https://adventofcode.com/2015/day/13
""")

    fp = open('inputs/day13.txt', 'r')

    diff_map = {}

    for line in fp:
        parts = line.split()
        name = parts[0]

        if name not in diff_map:
            diff_map[name] = {}

        diff_map[name][parts[-1][:-1]] = int(parts[3]) * (1 if parts[2] == 'gain' else -1)

    fp.close()

    def find_optimal_happiness_change(diff_map: dict[str, dict[str, int]]) -> int:
        optimal_happiness_change = None

        guest_count = len(diff_map)

        for arrangement in permutations(diff_map.keys()):
            happiness_change = 0

            for i in range(guest_count):
                happiness_change += diff_map[arrangement[i]][arrangement[i - 1]]
                happiness_change += diff_map[arrangement[i]][arrangement[i + 1 if i < guest_count - 1 else 0]]

            if optimal_happiness_change is None or happiness_change > optimal_happiness_change:
                optimal_happiness_change = happiness_change

        return optimal_happiness_change

    max_happiness_change_one = find_optimal_happiness_change(diff_map)

    guests = diff_map.keys()

    for guest in diff_map:
        diff_map[guest]['me'] = 0

    diff_map['me'] = {}
    for guest in guests:
        diff_map['me'][guest] = 0

    max_happiness_change_two = find_optimal_happiness_change(diff_map)

    assert max_happiness_change_one == 664
    assert max_happiness_change_two == 640

    print('Part One: ' + str(max_happiness_change_one))
    print('Part Two: ' + str(max_happiness_change_two))
