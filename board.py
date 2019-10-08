import point
import pygame, os
import variables as v
background = os.path.join("img", "background.png")


class Board:
    def __init__(self, board_size, pixel_size):
        self.board_size = board_size
        self.pixel_size = pixel_size
        self.lines = self.set_lines()
        self.surf = self.init_surf()
        self.board = self.set_init_board()
    
    def is_inside(self, coord):
        return 0 <= coord[0] < self.size and 0 <= coord[1] < self.size
    
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        return {(i+m, j+n) for m in {-2,-1,1,2} for n in {-2,-1,1,2} if self.is_inside((i+m,j+n)) and n != m and m+n != 0}
    
    def init_surf(self):
        s = pygame.image.load(background)
        s = pygame.transform.smoothscale(s, self.pixel_size)
        return s
        
    
    def set_lines(self):
        pass
    
    def set_init_board(self):
        board = {}
        for i in range(self.board_size):
            for j in range(self.board_size):
                new_point = point.Point((i,j))
                ps_x = v.point_size[0]
                step_x = int(1/25 * (v.window_size[0] - 24 * ps_x))
                step_y = step_x
                pos_x = (i+1) * step_x + i * ps_x
                pos_y = (j+1) * step_y + j * ps_x
                new_point.set_surf(self.surf.subsurface(pygame.Rect((pos_x, pos_y), v.point_size)))
                new_point.set_point_type("neutral")
                new_point.set_standard_image()
                new_point.set_blitted_surf(self.surf.subsurface(pygame.Rect((pos_x, pos_y), v.point_size)), new_point.standard_img)
                
                board[(i,j)] = new_point
        return board
        
    
    

