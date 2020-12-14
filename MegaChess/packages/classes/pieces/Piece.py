
class Piece(object):

    # Constructor
    def __init__(self, coord_x, coord_y, actual_turn):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coords = [coord_x, coord_y]
        self.color = actual_turn
        if self.color == "white":
            self.enemies = "prkhbq"
            self.friends = "PRQHBK"
            self.enemyColor = "black"
        else:
            self.enemies = "PRQHBK"
            self.friends = "prkhbq"
            self.enemyColor = "white"

    # Methods

    def is_move_possible(self, potential_move):
        """
        test_is_move_possible checks if the move falls within the boundaries of the board.
        Arguments: A list of ints with two elements, that represent the relative coordinates X and Y of where to move.
        Returns: True of False, depending if the move destination is or not in the board.
        """
        if 15 >= self.coord_x + potential_move[0] >= 0 and 15 >= self.coord_y + potential_move[1] >= 0:
            return True
        else:
            return False

    def is_destination_occupied(self, potential_move, current_board):
        """
        is_destination_occupied() checks if there is a friend occupying the spot.
        Returns Tue or False accordingly.
        """
        place_to_eval = [self.coord_x + potential_move[0], self.coord_y + potential_move[1]]
        if current_board[place_to_eval[0]][place_to_eval[1]] in self.friends:
            return True
        else:
            return False
