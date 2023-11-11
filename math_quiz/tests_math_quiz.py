import unittest
from math_quiz import random_int, random_oprator, operation_result


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_oprator(self):
        # Test if the random operators generated are one of the three options given
        valid_operator = {'+','-','*'}
        for _ in range(1000): # Test a large number of random operators
             operator = random_oprator()
             self.assertIn(operator, valid_operator)
             

    def test_operation_result(self):
            # Test the operation with different cases
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '+', '8 + 3', 11),
                (9, 7, '-', '9 - 7', 2),
                (6, 6, '-', '6 - 6', 0),
                (4, 5, '*', '4 * 5', 20),
                (2, 7, '*', '2 * 7', 14),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = operation_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
