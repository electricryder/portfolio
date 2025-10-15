import sys
from PIL import Image, ImageOps


def main():
    image_converter(valid_args())


def valid_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] not in [".jpg", ".jpeg", ".gif"]:
            sys.exit("Invalid input")

        if sys.argv[1][-4:] != sys.argv[2][-4:]:
            sys.exit("Input and output have different extensions")
        else:
            try:
                img = Image.open(sys.argv[1])
                img.close()
                return sys.argv[1]

            except FileNotFoundError:
                sys.exit(f"Input does not exist")


def image_converter(image_arg):
    with Image.open("shirt.png") as shirt_img:
        with Image.open(image_arg) as model_img:
            model_img = ImageOps.fit(model_img, shirt_img.size)
            model_img.paste(shirt_img, shirt_img)
        model_img.save(sys.argv[2])


if __name__ == "__main__":
    main()
