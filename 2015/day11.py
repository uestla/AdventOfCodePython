if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 11: Corporate Policy ---

https://adventofcode.com/2015/day/11
""")

    fp = open('inputs/day11.txt', 'r')
    password = fp.read()
    fp.close()

    new_password_one = None

    while True:
        inc_idx = 7

        while True:
            if password[inc_idx] == 'z':
                password = password[:inc_idx] + 'a' + password[inc_idx + 1:]
                inc_idx -= 1

                if inc_idx < 0:
                    raise 'Cannot increment anymore'

            else:
                new_char = chr(ord(password[inc_idx]) + 1)
                password = password[:inc_idx] + new_char + password[inc_idx + 1:]

                if new_char not in ['i', 'o', 'l']:
                    break

        increase_found = False
        double_pair_found = False
        pair_chars = []

        for i in range(7):
            a = password[i]
            ord_a = ord(a)

            if i <= 5 and not increase_found and ord_a == ord(password[i + 1]) - 1 and ord_a == ord(password[i + 2]) - 2:
                increase_found = True

            if not double_pair_found and a == password[i + 1] and a not in pair_chars:
                pair_chars.append(a)

                if len(pair_chars) == 2:
                    double_pair_found = True

            if increase_found and double_pair_found:
                break

        if increase_found and double_pair_found:
            if new_password_one is None:
                new_password_one = password

            else:
                break

    assert new_password_one == 'hepxxyzz'
    assert password == 'heqaabcc'

    print('Part One: ' + new_password_one)
    print('Part Two: ' + password)
