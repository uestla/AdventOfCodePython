if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 7: Some Assembly Required ---

https://adventofcode.com/2015/day/7
""")

    fp = open('inputs/day7.txt', 'r')

    instructions = {}

    for line in fp:
        instruction, wire = line.strip().split(' -> ')

        parts = instruction.split(maxsplit=3)
        part_count = len(parts)

        if part_count == 1:
            instructions[wire] = int(parts[0]) if parts[0].isdigit() else parts[0]

        elif part_count == 2:
            instructions[wire] = ~ int(parts[1]) if parts[1].isdigit() else ['NOT', parts[1]]

        else:
            a = int(parts[0]) if parts[0].isdigit() else parts[0]
            b = int(parts[2]) if parts[2].isdigit() else parts[2]
            instructions[wire] = [parts[1], a, b]

    fp.close()

    def assign_signals(instructions: dict) -> dict:
        values = {}

        def get_value(idf) -> int | None:
            if isinstance(idf, int):
                return idf

            if idf in values:
                return values[idf]

            return None

        while len(instructions):
            for wire in list(instructions):
                if isinstance(instructions[wire], int):
                    values[wire] = instructions[wire]
                    instructions.pop(wire)
                    continue

                if isinstance(instructions[wire], str):
                    if instructions[wire] in values:
                        values[wire] = values[instructions[wire]]
                        instructions.pop(wire)

                    continue

                if instructions[wire][0] == 'NOT':
                    value = get_value(instructions[wire][1])

                    if value is not None:
                        values[wire] = ~ value
                        instructions.pop(wire)

                    continue

                value_a = get_value(instructions[wire][1])
                value_b = get_value(instructions[wire][2])

                if value_a is not None and value_b is not None:
                    if instructions[wire][0] == 'AND':
                        values[wire] = value_a & value_b

                    elif instructions[wire][0] == 'OR':
                        values[wire] = value_a | value_b

                    elif instructions[wire][0] == 'LSHIFT':
                        values[wire] = value_a << value_b

                    else:
                        values[wire] = value_a >> value_b

                    instructions.pop(wire)

        return values

    signals_one = assign_signals(instructions.copy())

    instructions['b'] = signals_one['a']
    signals_two = assign_signals(instructions)

    assert signals_one['a'] == 956
    assert signals_two['a'] == 40_149

    print('Part One: ' + str(signals_one['a']))
    print('Part Two: ' + str(signals_two['a']))
