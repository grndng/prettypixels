import argparse
from PIL import Image, ImageFilter

#TODO: Proper docstrings
#TODO: For shadows I could copy the image size, create a black image, blur it iteratively and paste it inbetween bg and fg

input = "./sample_images/a.png"
color = "#c3c3c3"

def create_background(input, bgcolor="#c3c3c3"):
    try:
        foreground = Image.open(input)
    except FileNotFoundError as e:
        print(f'Please check your path. "{input}" does not seem to be valid.')
    else:
        w, h = foreground.size
        bg = ((int(w*1.5), int(h*1.5)))
        background = Image.new(mode = "RGB", size=bg, color=bgcolor)
        #background.save("background.png")
        
        # enlightenment: the background is a solid color so I can
        # simply go and blur the entire thing with a black box in the
        # middle, no?
        
        # Okay, this does something but not as expected...
        background.paste(0, box=(int(w*0.25), int(h*0.25), w-int(h*0.25), h-int(h*0.25)))

        background.save("bg_blackbox.png")

create_background(input)
#create_background(input, "#c3c3c3")

"""
def blackimg(input):
    im = Image.open(input)
    w, h = im.size
    black = Image.new(mode="RGBA", size=(w,h), color=0)
    black.save("black.png")
    return black
"""

def create_blur(input, amount):
    im = Image.open(input)
    w,h = im.size
    blackimg = Image.new(mode=im.mode, size=(w,h), color=0)
    blur = blackimg.filter(ImageFilter.GaussianBlur(radius=amount))
    blur.save("blur.png")
    return blur

#create_blur(input, 5)