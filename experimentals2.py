import os, pygame, base64

#img = os.path.join("img", "background.png")

with open("img/background.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

surf = pygame.image.fromstring(my_string, (5000,5000), "RGB")