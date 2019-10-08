import pygame
import variables as v
import game
import painter

class App:
    
    def __init__(self):
        self.running = False
        self.game = game.HvsH_Game(v.window_size)
        self.painter = painter.Painter(self.game)
    
    def do_init(self):
        pygame.init()
        pygame.display.init()
        surface_full = pygame.display.set_mode(v.window_size)
        self.game.set_surface(surface_full) 
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
        self.painter.draw_ingame_frame()
    
    
    
    
    
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