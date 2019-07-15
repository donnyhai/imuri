import point

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[point.Point((i,j)) for i in range(self.size)] for j in range(self.size)]
        self.lines = self.set_lines()
    
    def is_inside(self, coord):
        return 0 <= coord[0] < self.size and 0 <= coord[1] < self.size
    
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        return {(i+m, j+n) for m in {-2,-1,1,2} for n in {-2,-1,1,2} if self.is_inside((i+m,j+n)) and n != m and m+n != 0}
        
    
    def set_lines(self):
        pass
    

b = Board(10)