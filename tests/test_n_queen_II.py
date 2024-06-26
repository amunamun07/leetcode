import unittest
from n_queen_II import NQueenII


class TestNQueen(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        self.assertTrue(NQueenII.validate_input("4"))
        self.assertTrue(NQueenII.validate_input("9"))

    def test_invalid_input(self):
        # Test with invalid input
        self.assertFalse(NQueenII.validate_input("0"))
        self.assertFalse(NQueenII.validate_input("10"))
        self.assertFalse(NQueenII.validate_input("abc"))

    def test_solve(self):
        # Test the solve method
        n_queen = NQueenII(size=4)
        n_queen.solve()
        # There should be 2 solutions for 4-Queens
        self.assertEqual(len(n_queen.solutions), 2)

        n_queen = NQueenII(size=8)
        n_queen.solve()
        # There should be 92 solutions for 8-Queens
        self.assertEqual(len(n_queen.solutions), 92)

    def test_can_be_placed(self):
        # Test the _can_be_placed method indirectly through the public solve method
        n_queen = NQueenII(size=4)

        # Set position (1, 2) to True
        n_queen.chess_grid[1][2] = True

        # Test placing a queen at a valid position
        self.assertTrue(n_queen.can_be_placed(2, 0))

        # Test placing a queen at an invalid position
        self.assertFalse(n_queen.can_be_placed(2, 3))


if __name__ == "__main__":
    unittest.main()
