import sys
import os
from PIL import Image
image_folder=sys.argv[1]
output_folder=sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for fileneame in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{fileneame}')
    clean_name=os.path.splitext(fileneame)[0]
    img.save(f'{output_folder}{clean_name}.png','png')


