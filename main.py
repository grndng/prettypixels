from PIL import Image, ImageFilter

#TODO: Proper docstrings
#TODO: package and argparse it!
#TODO: Offer sample colors (pastel palette?)
#TODO: GUI it?

input = "./sample_images/a.png"
*_, filename = input.split("/")
out = f"./sample_images/bg_{filename}"
color = "#c3c3c3"

def prettify(input, output, bgcolor="#c3c3c3", bordersize=100, bluramount=10):
    im = Image.open(input)

    w, h = im.size
    background = Image.new(mode = "RGB", size=(w+bordersize*2, h+bordersize*2), color=bgcolor)

    background.paste(0, box=(bordersize, bordersize, w+bordersize, h+bordersize))
    blur = background.filter(ImageFilter.GaussianBlur(radius=bluramount))
    blur.paste(im, box=(bordersize, bordersize))
    blur.save(output)
        
prettify(input, out, "#c3c3c3", 100, 2)