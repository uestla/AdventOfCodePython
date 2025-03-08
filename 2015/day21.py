import math
from typing import Tuple

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 21: RPG Simulator 20XX ---

https://adventofcode.com/2015/day/21
""")

    fp = open('inputs/day21.txt', 'r')

    lines = fp.readlines()
    foe_hitpoints = int(lines[0].split()[-1])
    foe_damage = int(lines[1].split()[-1])
    foe_armor = int(lines[2].split()[-1])

    fp.close()

    def fight(hitpoints_a, damage_a, armor_a, hitpoints_b, damage_b, armor_b) -> bool:
        while True:
            hitpoints_b -= (damage_a - armor_b)

            if hitpoints_b <= 0:
                return True

            hitpoints_a -= (damage_b - armor_a)

            if hitpoints_a <= 0:
                return False

    weapons = [
        [8, 4],
        [10, 5],
        [25, 6],
        [40, 7],
        [74, 8],
    ]

    armor = [
        [0, 0],
        [13, 1],
        [31, 2],
        [53, 3],
        [75, 4],
        [102, 5],
    ]

    rings = [
        [0, 0, 0],
        [20, 0, 1],
        [25, 1, 0],
        [40, 0, 2],
        [50, 2, 0],
        [80, 0, 3],
        [100, 3, 0],
    ]

    min_cost = None
    max_cost = None
    player_hitpoints = 100

    for weapon in weapons:
        for armor_item in armor:
            for ring_one in rings:
                for ring_two in rings:
                    if ring_two[0] > 0 and ring_two == ring_one:
                        continue

                    victory = fight(
                        player_hitpoints,
                        weapon[1] + ring_one[1] + ring_two[1],
                        armor_item[1] + ring_one[2] + ring_two[2],
                        foe_hitpoints,
                        foe_damage,
                        foe_armor,
                    )

                    cost = weapon[0] + armor_item[0] + ring_one[0] + ring_two[0]

                    if victory:
                        if min_cost is None or cost < min_cost:
                            min_cost = cost

                    else:
                        if max_cost is None or cost > max_cost:
                            max_cost = cost

    assert min_cost == 121
    assert max_cost == 201

    print('Part One: ' + str(min_cost))
    print('Part Two: ' + str(max_cost))
