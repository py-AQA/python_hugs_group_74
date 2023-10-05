'''
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.'''

# from math import sqrt
# def square(x):
#     per = 4 * x
#     pl = x ** 2
#     d = x * (sqrt(2))
#     return tuple((per, pl, d))
#
# print(square(5))

'''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer'''

# def person(name='', last_name='', age=0, position=''):
#     print(f'name: {name}')
#     print(f'last_name: {last_name}')
#     print(f'age: {age}')
#     print(f'position: {position}')
#
# person('John', 'Smith', 35, 'web developer')

'''4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
     положительные числа'''

# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)

'''4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке '''
# from functools import reduce
#
# my_list = [20, -3, 15, 2, -1, -21]
# result = (reduce(lambda x, y: x*y, my_list))
#
# print(result)

'''4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра '''

import time

def my_decorator():

def person(name='', last_name='', age=0, position=''):
    print(f'name: {name}')
    print(f'last_name: {last_name}')
    print(f'age: {age}')
    print(f'position: {position}')

'''4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле. 
'''

