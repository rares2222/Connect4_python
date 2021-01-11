import numpy as np

from play.srv import *


class UI:

    def __init__(self, srv):
        self.__srv = srv

    def __ui_print_board(self):
        b = self.__srv.board_game()
        print(np.flip(b, 0))

    def __ui_player1(self):
        col = int(input("Player 1 turn:\n-choose a column between 0-6:\n"))
        if col < 0 or col > 6:
            raise ValueError("Input must be  between 0 and 6!!!!!")
        else:
            value = 1
            self.__srv.drop_piece(col, value)

    def __ui_player2(self):
        col = int(input("Player 2 turn:\n-choose a column between 0-6:\n"))
        if col < 0 or col > 6:
            raise ValueError("Input must be  between 0 and 6!!!!!")
        else:
            value = 2
            self.__srv.drop_piece(col, value)

    def __ui_winning_move_player1(self):
        value = 1
        if self.__srv.winning_move(value):
            return True

    def __ui_winning_move_player2(self):
        value = 2
        if self.__srv.winning_move(value):
            return True

    def run(self):
        turn = 0
        while True:

            if turn == 0:  # Player 1
                try:
                    self.__ui_player1()
                    turn += 1
                except ValueError as ve:
                    print(ve)
                self.__ui_print_board()
                if self.__ui_winning_move_player1():
                    print("player 1 wins!!!!!!")
                    return

            if turn == 1:  # Player 2
                try:
                    self.__ui_player2()
                    turn += 1

                except ValueError as ve:
                    print(ve)
                self.__ui_print_board()
                if self.__ui_winning_move_player2():
                    print("player 2 wins!!!!!!")
                    return
            turn = turn % 2
