from packages.classes.pieces.Piece import Piece


class Bishop(Piece):

    def __init__(self, coord_x, coord_y, actual_turn):
        Piece.__init__(self, coord_x, coord_y, actual_turn)

        self.potentialMovesNE = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9],
                                 [-10, 10], [-11, 11], [-12, 12], [-13, 13], [-14, 14], [-15, 15]]  # NE
        self.potentialMovesSE = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
                                 [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]  # SE
        self.potentialMovesSW = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9],
                                 [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15]]  # SW
        self.potentialMovesNW = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8],
                                 [-9, -9], [-10, -10], [-11, -11], [-12, -12], [-13, -13], [-14, -14], [-15, -15]]  # NW

        self.potentialMoves = [self.potentialMovesNE, self.potentialMovesSE, self.potentialMovesSW,
                               self.potentialMovesNW]
        self.points = 40

        """
        potential_moves is how does the piece moves according to rules. These values are added to the initial 
        coordinates XY.
        Remember this is a list, so a queen would potentially move in 8 directions, a distance of 15 to each
        """

    def think_possible_moves(self, current_board):
        """Returns a list with 2 lists, eating moves first, and the rest of availables moves in second place. Each
        conintains any number of pairs of coordinates [move_from, move_to].
        example: [[[move_from1, move_to1], [move_from2, move_to2]], [[move_from3, move_to3]]]
        Arguments: current_board."""

        common_moves = []
        eating_moves = []
        for i in self.potentialMoves:
            # print ("Evaluating", i)
            for j in i:
                # print ("Evaluating", j)
                if not self.is_move_possible(j):
                    break  # Stops evaluation for that direction, if it mets the boundary of the board.
                else:
                    if self.is_destination_occupied(j, current_board):
                        break  # Stops evaluation for that direction, if it finds a friend in that direction .
                    else:
                        if current_board[self.coord_x + j[0]][self.coord_y + j[1]] in self.enemies:
                            eating_moves.append(j)
                            break  # Stops evaluation for that direction, if it finds a foe in that direction, and
                            # adds location to possibleEats.
                        else:
                            common_moves.append(j)

        return [eating_moves, common_moves]
