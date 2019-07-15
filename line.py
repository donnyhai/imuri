

class Line:
    def __init__(self, point1, point2):
        self.points = {point1, point2}
        self.has_wall = False
        
        