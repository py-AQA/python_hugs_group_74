# https://www.codewars.com/kata/583df40bf30065fa9900010c
# used lambda + reduce
'''Write a function that takes as parameters an array (arr) and 2 integers (x and y). The function should return the
mean between the mean of the the first x elements of the array and the mean of the last y elements of the array.

The mean should be computed if both x and y have values higher than 1 but less or equal to the array's length.
Otherwise the function should return -1.

Examples
[1, 3, 2, 4], 2, 3 => should return 2.5
because: the mean of the first 2 elements of the array is (1+3)/2=2 and
the mean of the last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.

[1, 3, 2, 4], 1, 2 => should return -1
because x is not higher than 1.

[1, 3, 2, 4], 2, 8 => should return -1 because 8 is higher than the array's length.
'''
from functools import reduce
def get_mean(inp_list: list, x:int, y:int)->float:
    if x > len(inp_list) or y > len(inp_list) or x <= 1 or y <= 1:
        return -1
    a = reduce(lambda i, j: i+j, inp_list[:x]) / x
    b = reduce(lambda i, j: i+j, inp_list[-y:]) / y

    return (a+b) / 2

assert get_mean([1, 3, 2, 4], 2, 3) == 2.5
assert get_mean([1, 3, 2, 4], 1, 2) == -1
assert get_mean([1, 3, 2, 4], 2, 8) == -1
print('Thats working')