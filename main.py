import argparse
from PIL import Image, ImageFilter

#TODO: Proper docstrings
#TODO: For shadows I could copy the image size, create a black image, blur it iteratively and paste it inbetween bg and fg

input = "./sample_images/a.png"
color = "#c3c3c3"

def create_background(input, bgcolor="#c3c3c3", bordersize=100):
    foreground = Image.open(input)

    w, h = foreground.size
    background = Image.new(mode = "RGB", size=(w+bordersize*2, h+bordersize*2), color=bgcolor)
            
    # Need to specify the entire region size with a 4-item box
    # first two elements determine upper left corner, last two
    # lower right corner of pasted box
    background.paste(0, box=(bordersize, bordersize, w+bordersize, h+bordersize))
    
    # "repotting" create_blur into this to have everything
    # at the same place and work with a single function
    
    blur = background.filter(ImageFilter.GaussianBlur(radius=5))
    blur.save("blur.png")
    blur.paste(foreground, box=(bordersize, bordersize))
    blur.save("blur_foreground.png")
        
create_background(input)
