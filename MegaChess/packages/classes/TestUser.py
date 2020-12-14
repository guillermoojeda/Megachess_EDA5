import unittest
from .Board import Board
from .User import User
from .pieces.King import King # Used only to test function instantiate_piece()


class TestUser(unittest.TestCase):

    def test_think_all_possible_eats(self):
        # Scenario one: test that returns all possible eating moves.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        " p p            "
                        "  P             "
                        "      r         "
                        "           p    "
                        "                "
                        "                "
                        "                "
                        "   q       Q    "
                        "PPPPPPPPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = [[5, 2, 4, 1, 0, 100, 100], [5, 2, 4, 3, -100, 100, 0],
                          [11, 11, 7, 11, 0, 100, 100], [11, 11, 11, 3, 0, 700, 700], [11, 11, 6, 6, 0, 600, 600],
                          [12, 2, 11, 3, 0, 700, 700],
                          [12, 4, 11, 3, 0, 700, 700],
                          ]

        user1 = User("white")

        my_test1 = user1.think_all_possible_eats(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

        # Scenario one: test that works OK when playing blacks.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       b        "
                        "                "
                        "            q   "
                        "P               "
                        "           r   b"
                        "      r         "
                        "             R  "
                        "   P           h"
                        "r      p   b    "
                        "    p       h   "
                        "                ")
        board1 = Board(board_string, "black")

        correct_result = [[2, 4, 4, 2, 0, 600, 600], [2, 15, 7, 15, 0, 100, 100], [3, 0, 4, 2, 0, 600, 600],
                          [6, 0, 4, 2, 0, 600, 600]]

        user1 = User("black")

        my_test1 = user1.think_all_possible_eats(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

    def test_think_all_possible_common_moves(self):
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       b        "
                        "                "
                        "                "
                        "P               "
                        "           r   b"
                        "      r         "
                        "            h   "
                        "   P           h"
                        "r      p   b    "
                        "    p       h  Q"
                        "                ")
        board1 = Board(board_string, "white")

        correct_result = [[8, 0, 7, 0, 0, "P"],
                          [12, 3, 10, 3, -100, "P"], [12, 3, 11, 3, 0, "P"],
                          [14, 15, 13, 15, 0, "Q"], [14, 15, 15, 15, 0, "Q"], [14, 15, 15, 14, -700, "Q"],
                          [14, 15, 14, 14, -700, "Q"], [14, 15, 14, 13, 0, "Q"], [14, 15, 13, 14, -700, "Q"],
                          [14, 15, 12, 13, -700, "Q"]
                          ]

        user1 = User("white")

        my_test1 = user1.think_all_possible_common_moves(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

        # Scenario 4: Need to debug this
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
                        "                "
                        "              q "
                        "     Q          "
                        "                "
                        "                "
                        "                "
                        "PPPPP PPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = []

        user1 = User("white")

        my_test1 = user1.think_all_possible_common_moves(board1.currentBoard, user1.player_color)

        self.assertNotEqual(my_test1, correct_result)

    def test_can_be_eaten(self):
        # Scenario 1: Enemy pawn is threat to position
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "          p     "
                        "         X      "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 9

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 2: Enemy horse is threat to position
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "        h       "
                        "                "
                        "         X      "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 9

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 3: Enemy queen is threat to position. Enemies are whites.
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
                        "         X      "
                        "                "
                        "                "
                        "      Q         "
                        "                "
                        "                ")
        board1 = Board(board_string, "black")

        coord_x_test = 10
        coord_y_test = 9

        correct_result = True

        user1 = User("black")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 4: Enemy rook is threat to position.
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
                        "               X"
                        "                "
                        "                "
                        "               r"
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 15

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 5: Enemy bishop is threat to position.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "         b      "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "               X"
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 15

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 6: Enemy king is a threat to position.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "              k "
                        "               X"
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 15

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 7: Enemy queen is not a threat to position beacuse path is blocked.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "            q   "
                        "           K    "
                        "                "
                        "         X      "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")
        board1 = Board(board_string, "white")

        coord_x_test = 10
        coord_y_test = 9

        correct_result = False

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

        # Scenario 8: Surrounded Place, in an edge. Some enemies block themselves

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       b        "
                        "                "
                        "                "
                        "                "
                        "           r   b"
                        "      r         "
                        "            h   "
                        "               h"
                        "r      p   b    "
                        "    p       h   "
                        "              X ")

        board1 = Board(board_string, "white")

        coord_x_test = 15
        coord_y_test = 14

        correct_result = True

        user1 = User("white")

        my_test1 = user1.can_be_eaten(board1.currentBoard, coord_x_test, coord_y_test)

        self.assertEqual(my_test1, correct_result)

    def test_playBestMove(self):
        # Scenario one: test case with a few options.
        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        " p p     r      "
                        "  P       K     "
                        "      r         "
                        "           p    "
                        "        k       "
                        "                "
                        "                "
                        "   q       Q    "
                        "PPPPPPPPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = [11, 11, 8, 8, 0, 1000, 1000]

        user1 = User("white")

        my_test1 = user1.play_best_move(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

        # Scenario two: test case where queen can be eaten. Should choose King eats Rook
        board_string = ("              q "
                        "   Q          K "
                        "  p             "
                        "                "
                        " p p     r      "
                        "  P       K     "
                        "      r         "
                        "           p    "
                        "       rk       "
                        "                "
                        "                "
                        "   q       Q    "
                        "                "
                        "         b      "
                        "      H         "
                        "                ")
        board1 = Board(board_string, "white")

        correct_result = [11, 11, 8, 8, -700, 1000, 300]

        user1 = User("white")

        my_test1 = user1.play_best_move(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

        # Scenario 3: Nothing to eat, such as the first turn
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
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
        board1 = Board(board_string, "white")  # El tablero es White porq no hace falta

        correct_result = []

        user1 = User("white")

        my_test1 = user1.play_best_move(board1.currentBoard, user1.player_color)

        self.assertEqual(my_test1, correct_result)

        # Scenario 4: Testing a case I came across buy didn´t seem to work

        board_string = ('                '
                        '   h       p    '
                        '        p      r'
                        'h           P   '
                        '  R             '
                        '         r      '
                        '    r           '
                        '               P'
                        '   q            '
                        '                '
                        '        b       '
                        '                '
                        '                '
                        '                '
                        '                '
                        '                ')

        board1 = Board(board_string, "black")

        correct_result = [12, 15, 11, 13, 0, 600, 600]

        user1 = User("black")

        my_test1 = user1.play_best_move(board1.currentBoard, "black")

        self.assertEqual(my_test1, correct_result)

    def test_simulate_move(self):
        # Scenario 1: Enemy cannot eat me after I move.

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       b        "
                        "                "
                        "                "
                        "                "
                        "           r   b"
                        "      r         "
                        "            h   "
                        "   P           h"
                        "r      p   b    "
                        "    p       h  Q"
                        "                ")
        board1 = Board(board_string, "white")

        correct_result = 0

        user1 = User("white")

        my_test1 = user1.simulate_move(board1.currentBoard, 14, 15, 11, 12)

        self.assertEqual(my_test1, correct_result)

        # Scenario 2: Enemy can eat me after I move. Should return Rook´s points.

        board_string = ("                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       b        "
                        "                "
                        "            q   "
                        "P               "
                        "           r   b"
                        "      r         "
                        "          R  h  "
                        "   P           h"
                        "r      p   b    "
                        "    p       h   "
                        "                ")
        board1 = Board(board_string, "white")

        correct_result = 600

        user1 = User("white")

        my_test1 = user1.simulate_move(board1.currentBoard, 11, 10, 11, 13)

        self.assertEqual(my_test1, correct_result)

    def test_think_all_possible_actions(self):
        """
        grants a list with the possible eating moves and scores for each one...
        Pay attention that the last column gives the (probably) best score for decision making
        """

        # Scenario 1: Different choices.

        board_string = ("                "
                        "                "
                        "  r             "
                        "        k       "
                        "            h   "
                        "                "
                        "                "
                        "                "
                        "  b     Q       "
                        "                "
                        "                "
                        "     p          "
                        "        q       "
                        "          r     "
                        "              q "
                        "                ")

        board1 = Board(board_string, "white")

        correct_result = [[8, 8, 3, 8, 0, 1000, 1000, -700, 300],
                          [8, 8, 4, 12, 0, 300, 300, 0, 300],
                          [8, 8, 14, 14, 0, 700, 700, 0, 700],
                          [8, 8, 12, 8, 0, 700, 700, 0, 700],
                          [8, 8, 11, 5, -700, 100, -600, -700, -600],
                          [8, 8, 8, 2, -700, 400, -300, -700, -300],
                          [8, 8, 2, 2, 0, 600, 600, -700, -100]]

        user1 = User("white")

        my_test1 = user1.think_all_possible_actions(board1.currentBoard)

        self.assertEqual(my_test1, correct_result)

        # Scenario 2: Different choices, must be smart.
        """
        I am testing the AI decision making algorithm.
        It would be tempting to eat a king and get 1000 points in this turn, but the wise move
        should be eating the rook with the pawn, because the opponent´s counterattack will be less painful.
        The indicator for the  right move should be the last column of the output.
        """

        board_string = ("                "
                        "                "
                        "                "
                        "         p      "
                        "        r       "
                        "       P        "
                        "                "
                        "                "
                        "        Q       "
                        "                "
                        "                "
                        "        k       "
                        "                "
                        "                "
                        "                "
                        "                ")

        board1 = Board(board_string, "white")

        correct_result = [[5, 7, 4, 8, -100, 600, 500, -100, 500],
                          [8, 8, 4, 8, -700, 600, -100, -700, -100],
                          [8, 8, 11, 8, 0, 1000, 1000, -700, 300]]

        user1 = User("white")

        my_test1 = user1.think_all_possible_actions(board1.currentBoard)

        self.assertEqual(my_test1, correct_result)

        # Scenario 3: Black should yield the same result.
        """
        I am testing the AI decision making algorithm.
        It would be tempting to eat a king and get 1000 points in this turn, but the wise move
        should be eating the rook with the pawn, because the opponent´s counterattack will be less painful.
        The indicator for the  right move should be the last column of the output.
        """

        board_string = ("                "
                        "                "
                        "                "
                        "         P      "
                        "        R       "
                        "       p        "
                        "                "
                        "                "
                        "        q       "
                        "                "
                        "                "
                        "        K       "
                        "                "
                        "                "
                        "                "
                        "                ")

        board1 = Board(board_string, "white")  # Remember that during testing, board_string is always white,
        # Unless you want to test black with white´s perspective
        # In that case, reverse the coordinates

        correct_result = [[5, 7, 4, 8, -100, 600, 500, -100, 500],
                          [8, 8, 4, 8, -700, 600, -100, -700, -100],
                          [8, 8, 11, 8, 0, 1000, 1000, -700, 300]]

        user1 = User("black")

        my_test1 = user1.think_all_possible_actions(board1.currentBoard)

        self.assertEqual(my_test1, correct_result)

        # Scenario 4: Different choices. Of course the couldnt be missing the famous "no available move found".

        board_string = ("           r    "
                        "   r            "
                        "                "
                        "          r     "
                        "                "
                        "                "
                        "                "
                        "                "
                        "        Q       "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                ")

        board1 = Board(board_string, "white")

        correct_result = []

        user1 = User("white")

        my_test1 = user1.think_all_possible_actions(board1.currentBoard)

        self.assertEqual(my_test1, correct_result)

        # Scenario 5:
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
                        "                "
                        "              q "
                        "     Q          "
                        "                "
                        "                "
                        "                "
                        "PPPPP PPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = []

        user1 = User("white")

        my_test1 = user1.think_all_possible_actions(board1.currentBoard)

        self.assertNotEqual(my_test1, correct_result)

    def test_forTheQueens(self):
        # Scenario 1: First turn
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
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

        correct_result = []

        user1 = User("white")

        my_test1 = user1.for_the_queens(board1.currentBoard, 200)

        self.assertNotEqual(my_test1, correct_result)

        # Scenario 2: Nothing to eat, such as the first turn
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "       P        "
                        "                "
                        "PPPPPPP PPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = [10, 7, 9, 7, 0, "P"]

        user1 = User("white")

        my_test1 = user1.for_the_queens(board1.currentBoard, 200)

        self.assertEqual(my_test1, correct_result)

        # Scenario 3: Nothing to eat, such as the first turn
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "ppppppp pppppppp"
                        "                "
                        "       p        "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "                "
                        "P      P        "
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = [12, 0, 10, 0, 0, "P"]

        user1 = User("white")

        my_test1 = user1.for_the_queens(board1.currentBoard, 200)

        self.assertEqual(my_test1, correct_result)

        # Scenario 4: Need to debug this
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
                        "                "
                        "              q "
                        "     Q          "
                        "                "
                        "                "
                        "                "
                        "PPPPP PPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        correct_result = []

        user1 = User("white")

        my_test1 = user1.for_the_queens(board1.currentBoard, 200)

        self.assertNotEqual(my_test1, correct_result)

    def instantiate_piece(self):

        # Scenario 1: Instantiating two examples
        board_string = ("rrhhbbqqkkbbhhrr"
                        "rrhhbbqqkkbbhhrr"
                        "pppppppppppppppp"
                        "pppppppppppppppp"
                        "                "
                        "                "
                        "                "
                        "            Q   "
                        "           K    "
                        "                "
                        "                "
                        "                "
                        "PPPPP PPPPPPPPPP"
                        "PPPPPPPPPPPPPPPP"
                        "RRHHBBQQKKBBHHRR"
                        "RRHHBBQQKKBBHHRR")
        board1 = Board(board_string, "white")

        user1 = User("white")

        my_test1 = user1.instantiate_piece(board1.currentBoard, 8, 11, "white")

        self.assertIsInstance(my_test1, King)


if __name__ == '__main__':
    unittest.main()

# python3 -m unittest classes/TestUser.py
