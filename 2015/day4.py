import hashlib

if __name__ == '__main__':
    print("""
Advent of Code 2015
===================

--- Day 4: The Ideal Stocking Stuffer ---

https://adventofcode.com/2015/day/4
""")

    fp = open('inputs/day4.txt', 'r')
    secret_key = fp.read()
    fp.close()

    n = 1
    n_one = None
    n_two = None

    while True:
        result_hash = hashlib.md5((secret_key + str(n)).encode('UTF-8')).hexdigest()

        if result_hash.startswith('00000'):
            if n_one is None:
                n_one = n

            if result_hash.startswith('000000'):
                n_two = n
                break

        n += 1

    assert n_one == 282_749
    assert n_two == 9_962_624

    print('Part One: ' + str(n_one))
    print('Part Two: ' + str(n_two))
