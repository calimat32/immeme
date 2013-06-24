#!/usr/bin/python

import caption, sys
from PIL import ImageFilter

caption.write_on_image("wonka.jpg", "Writing a program to make memes?", "I bet nobody has done that before").show()

#caption.draw_shadow("Longer text").save("test.png", "PNG")
