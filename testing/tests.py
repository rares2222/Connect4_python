import unittest
from board.repo import Board
import numpy as np
from play.srv import Service


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__repo = Board()
        self.__srv = Service(self.__repo)

    def test_Board(self):
        b = self.__repo.get_board()
        x = np.zeros((6, 7))
        self.assertTrue((b == x).all())

    def test_drp(self):
        b = self.__repo.drp(0, 0, 1)
        x = np.zeros((6, 7))
        x[0][0] = 1
        self.assertTrue((b == x).all())

    def test_valid(self):
        self.assertTrue(self.__srv.is_valid_location(0))
        x=self.__repo.get_board()



    def test_get_next_open_row(self):
        b=self.__repo.get_board()
        self.assertEqual(self.__srv.get_next_open_row(0),b[0][0])

    def test_drop_piece(self):
        x = self.__repo.get_board()
        x[0][0]=1
        self.__srv.drop_piece(0,1)
        b = self.__srv.board_game()
        self.assertTrue((b == x).all())

    def test_winning_move_vertical(self):
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.assertTrue(self.__srv.winning_move(1))

    def test_winning_move_orizontal(self):
        self.__srv.drop_piece(1, 2)
        self.__srv.drop_piece(2, 2)
        self.__srv.drop_piece(3, 2)
        self.__srv.drop_piece(4, 2)
        self.assertTrue(self.__srv.winning_move(2))

    def test_winning_move_diagonal1(self):
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(1, 2)
        self.__srv.drop_piece(2, 2)
        self.__srv.drop_piece(3, 2)
        self.__srv.drop_piece(4, 2)
        self.__srv.drop_piece(1, 1)
        self.__srv.drop_piece(2, 2)
        self.__srv.drop_piece(3, 2)
        self.__srv.drop_piece(2, 1)
        self.__srv.drop_piece(3, 2)
        self.__srv.drop_piece(3, 1)
        self.assertTrue(self.__srv.winning_move(1))

    def test_winning_move_diagonal2(self):
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(0, 1)
        self.__srv.drop_piece(1, 1)
        self.__srv.drop_piece(1, 1)
        self.__srv.drop_piece(1, 1)
        self.__srv.drop_piece(2, 1)
        self.__srv.drop_piece(2, 1)
        self.__srv.drop_piece(3, 1)
        self.assertTrue(self.__srv.winning_move(1))
        self.assertFalse(self.__srv.winning_move(2))


