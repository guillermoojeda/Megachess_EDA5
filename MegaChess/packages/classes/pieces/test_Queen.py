import unittest
from packages.classes.pieces.Queen import Queen
from packages.classes.Board import Board


class TestQueenPossibleMoves(unittest.TestCase):

    def test_think_possible_moves(self):
        eating_moves = [[-2, 2], [-3, -3]]
        possible_moves = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0], [-10, 0],
                          [-11, 0],
                          [-12, 0], [-13, 0],
                          [-1, 1],
                          [0, 1], [0, 2],
                          [1, 1], [2, 2],
                          [1, 0], [2, 0],
                          [1, -1], [2, -2],
                          [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9], [0, -10],
                          [0, -11], [0, -12],
                          [0, -13], [-1, -1], [-2, -2]
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
                        "               p"
                        "               p"
                        "             Q  "
                        "                "
                        "    P           ")
        board1 = Board(board_string, "white")

        queen1 = Queen(13, 13, "white")

        my_test1 = queen1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
