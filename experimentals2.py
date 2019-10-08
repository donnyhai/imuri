#import PIL, pygame
#pygame.init()
#
#window_size = (400,300)
#surf = pygame.Surface(window_size)
#filename = "img/background1.png"
#
#img = PIL.Image.open(filename)
#img = img.resize((400,300), PIL.Image.ANTIALIAS)
#img.save(filename)
#
#print(img.size)

import pygame, sys
pygame.init()
pygame.display.init()

window_size = (400, 300)

surface = pygame.display.set_mode(window_size,0,32)

img = pygame.image.load("img/background.png")
img = pygame.transform.smoothscale(img, window_size)
surface.blit(img, (0,0))
#actions

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    pygame.display.update()