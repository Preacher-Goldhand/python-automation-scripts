# Description:
# Simple file format converter

from PIL import Image                # Python Image Library
import glob                          # UNIX style paths

# Working in a working directory
print(glob.glob("*.png"))            # List files with .png format in the current directory

for file in glob.glob("*.jpg"):
    im = Image.open(file)
    rgb_im = im.convert('RGBA')      # PNG has alpha channel 
    rgb_im.save(file.replace("jpg", "png"), quality=95)
