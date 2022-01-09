#! /usr/bin/env python3

import requests
import os
from multiprocessing import Pool


srcDir = "/home/student-01-3284f0cbd11a/supplier-data/descriptions/"
url = "http://104.197.165.112/fruits/"

def sender(filename):
    dataDict = {}
    with open(srcDir+filename, 'r') as fh:
        lines = fh.readlines()
        dataDict['name'] = lines[0]
        dataDict['weight'] = int(lines[1].strip(" lbs\n"))
        dataDict['description'] = lines[2]
        dataDict['image_name'] = filename[:-4]+".jpeg"

    resp = requests.post(url, json=dataDict)
    print(resp.raise_for_status())
    print(resp.status_code)


Files = os.listdir(srcDir)
Po = Pool(len(Files))
Po.map(sender, Files)
