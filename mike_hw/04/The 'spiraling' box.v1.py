# https://www.codewars.com/kata/63b84f54693cb10065687ae5

def create_box(m, n):  # m and n positive integers
    def fill(x, matrix):
        for i in range(x - 1, len(matrix) - x + 1):
            for j in range(x - 1, len(matrix[0]) - x + 1):
                matrix[i][j] = x

    arr = [[0 for el in range(m)] for row in range(n)]
    for number in range(1, min(m, n) // 2 + 2):
        fill(number, arr)

    # [print(row) for row in arr]

    return arr


def do_test(r, er):
    print("Фактический результат:")
    [print(*i) for i in r]
    print("Oжидаемый результат:")
    [print(*i) for i in er]
    print(f"Test: {['FAIL', 'OK'][r == er]}")


do_test(create_box(7, 8), [[1, 1, 1, 1, 1, 1, 1],
                           [1, 2, 2, 2, 2, 2, 1],
                           [1, 2, 3, 3, 3, 2, 1],
                           [1, 2, 3, 4, 3, 2, 1],
                           [1, 2, 3, 4, 3, 2, 1],
                           [1, 2, 3, 3, 3, 2, 1],
                           [1, 2, 2, 2, 2, 2, 1],
                           [1, 1, 1, 1, 1, 1, 1]])

do_test(create_box(6, 4), [[1, 1, 1, 1, 1, 1],
                           [1, 2, 2, 2, 2, 1],
                           [1, 2, 2, 2, 2, 1],
                           [1, 1, 1, 1, 1, 1]])
