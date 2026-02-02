a = [2, 6, 3, 7, 9, 0]


def buble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(a)


buble_sort(a)
