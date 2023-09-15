# https://www.codewars.com/kata/63b84f54693cb10065687ae5

def create_box(m, n):  # m and n positive integers
    # arr = [[1 for j in range(m)] for i in range(n)]
    arr = [[min(i + 1, j + 1, m - j, n - i) for j in range(m)] for i in range(n)]
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
