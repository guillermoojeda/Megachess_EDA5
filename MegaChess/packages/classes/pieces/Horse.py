from .Piece import Piece

class Horse(Piece):

    def __init__(self, coord_x, coord_y, actual_turn):
        Piece.__init__(self, coord_x, coord_y, actual_turn)

        self.potential_moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        self.points = 30
        """
        potential_moves is how does the piece moves according to rules. These values are added to the initial 
        coordinates XY.
        Remember this is a list, so a queen would potentially move in 8 directions, a distance of 15 to each
        """      
        
    def think_possible_moves(self, current_board):
        """Returns the actually valid moves in a list with 2 lists: eating moves first, and the rest of
        available moves in second place
        Arguments: current_board."""

        common_moves = []
        eating_moves = []
        for i in self.potential_moves:
            if self.is_move_possible(i):
                if not self.is_destination_occupied(i, current_board):
                    
                    if current_board[self.coord_x + i[0]][self.coord_y + i[1]] in self.enemies:
                        eating_moves.append(i)
                    else:
                        if 15 >= self.coord_x + i[0] >= 0 and 15 >= self.coord_y + i[1] >= 0:
                            common_moves.append(i)

        return [eating_moves, common_moves]
