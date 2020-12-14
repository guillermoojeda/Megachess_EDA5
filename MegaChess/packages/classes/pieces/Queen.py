from .Piece import Piece


class Queen(Piece):

    def __init__(self, coord_x, coord_y, actual_turn):
        Piece.__init__(self, coord_x, coord_y, actual_turn)

        self.potentialMovesN = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0],
                                [-10, 0], [-11, 0], [-12, 0], [-13, 0], [-14, 0], [-15, 0]]  # N
        self.potentialMovesNE = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9],
                                 [-10, 10], [-11, 11], [-12, 12], [-13, 13], [-14, 14], [-15, 15]]  # NE
        self.potentialMovesE = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
                                [0, 11], [0, 12], [0, 13], [0, 14], [0, 15]]  # E
        self.potentialMovesSE = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
                                 [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]  # SE
        self.potentialMovesS = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0],
                                [11, 0], [12, 0], [13, 0], [14, 0], [15, 0]]  # S
        self.potentialMovesSW = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9],
                                 [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15]]  # SW
        self.potentialMovesW = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],
                                [0, -10], [0, -11], [0, -12], [0, -13], [0, -14], [0, -15]]  # W
        self.potentialMovesNW = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8],
                                 [-9, -9], [-10, -10], [-11, -11], [-12, -12], [-13, -13], [-14, -14], [-15, -15]]  # NW

        self.potentialMoves = [self.potentialMovesN, self.potentialMovesNE, self.potentialMovesE, self.potentialMovesSE,
                               self.potentialMovesS, self.potentialMovesSW, self.potentialMovesW, self.potentialMovesNW]
        self.points = 70  # I know its 5. For decision-making i am basing on threat level not points, it has given me
        # better results

        """
        potential_moves is how does the piece moves according to rules. These values are added to the initial 
        coordinates XY position.
        Remember this is a list, so a queen would potentially move in 8 directions, a distance of 15 to each
        """

    def think_possible_moves(self, current_board):
        """Returns the actually valid moves in a list with 2 lists: eating moves first, and the rest of
        available moves in second place
        Arguments: current_board."""

        common_moves = []
        eating_moves = []
        for i in self.potentialMoves:
            # print ("Evaluating", i)
            for j in i:
                # print ("Evaluating", j)
                if not self.is_move_possible(j):
                    break  # Stops evaluation for that direction, if it meets the boundary of the board.
                else:
                    if self.is_destination_occupied(j, current_board):
                        break  # Stops evaluation for that direction, if it finds a friend in that direction .
                    else:
                        if current_board[self.coord_x + j[0]][self.coord_y + j[1]] in self.enemies:
                            eating_moves.append(j)
                            break  # Stops evaluation for that direction, if it finds a foe in that direction,
                            # and adds location to possibleEats.
                        else:
                            common_moves.append(j)

        # print ([eating_moves, common_moves])
        return [eating_moves, common_moves]
