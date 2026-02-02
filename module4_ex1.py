a = [2, 3, 7, 9, 13, 15, 16, 21]

def binary_search(a, n):
    while len(a) != 1:
        print(a)
        mid = len(a) // 2
        if n < a[mid]:
            a = a[:mid]
        elif n > a[mid]:
            a = a[mid:]
        elif n == a[mid]:
            return True
    return False

print(binary_search(a, 20))
