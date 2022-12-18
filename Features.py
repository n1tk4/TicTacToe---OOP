from Model import *
import Controller
import json

class Features:
    def __init__(self, controller):
        self.model = Model()
        self.controller = controller


    def computer(self, board):
        best_score = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'O'
                score = self.minimax(board, False)
                print(self.model.board)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
                    best_move = key
        return best_move

    def minimax(self, board, is_maximizing):
        result = self.controller.get_winner(board)
        if result != ' ':
            score = self.controller.scores[result]
        if is_maximizing:
            best_score = -99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'O'
                    score = self.minimax(board, False)
                    board[key] = ' '
                    if (score > best_score):
                        best_score = score
            return best_score
        else:
            best_score = 99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'X'
                    score = self.minimax(board, True)
                    board[key] = ' '
                    if (score < best_score):
                        best_score = score
            return best_score

    def save_game(self):
        filename = 'board.json'
        data ={
            "board": self.model.board
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_game(self):
        board = None
        filename = 'board.json'
        with open(filename) as f:
            data = json.load(f)
            board = data["board"]
            board = {int(k):str(v) for k,v in board.items()}
        return board
