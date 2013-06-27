#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import textwrap
import StringIO
import base64

def write_on_image64(filename, top, bottom):
    image = write_on_image(filename, top, bottom)
    output = StringIO.StringIO()
    image.save(output, "PNG")
    content = output.getvalue()
    output.close()
    return content.encode("base64")


def write_on_image(filename, top, bottom):
    background = Image.open(filename)
    width = background.size[0]
    height = background.size[1]
    max_width = width 
    max_chars = int(max_width/18) # 25 is the average width for the Impact font at 36pt
    text_height = 44 # height for 36pt Impact
    # Write top

    if len(top) > max_chars:
        i = 0 # Line counter used in loop
        for line in textwrap.wrap(top, max_chars):
            # Draw 5 pixels from the top
            # Also leave a 5 pixel separation between lines
            write_at_offset(line, 5 + text_height*i, background)
            i += 1
    else:
        write_at_offset(top, 5, background)

    # Write bottom
    
    if len(bottom) > max_chars:
        # We need to know all text height before we start writing
        lines = textwrap.wrap(bottom, max_chars)
        from_bottom = (text_height+5)*len(lines) # text_height + 5 pixels for line separation
        from_top = height - from_bottom
        i = 0 # Line counter used in loop
        for line in lines:
            write_at_offset(line, from_top + text_height*i, background)
            i += 1
    else:
        write_at_offset(bottom, height - (text_height + 10), background)


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
    blurred = canvas.filter(ImageFilter.GaussianBlur(5))
    return blurred

def get_text_size(text, font_size):
    dummy = Image.new("RGBA", (100,100), (0,0,0,0))
    dummy_draw = ImageDraw.Draw(dummy)
    font = ImageFont.truetype("resources/impact.ttf", 36)
    width, height = dummy_draw.textsize(text,font)
    return (width, height)
