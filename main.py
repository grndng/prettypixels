import argparse
from inspect import Attribute
from PIL import Image

#TODO: Proper docstrings
#TODO: How to generate new image? -> Image.new()
#TODO: How to put image onto another image? -> Image.paste()
#TODO: How to create a good looking shadow?


def load_image(imgpath):
    try:
        return Image.open(imgpath)
    except FileNotFoundError as e:
        print(f'Please check your path. "{imgpath}" does not seem to be valid.')

def generate_new_image(img, hexcode):
    w, h = img.size[0], img.size[1]
    bg = ((int(w*1.5), int(h*1.5)))
    background = Image.new(mode = "RGB", size=bg, color=hexcode)
    return background


# Works but fucking clunky to call
generate_new_image(load_image("a.png"), "#000000").save("b.png")