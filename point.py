import pygame, os

point_images = {"white": os.path.join("img", "point_white.png"),
                "red": os.path.join("img", "point_red.png"),
                "black": os.path.join("img", "point_black.png"),
                "neutral": os.path.join("img", "point_neutral.png")}

class Point:
    def __init__(self, board_pos):
        self.has_tower = False
        self.board_pos = board_pos
        
    def put_tower(self, tower):
        self.tower = tower
        self.has_tower = True
        
    def set_surf(self, subsurface):
        s = subsurface
        s.set_colorkey((0,0,0))
        self.surf = s
    
    def set_blitted_surf(self, subsurface, img):
        s = subsurface
        s.set_colorkey((0,0,0))
        img = pygame.transform.smoothscale(img, self.surf.get_size())
        s.blit(img, (0,0))
        self.blitted_surf = s
    
    #types like white, red, black, neutral (corner points are black, middle points neutral, edge points white resp. red)
    def set_point_type(self, point_type):
        self.point_type = point_type
        
    def set_standard_image(self):
        if self.point_type != None:
            if self.point_type == "white":
                img = pygame.image.load(point_images["white"])
            elif self.point_type == "red":
                img = pygame.image.load(point_images["red"])
            elif self.point_type == "neutral":
                img = pygame.image.load(point_images["neutral"])
            elif self.point_type == "black":
                img = pygame.image.load(point_images["black"])
            self.standard_img = img


















