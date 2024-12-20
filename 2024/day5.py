if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 5: Print Queue ---

https://adventofcode.com/2024/day/5
""")

    fp = open('inputs/day5.txt', 'r')

    rules = {}
    middle_sum = 0
    middle_sum_fixed = 0

    def is_update_valid(update: list[str]) -> bool:
        for page_idx in range(len(update)):
            page = update[page_idx]

            for check_idx in range(page_idx):
                if page in rules and update[check_idx] in rules[page]:
                    return False

        return True

    def fix_update(update: list[str]) -> list[str]:
        update_fixed = []

        for page in update:
            if len(update_fixed) == 0:
                update_fixed.append(page)

            else:
                for page_idx in range(len(update_fixed) + 1):
                    update_fixed.insert(page_idx, page)

                    if is_update_valid(update_fixed):
                        break

                    else:
                        update_fixed.pop(page_idx)

        return update_fixed

    for line in fp:
        if '|' in line:
            a, b = line.strip().split('|', 2)

            if a not in rules:
                rules[a] = []

            rules[a].append(b)

        elif ',' in line:
            update = line.strip().split(',')
            middle_page_idx = int(len(update) / 2)

            if is_update_valid(update):
                middle_sum += int(update[middle_page_idx])

            else:
                update_fixed = fix_update(update)
                middle_sum_fixed += int(update_fixed[middle_page_idx])

    fp.close()

    assert middle_sum == 4_959
    assert middle_sum_fixed == 4_655

    print('Part One: ' + str(middle_sum))
    print('Part Two: ' + str(middle_sum_fixed))
