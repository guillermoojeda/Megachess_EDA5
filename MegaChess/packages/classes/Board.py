class Board(object):

    def __init__(self, board_string, actual_turn):
        self.playerColor = actual_turn
        if actual_turn == "white":
            self.boardString = board_string
        elif actual_turn == "black":
            self.boardString = board_string[::-1]
        self.currentBoard = [self.boardString[0:16],
                             self.boardString[16:32],
                             self.boardString[32:48],
                             self.boardString[48:64],
                             self.boardString[64:80],
                             self.boardString[80:96],
                             self.boardString[96:112],
                             self.boardString[112:128],
                             self.boardString[128:144],
                             self.boardString[144:160],
                             self.boardString[160:176],
                             self.boardString[176:192],
                             self.boardString[192:208],
                             self.boardString[208:224],
                             self.boardString[224:240],
                             self.boardString[240:256]]

    def print_board(self):
        """ Prints the board in a more user-friendly format, always from current-player perspective. Needs no arguments.
        Arguments: none,
        Returns: nothing, but prints the board in the console."""
        hexa = "0123456789ABCDEF"
        print("   ", hexa)
        count = 0
        for i in self.currentBoard:
            i = i.replace(" ", "_")
            print(hexa[count], "|", i, "|", hexa[count])
            count += 1
        print("   ", hexa)
