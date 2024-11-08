import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    #positive case: typical array with integers
    def test_merge_sort_typical_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    #negative case: input with a string
    def test_merge_sort_with_string(self):
        arr = [3, 'a', 4, 1]
        with self.assertRaises(TypeError):
            merge_sort(arr)

    #performance case: large array
    def test_merge_sort_large_array(self):
        arr = list(range(1000, 0, -1))  #a large array in reverse order
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, list(range(1, 1001)))

    #boundary case: edge cases like empty array and single element array
    def test_merge_sort_edge_cases(self):
        self.assertEqual(merge_sort([]), [])  #empyt array
        self.assertEqual(merge_sort([42]), [42])  #single element array
        self.assertEqual(merge_sort([3, 1, 2, 3]), [1, 2, 3, 3])  #array with dupes
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])  #already sorted array
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])  #reverse sorted array

    #idempotency Case:running sort multiple times on same input
    def test_merge_sort_idempotency(self):
        arr = [10, 3, 5, 2, 8, 3]
        sorted_arr = merge_sort(arr)
        self.assertEqual(merge_sort(sorted_arr), sorted_arr)  #should stay the same

#run the tests
if __name__ == "__main__":
    unittest.main()
