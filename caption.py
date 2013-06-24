#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageFilter

def write_on_image(filename, top, bottom):
    background = Image.open("resources/" + filename)
    height = background.size[1]
    write_at_offset(top, 5, background) 
    write_at_offset(bottom, height-70, background) 

    return background

def write_at_offset(text, from_top, image, shadow=True):
    drawer = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    font = ImageFont.truetype("resources/impact.ttf", 36)
    location_x = get_center_position(text, image)
    location_y = from_top
    location = (location_x, location_y)
    if shadow:
        image.paste(draw_shadow(text), (location_x-5, location_y-5), mask=draw_shadow(text))
    drawer.text(location, text, "white", font=font)


def get_center_position(text, image):
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype("resources/impact.ttf", 36)
    from_left = int((image.size[0]/2) - (drawer.textsize(text, font)[0]/2))

    return from_left

def draw_shadow(text):
    dummy = Image.new("RGBA", (100,100), (0,0,0,0))
    dummy_draw = ImageDraw.Draw(dummy)
    font = ImageFont.truetype("resources/impact.ttf", 36)
    width, height = dummy_draw.textsize(text,font)

    canvas = Image.new("RGBA", (width+10, height+10))
    draw = ImageDraw.Draw(canvas)
    draw.text((5,5), text, "black", font=font)
    blured = canvas.filter(ImageFilter.GaussianBlur(5))
    return blured

