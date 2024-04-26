import os
from wand.image import Image
from wand.color import Color

project_root = os.getcwd()


def add_background(image_path):
    with Image(filename=image_path) as image:
        original_width, original_height = image.width, image.height

        # change here if you want to change the resolution
        new_width, new_height = 3840, 2160

        # change here if you want to change the scaling
        logo_width, logo_height = original_width, original_height
        image.resize(logo_width, logo_height)

        # change here if you want to change the background color
        background_color = Color("#282a36")

        new_image = Image(width=new_width, height=new_height, background=background_color)
        new_image.composite(image, left=(new_width - logo_width) // 2, top=(new_height - logo_height) // 2)
        new_image.save(filename=image_path)

        print(f"file {image_path} has been processed")


def main():
    for filename in os.listdir(project_root):
        if filename.startswith(".") or filename == "docs":
            continue

        filepath = os.path.join(project_root, filename)

        if os.path.isdir(filepath):
            for image_filename in os.listdir(filepath):
                image_path = os.path.join(filepath, image_filename)
                if image_filename.endswith(".png"):
                    add_background(image_path)


if __name__ == "__main__":
    main()
