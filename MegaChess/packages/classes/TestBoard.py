import unittest
from packages.classes.Board import Board


class TestBoard(unittest.TestCase):

    def test_print_board(self):
        # Scenario 1: Game start

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

        my_test1 = board1.print_board()

        self.assertEqual(my_test1, None)

        #  Note: I do not know how to test a function that only "prints", but has no "return", so I just wrote "None".


