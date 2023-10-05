# health = int(input('Enter the level of health: '))
# if health <= 0:
#     print(False)
# else:
#     print(True)

''' 2 '''
# number = int(input('Enter the number: '))
# if number % 2 == 0:
#     print('Четное')
# if number % 2 != 0:
#     print('Нечетное')

''' 3 '''
# year = int(input('Enter the year: '))
# I Variant
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(True)
# else:
#     print(False)

# II Variant
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(True)
# else:
#     print(False)

'''      4        '''
# text = input('Please enter your text: ')
# num = int(input('How many times should I print? '))
# for i in range(num):
#     print(text)

'''   5   '''

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
oper = input('Choose the operator: 1. Plus, 2. Minus, 3. Multi, 4. Divide: ')
if oper == '1':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif oper == '2':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif oper == '3':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif oper == '4':
    result = num1 / num2
    print(f'{num1} / {num2} = {result}')
else:
    print('Something went wrong!!!')
