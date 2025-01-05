if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 6: Probably a Fire Hazard ---

https://adventofcode.com/2015/day/6
""")

    fp = open('inputs/day6.txt', 'r')

    lights = {}
    brightnesses = {}

    lights_on = 0
    total_brightness = 0

    for line in fp:
        parts = line.split()
        start_x, start_y = map(int, parts[-3].split(','))
        end_x, end_y = map(int, parts[-1].split(','))

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                idx = x * 1000 + y

                if idx not in lights:
                    lights[idx] = False
                    brightnesses[idx] = 0

                if parts[0] == 'toggle':
                    lights_on += -1 if lights[idx] else 1
                    lights[idx] = not lights[idx]
                    total_brightness += 2
                    brightnesses[idx] += 2

                elif parts[1] == 'on':
                    lights_on += 1 if not lights[idx] else 0
                    lights[idx] = True
                    total_brightness += 1
                    brightnesses[idx] += 1

                else:
                    lights_on -= 1 if lights[idx] else 0
                    lights[idx] = False
                    total_brightness -= 1 if brightnesses[idx] > 0 else 0
                    brightnesses[idx] = max(0, brightnesses[idx] - 1)

    fp.close()

    assert lights_on == 569_999
    assert total_brightness == 17_836_115

    print('Part One: ' + str(lights_on))
    print('Part Two: ' + str(total_brightness))
