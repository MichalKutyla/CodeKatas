import unittest


def sort(a):
    if (len(a) <= 1):
        return a
    a1 = a[len(a) // 2:]
    a2 = a[:len(a) // 2]
    a1 = sort(a1)
    a2 = sort(a2)
    return merge(a1, a2)


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if (a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])

    return c


class MergeSortTests(unittest.TestCase):

    def test_sort_empty(self):
        self.assertEqual(sort([]), [])

    def test_sort_one(self):
        self.assertEqual(sort([1]), [1])

    def test_sort_two(self):
        self.assertEqual(sort([2, 1]), [1, 2])

    def test_sort_many(self):
        self.assertEqual(
            sort([3, 4, -1, 0, -2, 5, 4]), [-2, -1, 0, 3, 4, 4, 5])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
