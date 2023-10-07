import time


# '''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.'''
#
#
# def square(n):
#     perimetr = 4 * n
#     sq = n ** n
#     diagonal = n * n ** 0.5
#     return (perimetr, sq, diagonal)
#
#
# print(square(2))
#
# '''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer'''
#
#
# #def print_dict(**kwargs):
# #    print(kwargs, sep="\n")
#
#
# #print_dict("name"= "John", "last_name"="Smith", "age"=35, "position"="web_developer")
#
# '''4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа'''
# my_list = [20, -3, 15, 2, -1, -21]
# #new_list = [a for a in my_list if a > 0]
# new_list = list(filter(lambda x : x > 0, my_list))
# print(new_list)
#
# #4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# list_reduce = reduce(lambda x, y: y*x, new_list)
# print(list_reduce)

#4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"#timing_decorator: Вызвана функция {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"#timing_decorator: Функция {func.__name__} выполнилась за {elapsed_time:.6f} секунд.")
        return result

    return wrapper


@timing_decorator
def calc_factorial(n):
    rez = 1
    for i in range(1, n):
       rez += i
    time.sleep(1)
    return rez


x = 20
rez = calc_factorial(x)
print(f" факториал от {x} равен {rez}")

'''4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.'''
