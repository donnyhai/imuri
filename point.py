import pygame, os

point_images = {"white": os.path.join("img", "point_white.png"),
                "red": os.path.join("img", "point_red.png"),
                "black": os.path.join("img", "point_black.png"),
                "neutral": os.path.join("img", "point_neutral.png")}

class Point:
    def __init__(self, board_pos):
        self.has_tower = False
        self.board_pos = board_pos
        self.surf = None
        self.point_type = None
        
    def put_tower(self, tower):
        self.tower = tower
        self.has_tower = True
        
    def set_surf(self, subsurface):
        s = subsurface
        s.set_colorkey((0,0,0))
        return s
    
    #types like white, red, black, neutral (corner points are black, middle points neutral, edge points white resp. red)
    def set_point_type(self, point_type):
        self.point_type = point_type
        
    def set_standard_image(self):
        if self.point_type != None and self.rect != None:
            if self.type == "white":
                point_images["white"]
            elif self.type == "red":
                point_images["red"]
            elif self.type == "neutral":
                point_images["neutral"]
            elif self.type == "black":
                point_images["black"]