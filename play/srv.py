class Service:

    def __init__(self, repo):
        self.__repo = repo

    def board_game(self):
        return self.__repo.get_board()

    def is_valid_location(self, col):
        # verify if in selected col exist an empty row
        B = self.__repo.get_board()
        if B[5][col] == 0:
            return True
        else:
            raise ValueError ("The chosen column is full,chose another one!!!!!!")

    def get_next_open_row(self, col):
        # find the next empty space in a given column and return the row where it is
        x = self.__repo.get_board()
        for r in range(6):
            if x[r][col] == 0:
                return r


    def drop_piece(self, col, value):
        # add a new piece (1 or 2(the value)) on a given column(col) in the last free row
        # if a free row doesn't exist raise error
        try:
            self.is_valid_location(col)
            row=self.get_next_open_row(col)
            self.__repo.drp(col, row, value)
        except ValueError :
            raise ValueError("The chosen column is full,chose another one!!!!!!")



    def winning_move(self,value):
        COLUMN_COUNT=7
        ROW_COUNT=6
        board=self.__repo.get_board()

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == value and board[r][c+1] == value and board[r][c+2] == value and board[r][c+3] == value:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == value and board[r+1][c] == value and board[r+2][c] == value and board[r+3][c] == value:
                    return True
        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == value and board[r+1][c+1] == value and board[r+2][c+2] == value and board[r+3][c+3] == value:
                    return True
        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == value and board[r-1][c+1] == value and board[r-2][c+2] == value and board[r-3][c+3] == value:
                    return True
