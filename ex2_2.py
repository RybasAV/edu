import random

n = int(input("Введите размер матрицы:"))
spisok1 = []
y = 0
for i in range(n):
    spisok = []
    for j in range(n):
        spisok.append(random.randint(-100, 100))
    spisok1.append(spisok)
for i in range(n):
    x = spisok1[i]
    print(x)
    for j in range(n):
        if x[j] > y:
            y = x[j]
print(y)
