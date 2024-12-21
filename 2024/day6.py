if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 6: Guard Gallivant ---

https://adventofcode.com/2024/day/6
""")

    fp = open('inputs/day6.txt', 'r')

    visited_positions = 0
    obst_loops = 0

    map_original = []
    pos_original = None

    lines = fp.readlines()

    for line_idx in range(len(lines)):
        line = lines[line_idx]
        parts = [* line.strip()]

        if '^' in parts:
            pos_original = [line_idx, parts.index('^'), 'up']

        map_original.append(parts)

    fp.close()

    def next_move(map: list[list[str]]) -> list|None:
        if pos[2] == 'up':
            forward_y = pos[0] - 1
            forward_x = pos[1]
            turn = 'right'

        elif pos[2] == 'right':
            forward_y = pos[0]
            forward_x = pos[1] + 1
            turn = 'down'

        elif pos[2] == 'down':
            turn = 'left'
            forward_y = pos[0] + 1
            forward_x = pos[1]

        else:
            turn = 'up'
            forward_y = pos[0]
            forward_x = pos[1] - 1

        if not (0 <= forward_y < len(map) and 0 <= forward_x < len(map[pos[1]])):
            return None

        if map[forward_y][forward_x] == '#':
            return [pos[0], pos[1], turn]

        return [forward_y, forward_x, pos[2]]

    map_first = [row[:] for row in map_original]
    pos = pos_original[:]

    while True:
        if map_first[pos[0]][pos[1]] != 'X':
            visited_positions += 1
            map_first[pos[0]][pos[1]] = 'X'

        pos_new = next_move(map_first)

        if pos_new is None:
            break

        pos = pos_new

    for y in range(len(map_original)):
        for x in range(len(map_original[y])):
            if map_original[y][x] != '.':
                continue

            map_obst = [row[:] for row in map_original]
            map_obst[y][x] = '#'
            pos = pos_original[:]

            pos_idfs = {}
            obst_loop = False

            while True:
                pos_new = next_move(map_obst)

                if pos_new is None:
                    break

                pos_idf = ':'.join(map(str, pos))

                if pos_idf in pos_idfs:
                    obst_loop = True
                    break

                pos_idfs[pos_idf] = True
                pos = pos_new

            if obst_loop:
                obst_loops += 1

    assert visited_positions == 5_453
    assert obst_loops == 2_188

    print('Part One: ' + str(visited_positions))
    print('Part Two: ' + str(obst_loops))
