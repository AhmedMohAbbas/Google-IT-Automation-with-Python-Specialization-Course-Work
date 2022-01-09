#! /usr/bin/env python3

import requests
import os
from multiprocessing import Pool


srcDir = "/data/feedback/"
dataKeys = ['title', 'name', 'date', 'feedback']


def sender(filename):
	dataDict = {}
	with open(srcDir+filename, 'r') as fh:
		lines = fh.readlines()
		for k, v in zip(dataKeys, lines):
			dataDict.update({k: v})
	resp = requests.post("http://<corpweb-external-IP>/feedback/", json=dataDict)
	print(resp.raise_for_status())
	print(resp.status_code)


Files = os.listdir(srcDir)
Po = Pool(len(Files))
Po.map(sender, Files)