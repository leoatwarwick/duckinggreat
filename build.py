from os.path import getmtime
from PIL import Image
import chevron
import os

os.chdir("./images")

files = reversed(
    sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime))

images = []

for item in files:
    if os.path.isfile(item) and (item.endswith((".png", ".jpg", ".jpeg"))):
        path = f"./images/{item}"
        images.append(path)

        duck_photo = Image.open(item)

        base_width = 768
        width_percentage = base_width / float(duck_photo.size[0])
        height = int(float(duck_photo.size[1]) * float(width_percentage))

        duck_photo = duck_photo.resize((base_width, height), Image.LANCZOS)

        duck_photo.save(item, optimize=True, quality=75)

with open("../index.mustache", "r") as template:
    index_html = chevron.render(template, {
        "images": images
    })

    with open("../index.html", "w") as index:
        index.write(index_html)
