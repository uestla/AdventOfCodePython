if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 18: Like a GIF For Your Yard ---

https://adventofcode.com/2015/day/18
""")

    grid_size = 100
    lights_one = []

    fp = open('inputs/day18.txt', 'r')

    for line in fp:
        lights_one.append(list(line.strip()))

    fp.close()

    lights_two = [x[:] for x in lights_one]

    def count_neighbors_on(lights: list[list[str]], x: int, y: int) -> int:
        count = 0

        check_coords = [
            [x - 1, y - 1],
            [x, y - 1],
            [x + 1, y - 1],
            [x + 1, y],
            [x + 1, y + 1],
            [x, y + 1],
            [x - 1, y + 1],
            [x - 1, y],
        ]

        for coord in check_coords:
            if coord[0] < 0 or coord[1] < 0 or coord[1] >= len(lights) or coord[0] >= len(lights[coord[1]]):
                continue

            if lights[coord[1]][coord[0]] == '#':
                count += 1

        return count

    corners = [
        [0, 0],
        [0, grid_size - 1],
        [grid_size - 1, 0],
        [grid_size - 1, grid_size - 1],
    ]

    for _ in range(100):
        new_lights_one = [x[:] for x in lights_one]
        new_lights_two = [x[:] for x in lights_two]

        for y in range(grid_size):
            for x in range(grid_size):
                neighbors_on_one = count_neighbors_on(lights_one, x, y)

                if lights_one[y][x] == '#':
                    new_lights_one[y][x] = '#' if neighbors_on_one in [2, 3] else '.'

                elif neighbors_on_one == 3:
                    new_lights_one[y][x] = '#'

                if [x, y] not in corners:
                    neighbors_on_two = count_neighbors_on(lights_two, x, y)

                    if lights_two[y][x] == '#':
                        new_lights_two[y][x] = '#' if neighbors_on_two in [2, 3] else '.'

                    elif neighbors_on_two == 3:
                        new_lights_two[y][x] = '#'

        lights_one = new_lights_one
        lights_two = new_lights_two

    lights_on_one = ''.join(''.join(row) for row in lights_one).count('#')
    lights_on_two = ''.join(''.join(row) for row in lights_two).count('#')

    assert lights_on_one == 768
    assert lights_on_two == 781

    print('Part One: ' + str(lights_on_one))
    print('Part Two: ' + str(lights_on_two))
