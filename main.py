from typing import Tuple
from PIL import Image, ImageFilter
from statistics import mean

#TODO: Proper docstrings
#TODO: package and argparse it!
#TODO: Offer sample colors (pastel palette?)
#TODO: Compute background color by taking mean rgb val of image
#TODO: GUI it?

input = "./sample_images/a.png"
*_, filename = input.split("/")
out = f"./sample_images/bg_{filename}"
color = "#c3c3c3"

def compute_average_rgb_val(input) -> Tuple:
    avg_color_rgb = tuple([int(mean(input.getdata(band))) for band in range(len(input.mode))])
    R,G,B = avg_color_rgb
    avg_color_hex = f"#{R:02x}{G:02x}{B:02x}"
    return avg_color_hex

print(compute_average_rgb_val(Image.open(input)))

def prettify(input, output, bgcolor="#c3c3c3", bordersize=100, bluramount=10) -> None:
    im = Image.open(input)

    w, h = im.size

    background = Image.new(mode = "RGB", size=(w+bordersize*2, h+bordersize*2), color=bgcolor)
    background.paste(0, box=(bordersize, bordersize, w+bordersize, h+bordersize))
    blur = background.filter(ImageFilter.GaussianBlur(radius=bluramount))
    blur.paste(im, box=(bordersize, bordersize))
    blur.save(output)
    return None
        
prettify(input, out, f"{compute_average_rgb_val(Image.open(input))}", 100, 2)
