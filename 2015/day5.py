if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 5: Doesn't He Have Intern-Elves For This? ---

https://adventofcode.com/2015/day/5
""")

    fp = open('inputs/day5.txt', 'r')

    nice_count_one = 0
    nice_count_two = 0

    for line in fp:
        line_len = len(line)

        double_char_found = False
        has_forbidden_pair = False
        vowel_count = 1 if line[0] in 'aeiou' else 0

        pairs_idxs = {}
        double_pair_found = False
        between_repeat_found = False

        for c_idx in range(line_len - 1):
            c_a = line[c_idx]
            c_b = line[c_idx + 1]

            pair = f'{c_a}{c_b}'

            if pair in ['ab', 'cd', 'pq', 'xy']:
                has_forbidden_pair = True

            if c_a == c_b:
                double_char_found = True

            if c_b in 'aeiou':
                vowel_count += 1

            if pair not in pairs_idxs:
                pairs_idxs[pair] = c_idx

            elif (c_idx - pairs_idxs[pair]) >= 2:
                double_pair_found = True

            if c_idx < line_len - 2 and c_a == line[c_idx + 2]:
                between_repeat_found = True

        if not has_forbidden_pair and double_char_found and vowel_count >= 3:
            nice_count_one += 1

        if double_pair_found and between_repeat_found:
            nice_count_two += 1

    fp.close()

    assert nice_count_one == 238
    assert nice_count_two == 69

    print('Part One: ' + str(nice_count_one))
    print('Part Two: ' + str(nice_count_two))
