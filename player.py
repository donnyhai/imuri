import tower
import wall

class Player:
    def __init__(self, color):
        self.color = color
        self.towers = [tower.Tower(self.color)] * 100
        self.walls = [wall.Wall(self.color)] * 100
        
    def puts_tower(self, tower, board, coord):
        if not board.board[coord[0]][coord[1]].has_tower and self.color == tower.color:
            board.board[coord[0]][coord[1]].put_tower(tower)
            tower.is_on_board = True
            tower.coordinate = coord
            
            #put walls if possible
            neighbours = board.get_neighbours(coord)
            for neigh in neighbours:
                if board.board[neigh[0]][neigh[1]].has_tower:
                    pass
                    #
                    #
                    # needs lines coordination
                    #
                    #
                    #
                    #
                    #
                    #

                    
                    
class Human_Player(Player):
    pass

class Computer_Player(Player):
    pass