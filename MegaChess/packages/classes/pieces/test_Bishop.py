import unittest
from packages.classes.pieces.Bishop import Bishop
from packages.classes.Board import Board


class TestBishopPossibleMoves(unittest.TestCase):

    def test_thinkPossibleMoves(self):
        eating_moves = [[2, -2], [-3, -3]]
        possible_moves = [[-1, 1], [-2, 2],
                          [1, 1], [2, 2],
                          [1, -1],
                          [-1, -1], [-2, -2],
                          ]
        result_should = [eating_moves, possible_moves]

        board_string = ("k               "
                        "                "
                        "                "
                        "                "
                        " p              "
                        "  P             "
                        "                "
                        "                "
                        "                "
                        "                "
                        "          k     "
                        "                "
                        "               p"
                        "             B  "
                        "                "
                        "    P      p    ")
        board1 = Board(board_string, "white")

        bishop1 = Bishop(13, 13, "white")

        my_test1 = bishop1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
