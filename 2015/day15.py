if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 15: Science for Hungry People ---

https://adventofcode.com/2015/day/15
""")

    fp = open('inputs/day15.txt', 'r')

    ingredients = []

    for line in fp:
        parts = line.split()

        ingredients.append({
            'name': parts[0][:-1],
            'capacity': int(parts[2][:-1]),
            'durability': int(parts[4][:-1]),
            'flavor': int(parts[6][:-1]),
            'texture': int(parts[8][:-1]),
            'calories': int(parts[10]),
        })

    fp.close()

    max_score_one = None
    max_score_two = None

    teaspoons = 100

    for i in range(teaspoons + 1):
        for j in range(teaspoons + 1):
            for k in range(teaspoons + 1):
                for l in range(teaspoons + 1):
                    if i + j + k + l == teaspoons:
                        score = max(0, i * ingredients[0]['capacity'] + j * ingredients[1]['capacity'] + k * ingredients[2]['capacity'] + l * ingredients[3]['capacity'])
                        score *= max(0, i * ingredients[0]['durability'] + j * ingredients[1]['durability'] + k * ingredients[2]['durability'] + l * ingredients[3]['durability'])
                        score *= max(0, i * ingredients[0]['flavor'] + j * ingredients[1]['flavor'] + k * ingredients[2]['flavor'] + l * ingredients[3]['flavor'])
                        score *= max(0, i * ingredients[0]['texture'] + j * ingredients[1]['texture'] + k * ingredients[2]['texture'] + l * ingredients[3]['texture'])

                        if max_score_one is None or score > max_score_one:
                            max_score_one = score

                        if (max_score_two is None or score > max_score_two) and i * ingredients[0]['calories'] + j * ingredients[1]['calories'] + k * ingredients[2]['calories'] + l * ingredients[3]['calories'] == 500:
                            max_score_two = score

    assert max_score_one == 21_367_368
    assert max_score_two == 1_766_400

    print('Part One: ' + str(max_score_one))
    print('Part Two: ' + str(max_score_two))
