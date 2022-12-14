class Model:
    def __init__(self):
        self.board = self.new_board()
        self.winner = ' '
        self.valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = 'O'

    @staticmethod
    def new_board():
        board = {
            1 : 'O', 2 : ' ', 3 : ' ',
            4 : ' ', 5 : ' ', 6 : ' ',
            7 : 'X', 8 : ' ', 9 : 'O'
        }
        return board

    def get_winner(self):
        # Rows
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != ' ':
            self.winner = self.board[1]
        elif self.board[4] == self.board[5] == self.board[6] and self.board[4] != ' ':
            self.winner = self.board[4]
        elif self.board[7] == self.board[8] == self.board[9] and self.board[7] != ' ':
            self.winner = self.board[7]

        # Columns
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            self.winner = self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ':
            self.winner = self.board[2]
        elif self.board[3] == self.board[6] == self.board[9] and self.board[3] != ' ':
            self.winner = self.board[3]

        # Diagonals
        elif self.board[1] == self.board[5] == self.board[9] and self.board[1] != ' ':
            self.winner = self.board[5]
        elif self.board[3] == self.board[5] == self.board[7] and self.board[3]!= ' ':
            self.winner = self.board[5]
        return self.winner

    def is_draw(self):
        for key in self.board.keys():
            if self.board[key] == ' ':
                return False
        return True
