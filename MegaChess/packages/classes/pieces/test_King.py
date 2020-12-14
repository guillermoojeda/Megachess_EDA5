import unittest
from packages.classes.pieces.King import King
from packages.classes.Board import Board


class TestKingPossibleMoves(unittest.TestCase):

    def test_think_possible_moves(self):
        eating_moves = [[-1, 1]]
        possible_moves = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
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
                        "                "
                        "                "
                        "                "
                        "           p    "
                        "          K     "
                        "                ")
        board1 = Board(board_string, "white")

        king1 = King(14, 10, "white")

        my_test1 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Testing case 2: 3 enemies near

        eating_moves = [[-1, 1], [0, -1], [1, -1]]
        possible_moves = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, 1]]
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
                        "                "
                        "                "
                        "                "
                        "           p    "
                        "         pK     "
                        "         p      ")
        board1 = Board(board_string, "white")

        king1 = King(14, 10, "white")

        my_test2 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test2), sorted(result_should))

        # Testing case 3: surrounded, no way out except eating someone.

        eating_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        possible_moves = []
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
                        "                "
                        "                "
                        "                "
                        "         ppp    "
                        "         pKp    "
                        "         ppp    ")
        board1 = Board(board_string, "white")

        king1 = King(14, 10, "white")

        my_test3 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test3), sorted(result_should))

        # Testing case 4: No enemies in range.

        eating_moves = []
        possible_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
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
                        "                "
                        "                "
                        "                "
                        "                "
                        "          K     "
                        "                ")
        board1 = Board(board_string, "white")

        king1 = King(14, 10, "white")

        my_test4 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test4), sorted(result_should))

        # Testing case 5: No moves possibles, surrounded by friends.

        eating_moves = []
        possible_moves = []
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
                        "                "
                        "                "
                        "                "
                        "         PPP    "
                        "         PKP    "
                        "         PPP    ")
        board1 = Board(board_string, "white")

        king1 = King(14, 10, "white")

        my_test5 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test5), sorted(result_should))

        # Testing case 6: In one corner.

        eating_moves = []
        possible_moves = [[-1, -1], [-1, 0], [0, -1]]
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
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "               K")
        board1 = Board(board_string, "white")

        king1 = King(15, 15, "white")

        my_test6 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test6), sorted(result_should))

        # Testing case 7: from the start.

        eating_moves = []
        possible_moves = []
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
                        "                "
                        "                "
                        "PPPPPPPPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        king1 = King(14, 8, "white")

        my_test7 = king1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test7), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
