import random

from .pieces.Pawn import Pawn
from .pieces.Rook import Rook
from .pieces.Horse import Horse
from .pieces.Bishop import Bishop
from .pieces.Queen import Queen
from .pieces.King import King
from .Board import Board


class User(object):
    """Class that represent a player, or user. It is the actual AI of this client."""

    # Constructor
    def __init__(self, actual_turn):
        self.player_color = actual_turn
        if self.player_color == "white":
            self.enemies = "prqhbk"
            self.friends = "PRQHBK"
            self.enemy_color = "black"
        else:
            self.enemies = "PRQHBQK"
            self.friends = "prqhbqk"
            self.enemy_color = "white"

    # Methods

    def instantiate_piece(self, current_board, coord_x, coord_y, color):
        """ Instantiates a corresponding piece, according what letter is read in the entered coordinates. Used to
        "think" what would happen if a piece is generated somewhere in the board.
        Arguments:  board as a board.current_board property, coord_x (int), coord_y (int), color ("white" or "black",
        can also use self.player_color or self.enemy_color property)
        Returns: the corresponding instance of piece (returns an object!)
        """
        letter = current_board[coord_x][coord_y]

        if letter == "p" or letter == "P":
            instance1 = Pawn(coord_x, coord_y, color)

        elif letter == "r" or letter == "R":
            instance1 = Rook(coord_x, coord_y, color)

        elif letter == "h" or letter == "H":
            instance1 = Horse(coord_x, coord_y, color)

        elif letter == "b" or letter == "B":
            instance1 = Bishop(coord_x, coord_y, color)

        elif letter == "q" or letter == "Q":
            instance1 = Queen(coord_x, coord_y, color)

        elif letter == "k" or letter == "K":
            instance1 = King(coord_x, coord_y, color)

        else:
            raise Exception(
                f"Attempted to instantiate a piece from board, but that character is not recognized as a piece. "
                f"CoordX = {coord_x} CoordY = {coord_y} from player´s perspective. Current player:{color}"
            )

        return instance1

    def think_all_possible_actions(self, current_board):
        """Will see the board and evaluate what moves can eat something, 
        Arguments: current_board (as board.CurrentBoard method), color (as string, or as player.Color or
        player.enemy_color property)
        Returns a list of pairs of coordinates (from_row, from_col, to_row, to_col), which are the available moves that
        eat something or not, with values:
        (from_row, from_col, to_row, to_col, pointsLost, pointsEarned, (pointsEarned + pointsLost), worstPointsLost,
        decision_score)."""

        actions_list = self.think_all_possible_eats(current_board, self.player_color)

        for i in actions_list:
            i.append(- self.simulate_move(current_board, i[0], i[1], i[2], i[3]))
            decision_score = i[5] + i[7]
            i.append(decision_score)

        return actions_list

    def think_all_possible_eats(self, current_board, color):
        """Will see the board and evaluate what moves can eat something.
        Arguments: current_board (as board.CurrentBoard method), color (as string, or as player.Color or
        player.enemy_color property)
        Returns a list of coordinates (from_row, from_col, to_row, to_col), which are the available moves to eat
        something."""

        friends = " "

        if color == "white":
            friends = "PRHBQK"
            enemies = "prhbqk"
        if color == "black":
            enemies = "PRHBQK"
            friends = "prhbqk"

        eats_list = []

        count_i = 0
        for i in current_board:
            count_j = 0
            for j in i:
                if j in friends:

                    piece1 = self.instantiate_piece(current_board, count_i, count_j, color)
                    possible_eats = piece1.think_possible_moves(current_board)[0]
                    if possible_eats != []:
                        for k in possible_eats:
                            gets_eaten = self.can_be_eaten(current_board, count_i + k[0], count_j + k[1])
                            if gets_eaten:
                                points_lost = - (piece1.points * 10)
                            else:
                                points_lost = 0
                            piece2 = self.instantiate_piece(current_board, count_i + k[0], count_j + k[1],
                                                            piece1.enemyColor)
                            points_earned = piece2.points * 10
                            to_add = [count_i, count_j, count_i + k[0], count_j + k[1], points_lost, points_earned, (
                                    points_earned + points_lost)]  # PointsLost should be calculated other way
                            # (see below)
                            eats_list.append(to_add)
                count_j += 1
            count_i += 1
        return eats_list

    def can_be_eaten(self, current_board, coord_x, coord_y):
        """ Tells if an enemy piece can make a eating move to that location, during the enemy turn,
        Arguments: current_board as board.current_board, coord_x as int, coord Y as int.
        Returns True or False.
        """
        # La pregunta sería: Si me muevo acá, y me transformo en un peón, puedo comer a un peón enemigo? 
        # Hacerse la misma pregunta con Rey, Torre, Bishop, Reina, Caballo.
        # Si alguna pregunta responde "sí", return True.

        pawn_potential_moves = [[-1, -1], [-1, 1]]
        horse_potential_moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        king_potential_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        potential_moves_n = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0],
                             [-10, 0], [-11, 0], [-12, 0], [-13, 0], [-14, 0], [-15, 0]]  # N
        potential_moves_ne = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9],
                              [-10, 10], [-11, 11], [-12, 12], [-13, 13], [-14, 14], [-15, 15]]  # NE
        potential_moves_e = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10],
                             [0, 11], [0, 12], [0, 13], [0, 14], [0, 15]]  # E
        potential_moves_se = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
                              [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]  # SE
        potential_moves_s = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                             [12, 0], [13, 0], [14, 0], [15, 0]]  # S
        potential_moves_sw = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9],
                              [10, -10], [11, -11], [12, -12], [13, -13], [14, -14], [15, -15]]  # SW
        potential_moves_w = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9],
                             [0, -10], [0, -11], [0, -12], [0, -13], [0, -14], [0, -15]]  # W
        potential_moves_nw = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9],
                              [-10, -10], [-11, -11], [-12, -12], [-13, -13], [-14, -14], [-15, -15]]  # NW

        cross_potential_moves = [potential_moves_n, potential_moves_e, potential_moves_s, potential_moves_w]
        x_potential_moves = [potential_moves_ne, potential_moves_se, potential_moves_sw, potential_moves_nw]

        for i in pawn_potential_moves:
            if coord_x + i[0] > 15 or coord_x + i[0] < 0 or coord_y + i[1] > 15 or coord_y + i[1] < 0:
                pass

            else:

                resulting_move = current_board[coord_x + i[0]][coord_y + i[1]]

                if (resulting_move == "p" or resulting_move == "P") and resulting_move in self.enemies:

                    return True

        for i in king_potential_moves:
            if coord_x + i[0] > 15 or coord_x + i[0] < 0 or coord_y + i[1] > 15 or coord_y + i[1] < 0:
                pass

            else:
                resulting_move = current_board[coord_x + i[0]][coord_y + i[1]]

                if (resulting_move == "k" or resulting_move == "K") and resulting_move in self.enemies:
                    return True

        for i in horse_potential_moves:
            if coord_x + i[0] > 15 or coord_x + i[0] < 0 or coord_y + i[1] > 15 or coord_y + i[1] < 0:
                pass
            else:
                resulting_move = current_board[coord_x + i[0]][coord_y + i[1]]
                if (resulting_move == "h" or resulting_move == "H") and resulting_move in self.enemies:
                    return True

        for i in cross_potential_moves:
            for j in i:
                if coord_x + j[0] > 15 or coord_x + j[0] < 0 or coord_y + j[1] > 15 or coord_y + j[1] < 0:
                    break

                resulting_move = current_board[coord_x + j[0]][coord_y + j[1]]
                if resulting_move in self.friends:  # Stops evaluating in that direction if it comes across a friend.
                    break

                if resulting_move in self.enemies:
                    if resulting_move == "r" or resulting_move == "R" or resulting_move == "q" or resulting_move == "Q":
                        return True
                    else:
                        break  # Will also stop evaluating direction if the enemy found is not a queen or a rook

        for i in x_potential_moves:
            for j in i:
                if coord_x + j[0] > 15 or coord_x + j[0] < 0 or coord_y + j[1] > 15 or coord_y + j[1] < 0:
                    break

                resulting_move = current_board[coord_x + j[0]][coord_y + j[1]]
                if resulting_move in self.friends:  # Stops evaluating in that direction if it comes across a friend.
                    break

                if resulting_move in self.enemies:
                    if resulting_move == "b" or resulting_move == "B" or resulting_move == "q" or resulting_move == "Q":
                        return True
                    else:
                        break
        return False

    def think_all_possible_common_moves(self, current_board, color):
        """Will see the board and evaluate what moves can eat something.
        Arguments: current_board, current color.
        Returns a list of available moves to eat something, which contains coordinates and points that will be lost if
        the piece gets eaten, in the format:
        [from_row, from_col, to_col, to_row, points_lost, pieceThatIsMoving]. """

        moves_list = []

        count_i = 0
        for i in current_board:
            count_j = 0
            for j in i:
                if j in self.friends:
                    piece1 = self.instantiate_piece(current_board, count_i, count_j, color)
                    possible_moves = piece1.think_possible_moves(current_board)[1]
                    if possible_moves != []:
                        for k in possible_moves:
                            # toAdd = [[count_i, count_j], [count_i+k[0], count_j+k[1]]]
                            # Format is from_row, form_col, to_row, to_col.
                            gets_eaten = self.can_be_eaten(current_board, count_i + k[0], count_j + k[1])
                            if gets_eaten:
                                points_lost = - (piece1.points * 10)
                            else:
                                points_lost = 0

                            to_add = [count_i, count_j, count_i + k[0], count_j + k[1], points_lost,
                                      current_board[count_i][count_j]]
                            moves_list.append(to_add)
                count_j += 1
            count_i += 1

        # Now, to moves_list, I have to:
        # add points in danger if not move, 
        # add pointsYield
        # add pointsLostNextTurn. Its the value of the piece if it can be eaten.

        return moves_list

    def simulate_move(self, current_board, from_row, from_col, to_row, to_col):
        """Get the highest possible points that the enemy would get if a given move is made.
        Arguments: current board as board.current_board, then coordinates, all of them as int.
        Returns: a points value that goes from zero to below, with the potential score the opponent may get
        """

        current_board2 = current_board

        piece_move = current_board2[from_row][from_col]

        eaten_piece = current_board2[to_row][to_col]

        # Next lines to replace one character in the strings (that are our rows)

        current_board2[from_row] = current_board2[from_row][:from_col] + " " + current_board2[from_row][from_col + 1:]

        current_board2[to_row] = current_board2[to_row][:to_col] + piece_move + current_board2[to_row][to_col + 1:]

        # Next lines to get enemy´s perspective

        current_board3 = []

        for i in current_board2:
            i = i[::-1]
            current_board3.append(i)

        current_board3 = current_board3[::-1]  # board with enemy´s perspective

        # returning board to its original state:

        color = self.enemy_color

        best_move = self.play_best_move(current_board3, color)

        # Return board to original state,

        current_board2[to_row] = current_board2[to_row][:to_col] + eaten_piece + current_board2[to_row][to_col + 1:]

        current_board2[from_row] = current_board2[from_row][:from_col] + piece_move + current_board2[from_row][from_col
                                                                                                               + 1:]
        # Continue

        if best_move == []:
            return 0

        else:
            return best_move[5]

    def play_best_move(self, current_board, player_color):
        """ Strategy. Plays the best possible move based on points balance.
        Arguments: current board as board1.current_board.
        Returns: A move (list with 4 ints), that will yield the best balance available.
        In case of a draw between one or more moves, will prioritize moves with no casualties in next opponent´s turn
        Then,  will return one of those possible moves randomly.
        """
        possible_moves = self.think_all_possible_eats(current_board, player_color)

        if not possible_moves:
            return []

        sorted_moves = sorted(possible_moves, key=lambda x: int(x[5]))[::-1]

        max_balance = sorted_moves[0][5]

        best_moves = []

        for i in sorted_moves:
            if i[5] == max_balance:
                best_moves.append(i)

        ncbm = []  # Stands for "No Casualties Best Moves"

        for i in best_moves:
            if i[4] == 0:
                ncbm.append(i)

        if ncbm != []:
            move = ncbm[random.randint(0, len(ncbm) - 1)]

        elif best_moves != []:
            move = best_moves[random.randint(0, len(best_moves) - 1)]

        else:
            move = []

        if move != []:
            move_result = move
            return move_result

        else:
            return move

    # Strategies begin here

    def for_the_queens(self, current_board, turns_left):
        """Strategy. Attempts to crown pawns into queens, being careful that they don´t get eaten before crowning.
        Returns: a move [from_row, from_col, to_col, to_row]
        """

        enemy_pawn_threat = False  # Tells if there is a pawn that will become a queen. or a queen that could eat
        # a pawn after I crown it. Only useful at the first 20 turns (see code below), will be useful to tell me what
        # positions will be eaten by an enemy pawn, if I keep advancing with this pawn to crown it.

        pawn_count = 0

        pawn_threats = []

        possible_moves = self.think_all_possible_common_moves(current_board, self.player_color)
        if possible_moves == []:
            return []

        pawn_possible_moves = []

        for i in possible_moves:
            if i[5] == "p" or i[5] == "P":
                pawn_possible_moves.append(i)
        if pawn_possible_moves == []:
            return []

        pawn_best_moves = []  # Had to initialize to prevent crash

        count_i = 0
        for i in current_board[4:8]:

            count_j = 0
            for j in i:
                if (j == "p" or j == "P" or j == "q" or j == "Q") and j in self.enemies and turns_left > 180:
                    pawn_count += 1  # Enemy pawns are not assumed to be a danger if there are more than 2 in the 3rd
                    # quarter of map, because it is assumed that opponent is not thinking to kill my crowned queens or
                    # pawns. Later in the game, there will be surely more than 2 of these pieces, so the variable
                    # enemy_pawn_threat is set to False in this case by default.
                    pawn_threats.append([count_i + 4, count_j])
                    enemy_pawn_threat = True

                if pawn_threats != [] and enemy_pawn_threat:
                    pawn_best_moves = []
                    for k in pawn_threats:
                        for m in pawn_possible_moves:  # This was painful. Basically I have to make sure my pawn gets
                            # crowned b4 an enemy pawn does in front of him, that can eat him.

                            col_ally = m[1]
                            col_enemy = k[1]
                            row_ally = m[0]
                            row_enemy = k[0]

                            diff_col = col_ally - col_enemy

                            if abs(diff_col) > 1:
                                pawn_best_moves.append(m)

                            elif row_ally - 8 <= 7 - row_enemy:
                                pawn_best_moves.append(m)

                else:
                    pawn_best_moves = pawn_possible_moves
                count_j += 1
            count_i += 1

        if pawn_best_moves == []:
            pawn_best_moves = pawn_possible_moves

        # Note that think_all_possible_moves returns a list of list with these headers:
        # (from_row, from_col, to_col, to_row, pointsLost, pieceThatIsMoving)

        pawn_best_moves2 = []
        for i in pawn_best_moves:
            if i[4] == 0:
                pawn_best_moves2.append(i)

        if pawn_best_moves2 == []:  # Makes no sense moving something that is going to die anyways...
            return []

        pawn_best_moves3 = []  # Attempts to make pawn move two places.
        for i in pawn_best_moves2:
            if i[2] - i[0] == 0:
                pawn_best_moves3.append(i)
        if pawn_best_moves3 == []:
            pawn_best_moves3 = pawn_best_moves2

        sorted_moves = sorted(pawn_best_moves, key=lambda x: int(x[2]))  # Ordering options checking what makes my
        # pawns go most forward.

        most_forward = sorted_moves[0][2]

        sorted_moves2 = []

        for i in sorted_moves:
            if i[2] == most_forward:
                sorted_moves2.append(i)

        moves = sorted_moves[random.randint(0, len(sorted_moves2) - 1)]

        return moves

    @staticmethod
    def coord_to_send(coord, actual_turn):
        """Corrects the coordinates ONLY if needed due to perspective change when playing black color.
        Argument: one coordinate, X OR Y, not both.
        Returns the corrected coordinates if playing black, or the same coordinate if playing white"""

        if actual_turn == "white":
            return coord
        elif actual_turn == "black":
            step1 = coord - 7
            step2 = 8 - step1
            new_coord = step2
            return new_coord

    def decide_move(self, data):
        """
        Decides the move to make.
        Arguments: self, and data (the incoming socket, after using json.loads(incoming_socket))
        Returns: a list with 4 ints, that are the coordinates: [from_row, from_col, to_row, to_col]
        Will print board and coordinates decided on console.
        """

        board_string = data['data']['board']
        actual_turn = data['data']['actual_turn']
        turns_left = data['data']['move_left']

        board1 = Board(board_string, actual_turn)
        current_board = board1.currentBoard

        move1 = []
        moves = []
        print("mark1")

        try:
            move1 = self.think_all_possible_actions(current_board)
            move2 = sorted(move1, key=lambda x: int(x[8]))[::-1]
            move1 = move2[0]
            print("mark2")
            print(move1)
        except Exception as e:
            print("Error found:", e)
            print("Strategy cannot be accomplished since there are no possible eating moves.")
            print("Proceeding with other strategy")
            moves = []

        if not moves:
            moves = move1

        move1 = self.for_the_queens(board1.currentBoard, turns_left)

        print("mark3")
        print(move1)

        if not moves:
            moves = move1

        try:
            move1 = self.think_all_possible_common_moves(current_board, self.player_color)
            move2 = sorted(move1, key=lambda x: int(x[4]))[::-1]
            move1 = move2[0]
            print("mark4")
            print(move1)
        except Exception as e:
            print("Error found:", e)
            moves = []

        if not moves:
            moves = move1

        """
        Preparing coordinates sending.
        """

        board1.print_board()

        print("mark5")
        print(moves)

        from_row = moves[0]
        from_col = moves[1]

        to_row = moves[2]
        to_col = moves[3]

        from_row = self.coord_to_send(from_row, actual_turn)
        from_col = self.coord_to_send(from_col, actual_turn)
        to_row = self.coord_to_send(to_row, actual_turn)
        to_col = self.coord_to_send(to_col, actual_turn)

        print("Move")
        print("from_row=", from_row)
        print("from_col=", from_col)

        print("To")
        print("to_row=", to_row)
        print("to_col=", to_col)

        print("Decision Made:")
        print("Moving from [" + str(from_row) + " " + str(from_col) + "]")
        print("to [" + str(to_row) + " " + str(to_col) + "]")
        print("\n")

        return [from_row, from_col, to_row, to_col]
