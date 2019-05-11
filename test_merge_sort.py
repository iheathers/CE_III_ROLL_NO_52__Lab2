import unittest
from merge_sort import merge_sort

def unit_test_merge_sort(self):
    values = [1, 5, 8, 2, 18, 11]
    self.merge_sort(values)

    sorted_value = [1, 2, 5, 8, 11, 18]
    self.assertListEqual(values, sorted_value)

if __name__ == "__main__":
    unittest.main()