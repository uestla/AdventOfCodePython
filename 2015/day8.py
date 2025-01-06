if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 8: Matchsticks ---

https://adventofcode.com/2015/day/8
""")

    fp = open('inputs/day8.txt', 'r')

    result_one = 0
    result_two = 0

    for line in fp:
        code_length = len(line.strip())
        code_length_encoded = code_length + line.count('"') + line.count('\\') + 2

        memory_taken = 0
        escaping = False

        i = 1
        while i <= code_length - 2:
            c = line[i]

            if escaping:
                if c == '\\' or c == '"':
                    memory_taken += 1

                elif c == 'x' and i <= code_length - 3:
                    try:
                        int(line[i + 1 : i + 2], 16)
                        memory_taken += 1
                        i += 2

                    except ValueError:
                        memory_taken += 1

                else:
                    memory_taken += 2

                escaping = False

            elif c == '\\':
                escaping = True

            else:
                memory_taken += 1
                escaping = False

            i += 1

        result_one += code_length - memory_taken
        result_two += code_length_encoded - code_length

    fp.close()

    assert result_one == 1_342
    assert result_two == 2_074

    print('Part One: ' + str(result_one))
    print('Part Two: ' + str(result_two))
