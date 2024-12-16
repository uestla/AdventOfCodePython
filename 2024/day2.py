if __name__ == '__main__':
    print("""
Advent of Code 2024
===================

--- Day 2: Red-Nosed Reports ---

https://adventofcode.com/2024/day/2
""")

    def is_report_safe(report: list[int]) -> bool:
        report_sgn = None

        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]

            if diff == 0 or abs(diff) > 3:
                return False

            pair_sgn = 1 if diff > 0 else -1

            if report_sgn is None:
                report_sgn = pair_sgn

            elif report_sgn != pair_sgn:
                return False

        return True

    fp = open('inputs/day2.txt', 'r')

    safe_count = 0
    tolerated_safe_count = 0

    for line in fp:
        report = list(map(int, line.split()))

        if is_report_safe(report):
            safe_count += 1
            tolerated_safe_count += 1

        else:
            for i in range(len(report)):
                new_report = report.copy()
                new_report.pop(i)

                if is_report_safe(new_report):
                    tolerated_safe_count += 1
                    break

    fp.close()

    print('Part One: ' + str(safe_count))
    print('Part Two: ' + str(tolerated_safe_count))
