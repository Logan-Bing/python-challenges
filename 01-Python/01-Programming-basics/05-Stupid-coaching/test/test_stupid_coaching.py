import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import unittest
from stupid_coaching import coach_answer

class TestStupidCoaching(unittest.TestCase):

    def test_answer(self):
        result = coach_answer("Can i go eat a pizza?")
        expected = "Silly question, get dressed and go to work!"
        self.assertEqual(result, expected)

    def test_good_response(self):
        result = coach_answer('I am going to work right now!')
        expected = "Congratulations, have a great day!"
        self.assertEqual(result, expected)

    def test_others_responses(self):
        result = coach_answer('hi him tired')
        expected = "I don't care, get dressed and go to work!"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
