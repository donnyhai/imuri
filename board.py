import point
import pygame, os

background = os.path.join("pictures", "background.png")

class Board:
    def __init__(self, board_size, pixel_size):
        self.size = board_size
        self.board = self.set_init_board()
        self.lines = self.set_lines()
        self.rect = pygame.Rect((0,0), pixel_size)
        self.background = background
    
    def is_inside(self, coord):
        return 0 <= coord[0] < self.size and 0 <= coord[1] < self.size
    
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        return {(i+m, j+n) for m in {-2,-1,1,2} for n in {-2,-1,1,2} if self.is_inside((i+m,j+n)) and n != m and m+n != 0}
        
    
    def set_lines(self):
        pass
    
    def set_init_board(self):
        board = {}
        for i in range(self.size):
            for j in range(self.size):
                board[(i,j)] = point.Point((i,j))
                #######################################set rect
    
    def draw_background(self, surface_full):
        surface_full.blit(self.background, (0,0))
        
    

