import pygame
import variables as v
import board

class App:
    
    def __init__(self):
        self.running = False
        self.surface_full = None
        self.board = board.Board(30, (0,0))
    
    def do_init(self):
        pygame.init()
        self.surface_full = pygame.display.set_mode(v.window_size, pygame.HWSURFACE)
        self.running = True
    
    def do_clean_up(self):
        pygame.quit()
    
    def react_to_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        if event.type == pygame.MOUSEMOTION:
            pass
        
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            
    def do_render(self):
        
        self.board.draw_background(self.surface_full)
    
    
    
    
    
    def do_execute(self):
        
        if not self.running:
            self.do_init()
        
        while self.running:
            for event in pygame.event.get():
                self.react_to_event(event)
                
                self.do_render()
            
            
            pygame.display.flip()
        
        self.do_clean_up()
    







if __name__ == "__main__":
    
    app = App()
    app.do_execute()