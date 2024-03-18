#! /usr/bin/env python3

import os
from PIL import Image
#  Replace x in save dir with directory where you want new files to be saved
savedir = "/home/student-03-ef3e8b274a0f/supplier-data/images"
# Replace y with directory of files
os.chdir('/home/student-03-ef3e8b274a0f/supplier-data/images')
filedir = os.listdir()

for infile in filedir:
    if os.path.isdir(infile):
        continue
    f, e = os.path.splitext(infile)
    #  converts to .jpg, replace for other files
    outfile = os.path.join(savedir, f + ".jpeg")
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                if im.mode != 'RGB':
                    im = im.convert('RGB')
                rgb_im = im.convert('RGB') 
                resize_img = rgb_im.resize((600,400))
                #  resizes images to specified paramets
                resize_img.save(outfile)
        except OSError as e:
            print(f"{e}")