from typing import Tuple
from PIL import Image, ImageFilter
from statistics import mean

#TODO: What happens if I don't enter any bordersize or blur amount? :(
#TODO: package and argparse it!
#TODO: Offer sample colors (pastel palette?)
#TODO: GUI it?

input = "./prettypixels/sample_images/guron.jpg"
*_, filename = input.split("/")
out = f"./prettypixels/sample_images/bg_{filename}"
color = "#c3c3c3"

def avg_rgb(input) -> str:
    """Helper function to compute the average RGB(*) value of a raster image
    considering the amount of image channels
    
    Args:
        input (str): Path to image file

    Returns:
        str: Hexcode including the pound
    """
    input = Image.open(input)
    avg_color_rgb = tuple([int(mean(input.getdata(band))) for band in range(len(input.mode))])
    R,G,B = avg_color_rgb
    avg_color_hex = f"#{R:02x}{G:02x}{B:02x}"
    return avg_color_hex


def prettify(input, output, bgcolor="#c3c3c3", bordersize=100, bluramount=None) -> None:
    """Creates and saves a new image with a specified background color and drop shadow

    Args:
        input (str): Path to image file
        output (str): Path to image file (please specify file type)
        bgcolor (str, optional): Background color as hexcode. Defaults to "#c3c3c3".
        bordersize (int, optional): Border size in pixels. Defaults to roughly 20 % of the original image.
        bluramount (int, optional): Amount of blur to apply. Defaults to computing a "good" value considering image size.
    """
    im = Image.open(input)

    w, h = im.size

    #TODO: Set bordersize depending on image size
    background = Image.new(mode = "RGB", size=(w+bordersize*2, h+bordersize*2), color=bgcolor)
    background.paste(0, box=(bordersize, bordersize, w+bordersize, h+bordersize))
    #TODO: Set blur amount depending on image size
    blur = background.filter(ImageFilter.GaussianBlur(radius=bluramount))
    blur.paste(im, box=(bordersize, bordersize))
    blur.save(output, quality=100)

prettify(input, out, "#fcf4dd", 400, 20)

