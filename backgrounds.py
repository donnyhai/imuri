import random
import pygame
import colors as c



############### functions to create backgrounds #################

def randomly_mixed_colors(surface_size, colors):
    color0 = colors[0]
    color1 = colors[1]
    color2 = colors[2]
    color3 = colors[3]
    s = pygame.Surface(surface_size)
    for i in range(s.get_width()):
        for j in range(s.get_height()):
            color = random.choice([color1, color0, color2, color0, color0, color3])
            s.set_at((i,j), color)
    return s

def standard_color(surface_size, color):
    s = pygame.Surface(surface_size)
    s.fill(color)
    return s

#################################################################




new_image_file = "img/background3.png"
pygame.image.save(randomly_mixed_colors((5000,5000), [c.background_color1, c.background_color2, c.background_color3, c.background_color4]), new_image_file)