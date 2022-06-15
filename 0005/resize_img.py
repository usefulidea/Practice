import os
from PIL import Image

path = "/Users/wangyu/Desktop/image"

for i in os.listdir(path):
    img = Image.open(os.path.join(path, i))
    width, height = img.size
    out = img
    if width > 500:
        width = 500
        out = img.resize((width, height), Image.ANTIALIAS)
    if height > 500:
        height = 500
        out = img.resize((width, height), Image.ANTIALIAS)
    out.save(i)
