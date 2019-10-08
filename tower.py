import pygame

class Tower:
    
    def __init__(self, color, pixel_size):
        self.color = color
        self.is_on_board = False
        self.size = pixel_size
        
        self.rect = pygame.Rect((0,0), self.size)
        
    def set_board_coordinate(self, coord):   
        self.coordinate = coord
    
    def set_tower_type(self, tower_type):
        self.tower_type = tower_type
        
        
    
        