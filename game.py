import board
import tower
import wall
import point
import pygame
import player as pl
import interactor


class Game:
    
    def __init__(self, window_size):
        
        self.window_size = window_size
        self.board = board.Board(24, window_size)
        
        self.turn = ("white", 1)
        
    def set_surface(self, surface):
        self.surface_full = surface
        
        



class HvsH_Game(Game):
    
     def __init(self, window_size):
         super().__init__(window_size)
         
         self.players = {"white": pl.Human_Player("white"), "red": pl.Human_Player("red")}
         self.interactor = interactor.Interactor(self.players)
         
class HvsC_Game(Game):
    def __init(self, window_size):
         super().__init__(window_size)
         
         self.players = {"white": pl.Human_Player("white"), "red": pl.Computer_Player("red")}
         self.interactor = interactor.Interactor(self.players)