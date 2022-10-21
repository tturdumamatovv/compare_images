from PIL import Image, ImageDraw

IMAGE_FOLDER = 'images/'
IMAGE_1 = IMAGE_FOLDER + 'im1.png'
IMAGE_2 = IMAGE_FOLDER + 'im2.png'

def region_analyze(image, x, y, width, height):
    region_status = 0
    for x_cord in range(x, x + width):
        for y_cord in range(y, y + height):
            try:
                pixel = image.getpixel((x_cord, y_cord))
                region_status += sum(pixel)
            except:
                return None
    return region_status


def analyze(image_ref, image_target, col=100, row=100):
    reference = Image.open(image_ref)
    target = Image.open(image_target)

    width, height = reference.size
    block_width = width // col
    block_height = height // row

    for x in range(0, width, block_width + 1):
        for y in range(0, height, block_height + 1):
            region_ref = region_analyze(reference, x, y, block_width, block_height)
            region_target = region_analyze(target, x, y, block_width, block_height)
            if region_ref != region_target:
                draw = ImageDraw.Draw(reference)
                draw.rectangle((x, y, x + block_width, y + block_height), outline='red')

    reference.save('diff.png')

analyze(IMAGE_1, IMAGE_2)


