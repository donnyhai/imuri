import PIL

def resize_image(file):
    img = PIL.Image.open(file)
    img = img.resize((800, 600), PIL.Image.ANTIALIAS)
#    img = img.resize((800, 600))
    img.save("img_resized/" + file)

resize_image("img/background.png")