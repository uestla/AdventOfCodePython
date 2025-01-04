if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

https://adventofcode.com/2015/day/3
""")

    fp = open('inputs/day3.txt', 'r')

    coords = {
        'santa_1': [0, 0],
        'santa_2': [0, 0],
        'robo_santa': [0, 0],
    }

    visited_coords = {
        'part_one': {"0:0": True},
        'part_two': {"0:0": True},
    }

    gifted_houses = {
        'part_one': 1,
        'part_two': 1,
    }

    robo_turn = False

    for line in fp:
        for c in line:
            for coord_key in ['santa_1', 'robo_santa' if robo_turn else 'santa_2']:
                part_key = 'part_one' if coord_key == 'santa_1' else 'part_two'

                if c == '>':
                    coords[coord_key][0] += 1

                elif c == 'v':
                    coords[coord_key][1] += 1

                elif c == '<':
                    coords[coord_key][0] -= 1

                else:
                    coords[coord_key][1] -= 1

                coord = f'{coords[coord_key][0]}:{coords[coord_key][1]}'

                if coord not in visited_coords[part_key]:
                    visited_coords[part_key][coord] = True
                    gifted_houses[part_key] += 1

            robo_turn = not robo_turn

    fp.close()

    assert gifted_houses['part_one'] == 2_592
    assert gifted_houses['part_two'] == 2_360

    print('Part One: ' + str(gifted_houses['part_one']))
    print('Part Two: ' + str(gifted_houses['part_two']))
