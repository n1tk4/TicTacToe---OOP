from Model import *


class View:
    """View is just for printing states and highlights input hints"""
    def __init__(self, model):
        self.model = model

    def print_board(self, board):
        print('Current board:')
        print('+---+---+---+')
        print(f"| {board[1]} | {board[2]} | {board[3]} |   1  2  3")
        print('+---+---+---+')
        print(f"| {board[4]} | {board[5]} | {board[6]} |   4  5  6")
        print('+---+---+---+')
        print(f"| {board[7]} | {board[8]} | {board[9]} |   7  8  9")
        print('+---+---+---+')

    def greet(self):
        print("Welcome to Tic Tac Toe!")

    def print_winner(self, winner):
        print(f"The {winner} won the game!")

    def print_draw(self):
        print("No winner - it's a draw!")

    def choose_mode(self):
        print("We have 2 modes in our game:")
        return "enter 'p' for player mode and 'a' for ai mode: \n"

    def not_possible(self, square):
        print(f"Can't make move {square}, square already taken!")

    def print_ai_mode(self):
        print("AI mode has been started...")

    def print_player_mode(self):
        print("Player mode has been started...")

    def print_value_error(self):
        print("\nPlease, give a valid number: ")

    def print_input_number(self):
        return "\nPlease, give a spot's position: "