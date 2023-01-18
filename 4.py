from PIL import Image
import os

image = Image.open("img.png")

quality = 1


image.save("compressed_img.png",  optimize=True ,quality=quality)

# check the original file size
original_size = os.path.getsize("img.png")

# check the compressed file size
compressed_size = os.path.getsize("compressed_img.png")

print(f"Original image size: {original_size/1024} MB")
print(f"Compressed image size: {compressed_size/1024} MB")