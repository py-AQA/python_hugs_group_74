# task 3.1.
# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#my_list = ['a', 'b', [1, 2, 3], 'd']
#print(my_list[2])
#print(*my_list[2])
#print(f"{my_list[2][0]}, {my_list[2][1]}, {my_list[2][2]}")

#task 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'
#list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#sum_chisla = sum([a for a in list_1 if str(a).isdigit()])
#stroka_a = [w for w in list_1 if "a" in str(w)]
#print(sum_chisla)
#print(*stroka_a)

# task 3.3  Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
#list_1 = ['cat', 'dog', 'horse', 'cow']
#my_tuple = tuple(list_1)
#print(my_tuple)

# task 3.4
#family_1 = input()
#family_2 = input()
#if len(family_1) > len(family_2):
#    print(family_1)
#elif len(family_2) > len(family_1):
#    print(family_2)
#else:
#    print("equal")

# task 3.5 dict
# film = dict(title="Angels", director="Liuk Besson", year=1998, budget=20000000, main_actor="Kafka", slogan="hey")
# for k in film.keys():
#     print(k, end=", ")
# print()
# for v in film.values():
#     print(v, end=", ")
# print()
# for k, v in film.items():
#     print(f"{k}={v}", end=", ")

# task 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum_d = 0
# for k, v in my_dictionary.items():
#     sum_d += v
# print(sum_d)

# task 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#list_n = [1, 2, 3, 4, 5, 3, 2, 1]
#print(set(list_n))

# task 3.8 Даны два множества:
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1 & set2)
print((set1 | set2) - (set1 & set2))
print(set1.issubset(set2))
print(set2.issubset(set1))
