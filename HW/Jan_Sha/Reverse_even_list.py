#https://www.codewars.com/kata/64c7bbad0a2a00198657013d
'''
Write a function revSub which reverses all sublists where consecutive elements are even. Note that the odd numbers
should remain where they are.

Example
With [1,2,4,5,9] as input, we should get [1,4,2,5,9]. Here, because [2,4] is a sublist of consecutive even numbers,
it should be flipped. There could be more than one sublist of even numbers, or none at all.

A few other examples:

[] -> []
[2,4] -> [4,2]
[2,4,3] -> [4,2,3]
[2,4,3,10,2] -> [4,2,3,2,10]
'''

def revSub(my_list: list)-> list:
    k = -1
    for i, j in enumerate(my_list):
        if j % 2 != 0:
            continue
        else:
            if k == -1:
                k = i
                continue
            else:
                a = my_list[k]
                my_list[k] = my_list[i]
                my_list[i] = a
                k = -1
    return my_list

def revSub2(my_list: list)-> list:
    k = -1
    for i, j in enumerate(my_list):
        if j % 2 != 0 or i == len(my_list)-1:
            if k == -1:
                continue
            else:
                if i == len(my_list)-1 and j % 2 == 0:
                    my_list[k:i+1] = my_list[k:i+1][::-1]
                else:
                    my_list[k:i] = my_list[k:i][::-1]
                k = -1
        else:
            if k == -1:
                k = i

    return my_list


assert revSub2([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert revSub2([2, 4, 3]) == [4, 2, 3]
assert revSub2([2,4]) == [4,2]
assert revSub2([2,4,3,10,2] ) == [4,2,3,2,10]
assert revSub2([] ) == []

# With arr =      [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#                 [4, 2, 8, 6, 12, 10, 16, 14, 20, 18, 1, 4, 3, 2, 5, 8, 7, 6, 9, 10]
# should equal    [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Thats working')