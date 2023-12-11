import unittest
import numpy as np
from knn import knn_M

# hello

class TestKnnMFunction(unittest.TestCase):
    def setUp(self):
        # Set up common data for your test cases, e.g., sample query and dataset
        self.sample_query = np.array([[1, 2, 3], [4, 5, 6]])
        self.sample_dataset = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])


    def test_knn_M_pck_greater_than_0_5(self):
        # Test that PCK is greater than 0.5
        result = knn_M(self.sample_query, self.sample_dataset, K=2, method='knn', metric='euclidean')
        self.assertGreater(result, 0.5)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
