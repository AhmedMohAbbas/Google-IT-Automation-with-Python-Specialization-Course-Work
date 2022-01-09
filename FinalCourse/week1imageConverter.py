#!/usr/bin/env python3

import os
from PIL import Image
from multiprocessing import Pool

srcdir ="/home/<user name>/images/" # use the correct paths of course :)
targetdir = "/opt/icons/"

if not os.path.exists(targetdir):
    os.mkdir(targetdir)

def Converter(filename):
    if not filename.endswith("48dp"):return None # there were more 7000 pictures, Had to put some check to protect against rogue files
    img = Image.open(srcdir+filename)
    img.rotate(270).resize((128,128)).convert('RGB').save(targetdir+filename, "jpeg")
    # Had to convert to RGB in order to be able to save as jpeg

imgFiles = os.listdir(srcdir)
Po = Pool(len(imgFiles))
Po.map(Converter, imgFiles)