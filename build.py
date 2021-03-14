from os.path import getmtime
import chevron
import os

os.chdir("./img")

files = reversed(
    sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime))

images = []

for item in files:
    if os.path.isfile(item) and (item.endswith((".png", ".jpg", ".jpeg"))):
        images.append(f"./img/{item}")

with open("../index.mustache", "r") as template:
    index_html = chevron.render(template, {
        "images": images
    })

    with open("../index.html", "w") as index:
        index.write(index_html)
