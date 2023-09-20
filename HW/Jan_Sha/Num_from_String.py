# https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python

'''
Task
Your task is to return a number from a string.

Details
You will be given a string of numbers and letters mixed up, you have to return all the numbers
in that string in the order they occur.

"11bb2c23c3" --> 112233
'''

def filter_string(string: str) -> int:
    # перебор строки через цикл -- оставлять только цифры

    # сделать из строки лист -- отфильтровать -- сделать строку -- convert to number
    my_list = list(filter(lambda x: x.isdigit(), list(string)))

    # перебор по строке как по последовательности
    my_1 = ''.join(filter(str.isdigit, string))

    return int(''.join(my_list))

assert filter_string("11bb2c23c3") == 112233
print('Thats working')