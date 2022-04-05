import argparse
from PIL import Image, ImageFilter

#TODO: Proper docstrings
#TODO: How to create a good looking shadow? nope...
#TODO: How to create a shadow anyway? -> ImageFilter and blur

input = "a.png"
color = "#c3c3c3"

def shadows(input):
    pass

def prettify(input, hexcode):
    try:
        im = Image.open(input)
    except FileNotFoundError as e:
        print(f'Please check your path. "{input}" does not seem to be valid.')
    else:
        w, h = im.size
        bg = ((int(w*1.5), int(h*1.5)))
        background = Image.new(mode = "RGB", size=bg, color=hexcode)
        background.paste(im, box=(int(w*0.25), int(h*0.25)))
        background.save("output.jpg")
        return background

prettify(input, "#cecece")