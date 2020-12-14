import unittest
from packages.classes.pieces.Pawn import Pawn
from packages.classes.Board import Board


class TestPawnPossibleMoves(unittest.TestCase):

    def test_think_possible_moves(self):
        eating_moves = [[-1, -1], [-1, 1]]
        possible_moves = [[-2, 0], [-1, 0]]
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "         q q    "
                        "          P     "
                        "           p    "
                        "          K     "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(12, 10, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Scenario 2: one queen to eat, cannot move 2 ahead.

        eating_moves = [[-1, 1]]
        possible_moves = [[-1, 0]]
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "           q    "
                        "          P     "
                        "                "
                        "           p    "
                        "          K     "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(11, 10, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Scenario 3: On the far side to the left.

        eating_moves = []
        possible_moves = [[-1, 0]]
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "P               "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(8, 0, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Scenario 4: Enemy 1 step to the front, block moves to the front.

        eating_moves = []
        possible_moves = []
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "            r   "
                        "            P   "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(12, 12, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Scenario 5: Enemy 2 steps to the front, movement 2 steps to front is blocked.

        eating_moves = []
        possible_moves = [[-1, 0]]
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "            r   "
                        "                "
                        "            P   "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(12, 12, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))

        # Scenario 6: Being blocked by a friendly piece

        eating_moves = []
        possible_moves = []
        result_should = [eating_moves, possible_moves]

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "            r   "
                        "                "
                        "            P   "
                        "            P   "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        pawn1 = Pawn(13, 12, "white")

        my_test1 = pawn1.think_possible_moves(board1.currentBoard)

        self.assertEqual(sorted(my_test1), sorted(result_should))


if __name__ == '__main__':
    unittest.main()
