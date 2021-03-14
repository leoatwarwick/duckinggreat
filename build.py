import chevron
import os

images = []

for item in os.listdir("./img"):
    if os.path.isfile(f'./img/{item}') and (item.endswith(".png") or item.endswith(".jpg")):
        images.append(item)

with open("./index.mustache", "r") as template:
    index_html = chevron.render(template, {
        "images": images
    })

    with open("./index.html", "w") as index:
        index.write(index_html)
