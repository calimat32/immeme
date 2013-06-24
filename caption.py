#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageFilter

def write_on_image(filename, top, bottom):
    background = Image.open("resources/" + filename)
    drawer = ImageDraw.Draw(background)
    width = background.size[0]
    height = background.size[1]

    font = ImageFont.truetype("resources/impact.ttf", 36)

    top_location = (get_center_position(top, background), 5)
    bottom_location = (get_center_position(bottom, background), height-70)

    background.paste(draw_shadow(top), (top_location[0]-5, top_location[1]-5), mask=draw_shadow(top))
    background.paste(draw_shadow(bottom), (bottom_location[0]-5, bottom_location[1]-5), mask=draw_shadow(bottom))

    drawer.text(top_location, top, "white", font=font)
    drawer.text(bottom_location, bottom, "white", font=font)

    return background

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

