import sys

logfile = sys.argv[1] # provide the path for the "log" file as a second parameter to the command which activates this script

with open(logfile) as f:
	for line in f:
		print(line.strip())