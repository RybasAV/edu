from random import randrange
import unittest


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = a[:median]
        right = a[median:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


class Test_merge_sort(unittest.TestCase):
    def test1(self):
        a = [randrange(100) for _ in range(15)]
        self.assertEqual(merge_sort(a), sorted(a))


if __name__ == "__main__":
    unittest.main()
