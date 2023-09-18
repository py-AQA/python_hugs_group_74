# https://www.codewars.com/kata/5503013e34137eeeaa001648

def diamond(n):
    # Make some diamonds!
    # делаем список с средним элементом (самым длинным)
    lst = ['*' * n]
    i = n
    while i > 1:
        i -= 2
        # собираем строку из пробелов и звездочек которую надо рисовать выше и ниже средней линии
        str_1 = ' ' * int((n - i) / 2) + '*' * i
        lst.insert(0, str_1)
        lst.append(str_1)
    # возвращаем строку собранную через \n из списка lst
    return '\n'.join(lst) + '\n' if n % 2 and n > 0 else None


# кусочек проверки с кодварс
assert diamond(5) == "  *\n ***\n*****\n ***\n  *\n", "не то!"
assert diamond(0) is None, "не то!"
assert diamond(2) is None, "не то!"
assert diamond(-1) is None, "не то!"

# отображение красоты ради
for size in range(3, 12, 2):
    print(diamond(size))

# через for
def diamond2(n):
    if n % 2 == 0 or n <= 0:
        return None
    lst = ['*' * n]
    for i in range(n-2, 0, -2):
        str = ' ' * (int((n - i) / 2)) + '*' * i
        lst.insert(0, str)
        lst.append(str)
    # str = '\n'.join(lst) + '\n'
    # возвращаем строку собранную через \n из списка lst
    return '\n'.join(lst) + '\n'

# кусочек проверки с кодварс
assert diamond2(5) == "  *\n ***\n*****\n ***\n  *\n", "не то!"
assert diamond2(0) is None, "не то!"
assert diamond2(2) is None, "не то!"
assert diamond2(-1) is None, "не то!"
