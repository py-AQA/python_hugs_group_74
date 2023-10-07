#task 2.1
#health = int(input("Please, enter health for your hero: "))
#if health <= 0:
#    print(False)
#else:
#    print(True)

# task 2.2
#num = int(input("Please, enter a number: "))
#if num % 2 == 0:
#    print("Четное")
#else:
#    print("Нечетное")

# task 2.3 visokosnyi god
#god = int(input())
#rez = "NO"
#if god % 4 == 0 and god % 100 != 0:
#    rez = "YES"
#if god % 400 == 0:
#    rez = "YES"
#print(rez)

# task 2.4  text for repeat
#text = input("Input your text for repeat: ")
#qu = int(input("How many times text should be repeated?"))
#for i in range(qu):
#    print(text)

# task 2.5 calculator
a= int(input("first numebr: "))
b= int(input("second numebr: "))
sign = input("What action should be performed: ")
if sign == "/" and b == 0:
    print("I can't do this")
else:
    if sign == "+":
        rezult = a + b
    elif sign == "-":
        rezult = a - b
    elif sign == "*":
        rezult = a * b
    elif sign == "/":
        rezult = a / b
    print(f" {a} {sign} {b} = {rezult}")