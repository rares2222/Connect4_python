import numpy as np


class Board():
    def __init__(self):
        self.__board = np.zeros((6, 7))

    def get_board(self):
        return self.__board[:]

    def drp(self, col, row, value):
        # add a new piece(1 or 2) in the board
        self.__board[row][col] = value
        return self.__board[:]
