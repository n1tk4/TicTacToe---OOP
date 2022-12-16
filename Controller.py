from Model import *
from View import *
import json
import random


class Controller:
    """Processes user input and applies it to the view and/or model"""
    def __init__(self):
        self.model = Model()
        self.view = View(Model())
        self.scores = {
            'X' : -1,
            'O' : 1,
            ' ' : 0
        }

    def get_move(self):
        self.chosen_position = None
        while self.chosen_position not in self.model.valid_inputs:
            try:
                self.chosen_position = int(input(self.view.print_value_error()))
            #except TypeError:
                #quit()
            except ValueError:
                self.view.print_value_error()
            except KeyboardInterrupt:
                quit()
            if self.chosen_position in self.model.valid_inputs:
                break
        return self.chosen_position

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
        return self.model.player

    def computer(self, board):
        best_score = -1000
        for key in board.keys():
            print(f"current key is {key}")
            if (board[key] == ' '):
                board[key] = 'O'
                print(fd,"current score is {best_score}")
                score = self.minimax(board, False)
                print(f"minmax score {score}")
                print(self.model.board)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
                    best_move = key
        return best_move

    def random_move(self, board):
        r = random.choice(board)
        while True:
            if r[board] == ' ':
                return r

    def minimax(self, board, is_maximizing):
        result = self.get_winner(board)
        if result != ' ':
            score = self.scores[result]
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

    def ask_load(self):
        inp = input(self.view.want_previous_game())
        if inp == 'y':
            self.model.board = self.load_game()

    def player_mode(self):
        self.ask_load()
        self.view.print_player_mode()
        if self.model.whose_move():
            self.model.player = 'O'
        while True:
            self.view.print_board(self.model.board)
            self.save_game()
            if self.get_winner(self.model.board) != ' ':
                self.view.print_winner()
                break
            elif self.is_draw(self.model.board):
                self.view.print_draw()
                break

            self.make_move(self.model.board, self.get_move(), self.player())

    def ai_mode(self):
        self.ask_load() #patch
        self.view.print_ai_mode()
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            # comp move
            if self.get_winner(self.model.board) != ' ':
                self.view.print_winner()
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), self.player())
                self.view.print_winner()
            else:
                print(f"{self.computer(self.model.board)}")
                self.make_move(self.model.board, self.computer(self.model.board), self.player())
                self.model.winner=' '
            counter += 1

    def random_move(self, board):
        while True:
            r = random.randint(1, 9)
            print(f"here is r: {r}")
            if board[r] == ' ':
                board[r] = 'O'
                break
            else:
                continue

    def random_mode(self):
        self.ask_load()
        self.view.print_ai_mode()
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            if self.get_winner(self.model.board) != ' ':
                self.view.print_winner()
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), 'X')
                self.view.print_winner()
            else:
                self.random_move(self.model.board)
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
        try:
            self.which_mode()
        except KeyboardInterrupt:
            quit()

    def get_winner(self, board):
        # Rows
        if board[1] == board[2] == board[3] and board[1] != ' ':
            self.model.winner = board[1]
        elif board[4] == board[5] == board[6] and board[4] != ' ':
            self.model.winner = board[4]
        elif board[7] == board[8] == board[9] and board[7] != ' ':
            self.model.winner = board[7]

        # Columns
        elif board[1] == board[4] == board[7] and board[1] != ' ':
            self.model.winner = board[1]
        elif board[2] == board[5] == board[8] and board[2] != ' ':
            self.model.winner = board[2]
        elif board[3] == board[6] == board[9] and board[3] != ' ':
            self.model.winner = board[3]

        # Diagonals
        elif board[1] == board[5] == board[9] and board[1] != ' ':
            self.model.winner = board[5]
        elif board[3] == board[5] == board[7] and board[3]!= ' ':
            self.model.winner = board[5]
        return self.model.winner

    def is_draw(self, board):
        for key in board.keys():
            if board[key] == ' ':
                return False
        return True
