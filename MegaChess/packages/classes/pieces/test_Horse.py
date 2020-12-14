import unittest
from packages.classes.pieces.Horse import Horse
from packages.classes.Board import Board


class TestHorsePossibleMoves(unittest.TestCase):

    def test_think_possible_moves(self):
        eating_moves = [[1, 2], [2, -1], [-1, -2]]
        possible_moves = [[-2, 1], [2, 1], [1, -2], [-2, -1]]
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        " p P            "
                        "  P             "
                        "                "
                        "                "
                        "                "
                        "                "
                        "      k   P     "
                        "        Hp      "
                        "          h     "
                        "       b        "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        horse1 = Horse(11, 8, "white")

        my_test1 = horse1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
