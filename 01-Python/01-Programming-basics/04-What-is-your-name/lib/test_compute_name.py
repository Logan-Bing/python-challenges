import unittest
from what_is_your_name import compute_name

class TestComputeName(unittest.TestCase):

    def test_full_name(self):
        result = compute_name("Boris", "Alexandre", "Papillard")
        expected = "Boris Alexandre Papillard"
        self.assertEqual(result, expected)

    def test_without_middle_name(self):
        result = compute_name("Ada", "", "Lovelace")
        expected = "Ada  Lovelace" 
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
