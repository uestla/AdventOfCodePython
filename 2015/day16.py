if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 16: Aunt Sue ---

https://adventofcode.com/2015/day/16
""")

    input = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    sue_no_one = None
    sue_no_two = None

    fp = open('inputs/day16.txt', 'r')

    for line in fp:
        matches_one = True
        matches_two = True
        name, data = line.strip().split(':', 1)

        for info in data.strip().split(', '):
            key, value = info.split(': ', 1)

            if matches_one and input[key] != int(value):
                matches_one = False

            if matches_two:
                if key in ['cats', 'trees']:
                    if input[key] >= int(value):
                        matches_two = False

                elif key in ['pomeranians', 'goldfish']:
                    if input[key] <= int(value):
                        matches_two = False

                elif input[key] != int(value):
                    matches_two = False

        if matches_one:
            name_parts = name.split()
            sue_no_one = int(name_parts[1])

        if matches_two:
            name_parts = name.split()
            sue_no_two = int(name_parts[1])

        if matches_one and matches_two:
            break

    fp.close()

    assert sue_no_one == 40
    assert sue_no_two == 241

    print('Part One: ' + str(sue_no_one))
    print('Part Two: ' + str(sue_no_two))
