import argparse
from PIL import Image

#TODO: Proper docstrings
#TODO: How to create a good looking shadow? nope...
#TODO: How to create a shadow anyway? -> ImageFilter

input = "a.png"
color = "#c3c3c3"

try:
    im = Image.open(input)
except FileNotFoundError as e:
    print(f'Please check your path. "{input}" does not seem to be valid.')


def generate_background(input, hexcode):
    im = Image.open(input)
    w, h = im.size[0], im.size[1]
    bg = ((int(w*1.5), int(h*1.5)))
    background = Image.new(mode = "RGB", size=bg, color=hexcode)
    background.paste(im, box=(int(w*0.25), int(h*0.25)))
    background.save("output.jpg")
    return background

generate_background(input, "#cecece")