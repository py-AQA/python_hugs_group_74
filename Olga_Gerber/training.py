# size = int(input('Enter the size of side of square: '))
# P = size*4
# S = size**2
# print(P)
# print(S)

'''_______________________________________________________'''
#
# year = int(input('Enter a year: '))
# answer = year % 4 == 0
# print(answer)

'''__________________'''
#
# number = 4586
# print(f'Thousands: {str(number)[0]}')
# print(f'Hunderds: {str(number)[1]}')
# print(f'Tens: {str(number)[2]}')
# print(f'Ones: {str(number)[3]}')

# def better_than_average(class_points, your_points):
#     a = your_points
#     for i in class_points:
#         a += i
#     average = a / (len(class_points) + 1)
#     answer = your_points > average
#     return answer
#
# better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)

'''Rekursion??????????????????????????????????'''
# def deep_count(a):
#     result = 0
#     for i in a:
#         if isinstance(i, list):
#             result += deep_count(i)
#             print('nächste Runde')
#         result += 1
#
#     return result
#
# print(deep_count([]))
# print(deep_count([1, 2, 3]))
# print((deep_count([[[[[[[[[]]]]]]]]])))
