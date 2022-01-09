#!/c/ProgramData/Anaconda3/envs/Python3.0 python
import os
import sys

print(sys.argv)

print("HOME: "+ os.environ.get("HOME", ""))
print("Fruit: "+ os.environ.get("Fruit", ""))
print("SHELL: "+ os.environ.get("SHELL", ""))
print("PATH: "+ os.environ.get("PATH", ""))