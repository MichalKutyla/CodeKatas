__author__ = 'SG0220823'

import unittest


def sort(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i + 1, len(a)):
            if a[min_ind] > a[j]:
                min_ind = j
        swap(a, i, min_ind)
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


class SelectionSortTests(unittest.TestCase):
    def test_sort_empty(self):
        a = []
        self.failUnlessEqual(sort(a), [])

    def test_sort_one(self):
        a = [1]
        self.failUnlessEqual(sort(a), [1])

    def test_sort_two(self):
        a = [2, 1]
        self.failUnlessEqual(sort(a), [1, 2])

    def test_sort_three(self):
        a = [2, 1, 3]
        self.failUnlessEqual(sort(a), [1, 2, 3])

def main():
    unittest.main()


if __name__ == '__main__':
    main()

