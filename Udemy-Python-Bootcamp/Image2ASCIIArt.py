from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)

def main():
    path = input("Enter image path: ")
    image = Image.open(path)

    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)

    pixel_count = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:i+100] for i in range(0, pixel_count, 100))

    print(ascii_img)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

main()
