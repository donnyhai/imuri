import random
import pygame
import colors as c
import numpy as np



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

def overlapping_circles(surface_size, colors):
    s = pygame.Surface(surface_size)
    l = len(colors)
    alpha = int(1/(l+1) * 255)
    for i in range(l):
        color = colors[i]
        color = (color[0], color[1], color[2], alpha)
        pygame.draw.circle(s, color, (int(1/2 * surface_size[0]), int(1/2 * surface_size[1])), int(3/8 * (1 - np.power(1/3,l-i)) * surface_size[0]))
        alpha += int(1/(1+l) * 255)
    return s

#################################################################



#adapt following variables to create a image file which you are wanting
new_image_file = "img/point.png"
pygame.image.save(overlapping_circles((200,200), [c.point_color1, c.point_color2, c.point_color3, c.point_color4]), new_image_file)
#pygame.image.save(randomly_mixed_colors((5000,5000), [c.background_color1, c.background_color2, c.background_color3, c.background_color4]), new_image_file)