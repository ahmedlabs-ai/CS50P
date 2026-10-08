import sys

import os

from PIL import Image
from PIL import ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].lower().endswith((".jpeg", ".jpg", ".png")):
    sys.exit("Invalid input")

elif not sys.argv[2].lower().endswith((".jpeg", ".jpg", ".png")):
    sys.exit("Invalid output")


input_extension = os.path.splitext(sys.argv[1])[1]
output_extension = os.path.splitext(sys.argv[2])[1]

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")

fitted_image = ImageOps.fit(input_image, shirt.size)
fitted_image.paste(shirt, shirt)
fitted_image.save(sys.argv[2])
