import point

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[point.Point((i,j)) for i in range(self.size)] for j in range(self.size)]
        self.lines = self.set_lines()
    
    def get_neighbour_points(self, coord):
        pass
    
    def set_lines(self):
        pass