x1 = int(input("Введите число №1: "))
x2 = int(input("Введите число №2: "))
x3 = int(input("Введите число №3: "))
if x1 == x2 == x3:
    print("Одинаковых чисел 3")
elif x1 == x2 or x2 == x3 or x1 == x3:
    print("Одинаковых чисел 2")
else:
    print("Одинковых чисел 0")
