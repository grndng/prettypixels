from PIL import Image, ImageFilter
from statistics import mean
import argparse

#TODO: avg_rgb for more than 4 channels
#TODO: Offer sample colors (pastel palette?)
#TODO: Offer to process entire folders with same parameters
#TODO: GUI it?

parser = argparse.ArgumentParser(description="Prettify your images by adding a smooth drop shadow and a custom background!")
parser.add_argument("input", type=str, help="Path to input image.")
parser.add_argument("output", type=str, help="Path for output image.")
parser.add_argument("-b", "--blur", type=int, help="Blur amount. Depending on the image size, choose a higher or lower value.")
parser.add_argument("-c", "--bgcolor", type=str, help="Background color as hexcode. Defaults to a transparent background (as RGBA *.png).")
parser.add_argument("-s", "--bordersize", type=int, help="Border size in pixels. Defaults to roughly 10 percent of the height.")
args = parser.parse_args()


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


def prettify(input, output, bgcolor=None, border=None, blur=5) -> None:
    """Creates and saves a new image with a specified background color and drop shadow

    Args:
        input (str): Path to image file
        output (str): Path to image file (please specify file type)
        bgcolor (str, optional): Background color as hexcode. Defaults to transparent background.
        border (int, optional): Border size in pixels. Defaults to roughly 10 % of the height.
        blur (int, optional): Amount of blur to apply. Defaults to computing a "pleasing" value considering image size (not yet implemented).
    """
    im = Image.open(input)
    w, h = im.size

    if border is None:
        border = int(h*0.1)

    if bgcolor is None:
        # If the blur amount is too high, then the border size might not be enough to make the edges of the blurry
        # black background look "smooth" so it is limited to 20 until I come up with a better solution.
        if blur is not None and blur > 20:
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

if __name__ == "__main__":
    prettify(args.input, args.output, args.bgcolor, args.bordersize, args.blur)