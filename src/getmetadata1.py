from PIL import Image
from PIL.ExifTags import TAGS

imagename = "C:\\PythonPrj\\resources\\WhatsApp Image 2023-03-14 at 19.04.40.jpeg"
image = Image.open(imagename)

exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    print(tag_id)
    data = exifdata.get(tag_id)
    # we decode bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f'{tag:25}: {data}')
    print()
