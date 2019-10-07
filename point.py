import pygame

class Point:
    def __init__(self, board_pos):
        self.has_tower = False
        self.board_pos = board_pos
        
    def put_tower(self, tower):
        self.tower = tower
        self.has_tower = True
        
    def set_rect(self, pixel_pos, pixel_size):
        return pygame.Rect(pixel_pos, pixel_size)