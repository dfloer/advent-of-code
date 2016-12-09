from PIL import Image
import tesserocr

def day8_split():
    with open('day8.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day8(screen_width=50, screen_height=6):
    data = day8_split()
    pixels = [[0 for _ in range(screen_width)] for _ in range(screen_height)]
    for line in data:
        split = line.split()
        op = split[0]
        if op == "rect":
            w, h = split[1].split('x')
            for i in range(int(w)):
                for j in range(int(h)):
                    pixels[j][i] = 1
        elif op == "rotate":
            direction = split[1]
            idx = int(split[2].split('=')[1])
            amount = int(split[4])
            if direction == "row":
                row = pixels[idx]
                amount *= -1
                new_row = row[amount:] + row[:amount]
                pixels[idx] = new_row
            elif direction == "column":
                col = [x[idx] for x in pixels]
                amount *= -1
                new_col = col[amount:] + col[:amount]
                for i, x in enumerate(pixels):
                    x[idx] = new_col[i]
    pprint_lists(pixels)
    test = ocr(pixels)
    print(test)
    return sum(flatten(pixels))


def flatten(l):
    return[val for sublist in l for val in sublist]


def pprint_lists(l):
    for x in l:
        for y in x:
            if y == 1:
                c = '#'
            else:
                c = '.'
            print(c, "", end='')
        print()

def ocr(pixels):
    # convert the array to a bw image.
    height = len(pixels)
    width = len(pixels[0])
    img = Image.new('1', (width + 2, height + 2), 0)
    for i in range(width):
        for j in range(height):
            img.putpixel((i, j), 0)
    for i in range(width):
        for j in range(height):
            img.putpixel((i + 1, j + 1), pixels[j][i])
    img = img.resize(((width + 2) * 100, (height + 2) * 100), Image.ANTIALIAS)
    #img.save("day8.bmp", format="bmp")
    try:
        out = tesserocr.image_to_text(img)
    except RuntimeError:
        out = None
