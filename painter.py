#painter


class Painter:
    
    def __init__(self, game):
        self.game = game
    
    def draw_ingame_frame(self):
        self.game.surface_full.blit(self.game.board.surf, (0,0))
        for point in self.game.board.board.values():   
            self.game.surface_full.blit(point.blitted_surf, point.blitted_surf.get_offset())
        
    def draw_board(self):
        self.game.surface_full.blit(self.game.board.surf, (0,0))
        