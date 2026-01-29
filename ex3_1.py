def streug(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return s


print(streug(3, 5, 6))
