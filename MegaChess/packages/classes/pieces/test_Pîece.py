import unittest
from packages.classes.pieces.Piece import Piece


class TestPiece(unittest.TestCase):

    def test_is_move_possible(self):

        # Scenario 1: Move should not be possible

        piece1 = Piece(11, 8, "white")

        my_test1 = piece1.is_move_possible([10, 10])

        result_should = False

        self.assertEqual(my_test1, result_should)

        # Scenario 2: Move should be possible

        piece1 = Piece(11, 8, "white")

        my_test1 = piece1.is_move_possible([2, 2])

        result_should = True

        self.assertEqual(my_test1, result_should)


if __name__ == '__main__':
    unittest.main()
