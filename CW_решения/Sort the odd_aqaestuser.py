# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    # делаем список нечетных по возрастанию
    lst = sorted(x for x in source_array if x % 2)
    count = 0
    for i, item in enumerate(source_array):
        # заменяем нечетное из оригинального списка значением из lst
        if item % 2:
            source_array[i] = lst[count]
            count += 1
    return source_array


# кусочек проверки с кодварс
assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4], "не то!"
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0], "не то!"
assert sort_array([]) == [], "не то!"

# отображение красоты ради
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
arr_lst = [[7, 1], [5, 8, 6, 3, 4], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
for arr in arr_lst:
    print(arr, sort_array(arr), sep=' => ')
