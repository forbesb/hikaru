import threading
import player, board


class Game(threading.Thread):

    black = None
    white = None
    size = None

    def __init__(self):
        super(Game, self).__init__()
        self.daemon = True

    def _setBlack(self, player):
        self.black = player

    def _setWhite(self, player):
        self.white = player

    def _setSize(self, x):
        self.size = x

    def _createBoard(self):
        self.board = board.Board(self.size, self.black, self.white)

    def initialize(self, size, black, white):
        self._setBlack(black)
        self._setWhite(white)
        self._setSize(size)
        self._createBoard()

    def run(self):
        x = 0
        y = 0
        while self.board.victory() == -1:
            print((self.black.name + ", Where do you want to place a stone?: "))
            x, y = list(map(int, input().split()))
            print((x, y))


if __name__ == "__main__":
    ng = Game()
    ng.initialize(9, player.Player("Bob", "b"), player.Player("Alice", "w"))
    ng.start()
