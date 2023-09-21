# https://www.codewars.com/kata/58daa7617332e59593000006

def find_longest(arr):
    return max((len(str(x)), -i, x) for i, x in enumerate(arr))[2]


# кусочек проверки с кодварс
assert find_longest([1, 10, 100]) == 100, "не то!"
assert find_longest([9000, 8, 800]) == 9000, "не то!"
assert find_longest([8, 900, 500]) == 900, "не то!"
assert find_longest([3, 40000, 100]) == 40000, "не то!"
assert find_longest([1, 200, 100000]) == 100000, "не то!"

# отображение красоты ради
print(find_longest([1, 10, 100]))
print(find_longest([9000, 8, 800]))
print(find_longest([8, 900, 500]))
print(find_longest([3, 40000, 100]))
print(find_longest([1, 200, 100000]))
