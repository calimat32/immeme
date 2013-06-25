#!/usr/bin/python

import imgbackend.caption as caption
import sys
from PIL import ImageFilter

caption.write_on_image("wonka.jpg", "Writing a program to make memes?", "I bet nobody has attempted such a massive feat before").show()
#caption.draw_shadow("Longer text").save("test.png", "PNG")

