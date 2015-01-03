import testcases
import unittest


def sort(a):
	return sort_range(a, 0, len(a) - 1)


def sort_range(a, start_index, end_index):
	if start_index >= end_index:
		return a
	pivot = start_index
	i = start_index + 1
	larger_start = i
	while i <= end_index:
		if a[pivot] > a[i]:
			swap(a, i, larger_start)
			larger_start += 1
		i += 1
	swap(a, pivot, larger_start - 1)
	sort_range(a, start_index, larger_start - 2)
	sort_range(a, larger_start, end_index)
	return a


def swap(a, i, j):
	a[i], a[j] = a[j], a[i]


class QuickSortTest(testcases.SortingTest):

	def __init__(self,a):
		super(QuickSortTest, self).__init__(a)
		self.sort = sort

    # def test_sort_empty(self):
    #     self.assertEqual(sort([]), [])

    # def test_sort_one(self):
    #     self.assertEqual(sort([1]), [1])

    # def test_sort_two(self):
    #     self.assertEqual(sort([2, 1]), [1, 2])

    # def test_sort_two(self):
    #     self.assertEqual(sort([2, 1, -3, 1, 5, 3, 0]), [-3, 0, 1, 1, 2, 3, 5])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
