if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 14: Reindeer Olympics ---

https://adventofcode.com/2015/day/14
""")

    fp = open('inputs/day14.txt', 'r')

    reindeers = []

    for line in fp:
        parts = line.split()

        reindeers.append({
            'speed': int(parts[3]),
            'flight_duration': int(parts[6]),
            'rest_duration': int(parts[-2]),
            'flying_seconds': 0,
            'resting_seconds': 0,
            'distance': 0,
            'score': 0,
        })

    fp.close()

    for _ in range(2_503):
        leading_distance = None

        for i in range(len(reindeers)):
            if reindeers[i]['flying_seconds'] == 0 and reindeers[i]['resting_seconds'] == 0:
                reindeers[i]['flying_seconds'] += 1
                reindeers[i]['distance'] += reindeers[i]['speed']

            elif reindeers[i]['resting_seconds'] == reindeers[i]['rest_duration']:
                reindeers[i]['resting_seconds'] = 0
                reindeers[i]['flying_seconds'] = 1
                reindeers[i]['distance'] += reindeers[i]['speed']

            elif reindeers[i]['flying_seconds'] == reindeers[i]['flight_duration']:
                reindeers[i]['flying_seconds'] = 0
                reindeers[i]['resting_seconds'] = 1

            elif reindeers[i]['flying_seconds'] > 0:
                reindeers[i]['flying_seconds'] += 1
                reindeers[i]['distance'] += reindeers[i]['speed']

            else:
                reindeers[i]['resting_seconds'] += 1

            if leading_distance is None or reindeers[i]['distance'] > leading_distance:
                leading_distance = reindeers[i]['distance']

        for i in range(len(reindeers)):
            if reindeers[i]['distance'] == leading_distance:
                reindeers[i]['score'] += 1

    max_distance = max([reindeer['distance'] for reindeer in reindeers])
    top_score = max([reindeer['score'] for reindeer in reindeers])

    assert max_distance == 2_660
    assert top_score == 1_256

    print('Part One: ' + str(max_distance))
    print('Part Two: ' + str(top_score))
