from PIL import Image, ImageDraw, ImageFont


def add_num(img):  # 构建函数
    draw = ImageDraw.Draw(img)  # 对图像进行绘制
    myfont = ImageFont.truetype("/Users/wangyu/Library/Fonts/RobotoMono-Medium.ttf", size=90)  # 字体文件，字体大小
    fillcolor = "#ff0000"  # 字体颜色
    width, height = img.size  # 获取图像宽， 高
    draw.text((width - 90, 0), '99', font=myfont, fill=fillcolor)  # 打印数字，控制位置以及字体颜色
    img.save("/Users/wangyu/Desktop/result.jpg", 'jpeg')  # 另存图片

    return 0


if __name__ == '__main__':
    image = Image.open('/Users/wangyu/Desktop/image.jpg')  # 图片路径
    add_num(image)  # 调用函数