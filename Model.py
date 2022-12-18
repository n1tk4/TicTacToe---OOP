class Model:
    def __init__(self):
        self.board = self.new_board()
        self.winner = ' '
        self.valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = 'O'

    def new_board(self):
        board = {
            1 : ' ', 2 : ' ', 3 : ' ',
            4 : ' ', 5 : ' ', 6 : ' ',
            7 : ' ', 8 : ' ', 9 : ' '
        }
        return board

    def winner_is_found(self):
        if self.get_winner() != ' ':
            return True

    def whose_move(self):
        if sum(value == 0 for value in self.board.values()) % 2 == 1:
            return True #X is turn
        else:
            return False
