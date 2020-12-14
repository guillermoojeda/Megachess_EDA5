from .Piece import Piece


class Rook(Piece):

    def __init__(self, coord_x, coord_y, actual_turn):
        Piece.__init__(self, coord_x, coord_y, actual_turn)

        self.potentialMovesN = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0],
                                [-10, 0], [-11, 0], [-12, 0], [-13, 0], [-14, 0], [-15, 0]]  # N
        self.potentialMovesE = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
                                [0, 11], [0, 12], [0, 13], [0, 14], [0, 15]]  # E
        self.potentialMovesS = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0],
                                [11, 0], [12, 0], [13, 0], [14, 0], [15, 0]]  # S
        self.potentialMovesW = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],
                                [0, -10], [0, -11], [0, -12], [0, -13], [0, -14], [0, -15]]  # W
        self.potentialMoves = [self.potentialMovesN, self.potentialMovesE, self.potentialMovesS, self.potentialMovesW]
        self.points = 60                      
        """
        potential_moves is how does the piece moves according to rules. These values are added to the initial
        coordinates XY.
        """      

    def think_possible_moves(self, current_board):
        """Returns the actually valid moves in a list with 2 lists: eating moves first, and the rest of
        available moves in second place
        Arguments: current_board."""

        common_moves = []
        eating_moves = []
        for i in self.potentialMoves:
            for j in i:
                if not self.is_move_possible(j):
                    break  # Stops evaluation for that direction, if it mets the boundary of the board.
                else:
                    if self.is_destination_occupied(j, current_board):
                        break  # Stops evaluation for that direction, if it finds a friend in that direction .

                    else:
                        if current_board[self.coord_x + j[0]][self.coord_y + j[1]] in self.enemies:
                            eating_moves.append(j)
                            break  # Stops evaluation for that direction, if it finds a foe in that direction, and
                            # adds it to the possible eats list.
                        else:
                            common_moves.append(j)

        return [eating_moves, common_moves]
