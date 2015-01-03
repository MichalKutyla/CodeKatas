import json
import unittest

class SortingTest(unittest.TestCase):

	def test_cases_from_file(self):
		filename="SortingTestCases.txt"
		with open(filename) as f:
			test_cases = json.load(f)

		for test_case in test_cases:
			input_arr = test_case[0]
			exp_out = test_case[1]
			print (test_case)
			self.assertEqual(exp_out, self.sort(input_arr))

