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
assert diamond(-1) is None, "не то!"

# отображение красоты ради
for size in range(3, 12, 2):
    print(diamond(size))
