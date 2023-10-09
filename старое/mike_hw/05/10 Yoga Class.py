# https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a
from helper import test


def yoga(classroom, poses):
    for row in classroom:
        s = sum(row)
        for i, p in enumerate(row):
            row[i] += s
    # [print(row) for row in classroom]
    return sum(sum([1 if x >= p else 0 for row in classroom for x in row]) for p in poses)


# проверка
test.assert_equals(yoga([
    [3, 2, 1, 3],
    [1, 3, 2, 1],
    [1, 1, 1, 2],
], [1, 7, 5, 9, 10, 21, 4, 3]), 68)
test.assert_equals(yoga([
    [7, 2, 1, 0],
    [1, 3, 2, 2],
    [1, 9, 1, 2],
], [1000, 20, 3, 105, 66, 204, 4, 1, 22, 86]), 38)
test.assert_equals(yoga([[0, 0], [0, 0]], [1, 1, 0, 1, 2, 3, 0, 1, 5]), 8, "Don't forget poses/skill levels can be 0")
test.assert_equals(yoga([], [1, 3, 4]), 0, 'Empty Classes Should Return 0')
test.assert_equals(yoga([[0, 0], [0, 0]], []), 0, 'Empty Poses Should Return 0')
test.assert_equals(yoga([], []), 0, 'Empty Classes & Poses Should Return 0')