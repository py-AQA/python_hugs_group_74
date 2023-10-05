'''  1 Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
Распечатайте значения 1, 2, 3'''

my_list = ['a', 'b', [1, 2, 3], 'd']
new_list = my_list[2]
print(*new_list, sep='\n')

'''3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'''

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# my_sum = 0
# my_lst = []
# for i in list_1:
#     if isinstance(i, int):
#         my_sum += i
# for j in list_1:
#     if isinstance(j, str):
#         if 'a' in j:
#             my_lst.append(j)
# print(my_sum)
# print(my_lst)

# print(sum([x for x in list_1 if isinstance(x, int)]))
# list_2 = [x for x in list_1 if isinstance(x, str) and 'a' in x]
# print(*list_2, sep=', ')

'''3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')'''

# family_1 = input('Write familys member please: ')
# family_2 = input('Write familys member please: ')
# if len(family_1) > len(family_2):
#     print(family_1)
# elif len(family_1) < len(family_2):
#     print(family_2)
# else:
#     print('Equal')

'''3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение'''
#
# film = {
#     'title': 'Ono',
#     'director': 'Tarantino',
#     'year': '2000',
#     'budget': '1000000',
#     'main_actor': 'Di Kaprio',
#     'slogan': 'Nobody except us'
# }
# print(film.keys())
# print(film.values())
# print(film.items())

'''3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}'''
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_sum = 0
# for i in my_dictionary.values():
#     my_sum += i
# print(my_sum)