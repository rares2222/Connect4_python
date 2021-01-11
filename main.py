from board.repo import Board
from console.ui import UI
from play.srv import Service

if __name__ == '__main__':
    repo = Board()
    srv = Service(repo)
    cons = UI(srv)
    cons.run()
