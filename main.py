from typing import Tuple
from PIL import Image, ImageFilter
from statistics import mean

#TODO: package and argparse it!
#TODO: Offer sample colors (pastel palette?)
#TODO: GUI it?

input = "./sample_images/a.png"
*_, filename = input.split("/")
out = f"./sample_images/bg_{filename}"
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


def prettify(input, output, bgcolor="#ffffff", nobg=False, border=None, blur=None) -> None:
    """Creates and saves a new image with a specified background color and drop shadow

    Args:
        input (str): Path to image file
        output (str): Path to image file (please specify file type)
        bgcolor (str, optional): Background color as hexcode. Defaults to "#ffffff" (white).
        nobg (bool, optional): "True" will set the background to transparent, regardless of the bgcolor.
        border (int, optional): Border size in pixels. Defaults to roughly 10 % of the height.
        blur (int, optional): Amount of blur to apply. Defaults to computing a "pleasing" value considering image size (not yet implemented).
    """
    im = Image.open(input)
    w, h = im.size

    if border is None:
        border = int(h*0.1)

    if nobg is True:
        # If the blur amount is too high, then the border size might not be enough to make the edges of the blurry
        # black background look "smooth" so it is limited to 20 until I come up with a better solution.
        if blur > 20:
            blur = 20
        background = Image.new(mode = "RGBA", size=(w+border*2, h+border*2), color=(0,0,0,0))
        background.paste((0,0,0), box=(border, border, w+border, h+border))
        blur_layer = background.filter(ImageFilter.GaussianBlur(radius=blur))
        blur_layer.paste(im, box=(border, border))
        blur_layer.save(output, quality=100)
    else:
        background = Image.new(mode = "RGBA", size=(w+border*2, h+border*2), color=bgcolor)
        background.paste(0, box=(border, border, w+border, h+border))
        #TODO: Set blur amount depending on image size
        blur_layer = background.filter(ImageFilter.GaussianBlur(radius=blur))
        blur_layer.paste(im, box=(border, border))
        blur_layer.save(output, quality=100)

#prettify(input, out, "#fcf4dd", 100, 20)
prettify(input, out, (255,255,255,0), nobg=True, blur = 200)
