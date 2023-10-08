#4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#     периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     perimetr = a * 4
#     sq = a ** 2
#     diag = (2 * a ** 2) ** 0.5
#     return (perimetr, sq, round(diag, 2))
#
#
# print(square(3))

#4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#     в формате аргумент: значение. Например:
#	name: John
#	last_name: Smith
#	age: 35
#	position: web developer
# def out_stroki(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
#
# dd = {'name': 'John', 'last_name': 'Smith', 'age': 35, 'position': 'web developer'}
# print(out_stroki(**dd))


#4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#     положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# #new_list = [a for a in my_list if a > 0]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)

#4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = reduce(lambda x, y: x * y, my_list)
# print(new_list)

#4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# import time
#
# def timer(function):
#     def wrapped(*args):
#         start_time = time.perf_counter_ns()
#         res = function(*args)
#         print(f'Time of execution: {(time.perf_counter_ns() - start_time)/1000}')
#         return res
#     return wrapped
#
# @timer
# def func(first, second):
#     return int(first) + int(second)
#
#
# print(func("111", "0000"))
#
# from datetime import datetime
# import time
#
# def decorating_func(own_func):
#     def wrapper(*args, **kwargs):
#         print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#         return own_func(*args, **kwargs)
#     return wrapper
#
# @decorating_func
# def addition(num1,num2):
#     return num1 + num2
#
#
# @decorating_func
# def multiply(num1,num2):
#     return num1 * num2
#
# print(addition(10,5))
# time.sleep(71)
# print(multiply(10,5))


#4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#     Примените эти функции в качестве методов в другом файле.
# import calc
# x, y = int(input()), int(input())
#
# print(f'Сумма будет равна: {calc.ssum(x, y)}')
# print(f'Умножение будет равно: {calc.mmult(x, y)}')
# print(f'Разность будет равна: {calc.ddif(x, y)}')
# print(f'Деление будет равно: {calc.ddivision(x, y)}')

