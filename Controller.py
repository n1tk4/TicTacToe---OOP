from Model import *
from View import *
import json
from functools import lru_cache


class Controller:
    """Processes user input and applies it to the view and/or model"""
    def __init__(self):
        self.model = Model()
        self.view = View(Model())
        self.call_function_times = 0

    def get_move(self):
        self.chosen_position = None
        while self.chosen_position not in self.model.valid_inputs:
            try:
                self.chosen_position = input("Please give a legal position: ")
            except KeyboardInterrupt:
                pass
            try:
                self.chosen_position = int(self.chosen_position)
            except KeyboardInterrupt:
                pass
            except ValueError:
                self.chosen_position = input("Please give a legal position: ")
            except KeyboardInterrupt:
                pass
            if self.chosen_position in self.model.valid_inputs:

                break
        return self.chosen_position

    def is_empty(self, board, chosen_position):
        while board[chosen_position] != ' ':
            self.view.print_is_taken()
            chosen_position = self.get_move()
            return True
        return False

    def make_move(self, board, chosen_position, player):
        while board[chosen_position] != ' ':
            print(f"Can't make move {chosen_position}, square already taken!") # realize in print view
            chosen_position = self.get_move()
        board[chosen_position] = player

    def player(self):
        if self.model.player == 'O':
            self.model.player = 'X'
        else:
            self.model.player = 'O'
            # print O is turn
        return self.model.player

    def computer(self, board):
        bestScore = -1000
        bestMove = 0
        score = None
        for key in board.keys():
            print(f"current key is {key}")
            if (board[key] == ' '):
                board[key] = 'O'
                print(f"current score is {bestScore}")
                score = self.minimax(False)
                print(f"minmax score {score}")
                print(self.model.board)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    print(f"bestsscore {bestScore}")
                    bestMove = key
                    print(f"Best move {bestMove}")
        return bestMove

    def best_move(self, computer):
        board = self.model.board
        board[computer] = 'O'

    @lru_cache()
    def minimax(self, is_maximizing):
        print(f"position in calculation {self.model.board}")
        self.call_function_times = self.call_function_times + 1
        print(f"call function times {self.call_function_times}")
        score = None
        if self.model.get_winner()  == 'O':
            return 1
        elif self.model.get_winner() == 'X':
            return -1
        elif self.model.is_draw():
            return 0
        self.model.winner = ' '
        if is_maximizing:
            bestScore = -99
            for key in self.model.board.keys():
                if (self.model.board[key] == ' '):
                    self.model.board[key] = 'O'
                    score = self.minimax(False)
                    self.model.board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore
        else:
            bestScore = 99
            for key in self.model.board.keys():
                if (self.model.board[key] == ' '):
                    self.model.board[key] = 'X'
                    score = self.minimax(True)
                    self.model.board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            self.call_function_times = 0
            return bestScore

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

    def ask_load(self):
        inp = input(self.view.want_previous_game())
        if inp == 'y':
            self.model.board = self.load_game()

    def player_mode(self):
        self.ask_load()
        while True:
            self.view.print_board(self.model.board)
            self.save_game()
            if self.model.get_winner() != ' ':
                self.view.print_winner()
                break
            elif self.model.is_draw():
                self.view.print_draw()
                break
            self.make_move(self.model.board, self.get_move(), self.player())

    def ai_mode(self):
        self.ask_load()
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            if self.model.get_winner() != ' ':
                self.view.print_winner()
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), self.player())
                self.view.print_winner()
            else:
                self.make_move(self.model.board, self.computer(self.model.board), self.player())
                self.model.winner=' '
            counter += 1

    def which_mode(self):
        inp = input(self.view.choose_mode())
        if inp == 'a':
            self.ai_mode()
        else:
            self.player_mode()

    def play(self):
        self.view.greet()
        self.which_mode()
