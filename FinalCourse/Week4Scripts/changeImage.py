#!/usr/bin/env python3

import os
from PIL import Image
from multiprocessing import Pool

srcdir ="/home/student-01-3284f0cbd11a/supplier-data/images/" # use the correct paths of course :)
targetdir = "/home/student-01-3284f0cbd11a/supplier-data/images/"

if not os.path.exists(targetdir):
    os.mkdir(targetdir)

def Converter(filename):
    if not filename.endswith(".tiff"):return None
    img = Image.open(srcdir+filename)
    img.resize((600,400)).convert('RGB').save(targetdir+filename[:-5]+".jpeg", "jpeg")
    # Had to convert to RGB in order to be able to save as jpeg

imgFiles = os.listdir(srcdir)
Po = Pool(len(imgFiles))
Po.map(Converter, imgFiles)
