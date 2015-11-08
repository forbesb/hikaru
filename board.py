import player


class Board:
    def __init__(self, size, black, white):
        assert(isinstance(black, player.Player))
        assert(isinstance(white, player.Player))
            #I hear good things about assert.
        self.size = size
        self.black = black
        self.white = white
        self.turn = white
        self.board = [['.' for x in range(size)] for x in range(size)]
        self.printBoard()
        self.identifiers = {black: 'B', white: 'W'}

    def valid(self, position, player):
        x, y = position
        if player != self.turn or self.board[y][x] != '.':
            return False
        return True

    def _switchTurn(self):
        self.turn = self.white if self.turn == self.black else self.black

    def _placeStone(self, position, player):
        x, y = position
        self.board[y][x] = self.identifiers[player]
        self._switchTurn()

    def printBoard(self):
        for line in self.board:
            print((line))

bl = player.Player('x', "Black")
wh = player.Player('y', "White")
b = Board(9, bl, wh)
print((b.valid((3, 7), bl)))
b._placeStone((3, 7), bl)
print((b.valid((3, 7), wh)))
print((b.valid((3, 7), bl)))
b.printBoard()