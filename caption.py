#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont

def write_on_image(filename, top, bottom):
    background = Image.open("resources/" + filename)
    drawer = ImageDraw.Draw(background)
    width = background.size[0]
    height = background.size[1]

    font = ImageFont.truetype("resources/impact.ttf", 36)

    top_location = (get_center_position(top, background) , 5)
    bottom_location = (get_center_position(bottom, background), height-70)


    drawer.text(top_location, top, "white", font=font)
    drawer.text(bottom_location, bottom, "white", font=font)

    return background

def get_center_position(text,image):
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype("resources/impact.ttf", 36)
    from_left = int((image.size[0]/2) - (drawer.textsize(text, font)[0]/2))

    return from_left

