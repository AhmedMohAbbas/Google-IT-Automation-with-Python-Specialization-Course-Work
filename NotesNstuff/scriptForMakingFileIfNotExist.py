import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, "w") as f:
		f.write("New File Created\n")
else:
	print(f"Error, the file {filename} already exists!")
	sys.exit(1)