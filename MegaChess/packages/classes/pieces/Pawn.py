from .Piece import Piece


class Pawn(Piece):

    def __init__(self, coord_x, coord_y, actual_turn):
        Piece.__init__(self, coord_x, coord_y, actual_turn)
        self.potentialMoves = [[-1, 0]]
        self.points = 10
        """
        potential_moves is how does the piece moves according to rules. These values are added to the initial 
        coordinates XY position when calculating a move.
        Remember this is a list, so a queen would potentially move in 8 directions, a distance of 15 to each
        """

    def think_possible_moves(self, current_board):
        """Returns the actually valid moves.
        Arguments is the current_board, as a list within a list format, (e.g.: board1.current_board, being board 1 an
        instance of Board)
        returns a list with two lists: [possible_eats, possible_moves], eg: [[[0, -1], [0, 1]],[[-1, 0], [-2, 0]]]
        """
        possible_moves = []
        possible_eats = []
        if self.coord_x == 13 or self.coord_x == 12:
            if current_board[self.coord_x - 1][self.coord_y] == " ":
                possible_moves.append([-2, 0])

        for i in self.potentialMoves:
            if self.is_move_possible(i) and not self.is_destination_occupied(i, current_board):
                possible_moves.append(i)

        # Next lines to check if pawns can eat something
        # These next lines enables a pawn to "eat" an enemy in diagonal

        if self.coord_x - 1 > -1 and self.coord_y - 1 > -1:  # To make sure we are evaluating inside the board.
            if current_board[self.coord_x - 1][self.coord_y - 1] in self.enemies:
                possible_eats.append([-1, -1])
        if self.coord_x - 1 > -1 and self.coord_y + 1 < 16:
            if current_board[self.coord_x - 1][self.coord_y + 1] in self.enemies:
                possible_eats.append([-1, 1])

        # Following 9 lines of code : pawns cannot  eat to the front, so the moves to the front must be removed
        # accordingly if an enemy is there.
        evaluated_position = current_board[self.coord_x - 2][self.coord_y]
        print(evaluated_position)

        if evaluated_position != " ":
            if [-2, 0] in possible_moves:
                possible_moves.remove([-2, 0])

        evaluated_position = current_board[self.coord_x - 1][self.coord_y]

        if evaluated_position != " ":
            if [-1, 0] in possible_moves:
                possible_moves.remove([-1, 0])
            if [-2, 0] in possible_moves:
                possible_moves.remove([-2, 0])

        return [possible_eats, possible_moves]
