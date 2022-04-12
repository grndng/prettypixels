from PIL import Image, ImageFilter

#TODO: Proper docstrings

input = "./sample_images/b.jpg"
color = "#c3c3c3"

def prettify(input, bgcolor="#c3c3c3", bordersize=100):
    foreground = Image.open(input)

    w, h = foreground.size
    background = Image.new(mode = "RGB", size=(w+bordersize*2, h+bordersize*2), color=bgcolor)
            
    background.paste(0, box=(bordersize, bordersize, w+bordersize, h+bordersize))
    
    blur = background.filter(ImageFilter.GaussianBlur(radius=5))
    blur.paste(foreground, box=(bordersize, bordersize))
    blur.save("blur_foreground.png")
        
prettify(input)
