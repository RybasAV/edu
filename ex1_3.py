chislo = int(input("введите целое число:"))
n = 0
sum = 0
chislo1 = chislo
while chislo > 0:
    chislo = chislo // 10
    n = n + 1
    # print(n)
for i in range(n):
    sum = sum + int(chislo1 % 10)
    chislo1 = chislo1 // 10
    # print(chislo1)
print(sum)
