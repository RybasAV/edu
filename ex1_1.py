sum = float(input("Введите начальную сумму вклада:"))
procent = float(input("Введите  процентную ставку:"))
itog = float(input("Введите желаемую сумму накопления:"))
n = 0
while sum < itog:
    sum = int(sum * (1 + procent / 100))
    n = n + 1
    print(sum)
    print(n)
