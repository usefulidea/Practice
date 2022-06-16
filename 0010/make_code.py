from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

data_base = string.ascii_letters + string.digits * 5


def ran_num():
    return random.choice(data_base)


def ran_color_1():
    return random.randint(150, 225), random.randint(150, 225), random.randint(150, 225)


def ran_color_2():
    return random.randint(65, 200), random.randint(65, 200), random.randint(65, 200)


def make_code():
    width = 260
    height = 120
    im = Image.new('RGB', (width, height), color=ran_color_1())

    font = ImageFont.truetype('RobotoMono-Medium.ttf', 50)

    draw = ImageDraw.Draw(im)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=ran_color_2())
    for i in range(4):
        draw.text((60 * i + 10, random.randint(25, 35)), ran_num(), fill=ran_color_1(), font=font)
    im = im.filter(ImageFilter.BLUR)
    im.show()


if __name__ == '__main__':
    make_code()
