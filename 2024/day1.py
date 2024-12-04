if __name__ == '__main__':
    lefts = []
    rights = []
    rightCounts = {}
    fp = open('inputs/day1.txt', 'r')

    for line in fp:
        nums = list(map(int, line.split()))
        lefts.append(nums[0])

        right = nums[1]
        rights.append(right)
        rightCounts[right] = rightCounts[right] + 1 if right in rightCounts else 1

    fp.close()

    lefts.sort()
    rights.sort()

    distance = similarity = 0

    for index, a in enumerate(lefts):
        distance += abs(a - rights[index])
        similarity += a * (rightCounts[a] if a in rightCounts else 0)

    print('Part One: ' + str(distance))
    print('Part Two: ' + str(similarity))
