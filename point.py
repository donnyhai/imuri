

class Point:
    def __init__(self, coordinate):
        self.has_tower = False
        self.coordinate = coordinate
        
    def put_tower(self, tower):
        self.tower = tower
        self.has_tower = True