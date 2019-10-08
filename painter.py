#painter


class Painter:
    
    def __init__(self, game):
        self.game = game
    
    def draw_ingame_frame(self):
        self.game.surface_full.fill((0,0,0))
        self.game.surface_full.blit(self.game.board.background, (0,0))