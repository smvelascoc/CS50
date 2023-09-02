import sys
from PIL import Image
from PIL import ImageOps
import os

def main():
    # Arguments check
    root1, ext1 = os.path.splitext(sys.argv[1])
    root2, ext2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
        sys.exit("Invalid input")

    if not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
        sys.exit("Invalid output")

    if ext1 != ext2:
        sys.exit("Input and Output have different extentions")

    #Image procedure
    image = open_image(sys.argv[1])
    shirt = open_image("shirt.png")
    #print(f"Original image size = {image.size}")
    #print(f"Original shirt size = {shirt.size}")

    image = ImageOps.fit(image, shirt.size )
    #print(f"New image size = {image.size}")
    image.paste(shirt,shirt)
    #print(f"Image size after paste= {image.size}")
    image.save(sys.argv[2])

def open_image(name):
    try:
        image_return = Image.open(name)
        return image_return
    except FileNotFound:
        sys.exit(f"Could not read {name}")

if __name__ == "__main__":
    main()