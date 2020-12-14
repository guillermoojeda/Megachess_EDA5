import unittest
from packages.classes.pieces.Rook import Rook
from packages.classes.Board import Board


class TestRookPossibleMoves(unittest.TestCase):

    def test_think_possible_moves(self):
        eating_moves = [[-1, 0], [2, 0]]
        possible_moves = [[1, 0],
                          [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]
                          ]
        result_should = [eating_moves, possible_moves]

        board_string = ("k               "
                        "                "
                        "                "
                        "                "
                        " p              "
                        "  P             "
                        "             q  "
                        "                "
                        "                "
                        "                "
                        "          k k   "
                        "               p"
                        "               p"
                        "   p   R       R"
                        "                "
                        "    P          b")
        board1 = Board(board_string, "white")

        rook1 = Rook(13, 15, "white")

        my_test1 = rook1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
