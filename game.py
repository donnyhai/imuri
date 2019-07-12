import player
import board

class Game:
    board_size = 24
    board = board.Board(board_size)
    
class HvsH_Game(Game):
    def __init__(self):
        pass
    
class HvsC_Game(Game):
    pass