#! /usr/bin/env python3

import requests
import os
from multiprocessing import Pool


srcDir = "/home/student-01-3284f0cbd11a/supplier-data/images/"
url = "http://localhost/upload/"


def sender(filename):
	if not ".jpeg" in filename: return None
	with open(srcDir+filename, 'rb') as fh:		
		resp = requests.post(url, files={'file': fh})
		print(resp.raise_for_status())
		print(resp.status_code)


Files = os.listdir(srcDir)
Po = Pool(len(Files))
Po.map(sender, Files)