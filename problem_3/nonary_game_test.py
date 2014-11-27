import unittest
from nonary_game import NonaryGame


class NonaryGameTest(unittest.TestCase):

    SOLUTIONS = ['12357', '12456', '135', '1458', '15678', '2358', '2457', '3456', '34578', '567']

    def setUp(self):
        nonary_game = NonaryGame()
        self.solutions = nonary_game.valid_groups()

    def test_returns_an_array_of_solutions(self):
        self.assertIsInstance(self.solutions, list)

    def test_each_solution_is_an_array(self):
        for solution in self.solutions:
            self.assertIsInstance(solution, list)

    def test_solutions_to_nonary_game(self):
        sorted_solutions = [''.join([str(char) for char in solution]) for solution in self.solutions]
        sorted_solutions.sort()
        self.assertEqual(self.SOLUTIONS, sorted_solutions)


if __name__ == '__main__':
    unittest.main()
