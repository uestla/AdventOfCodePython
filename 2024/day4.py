if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 4: Ceres Search ---

https://adventofcode.com/2024/day/4
""")

    fp = open('inputs/day4.txt', 'r')

    lines = fp.readlines()
    line_count = len(lines)

    xmas_count = 0
    x_mas_count = 0
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    for line_idx in range(line_count):
        line = lines[line_idx]
        col_count = len(line)

        for col_idx in range(col_count):
            c = line[col_idx]

            if c == 'X':
                for direction in directions:
                    seq = ''

                    for i in range(1, 4):
                        check_line_idx = line_idx + i * direction[0]
                        check_col_idx = col_idx + i * direction[1]

                        if check_line_idx < 0 or check_col_idx < 0 or check_line_idx >= line_count or check_col_idx >= col_count:
                            break

                        seq += lines[check_line_idx][check_col_idx]

                    if seq == 'MAS':
                        xmas_count += 1

            if c == 'A' and line_idx >= 1 and col_idx >= 1 and line_idx < line_count - 1 and col_idx < col_count - 1:
                firstSeq = lines[line_idx - 1][col_idx - 1] + lines[line_idx + 1][col_idx + 1]
                secondSeq = lines[line_idx + 1][col_idx - 1] + lines[line_idx - 1][col_idx + 1]

                if (firstSeq == 'MS' or firstSeq == 'SM') and (secondSeq == 'MS' or secondSeq == 'SM'):
                    x_mas_count += 1

    fp.close()

    print('Part One: ' + str(xmas_count))
    print('Part Two: ' + str(x_mas_count))
