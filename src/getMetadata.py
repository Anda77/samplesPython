from PIL import Image
from PIL.ExifTags import TAGS


def print_exif_data(exif_data):
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        content = exif_data.get(tag_id)
        print(f'{tag:25}: {content}')


with Image.open("C:\\PythonPrj\\resources\\WhatsApp Image 2023-03-14 at 19.04.40.jpeg") as im:
    exif = im.getexif()

    print_exif_data(exif)
    print()
    print_exif_data(exif.get_ifd(0x8769))
