if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 3: Mull It Over ---

https://adventofcode.com/2024/day/3
""")

    fp = open('inputs/day3.txt', 'r')

    result = 0
    result_enabled = 0

    mul_enabled = True

    x = None
    y = None

    state = None
    next_chars_expected = ['m', 'd']

    for line in fp:
        for c in line:
            if state == 'X':
                if x is not None and c == ',':
                    y = None
                    state = 'Y'

                elif not c.isdigit():
                    state = None
                    next_chars_expected = ['m', 'd']

                else:
                    x = 0 if x is None else x * 10
                    x += int(c)

                    if len(str(x)) == 3:
                        state = None
                        next_chars_expected = [',']

            elif state == 'Y':
                if y is not None and c == ')':
                    result += x * y

                    if mul_enabled:
                        result_enabled += x * y

                    state = None
                    next_chars_expected = ['m', 'd']

                elif not c.isdigit():
                    state = None
                    next_chars_expected = ['m', 'd']

                else:
                    y = 0 if y is None else y * 10
                    y += int(c)

                    if len(str(y)) == 3:
                        state = None
                        next_chars_expected = [')']

            elif c in next_chars_expected:
                match c:
                    case 'm':
                        next_chars_expected = ['u']

                    case 'u':
                        next_chars_expected = ['l']

                    case 'l':
                        state = 'MUL'
                        next_chars_expected = ['(']

                    case '(':
                        if state == 'MUL':
                            x = None
                            state = 'X'

                        else:
                            next_chars_expected = [')']

                    case ',':
                        y = None
                        state = 'Y'

                    case ')':
                        if state is None:
                            result += x * y

                            if mul_enabled:
                                result_enabled += x * y

                        elif state == 'DO':
                            mul_enabled = True

                        elif state == 'DONT':
                            mul_enabled = False

                        state = None
                        next_chars_expected = ['m', 'd']

                    case 'd':
                        next_chars_expected = ['o']

                    case 'o':
                        state = 'DO'
                        next_chars_expected = ['(', 'n']

                    case 'n':
                        next_chars_expected = ['\'']

                    case '\'':
                        next_chars_expected = ['t']

                    case 't':
                        state = 'DONT'
                        next_chars_expected = ['(']

            else:
                state = None
                next_chars_expected = ['m', 'd']

    fp.close()

    print('Part One: ' + str(result))
    print('Part Two: ' + str(result_enabled))
